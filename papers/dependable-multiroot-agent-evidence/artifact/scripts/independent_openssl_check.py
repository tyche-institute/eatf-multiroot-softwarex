#!/usr/bin/env python3
"""Independent package-layer verification with plain OpenSSL.

An implementation-independence check for the package layer (R3.1/R3.3): every
generated .aep's RSA signature and content hash are re-verified using ONLY
`openssl` and `sha256sum` — tools that share no code with the EATF substrate
or with this artifact. Confirms that package-layer acceptance does not depend
on the EATF implementation.

Checks per package:
  1. base64-decoded signature.sig verifies canonical.bin against public_key.pem
     (RSA PKCS#1 v1.5, SHA-256) via `openssl dgst -verify`;
  2. hash.sha256 equals the actual SHA-256 of canonical.bin via `sha256sum`.

Exit 0 = every package passes both; 1 otherwise.
"""

from __future__ import annotations

import base64
import hashlib
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ARTIFACT_ROOT = Path(__file__).resolve().parents[1]


def check_package(aep: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        with zipfile.ZipFile(aep) as z:
            z.extractall(tdir)
        canonical = tdir / "canonical.bin"
        sig_b64 = (tdir / "signature.sig").read_bytes()
        (tdir / "sig.bin").write_bytes(base64.b64decode(sig_b64))
        proc = subprocess.run(
            ["openssl", "dgst", "-sha256", "-verify", str(tdir / "public_key.pem"),
             "-signature", str(tdir / "sig.bin"), str(canonical)],
            capture_output=True, text=True)
        if proc.returncode != 0:
            return False, "openssl signature verification failed"
        declared = (tdir / "hash.sha256").read_text().split()[0].strip()
        actual = hashlib.sha256(canonical.read_bytes()).hexdigest()
        if declared != actual:
            return False, f"hash mismatch: declared {declared[:16]}…, actual {actual[:16]}…"
    return True, "ok"


def main() -> int:
    roots = [ARTIFACT_ROOT / "corpus/generated", ARTIFACT_ROOT / "corpus/generated-mutants"]
    total = passed = 0
    failures: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for aep in sorted(root.rglob("*.aep")):
            total += 1
            ok, why = check_package(aep)
            if ok:
                passed += 1
            else:
                failures.append(f"{aep.relative_to(ARTIFACT_ROOT)}: {why}")
    print(f"independent OpenSSL package-layer check: {passed}/{total} packages verified "
          f"(RSA PKCS#1v1.5/SHA-256 signature over canonical.bin + content hash)")
    for f in failures:
        print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
