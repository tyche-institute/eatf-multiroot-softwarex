> NOTE — reading `evaluation-summary.md` in this directory: its `Expected`
> column comes from the case plan, whose `expected_verdict` fields are derived
> under the BASELINE policy (`policies/org-a-policy.json`). Under any other
> policy the per-case match column is therefore not meaningful on its own.
> The per-policy ground truth is re-derived by `scripts/run_policy_variation.py`,
> which reports oracle-vs-pipeline agreement for EACH policy in
> `results-policy-variation/policy-variation-report.md`.
