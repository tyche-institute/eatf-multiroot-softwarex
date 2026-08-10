# EATF-Backed Multi-Root Evidence Artifact

This artifact implements the evaluation corpus for *Dependable Multi-Root
Verification of AI-Agent Action Evidence*.

It uses EATF as the cryptographic evidence-package substrate. The scripts
resolve EATF in this order:

1. `EATF_ROOT` environment variable;
2. the bundled runtime snapshot at `artifact/vendor/eatf`.

The submission packet includes a vendored EATF runtime snapshot so that the
corpus can be rebuilt without relying on a machine-local checkout:

- EATF signer: `artifact/vendor/eatf/cli/eatf-sign/bin/eatf-sign.js`
- EATF verifier: `artifact/vendor/eatf/cli/eatf-verify/bin/eatf-verify.js`
- EATF test vectors: `artifact/vendor/eatf/test-vectors/`

The artifact then applies a multi-root policy layer over sets of EATF `.aep`
packages. EATF verifies package integrity, canonicalization, RSA signatures,
OVERT (Observable Verification Evidence for Runtime Trust) receipt structure
and timestamp material. The policy layer checks the paper's model-level
conditions: trusted identity issuers, trusted action issuers, broker
constraints, scope compatibility, offline validation material, revocation
freshness, issuer distrust cutoffs and algorithm migration policy.

## Claim Boundary

This is a production-style research artifact, not a legal trust service.
It does not make Tyche Institute, EATF or this paper a trust service provider,
qualified trust service provider, certification authority, timestamp authority
or issuer of qualified electronic attestations. The generated keys are test
keys only.

## Reproduce

From this directory (the `artifact/` root of the unzipped capsule, which is
also the repository tree):

```sh
python3 scripts/build_eatf_corpus.py     # 10 reviewed seed cases
python3 scripts/run_evaluation.py        # expected: 10/10 verdicts match
python3 scripts/run_policy_variation.py  # builds the 192-mutant corpus if
                                         # absent, then judges it under BOTH
                                         # relying-party policies
```

To force the vendored runtime explicitly, prefix each command with
`EATF_ROOT=$PWD/vendor/eatf`.

The main outputs are:

- `results/…` — the 10 reviewed seed cases (JSON, CSV, Markdown summary,
  SHA-256 manifest);
- `results-mutants/…` — the 192 oracle-derived mutant cases under the baseline
  policy;
- `results-policy-a/…`, `results-policy-b/…` and
  `results-policy-variation/policy-variation-report.md` — the two-policy
  experiment (see the note below);
- `results/conformance/` — adversarial conformance transcripts (vendored
  verifier 8/8 invalid vectors rejected; current upstream 13/13);
- `results/oracle-vs-v01-handwritten.txt` — the oracle's reproduction of the
  ten hand-written v0.1 expected verdicts.

Expected high-level outcomes: 10/10 seed cases match; 192/192 oracle-vs-
pipeline agreement under EACH of the two policies, with 40 verdicts moving
between the policies, each attributable to a policy knob that moved.

**Reading `results-policy-b/evaluation-summary.md` on its own is misleading**:
its `Expected` column reuses the case plan's baseline-policy verdicts, so it
shows 152/192. The per-policy ground truth is re-derived by
`scripts/run_policy_variation.py`; see the `README.md` dropped into each
`results-policy-*` directory and the policy-variation report.

## v0.2 additions (revision, 2026-08)

- `src/spec_oracle.py` — specification-derived verdict oracle: derives expected
  verdicts for case-plan entries from `policies/org-a-policy.json` alone; shares
  no code with the policy overlay and never reads generated package metadata.
- `scripts/generate_mutants.py` — 25 typed mutation operators over the accepting
  seeds (+ pairwise compositions); every mutant's `expected_verdict` is computed
  by the oracle, none is hand-assigned. Output: `corpus/case_plan_mutants.json`.
- `scripts/check_reason_codes.py` — regression check asserting the
  operator→reason-code mapping (verdict matching alone cannot catch label
  relapses).
- `scripts/independent_openssl_check.py` — EATF-independent package-layer
  verification of every generated `.aep` with plain OpenSSL + sha256sum.
- `scripts/run_batch_scaling.sh` — two-mode throughput measurement (per-process
  vs `--batch`) with wall-clock and peak-RSS records.
- `scripts/run_policy_variation.py` + `policies/org-b-archive-policy.json` — the
  second relying-party experiment: the oracle re-derives every expected verdict
  from each policy document alone and the unchanged pipeline is re-run under
  each; writes `results-policy-variation/policy-variation-report.md`.
- `test-vectors-upstream/` — the public EATF conformance suite (4+1 valid,
  8 invalid vectors), used for adversarial testing of the vendored verifier.
- `docs/policy-overlay-pseudocode.md` — the overlay's decision procedure derived
  line-by-line from the source.
- Environment overrides for the unchanged pipeline: `CORPUS_PLAN`, `CORPUS_OUT`,
  `CORPUS_GENERATED`, `RESULTS_DIR`, `POLICY_FILE` (defaults reproduce v0.1
  behaviour).
- Fixes disclosed in the paper: the identity-assurance failure reason code
  (v0.1 mislabelled it `identity-method-unaccepted`), and two baseline models
  that were vacuous on this corpus (see `src/eatf_policy_overlay.py` comments).
