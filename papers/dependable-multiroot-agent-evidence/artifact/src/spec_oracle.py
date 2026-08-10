#!/usr/bin/env python3
"""Specification-derived verdict oracle for the multi-root corpus.

INDEPENDENCE CONTRACT (this is the point of the file — R3 comment 1):

* This module derives an expected verdict for a *case-plan entry* from the
  declarative policy document (``policies/org-a-policy.json``) alone.  It reads
  the same representation the corpus *author* writes, **before** generation:
  it never sees generated package metadata, never invokes the EATF substrate,
  and imports nothing from ``eatf_policy_overlay``.
* The system under test is the full pipeline: ``build_eatf_corpus.py`` →
  ``eatf-sign`` (real signatures, real timestamps) → ``eatf-verify`` →
  ``eatf_policy_overlay.evaluate_case``.  Agreement is measured between the
  two, over inputs the oracle produced verdicts for *first*.
* Shared-author caveat, stated rather than hidden: both sides are written by
  the same author.  What the oracle removes is per-case hand-assignment of
  verdicts — every expected verdict is computed by the ~20 declarative rules
  below, each traceable to a policy key, and the rule table is small enough
  to audit independently.

Assumption, stated: generated packages sign and verify correctly (the corpus
generator uses the bundled dev key and a valid timestamp), so package-layer
cryptographic checks are treated as passing.  Cryptographic failure modes are
exercised separately by the upstream adversarial vector suite
(``test-vectors-upstream/invalid/``), not by this oracle.

Verdict algebra (mirrors the published policy semantics):
    any FAIL → reject;  else any MISSING → indeterminate;  else accept.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

FAIL = "fail"
MISSING = "missing"
PASS = "pass"

_ASSURANCE = {"low": 0, "medium": 1, "high": 2}


def _t(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _rank(value: str) -> int:
    return _ASSURANCE.get(value, -1)


# Generator defaults, mirrored from the case-plan schema documentation.
# (An action/identity omitting a field is generated with these values.)
D_IDENTITY_METHOD = "did:web"
D_IDENTITY_ASSURANCE = "high"
D_ISSUED_AT = "2026-06-02T12:00:00Z"
D_SEQUENCE = 1
D_VALIDATION_EMBEDDED = True
D_REVOCATION_AT = "2026-06-02T00:00:00Z"
D_LIVE_LOOKUP = False
D_ALGORITHM = "rsa-sha256-transitional"
D_BROKER_ASSURANCE = "high"
_REVOCATION_UNSET = object()


def _issuer_trusted(issuer: str, key: str, issued_at: datetime,
                    tau: datetime, policy: dict[str, Any]) -> bool:
    """Rule: issuer must appear in policy[key]; a `trust_cutoffs` entry
    withdraws trust at `after`, except (`allow_issued_before_cutoff`) for
    evidence issued before the cut-off."""
    if issuer not in policy[key]:
        return False
    cutoff = policy.get("trust_cutoffs", {}).get(issuer)
    if not cutoff:
        return True
    cutoff_time = _t(cutoff["after"])
    if tau < cutoff_time:
        return True
    if cutoff.get("allow_issued_before_cutoff", False) and issued_at < cutoff_time:
        return True
    return False


def evaluate_entry(entry: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    """Derive the expected verdict for one case-plan entry under `policy`
    (policy_override already merged by the caller)."""
    tau = _t(entry["verification_time"])
    checks: list[tuple[str, str]] = []  # (rule, status)

    identities = {i["id"]: i for i in entry.get("identities", [])}

    # --- identity rules -------------------------------------------------
    for ident in entry.get("identities", []):
        # policy.trusted_identity_issuers
        checks.append(("identity.issuer",
                       PASS if ident["issuer"] in policy["trusted_identity_issuers"] else FAIL))
        # policy.accepted_identity_methods
        method = ident.get("method", D_IDENTITY_METHOD)
        checks.append(("identity.method",
                       PASS if method in policy["accepted_identity_methods"] else FAIL))
        # policy.min_identity_assurance
        assurance = ident.get("assurance", D_IDENTITY_ASSURANCE)
        checks.append(("identity.assurance",
                       PASS if _rank(assurance) >= _rank(policy["min_identity_assurance"]) else FAIL))

    # --- action rules ---------------------------------------------------
    seen: set[tuple[str, int]] = set()
    for act in entry.get("actions", []):
        issued_at = _t(act.get("issued_at", D_ISSUED_AT))

        # policy.trusted_action_issuers (+ trust_cutoffs)
        checks.append(("action.issuer",
                       PASS if _issuer_trusted(act["issuer"], "trusted_action_issuers",
                                               issued_at, tau, policy) else FAIL))

        # binding: referenced identity must exist; the acting subject must be
        # the referenced identity's subject (substitution check)
        ident = identities.get(act.get("identity", ""))
        if ident is None:
            checks.append(("action.binding", FAIL))
        elif act.get("subject", ident["subject"]) != ident["subject"]:
            checks.append(("action.binding", FAIL))
        else:
            checks.append(("action.binding", PASS))

        # policy.accepted_scopes
        checks.append(("action.scope",
                       PASS if act["scope"] in policy["accepted_scopes"] else FAIL))

        # replay: (acting subject, sequence) must be unique within the case
        subject = act.get("subject", ident["subject"] if ident else "unknown")
        seq_key = (subject, int(act.get("sequence", D_SEQUENCE)))
        checks.append(("action.replay", FAIL if seq_key in seen else PASS))
        seen.add(seq_key)

        # policy.offline_only vs live-lookup dependency
        if bool(act.get("requires_live_lookup", D_LIVE_LOOKUP)):
            checks.append(("action.lookup",
                           FAIL if policy.get("offline_only", True) else MISSING))

        # policy.require_embedded_validation_material
        if policy.get("require_embedded_validation_material", True):
            embedded = bool(act.get("validation_material_embedded", D_VALIDATION_EMBEDDED))
            checks.append(("action.material", PASS if embedded else FAIL))

        # policy.revocation {required, max_age_days, missing, stale}
        rev_policy = policy.get("revocation", {})
        if rev_policy.get("required", True):
            rev_at = act.get("revocation_status_issued_at", _REVOCATION_UNSET)
            if rev_at is _REVOCATION_UNSET:
                rev_at = D_REVOCATION_AT
            if rev_at is None:
                checks.append(("action.revocation",
                               FAIL if rev_policy.get("missing") == "reject" else MISSING))
            else:
                age_days = (tau - _t(str(rev_at))).total_seconds() / 86400
                if age_days > float(rev_policy["max_age_days"]):
                    checks.append(("action.revocation",
                                   FAIL if rev_policy.get("stale") == "reject" else MISSING))
                else:
                    checks.append(("action.revocation", PASS))

        # policy.accepted_algorithm_profiles (+ archive grandfathering)
        profile = act.get("algorithm_profile", D_ALGORITHM)
        if profile in policy["accepted_algorithm_profiles"]:
            checks.append(("action.algorithm", PASS))
        elif policy.get("archive_mode") and profile in policy.get("archive_algorithm_profiles", []):
            checks.append(("action.algorithm", PASS))
        else:
            checks.append(("action.algorithm", MISSING))

        # policy.broker {trusted_brokers, min_assurance, require_exposed_routing,
        #                require_validation_material} + non-authoritativeness
        if act.get("broker"):
            b = policy.get("broker", {})
            if act["broker"] not in b.get("trusted_brokers", []):
                checks.append(("action.broker", FAIL))
            elif _rank(act.get("broker_assurance", D_BROKER_ASSURANCE)) < _rank(b.get("min_assurance", "low")):
                checks.append(("action.broker", FAIL))
            elif b.get("require_exposed_routing", True) and ident is None and not act.get("identity_issuer"):
                # routing must expose the selected identity issuer; with a dangling
                # identity reference the generator cannot embed one
                checks.append(("action.broker", FAIL))
            elif b.get("require_validation_material", True) and not bool(
                    act.get("validation_material_embedded", D_VALIDATION_EMBEDDED)):
                checks.append(("action.broker", FAIL))
            elif act.get("broker_authoritative_verdict"):
                checks.append(("action.broker", FAIL))
            else:
                checks.append(("action.broker", PASS))

    statuses = [s for _, s in checks]
    if FAIL in statuses:
        verdict = "reject"
    elif MISSING in statuses:
        verdict = "indeterminate"
    else:
        verdict = "accept"
    return {"verdict": verdict, "checks": checks}


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = value
    return out
