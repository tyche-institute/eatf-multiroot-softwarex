# EATF-MultiRoot SoftwareX artifact v0.1

This repository is the public, paper-specific preservation copy of the
software and evaluation corpus reviewed with SoftwareX manuscript
`SOFTX-D-26-00623`, *EATF-MultiRoot: A Reproducible Verifier and Corpus for
AI-Agent Evidence Packages*.

The reviewed tree is preserved without modification at
[`papers/dependable-multiroot-agent-evidence/artifact`](papers/dependable-multiroot-agent-evidence/artifact).
The release asset `softwarex-eatf-multiroot-artifact-v0.1.zip` is the exact
archive submitted to the journal.

## Immutable identity

- SoftwareX release: `eatf-multiroot-softwarex-v0.1`
- source commit in the former repository:
  `d495dbfe856def17d46568b9104c533c3c0c8481`
- submitted ZIP size: `4,467,464` bytes
- submitted ZIP SHA-256:
  `efd64377c75a742f5eb456ff7de5b1d6b72e75ccdccc7ffad5c1467e872c22f2`

The former full-platform repository remains private. This repository exposes
only the bounded artifact reviewed with the paper, not unrelated platform
code.

## Reproduce

Requires Python 3 and Node.js 20 or later. Runtime JavaScript dependencies are
vendored to permit offline evaluation.

```sh
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/build_eatf_corpus.py
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/run_evaluation.py
```

Expected result: all 10 corpus cases match their expected verdicts. The
continuous-integration workflow runs the same commands.

## Integrity and security notes

An independent pre-publication run on 3 August 2026 reproduced 10/10 expected
verdicts. All 695 entries named in the artifact's internal manifest matched
their recorded hashes. The manifest is intentionally treated as a partial
research-artifact manifest: it does not enumerate every file in the vendored
runtime.

The tree contains the documented development-only key
`artifact/vendor/eatf/test-vectors/keys/dev-rsa-4096.key`. It is a public test
fixture, not a production secret or trust anchor. A targeted credential scan
found no service credentials or access tokens.

## Claim boundary

This is research software, not a legal trust service. It does not make Tyche
Institute, EATF, or the paper a trust service provider, qualified trust
service provider, certification authority, timestamp authority, or issuer of
qualified electronic attestations. Generated and bundled keys are test keys
only.

## License

MIT; see [`LICENSE`](LICENSE). Third-party and vendored components retain the
licenses included with them.
