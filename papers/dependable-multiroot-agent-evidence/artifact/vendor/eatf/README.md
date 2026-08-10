# Vendored EATF runtime snapshot

This directory is a pinned snapshot of the EATF (eAgent Trust Framework)
reference runtime, vendored so that the corpus in this artifact can be rebuilt
and re-verified offline, with no network access and no dependency on upstream
remaining available.

Only the parts the artifact executes are included:

- signer: `cli/eatf-sign/bin/eatf-sign.js`
- verifier: `cli/eatf-verify/bin/eatf-verify.js`
- runtime libraries: `lib/`
- conformance vectors: `test-vectors/` (4+1 valid, 8 invalid)

The signer and verifier are invoked from Python via subprocess; see
`../../scripts/build_eatf_corpus.py` and `../../scripts/run_evaluation.py`.

## What the package layer covers

EATF `.aep` packages bind the action payload: `signature.sig` is an RSA
PKCS#1 v1.5 / SHA-256 signature over `canonical.bin`, and `hash.sha256` is that
file's digest, also recorded as `content_hash` in `overt_receipt.json`. The
attribute metadata this artifact's policy layer evaluates travels in the
package as `metadata.json` and is **not** covered by that signature. The paper
states this explicitly (§Validation and §Limitations); it is a property of the
evidence format, not of the evaluation.

## Provenance and licence

Upstream project: EATF, maintained by Tyche Institute; public documentation at
<https://eatf.eu>.

Licence terms as shipped by upstream are inconsistent between files: `LICENSE`
in this directory is MIT, while `NOTICE` and the two CLI package manifests
declare Apache-2.0. Both are permissive and both permit the redistribution made
here; the discrepancy is upstream's. Third-party packages under
`lib/node_modules/` retain their own licences.

Development-only build and test dependencies were pruned when this snapshot was
taken, to keep the artifact within the journal's file-transfer limit.
Everything the corpus executes at runtime is present.
