#!/usr/bin/env python3
"""Judge the same mutant corpus under two relying-party policies.

For each policy document the specification oracle re-derives every expected
verdict from that document alone, the unchanged pipeline re-runs over the same
signed packages, and per-policy agreement is reported. Verdict changes between
the two configurations are then attributed to the reason codes that appeared
or disappeared — a verdict may only move for a knob the policy actually moved.

Exit 0 iff agreement is total under BOTH policies.
"""

from __future__ import annotations

import collections
import json
import os
import subprocess
import sys
from pathlib import Path

ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ARTIFACT_ROOT / "src"))
from spec_oracle import deep_merge, evaluate_entry  # noqa: E402

POLICIES = [
    ("A", "policies/org-a-policy.json"),
    ("B", "policies/org-b-archive-policy.json"),
]


def ensure_mutant_corpus() -> None:
    """Build the mutant corpus if this checkout does not carry it.

    The build is deterministic for verdict purposes: the plan, keys and the
    timestamp fixture are all pinned in the artifact.
    """
    index = ARTIFACT_ROOT / "corpus/generated-mutants/corpus-index.json"
    if index.exists():
        return
    print("mutant corpus not present; building it (about a minute)...")
    env = dict(
        os.environ,
        CORPUS_PLAN=str(ARTIFACT_ROOT / "corpus/case_plan_mutants.json"),
        CORPUS_OUT=str(ARTIFACT_ROOT / "corpus/generated-mutants"),
    )
    subprocess.run([sys.executable, str(ARTIFACT_ROOT / "scripts/build_eatf_corpus.py")],
                   env=env, check=True)


def main() -> int:
    ensure_mutant_corpus()
    plan = json.loads((ARTIFACT_ROOT / "corpus/case_plan_mutants.json").read_text(encoding="utf-8"))
    out: dict[str, tuple[dict, dict, dict]] = {}
    ok = True
    for tag, pol_file in POLICIES:
        policy = json.loads((ARTIFACT_ROOT / pol_file).read_text(encoding="utf-8"))
        expected = {}
        for case in plan["cases"]:
            entry = dict(case)
            entry.setdefault("verification_time", plan.get("verification_time"))
            merged = deep_merge(policy, case.get("policy_override", {}))
            expected[case["case_id"]] = evaluate_entry(entry, merged)["verdict"]

        env = dict(
            os.environ,
            CORPUS_GENERATED=str(ARTIFACT_ROOT / "corpus/generated-mutants"),
            RESULTS_DIR=str(ARTIFACT_ROOT / ("results-policy-" + tag.lower())),
            POLICY_FILE=str(ARTIFACT_ROOT / pol_file),
        )
        proc = subprocess.run([sys.executable, str(ARTIFACT_ROOT / "scripts/run_evaluation.py")],
                              env=env, capture_output=True, text=True)
        if proc.returncode not in (0, 1):
            # 0 = all matched, 1 = mismatches (expected under policy B, whose
            # expectations differ from the plan's policy-A verdict fields);
            # anything else means the evaluation itself failed.
            sys.stderr.write(proc.stderr)
            raise RuntimeError("evaluation failed under policy " + tag)
        res = json.loads((Path(env["RESULTS_DIR"]) / "evaluation-results.json").read_text(encoding="utf-8"))
        got = {c["case_id"]: c["verdict"] for c in res["results"]}
        codes = {c["case_id"]: c["reason_codes"] for c in res["results"]}
        agree = sum(1 for k in expected if expected[k] == got[k])
        ok = ok and agree == len(expected)
        out[tag] = (expected, got, codes)
        print("policy %s  oracle-vs-pipeline: %d/%d   verdicts: %s"
              % (tag, agree, len(expected), dict(collections.Counter(got.values()))))

    (_, a_got, a_codes), (_, b_got, b_codes) = out["A"], out["B"]
    moved = [k for k in a_got if a_got[k] != b_got[k]]
    print("\nverdict changed between policies: %d of %d cases" % (len(moved), len(a_got)))
    transitions = dict(collections.Counter(
        "%s->%s" % (a_got[k], b_got[k]) for k in moved))
    print("transitions:", transitions)
    print("\nreason codes that disappeared under policy B (knob attribution):")
    attribution = collections.Counter()
    for k in moved:
        gone = set(a_codes[k]) - set(b_codes[k])
        attribution[", ".join(sorted(gone)) or "(status change only)"] += 1
    for label, n in attribution.most_common():
        print("   %-55s %d" % (label[:55], n))
    write_report(out, moved, transitions, attribution)
    return 0 if ok else 1


CAVEAT = """> NOTE — reading `evaluation-summary.md` in this directory: its `Expected`
> column comes from the case plan, whose `expected_verdict` fields are derived
> under the BASELINE policy (`policies/org-a-policy.json`). Under any other
> policy the per-case match column is therefore not meaningful on its own.
> The per-policy ground truth is re-derived by `scripts/run_policy_variation.py`,
> which reports oracle-vs-pipeline agreement for EACH policy in
> `results-policy-variation/policy-variation-report.md`.
"""


def write_report(out, moved, transitions, attribution) -> None:
    for tag, _ in POLICIES:
        d = ARTIFACT_ROOT / ("results-policy-" + tag.lower())
        (d / "README.md").write_text(CAVEAT, encoding="utf-8")
    (_, a_got, _), (_, b_got, _) = out["A"], out["B"]
    lines = ["# Policy-variation report", "",
             "Generated by `scripts/run_policy_variation.py`. The specification",
             "oracle re-derives every expected verdict from each policy document",
             "alone; the unchanged pipeline re-runs over the same 192 signed",
             "mutant cases; agreement is per policy.", ""]
    for tag, pol_file in POLICIES:
        expected, got, _ = out[tag]
        agree = sum(1 for k in expected if expected[k] == got[k])
        lines.append("- policy %s (`%s`): oracle-vs-pipeline **%d/%d**, verdicts %s"
                     % (tag, pol_file, agree, len(expected),
                        dict(collections.Counter(got.values()))))
    lines += ["", "## Verdict movement between policies", "",
              "%d of %d verdicts change; transitions: %s" % (len(moved), len(a_got), transitions),
              "", "## Knob attribution (reason codes that disappeared under policy B)", ""]
    for label, n in attribution.most_common():
        lines.append("- `%s`: %d" % (label or "(status change only)", n))
    lines += ["", "| Case | Policy A | Policy B |", "|---|---|---|"]
    for k in sorted(moved):
        lines.append("| %s | %s | %s |" % (k, a_got[k], b_got[k]))
    rd = ARTIFACT_ROOT / "results-policy-variation"
    rd.mkdir(exist_ok=True)
    (rd / "policy-variation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\nreport written: results-policy-variation/policy-variation-report.md")


if __name__ == "__main__":
    raise SystemExit(main())
