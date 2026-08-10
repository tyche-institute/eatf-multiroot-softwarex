#!/usr/bin/env python3
"""Check the artifact against its own SHA-256 manifest.

Reads `results/artifact-manifest.json` and reports three classes of problem:
missing files, hash mismatches, and files present in the tree but absent from
the manifest. Exit 0 only if all three are empty.

The manifest is written by `run_evaluation.py` at the end of a run, so it
covers everything in the artifact except itself. Consequently it is complete
only if the ten-case evaluation is the LAST step of the packaging sequence —
which is what `scripts/run_all.sh` does.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ARTIFACT_ROOT / "results/artifact-manifest.json"


def tracked(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name == ".DS_Store" or path.suffix == ".pyc":
        return False
    if "__pycache__" in path.parts:
        return False
    return path != MANIFEST


def main() -> int:
    if not MANIFEST.exists():
        print("no manifest at", MANIFEST.relative_to(ARTIFACT_ROOT))
        return 1
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]

    missing: list[str] = []
    mismatched: list[str] = []
    listed = set()
    for entry in entries:
        listed.add(entry["path"])
        path = ARTIFACT_ROOT / entry["path"]
        if not path.is_file():
            missing.append(entry["path"])
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            mismatched.append(entry["path"])

    on_disk = {
        str(p.relative_to(ARTIFACT_ROOT))
        for p in ARTIFACT_ROOT.rglob("*")
        if tracked(p)
    }
    unlisted = sorted(on_disk - listed)

    print(f"manifest entries: {len(entries)}   files on disk: {len(on_disk)}")
    for label, items in (("missing", missing), ("hash mismatch", mismatched),
                         ("not in manifest", unlisted)):
        print(f"{label}: {len(items)}")
        for item in items[:20]:
            print("   ", item)
        if len(items) > 20:
            print(f"    … and {len(items) - 20} more")

    return 0 if not (missing or mismatched or unlisted) else 1


if __name__ == "__main__":
    raise SystemExit(main())
