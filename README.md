# EATF-MultiRoot SoftwareX artifact

This repository is the public, paper-specific preservation copy of the
software and evaluation corpus for SoftwareX manuscript `SOFTX-D-26-00623`,
*EATF-MultiRoot: A Reproducible Verifier and Corpus for AI-Agent Evidence
Packages*.

The tree lives at
[`papers/dependable-multiroot-agent-evidence/artifact`](papers/dependable-multiroot-agent-evidence/artifact).
`main` carries the current revision (v0.2.2); the tree reviewed with the
original submission is preserved without modification at tag
`eatf-multiroot-softwarex-v0.1`.

## Releases

| Tag | What it is |
|---|---|
| `eatf-multiroot-softwarex-v0.1` | the reviewed submission; its release asset `softwarex-eatf-multiroot-artifact-v0.1.zip` is the exact archive submitted to the journal |
| `eatf-multiroot-softwarex-v0.2`, `…-v0.2.1` | revision capsules published as release assets while the repository tree still carried v0.1 (superseded; kept for the record) |
| `eatf-multiroot-softwarex-v0.2.2` | the revision: repository tree and release capsule are byte-identical (`git archive` of the tagged tree) |

Zenodo: concept DOI `10.5281/zenodo.20777207`; each release capsule is
archived under its own version DOI.

## Immutable identity of the reviewed version

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
vendored to permit offline evaluation; no network access is needed at any
stage.

```sh
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/build_eatf_corpus.py
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/run_evaluation.py
python3 papers/dependable-multiroot-agent-evidence/artifact/scripts/run_policy_variation.py
```

Expected results: all 10 reviewed seed cases match their expected verdicts,
and the 192 oracle-derived mutant cases reach 192/192 oracle-vs-pipeline
agreement under each of the two relying-party policies (40 verdicts move
between the policies, each attributable to a policy knob that moved). The
continuous-integration workflow runs the same commands and asserts the same
counts. See the artifact
[`README.md`](papers/dependable-multiroot-agent-evidence/artifact/README.md)
for the full output map, including the adversarial-conformance transcripts
and the independent OpenSSL package-layer check.

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
