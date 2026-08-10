# Submission package note

This tree is the portal-sized SoftwareX submission package for EATF-MultiRoot
v0.2.2 (revision of manuscript `SOFTX-D-26-00623`). It preserves the
executable verifier/signing runtime, the generated corpus (10 reviewed seed
cases and 192 oracle-derived mutant cases, 705 mutant packages), negative
controls, the specification oracle, the two relying-party policies, the
policy overlay, measurement scripts and recorded results. Development-only
Node.js build and test dependencies were pruned in v0.1 to keep the upload
below Editorial Manager's file transfer limit and remain pruned; runtime
dependencies stay vendored for offline evaluation with Node.js 20+.

From v0.2.2 on, the release capsule is generated from this repository tree
with `git archive` — the unzipped `artifact/` directory and the tagged tree
have identical contents.

To reproduce from the unpacked archive:

```sh
cd artifact
python3 scripts/build_eatf_corpus.py
python3 scripts/run_evaluation.py
python3 scripts/run_policy_variation.py
```

Expected results: 10/10 seed cases match; 192/192 oracle-vs-pipeline
agreement under each of the two relying-party policies (40 verdicts move
between the policies, each attributable to a policy knob that moved). See
`README.md` for the full output map.
