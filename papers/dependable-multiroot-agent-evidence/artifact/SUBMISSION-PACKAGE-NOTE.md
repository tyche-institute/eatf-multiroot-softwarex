# Submission package note

This archive is the portal-sized SoftwareX submission package for EATF-MultiRoot v0.1.
It preserves the executable verifier/signing runtime, generated corpus, negative controls,
policy overlay, measurement scripts, and recorded results. Development-only Node.js build
and test dependencies have been pruned to keep the upload below Editorial Manager's file
transfer limit. Runtime dependencies remain vendored for offline evaluation with Node.js 20+.

To reproduce from the unpacked archive:

```sh
cd artifact
python3 scripts/build_eatf_corpus.py
python3 scripts/run_evaluation.py
```

Expected result: 10/10 corpus cases match expected verdicts.
