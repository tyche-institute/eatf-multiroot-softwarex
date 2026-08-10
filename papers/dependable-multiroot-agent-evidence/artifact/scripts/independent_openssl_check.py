#!/usr/bin/env python3
"""Independent package-layer verification with plain OpenSSL.

An implementation-independence check for the package layer: every generated
.aep's RSA signature and content hash are re-verified with the `openssl`
binary and Python's own `hashlib` — neither of which shares code with the EATF
substrate or with this artifact. It confirms that package-layer acceptance
does not depend on the EATF implementation.

Checks per package:
  1. base64-decoded signature.sig verifies canonical.bin against public_key.pem
     (RSA PKCS#1 v1.5, SHA-256) via `openssl dgst -verify`;
  2. hash.sha256 equals the SHA-256 of canonical.bin, recomputed here.

SCOPE. This is what an AEP binds: the action payload. The attribute metadata
the policy overlay evaluates (`metadata.json` — issuers, scope, broker fields,
revocation status, algorithm profile) is carried in the package but is NOT
covered by signature.sig or hash.sha256, so passing this check says nothing
about those attributes' authenticity. See the paper's Limitations section.

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
