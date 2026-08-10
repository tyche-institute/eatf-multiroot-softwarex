#!/usr/bin/env python3
"""Typed-mutation corpus generator with a specification-derived verdict oracle.

Answers R3(1)/R3(4)/R2(1): expected verdicts for every mutant are DERIVED by
``src/spec_oracle.py`` from the declarative policy document — never assigned by
hand.  Each mutant records full provenance: seed case, operator name, operator
category, mutation site.

Design:
* Seeds are the three clean *accept* cases (C1, C2, C8), so a unary operator's
  effect is attributable to that operator alone.
* Unary operators are applied at every applicable site of every seed.
* Pair mutants compose two independent unary operators on C1 (different
  categories, different sites where possible) — this exercises the verdict
  algebra's priority join (fail > missing > pass) rather than single rules.
* Boundary operators generate near-miss variants around every threshold in the
  policy: trust cut-off instant, revocation max-age, minimum assurance ranks.

Output: ``corpus/case_plan_mutants.json`` in the exact case-plan schema, so the
unmodified generator + evaluator pipeline runs over REAL signed packages.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable

ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ARTIFACT_ROOT / "src"))
from spec_oracle import deep_merge, evaluate_entry  # noqa: E402

SEED_IDS = ["C1", "C2", "C8"]

# --- typed operators -------------------------------------------------------
# op = (name, category, site, mutate) ; mutate(entry) edits in place.
# "site" targets: identity index, action index, or case level.

def _ops_for(entry: dict[str, Any]) -> list[tuple[str, str, str, Callable[[dict], None]]]:
    ops: list[tuple[str, str, str, Callable[[dict], None]]] = []

    def ident_op(idx: int, name: str, category: str, fn: Callable[[dict], None]) -> None:
        ops.append((name, category, f"identity[{idx}]",
                    lambda e, i=idx, f=fn: f(e["identities"][i])))

    def action_op(idx: int, name: str, category: str, fn: Callable[[dict], None]) -> None:
        ops.append((name, category, f"action[{idx}]",
                    lambda e, i=idx, f=fn: f(e["actions"][i])))

    for i, _ in enumerate(entry.get("identities", [])):
        ident_op(i, "identity-issuer-unknown", "identity-trust",
                 lambda d: d.update(issuer="identity-root-zz"))
        ident_op(i, "identity-method-unknown", "identity-method",
                 lambda d: d.update(method="did:example"))
        ident_op(i, "identity-assurance-low", "assurance-boundary",
                 lambda d: d.update(assurance="low"))
        ident_op(i, "identity-assurance-medium-boundary", "assurance-boundary",
                 lambda d: d.update(assurance="medium"))          # == min → still accept

    for i, act in enumerate(entry.get("actions", [])):
        action_op(i, "action-issuer-unknown", "action-trust",
                  lambda d: d.update(issuer="action-root-zz"))
        action_op(i, "action-issuer-retired-after-cutoff", "trust-cutoff-boundary",
                  lambda d: d.update(issuer="action-root-retired",
                                     issued_at="2026-06-02T12:00:00Z"))  # after 06-01 cut-off
        action_op(i, "action-issuer-retired-grandfathered", "trust-cutoff-boundary",
                  lambda d: d.update(issuer="action-root-retired",
                                     issued_at="2026-05-30T00:00:00Z"))  # before cut-off → accept
        action_op(i, "binding-dangling-identity", "binding",
                  lambda d: d.update(identity="id-ghost"))
        action_op(i, "binding-subject-substitution", "binding",
                  lambda d: d.update(subject="agent-mallory"))
        action_op(i, "scope-unknown", "scope",
                  lambda d: d.update(scope="agent:payments"))
        action_op(i, "live-lookup-under-offline-policy", "offline",
                  lambda d: d.update(requires_live_lookup=True))
        action_op(i, "validation-material-stripped", "archive-material",
                  lambda d: d.update(validation_material_embedded=False))
        action_op(i, "revocation-missing", "revocation",
                  lambda d: d.update(revocation_status_issued_at=None))
        action_op(i, "revocation-stale-8d", "revocation",
                  lambda d: d.update(revocation_status_issued_at="2026-05-26T00:00:00Z"))  # 8 d
        action_op(i, "revocation-boundary-just-fresh", "revocation-boundary",
                  lambda d: d.update(revocation_status_issued_at="2026-05-27T00:00:01Z"))  # 7 d − 1 s
        action_op(i, "revocation-boundary-just-stale", "revocation-boundary",
                  lambda d: d.update(revocation_status_issued_at="2026-05-26T23:59:59Z"))  # 7 d + 1 s
        action_op(i, "algorithm-unknown", "algorithm",
                  lambda d: d.update(algorithm_profile="sphincs-experimental"))
        action_op(i, "algorithm-pqc-accepted", "algorithm",
                  lambda d: d.update(algorithm_profile="rsa-sha256+pqc"))
        if act.get("broker"):
            action_op(i, "broker-untrusted", "broker",
                      lambda d: d.update(broker="broker-zz-9"))
            action_op(i, "broker-assurance-low", "broker-assurance-boundary",
                      lambda d: d.update(broker_assurance="low"))
            action_op(i, "broker-assurance-medium-boundary", "broker-assurance-boundary",
                      lambda d: d.update(broker_assurance="medium"))  # == min → accept
            action_op(i, "broker-claims-authoritative-verdict", "broker",
                      lambda d: d.update(broker_authoritative_verdict=True))
            action_op(i, "broker-removed", "broker",
                      lambda d: d.pop("broker"))
        else:
            action_op(i, "broker-added-untrusted", "broker",
                      lambda d: d.update(broker="broker-zz-9"))

    # case-level structural operator: replayed sequence number
    def replay(e: dict[str, Any]) -> None:
        clone = copy.deepcopy(e["actions"][0])
        clone["id"] = clone["id"] + "-replay"
        clone["payload"] = str(clone.get("payload", "")) + " (replayed)"
        e["actions"].append(clone)  # same subject, same sequence → replay hit

    ops.append(("sequence-replay-duplicate", "replay", "case", replay))
    return ops


def main() -> int:
    plan = json.loads((ARTIFACT_ROOT / "corpus/case_plan.json").read_text(encoding="utf-8"))
    policy = json.loads((ARTIFACT_ROOT / "policies/org-a-policy.json").read_text(encoding="utf-8"))
    seeds = {c["case_id"]: c for c in plan["cases"] if c["case_id"] in SEED_IDS}

    mutants: list[dict[str, Any]] = []

    def derive_and_add(entry: dict[str, Any], mutant_id: str,
                       provenance: dict[str, Any]) -> None:
        merged = deep_merge(policy, entry.get("policy_override", {}))
        oracle = evaluate_entry(entry, merged)
        entry["case_id"] = mutant_id
        entry["expected_verdict"] = oracle["verdict"]          # DERIVED, not authored
        entry["oracle_provenance"] = {
            **provenance,
            "oracle": "spec_oracle.evaluate_entry",
            "non_pass_checks": [c for c in oracle["checks"] if c[1] != "pass"],
        }
        mutants.append(entry)

    # unary operators over every seed
    for seed_id, seed in seeds.items():
        for n, (name, category, site, mutate) in enumerate(_ops_for(seed)):
            entry = copy.deepcopy(seed)
            entry["title"] = f"{seed_id} × {name} @ {site}"
            mutate(entry)
            derive_and_add(entry, f"M-{seed_id}-{n:03d}-{name}",
                           {"seed": seed_id, "operator": name,
                            "category": category, "site": site})

    # pair composition on C1: first applicable op of each category × ditto
    c1 = seeds["C1"]
    c1_ops = _ops_for(c1)
    by_category: dict[str, tuple[str, str, str, Callable]] = {}
    for op in c1_ops:
        by_category.setdefault(op[1], op)
    reps = sorted(by_category.values(), key=lambda o: o[1])
    for a in range(len(reps)):
        for b in range(a + 1, len(reps)):
            n1, c1cat, s1, f1 = reps[a]
            n2, c2cat, s2, f2 = reps[b]
            if s1 == s2 and c1cat == c2cat:
                continue
            entry = copy.deepcopy(c1)
            entry["title"] = f"C1 × {n1} + {n2}"
            f1(entry)
            f2(entry)
            derive_and_add(entry, f"P-{a:02d}{b:02d}-{n1}--{n2}",
                           {"seed": "C1", "operator": [n1, n2],
                            "category": [c1cat, c2cat], "site": [s1, s2]})

    out = {
        "schema": plan["schema"],
        "verification_time": plan.get("verification_time"),
        "oracle_note": ("expected_verdict fields in this file are derived by "
                        "src/spec_oracle.py from policies/org-a-policy.json; "
                        "none is hand-assigned"),
        "cases": mutants,
    }
    dst = ARTIFACT_ROOT / "corpus/case_plan_mutants.json"
    dst.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    from collections import Counter
    verdicts = Counter(m["expected_verdict"] for m in mutants)
    print(f"wrote {dst.name}: {len(mutants)} mutants "
          f"({verdicts['accept']} accept / {verdicts['reject']} reject / "
          f"{verdicts['indeterminate']} indeterminate)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
