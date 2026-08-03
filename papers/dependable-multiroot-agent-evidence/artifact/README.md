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

From the repository root:

```sh
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/build_eatf_corpus.py
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/run_evaluation.py
```

To force the vendored runtime explicitly:

```sh
EATF_ROOT=/path/to/paper/artifact/vendor/eatf \
  python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/build_eatf_corpus.py
EATF_ROOT=/path/to/paper/artifact/vendor/eatf \
  python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/run_evaluation.py
```

The main outputs are:

- `results/evaluation-results.json`
- `results/evaluation-summary.md`
- `results/evaluation-results.csv`
- `results/artifact-manifest.json`

Expected high-level outcome: 10/10 corpus cases match the expected verdicts.
