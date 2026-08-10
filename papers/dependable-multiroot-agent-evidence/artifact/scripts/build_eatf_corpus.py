#!/usr/bin/env python3
"""Build the EATF-backed multi-root corpus."""

from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any


ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ARTIFACT_ROOT.parents[2]
EATF_ROOT = ARTIFACT_ROOT / "vendor/eatf"
EATF_SIGN = EATF_ROOT / "cli/eatf-sign/bin/eatf-sign.js"
EATF_VERIFY = EATF_ROOT / "cli/eatf-verify/bin/eatf-verify.js"
EATF_KEY = EATF_ROOT / "test-vectors/keys/dev-rsa-4096.key"
EATF_PUBLIC_KEY = EATF_ROOT / "test-vectors/keys/dev-rsa-4096.pem"
TIMESTAMP_SPEC = (
    EATF_ROOT / "test-vectors/valid/valid-overt-profile/package.aep"
).as_posix() + ":timestamp.tsr"


def main() -> int:
    global EATF_ROOT, EATF_SIGN, EATF_VERIFY, EATF_KEY, EATF_PUBLIC_KEY, TIMESTAMP_SPEC
    EATF_ROOT = resolve_eatf_root()
    EATF_SIGN = EATF_ROOT / "cli/eatf-sign/bin/eatf-sign.js"
    EATF_VERIFY = EATF_ROOT / "cli/eatf-verify/bin/eatf-verify.js"
    EATF_KEY = EATF_ROOT / "test-vectors/keys/dev-rsa-4096.key"
    EATF_PUBLIC_KEY = EATF_ROOT / "test-vectors/keys/dev-rsa-4096.pem"
    TIMESTAMP_SPEC = (
        EATF_ROOT / "test-vectors/valid/valid-overt-profile/package.aep"
    ).as_posix() + ":timestamp.tsr"

    if not EATF_SIGN.exists() or not EATF_VERIFY.exists():
        raise SystemExit(f"EATF CLI missing under {EATF_ROOT}")

    # v0.2: CORPUS_PLAN / CORPUS_OUT env vars let the mutation pipeline reuse
    # this generator unchanged; defaults preserve v0.1 behaviour exactly.
    plan_path = Path(os.environ.get("CORPUS_PLAN", ARTIFACT_ROOT / "corpus/case_plan.json"))
    case_plan = json.loads(plan_path.read_text(encoding="utf-8"))
    generated = Path(os.environ.get("CORPUS_OUT", ARTIFACT_ROOT / "corpus/generated"))
    if generated.exists():
        shutil.rmtree(generated)
    generated.mkdir(parents=True)

    case_index: list[dict[str, Any]] = []
    for case in case_plan["cases"]:
        case_dir = generated / case["case_id"]
        payload_dir = case_dir / "payloads"
        metadata_dir = case_dir / "metadata"
        aep_dir = case_dir / "aep"
        for path in (payload_dir, metadata_dir, aep_dir):
            path.mkdir(parents=True)

        identity_map = {identity["id"]: identity for identity in case["identities"]}
        packages: list[dict[str, Any]] = []
        for identity in case["identities"]:
            packages.append(
                sign_package(
                    case=case,
                    role="identity",
                    item=identity,
                    payload=f"identity assertion for {identity['subject']}\n",
                    payload_dir=payload_dir,
                    metadata_dir=metadata_dir,
                    aep_dir=aep_dir,
                )
            )

        for action in case["actions"]:
            identity = identity_map.get(action["identity"])
            packages.append(
                sign_package(
                    case=case,
                    role="action",
                    item=action,
                    payload=str(action["payload"]) + "\n",
                    payload_dir=payload_dir,
                    metadata_dir=metadata_dir,
                    aep_dir=aep_dir,
                    identity=identity,
                )
            )

        case_index.append(
            {
                "case_id": case["case_id"],
                "title": case["title"],
                "expected_verdict": case["expected_verdict"],
                "verification_time": case["verification_time"],
                "policy_override": case.get("policy_override", {}),
                "packages": packages,
            }
        )

    index = {
        "schema": "urn:tyche:multiroot-eatf-corpus-index:1.0",
        "eatf_root": portable_artifact_path(EATF_ROOT),
        "eatf_signer": portable_artifact_path(EATF_SIGN),
        "eatf_verifier": portable_artifact_path(EATF_VERIFY),
        "timestamp_source": portable_timestamp_spec(TIMESTAMP_SPEC),
        "key_note": "Generated packages use the EATF bundled dev RSA keypair for reproducible research fixtures only.",
        "cases": case_index,
    }
    (generated / "corpus-index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {generated / 'corpus-index.json'}")
    return 0


def resolve_eatf_root() -> Path:
    candidates = []
    if os.environ.get("EATF_ROOT"):
        candidates.append(Path(os.environ["EATF_ROOT"]))
    candidates.append(ARTIFACT_ROOT / "vendor/eatf")

    for candidate in candidates:
        signer = candidate / "cli/eatf-sign/bin/eatf-sign.js"
        verifier = candidate / "cli/eatf-verify/bin/eatf-verify.js"
        if signer.exists() and verifier.exists():
            return candidate
    raise SystemExit(
        "EATF signer/verifier not found. Set EATF_ROOT or unpack/copy EATF "
        f"under {ARTIFACT_ROOT / 'vendor/eatf'}."
    )


def portable_artifact_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ARTIFACT_ROOT.resolve()))
    except ValueError:
        return str(path)


def portable_timestamp_spec(spec: str) -> str:
    suffix = ":timestamp.tsr"
    if not spec.endswith(suffix):
        return spec
    return portable_artifact_path(Path(spec[: -len(suffix)])) + suffix


def sign_package(
    *,
    case: dict[str, Any],
    role: str,
    item: dict[str, Any],
    payload: str,
    payload_dir: Path,
    metadata_dir: Path,
    aep_dir: Path,
    identity: dict[str, Any] | None = None,
) -> dict[str, Any]:
    package_id = f"{case['case_id'].lower()}-{item['id']}"
    payload_path = payload_dir / f"{package_id}.txt"
    metadata_path = metadata_dir / f"{package_id}.json"
    aep_path = aep_dir / f"{package_id}.aep"

    payload_path.write_text(payload, encoding="utf-8")
    metadata = build_metadata(case, role, item, identity)
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    command = [
        "node",
        str(EATF_SIGN),
        "--payload",
        str(payload_path),
        "--key",
        str(EATF_KEY),
        "--public-key",
        str(EATF_PUBLIC_KEY),
        "--metadata",
        str(metadata_path),
        "--scope",
        metadata["action_scope"] if role == "action" else "identity:assertion",
        "--timestamp",
        TIMESTAMP_SPEC,
        "--iap",
        metadata.get("action_issuer") or metadata.get("identity_issuer") or "EATF.eu",
        "--out",
        str(aep_path),
    ]
    subprocess.run(command, check=True, capture_output=True, text=True)

    return {
        "role": role,
        "id": item["id"],
        "attestation_id": metadata["attestation_id"],
        "path": str(aep_path.relative_to(ARTIFACT_ROOT)),
        "metadata": str(metadata_path.relative_to(ARTIFACT_ROOT)),
        "payload": str(payload_path.relative_to(ARTIFACT_ROOT)),
    }


def build_metadata(
    case: dict[str, Any],
    role: str,
    item: dict[str, Any],
    identity: dict[str, Any] | None,
) -> dict[str, Any]:
    created_at = item.get("issued_at", "2026-06-02T12:00:00Z")
    metadata: dict[str, Any] = {
        "schema": "urn:eatf:spec:aep:metadata:1.0",
        "attestation_id": f"{case['case_id']}-{item['id']}",
        "created_at": created_at,
        "agent_id": f"urn:eatf:agent:{item.get('subject', item['id'])}",
        "action_type": "identity.assert" if role == "identity" else "agent.action",
        "policy_id": "org-a-offline-multiroot-v1",
        "policy_version": "1.0",
        "policy_coverage": 1.0,
        "policy_decision": "allow",
        "format_version": "ATAP-1.0",
        "evidence_role": role,
        "case_id": case["case_id"],
    }

    if role == "identity":
        metadata.update(
            {
                "identity_issuer": item["issuer"],
                "identity_subject": item["subject"],
                "identity_method": item.get("method", "did:web"),
                "identity_assurance": item.get("assurance", "high"),
                "identity_scope": item.get("scope", []),
                "valid_from": item.get("valid_from", "2026-01-01T00:00:00Z"),
                "valid_to": item.get("valid_to", "2027-01-01T00:00:00Z"),
                "validation_material_embedded": True,
            }
        )
        return metadata

    if identity is None:
        identity_subject = item.get("subject", "unknown")
    else:
        identity_subject = identity["subject"]

    metadata.update(
        {
            "action_issuer": item["issuer"],
            "action_issued_at": created_at,
            "identity_attestation_id": f"{case['case_id']}-{item['identity']}",
            "identity_subject": item.get("subject", identity_subject),
            "action_scope": item["scope"],
            "sequence": item.get("sequence", 1),
            "previous_hash": item.get("previous_hash"),
            "validation_material_embedded": item.get("validation_material_embedded", True),
            "revocation_status_issued_at": item.get(
                "revocation_status_issued_at", "2026-06-02T00:00:00Z"
            ),
            "requires_live_lookup": item.get("requires_live_lookup", False),
            "algorithm_profile": item.get("algorithm_profile", "rsa-sha256-transitional"),
        }
    )
    if item.get("broker"):
        metadata.update(
            {
                "broker_id": item["broker"],
                "broker_assurance": item.get("broker_assurance", "high"),
                "broker_selected_identity_issuer": (
                    identity["issuer"] if identity is not None else item.get("identity_issuer")
                ),
                "broker_selected_action_issuer": item["issuer"],
                "broker_authoritative_verdict": item.get("broker_authoritative_verdict", False),
                "broker_claimed_verdict": item.get("broker_claimed_verdict"),
            }
        )
    return {key: value for key, value in metadata.items() if value is not None}


if __name__ == "__main__":
    raise SystemExit(main())
