#!/bin/bash
# Full reproduction of every number the paper reports, in the order that leaves
# a complete SHA-256 manifest behind.
#
#   Run from the artifact root:  bash scripts/run_all.sh
#
# The ten-case evaluation comes LAST on purpose: it writes
# results/artifact-manifest.json at the end of its run, so running it last
# makes the manifest cover every other file the packaging step produced.
set -euo pipefail
cd "$(dirname "$0")/.."
ART=$PWD

echo "== 1/6  mutation corpus (192 derived-verdict cases, 705 packages)"
python3 scripts/generate_mutants.py
CORPUS_PLAN=$ART/corpus/case_plan_mutants.json \
CORPUS_OUT=$ART/corpus/generated-mutants \
  python3 scripts/build_eatf_corpus.py
CORPUS_GENERATED=$ART/corpus/generated-mutants \
RESULTS_DIR=$ART/results-mutants \
  python3 scripts/run_evaluation.py

echo "== 2/6  the same corpus under two relying-party policies"
python3 scripts/run_policy_variation.py

echo "== 3/6  reason-code regression check"
python3 scripts/check_reason_codes.py

echo "== 4/6  independent package-layer check (OpenSSL, no EATF code)"
python3 scripts/independent_openssl_check.py

echo "== 5/6  adversarial conformance of the vendored verifier"
# Exit 1 is expected here and is itself a documented result: the pinned v0.1.1
# verifier rejects all 8 invalid vectors AND 5 valid ones, because it predates
# the suite's current ML-DSA encoding and requires an embedded timestamp. The
# paper reports this ageing effect; see results/conformance/.
mkdir -p results/conformance
set +e
node vendor/eatf/cli/eatf-verify/bin/eatf-verify.js --conformance test-vectors-upstream \
  | tee results/conformance/vendored-conformance.log
conf_status=${PIPESTATUS[0]}
set -e
if [ "$conf_status" -gt 1 ]; then
  echo "conformance runner failed with status $conf_status" >&2
  exit "$conf_status"
fi
grep -c "^PASS" results/conformance/vendored-conformance.log \
  | xargs -I{} echo "   invalid vectors rejected as expected: {} of 8"

echo "== 6/6  reviewed ten-case corpus (writes the manifest last)"
python3 scripts/build_eatf_corpus.py
python3 scripts/run_evaluation.py

echo
echo "== manifest self-check"
python3 scripts/verify_manifest.py

echo
echo "Batch throughput is measured separately (it writes a 10,000-package"
echo "scratch corpus): bash scripts/run_batch_scaling.sh"
