#!/usr/bin/env python3
"""Regression check: operator → expected reason code.

The mutation harness matches VERDICTS; this check asserts the LABELS. It exists
because the v0.1→v0.2 reason-code fix (identity-assurance-insufficient) was not
caught by verdict matching: the pre-fix run passed 192/192 while emitting the
wrong label. Verdicts say WHAT was decided; reason codes say WHY — and the
paper's interface claim is the WHY.

Asserts, for every mutant whose case_id carries the operator name, that the
operator's characteristic reason code appears in that case's reason_codes.
Exit code 0 = all present; 1 = any missing (listed).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
RESULTS = Path(os.environ.get("RESULTS_DIR", ARTIFACT_ROOT / "results-mutants"))

# operator substring in case_id  →  reason code that MUST be present
EXPECTED = {
    "identity-assurance-low": "identity-assurance-insufficient",   # the v0.2 fix
    "identity-method-unknown": "identity-method-unaccepted",
    "identity-issuer-unknown": "identity-issuer-untrusted",
    "action-issuer-unknown": "action-issuer-untrusted",
    "action-issuer-retired-after-cutoff": "action-issuer-untrusted",
    "binding-dangling-identity": "identity-hash-missing",
    "binding-subject-substitution": "identity-substitution",
    "scope-unknown": "scope-mismatch",
    "sequence-replay-duplicate": "sequence-replay",
    "live-lookup-under-offline-policy": "network-dependency-forbidden",
    "validation-material-stripped": "archive-material-insufficient",
    "revocation-missing": "revocation-missing",
    "revocation-stale-8d": "revocation-stale",
    "revocation-boundary-just-stale": "revocation-stale",
    "algorithm-unknown": "algorithm-unaccepted",
    "broker-untrusted": "broker-policy-violation",
    "broker-assurance-low": "broker-policy-violation",
    "broker-claims-authoritative-verdict": "broker-policy-violation",
}


def main() -> int:
    results = json.loads((RESULTS / "evaluation-results.json").read_text(encoding="utf-8"))
    checked = 0
    failures: list[str] = []
    for case in results["results"]:
        cid = case["case_id"]
        if not cid.startswith("M-"):        # unary mutants only: one operator, one attribution
            continue
        for op_sub, code in EXPECTED.items():
            if op_sub in cid:
                checked += 1
                if code not in case["reason_codes"]:
                    failures.append(f"{cid}: expected '{code}', got {case['reason_codes']}")
    print(f"reason-code regression: {checked} operator instances checked, "
          f"{len(failures)} failures")
    for f in failures:
        print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
