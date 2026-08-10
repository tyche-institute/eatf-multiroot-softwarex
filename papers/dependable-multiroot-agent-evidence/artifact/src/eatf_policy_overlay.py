#!/usr/bin/env python3
"""Multi-root policy overlay for EATF evidence packages.

The overlay consumes EATF verifier JSON lines and the metadata embedded in each
`.aep` package. It does not replace EATF cryptographic verification. Instead,
it evaluates the paper's policy-local checks over packages that EATF has already
accepted or rejected.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_time(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def assurance_rank(value: str) -> int:
    return {"low": 0, "medium": 1, "high": 2}.get(value, -1)


def add_reason(reasons: list[dict[str, str]], code: str, status: str, target: str) -> None:
    reasons.append({"code": code, "status": status, "target": target})


def final_verdict(reasons: list[dict[str, str]]) -> str:
    if any(item["status"] == "fail" for item in reasons):
        return "reject"
    if any(item["status"] == "missing" for item in reasons):
        return "indeterminate"
    return "accept"


@dataclass(frozen=True)
class PackageRecord:
    path: str
    valid: bool
    metadata: dict[str, Any]
    failure_reason: str | None
    size_bytes: int
    verify_ms: float

    @property
    def role(self) -> str:
        return str(self.metadata.get("evidence_role", "unknown"))

    @property
    def attestation_id(self) -> str:
        return str(self.metadata.get("attestation_id", self.path))


def load_policy(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(
    case: dict[str, Any],
    package_records: list[PackageRecord],
    policy: dict[str, Any],
) -> dict[str, Any]:
    tau = parse_time(case["verification_time"])
    reasons: list[dict[str, str]] = []

    for record in package_records:
        if record.valid:
            add_reason(reasons, "eatf-package-valid", "pass", record.attestation_id)
        else:
            add_reason(reasons, "eatf-package-invalid", "fail", record.attestation_id)
            if record.failure_reason:
                add_reason(reasons, record.failure_reason, "fail", record.attestation_id)

    identities = {
        record.attestation_id: record
        for record in package_records
        if record.role == "identity" and record.valid
    }
    actions = [record for record in package_records if record.role == "action" and record.valid]

    for identity in identities.values():
        meta = identity.metadata
        issuer = str(meta.get("identity_issuer", ""))
        if issuer in policy["trusted_identity_issuers"]:
            add_reason(reasons, "identity-issuer", "pass", identity.attestation_id)
        else:
            add_reason(reasons, "identity-issuer-untrusted", "fail", identity.attestation_id)

        if meta.get("identity_method") in policy["accepted_identity_methods"]:
            add_reason(reasons, "identity-method", "pass", identity.attestation_id)
        else:
            add_reason(reasons, "identity-method-unaccepted", "fail", identity.attestation_id)

        if assurance_rank(str(meta.get("identity_assurance", "low"))) >= assurance_rank(
            policy["min_identity_assurance"]
        ):
            add_reason(reasons, "identity-assurance", "pass", identity.attestation_id)
        else:
            # v0.2 fix: this branch previously emitted "identity-method-unaccepted"
            # (a copy of the method check's code), mislabelling WHY the case failed.
            add_reason(reasons, "identity-assurance-insufficient", "fail", identity.attestation_id)

    seen_sequences: set[tuple[str, int]] = set()
    for action in actions:
        meta = action.metadata
        issuer = str(meta.get("action_issuer", ""))
        issued_at = parse_time(str(meta.get("action_issued_at", meta.get("created_at"))))
        if issuer_is_trusted(issuer, "action", issued_at, tau, policy):
            add_reason(reasons, "action-issuer", "pass", action.attestation_id)
        else:
            add_reason(reasons, "action-issuer-untrusted", "fail", action.attestation_id)

        identity_id = str(meta.get("identity_attestation_id", ""))
        identity = identities.get(identity_id)
        if not identity:
            add_reason(reasons, "identity-hash-missing", "fail", action.attestation_id)
        else:
            identity_subject = identity.metadata.get("identity_subject")
            if identity_subject != meta.get("identity_subject"):
                add_reason(reasons, "identity-substitution", "fail", action.attestation_id)
            else:
                add_reason(reasons, "identity-binding", "pass", action.attestation_id)

        scope = str(meta.get("action_scope", ""))
        if scope in policy["accepted_scopes"]:
            add_reason(reasons, "scope", "pass", action.attestation_id)
        else:
            add_reason(reasons, "scope-mismatch", "fail", action.attestation_id)

        sequence_key = (str(meta.get("identity_subject", "unknown")), int(meta.get("sequence", 0)))
        if sequence_key in seen_sequences:
            add_reason(reasons, "sequence-replay", "fail", action.attestation_id)
        else:
            seen_sequences.add(sequence_key)

        if bool(meta.get("requires_live_lookup", False)):
            if policy.get("offline_only", True):
                add_reason(reasons, "network-dependency-forbidden", "fail", action.attestation_id)
            else:
                add_reason(reasons, "network-lookup-required", "missing", action.attestation_id)

        if bool(policy.get("require_embedded_validation_material", True)):
            if bool(meta.get("validation_material_embedded", False)):
                add_reason(reasons, "archive-material", "pass", action.attestation_id)
            else:
                add_reason(reasons, "archive-material-insufficient", "fail", action.attestation_id)

        revocation_issued_at = meta.get("revocation_status_issued_at")
        revocation_policy = policy.get("revocation", {})
        if revocation_policy.get("required", True):
            if not revocation_issued_at:
                status = "fail" if revocation_policy.get("missing") == "reject" else "missing"
                add_reason(reasons, "revocation-missing", status, action.attestation_id)
            else:
                age_days = (tau - parse_time(str(revocation_issued_at))).total_seconds() / 86400
                if age_days > float(revocation_policy["max_age_days"]):
                    status = "fail" if revocation_policy.get("stale") == "reject" else "missing"
                    add_reason(reasons, "revocation-stale", status, action.attestation_id)
                else:
                    add_reason(reasons, "revocation-status", "pass", action.attestation_id)

        algorithm_profile = str(meta.get("algorithm_profile", ""))
        if algorithm_profile in policy["accepted_algorithm_profiles"]:
            add_reason(reasons, "algorithm-profile", "pass", action.attestation_id)
        elif policy.get("archive_mode") and algorithm_profile in policy.get("archive_algorithm_profiles", []):
            add_reason(reasons, "algorithm-profile", "pass", action.attestation_id)
        else:
            add_reason(reasons, "algorithm-unaccepted", "missing", action.attestation_id)

        evaluate_broker(meta, action.attestation_id, policy, reasons)

    verdict = final_verdict(reasons)
    reason_codes = sorted({item["code"] for item in reasons if item["status"] != "pass"})
    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "expected_verdict": case["expected_verdict"],
        "verdict": verdict,
        "matched_expectation": verdict == case["expected_verdict"],
        "reason_codes": reason_codes,
        "reason_trace": reasons,
        "metrics": {
            "packages": len(package_records),
            "package_size_bytes": sum(record.size_bytes for record in package_records),
            "eatf_verify_ms": round(sum(record.verify_ms for record in package_records), 3),
            "network_lookups_required": sum(
                1 for record in package_records if record.metadata.get("requires_live_lookup")
            ),
        },
        "baselines": baseline_verdicts(case, package_records),
    }


def issuer_is_trusted(
    issuer: str,
    role: str,
    issued_at: datetime,
    verification_time: datetime,
    policy: dict[str, Any],
) -> bool:
    trusted_key = "trusted_identity_issuers" if role == "identity" else "trusted_action_issuers"
    if issuer not in policy[trusted_key]:
        return False
    cutoff = policy.get("trust_cutoffs", {}).get(issuer)
    if not cutoff:
        return True
    cutoff_time = parse_time(cutoff["after"])
    if verification_time < cutoff_time:
        return True
    if cutoff.get("allow_issued_before_cutoff", False) and issued_at < cutoff_time:
        return True
    return False


def evaluate_broker(
    metadata: dict[str, Any],
    target: str,
    policy: dict[str, Any],
    reasons: list[dict[str, str]],
) -> None:
    broker_id = metadata.get("broker_id")
    if not broker_id:
        add_reason(reasons, "broker-absent", "pass", target)
        return

    broker_policy = policy.get("broker", {})
    if broker_id not in broker_policy.get("trusted_brokers", []):
        add_reason(reasons, "broker-policy-violation", "fail", target)
    elif assurance_rank(str(metadata.get("broker_assurance", "low"))) < assurance_rank(
        broker_policy.get("min_assurance", "low")
    ):
        add_reason(reasons, "broker-policy-violation", "fail", target)
    elif broker_policy.get("require_exposed_routing", True) and not metadata.get(
        "broker_selected_identity_issuer"
    ):
        add_reason(reasons, "broker-policy-violation", "fail", target)
    elif broker_policy.get("require_validation_material", True) and not metadata.get(
        "validation_material_embedded"
    ):
        add_reason(reasons, "broker-policy-violation", "fail", target)
    elif metadata.get("broker_authoritative_verdict"):
        add_reason(reasons, "broker-policy-violation", "fail", target)
    else:
        add_reason(reasons, "broker-policy", "pass", target)


def baseline_verdicts(case: dict[str, Any], records: list[PackageRecord]) -> dict[str, str]:
    # v0.2: two baseline models corrected so each is non-vacuous on this corpus.
    #
    # mutable_log — a verifier that trusts the runtime's own log accepts whatever
    # the log asserts. Every generated case has a log assertion by construction,
    # so this model accepts every case (v0.1 keyed on a  flag
    # no corpus case set, making the model vacuously indeterminate).
    mutable_log = "accept"

    # single_root_registry — all trust chains to registry family A only: accept
    # iff every issuer in the case belongs to the "-root-a" family, reject any
    # mixed-root or non-A evidence. (v0.1 compared the issuer set to the literal
    # {"root-a"}, which no corpus issuer ever used, making the model vacuously
    # reject-everything.)
    issuers = {
        str(record.metadata.get("identity_issuer") or record.metadata.get("action_issuer"))
        for record in records
    }
    single_root = "accept" if issuers and all(i.endswith("-root-a") for i in issuers) else "reject"

    detached_signature = (
        "accept"
        if all(record.valid for record in records)
        and all(record.metadata.get("validation_material_embedded") for record in records if record.role == "action")
        else "indeterminate"
    )

    broker_claims = [
        record.metadata.get("broker_claimed_verdict")
        for record in records
        if record.metadata.get("broker_claimed_verdict")
    ]
    broker_authoritative = str(broker_claims[0]) if broker_claims else "indeterminate"

    return {
        "mutable_log": mutable_log,
        "single_root_registry": single_root,
        "detached_signature": detached_signature,
        "broker_authoritative": broker_authoritative,
    }

