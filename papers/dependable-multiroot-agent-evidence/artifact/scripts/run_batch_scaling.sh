#!/bin/bash
# P3 scaling harness — SoftwareX SOFTX-D-26-00623 revision (R1.4ii, R2.2).
#
# Measures the package-verification path (vendored eatf-verify) two ways:
#   (1) per-package process spawn  — the mode the v0.1 paper timed;
#   (2) --batch, one Node process  — amortizes startup.
# Then scales --batch over N replicated packages, recording wall time and
# peak RSS via /usr/bin/time -v.
#
# HONESTY NOTE (goes into the paper verbatim): replication multiplies the
# 22 corpus packages; content diversity does not grow with N. Per-package
# cryptographic work is content-independent (signature + hash + policy
# checks over same-sized packages), so this measures verifier THROUGHPUT,
# not corpus coverage. The mutation corpus (P1) replaces replication for
# coverage claims.
set -euo pipefail
cd "$(dirname "$0")/.."
V=vendor/eatf/cli/eatf-verify/bin/eatf-verify.js
OUT=results/scaling
mkdir -p "$OUT"
SRC=corpus/generated

echo "== packages in corpus: $(find $SRC -name '*.aep' | wc -l)"

# (1) per-spawn over the corpus
echo "== mode 1: per-package spawn"
/usr/bin/time -v bash -c '
  find '"$SRC"' -name "*.aep" | while read p; do
    node '"$V"' --json "$p" > /dev/null
  done' 2> "$OUT/per-spawn-22.time"
grep -E "Elapsed|Maximum resident" "$OUT/per-spawn-22.time"

# (2) batch over the same corpus
echo "== mode 2: --batch, one process"
/usr/bin/time -v node "$V" --batch "$SRC" > "$OUT/batch-22.out" 2> "$OUT/batch-22.time"
grep -E "Elapsed|Maximum resident" "$OUT/batch-22.time"
tail -2 "$OUT/batch-22.out"

# (3) scaling: replicate to N packages, batch once
for N in 100 1000 10000; do
  SCRATCH=$(mktemp -d /tmp/eatf-scale-XXXX)
  i=0
  while [ "$i" -lt "$N" ]; do
    for p in $(find "$SRC" -name '*.aep'); do
      [ "$i" -ge "$N" ] && break
      cp "$p" "$SCRATCH/pkg-$i.aep"; i=$((i+1))
    done
  done
  echo "== mode 3: --batch over N=$N replicated packages"
  /usr/bin/time -v node "$V" --batch "$SCRATCH" > "$OUT/batch-$N.out" 2> "$OUT/batch-$N.time"
  grep -E "Elapsed|Maximum resident" "$OUT/batch-$N.time"
  tail -2 "$OUT/batch-$N.out"
  rm -rf "$SCRATCH"
done
echo "== done; records in $OUT/"
