#!/usr/bin/env python3
"""Run the EATF-backed multi-root evaluation corpus."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from eatf_policy_overlay import PackageRecord, evaluate_case, load_policy  # noqa: E402


ARTIFACT_ROOT = Path(__file__).resolve().parents[1]
EATF_ROOT = ARTIFACT_ROOT / "vendor/eatf"
EATF_VERIFY = EATF_ROOT / "cli/eatf-verify/bin/eatf-verify.js"
# v0.2: env-var overrides for the mutation pipeline; defaults = v0.1 behaviour.
GENERATED = Path(os.environ.get("CORPUS_GENERATED", ARTIFACT_ROOT / "corpus/generated"))
RESULTS = Path(os.environ.get("RESULTS_DIR", ARTIFACT_ROOT / "results"))


def main() -> int:
    global EATF_ROOT, EATF_VERIFY
    EATF_ROOT = resolve_eatf_root()
    EATF_VERIFY = EATF_ROOT / "cli/eatf-verify/bin/eatf-verify.js"

    if not (GENERATED / "corpus-index.json").exists():
        subprocess.run([sys.executable, str(ARTIFACT_ROOT / "scripts/build_eatf_corpus.py")], check=True)

    RESULTS.mkdir(parents=True, exist_ok=True)
    index = json.loads((GENERATED / "corpus-index.json").read_text(encoding="utf-8"))
    base_policy = load_policy(Path(os.environ.get("POLICY_FILE",
                                                 ARTIFACT_ROOT / "policies/org-a-policy.json")))

    case_results: list[dict[str, Any]] = []
    for case in index["cases"]:
        policy = deep_merge(base_policy, case.get("policy_override", {}))
        records = [verify_package(package) for package in case["packages"]]
        case_results.append(evaluate_case(case, records, policy))

    matched = sum(1 for result in case_results if result["matched_expectation"])
    total = len(case_results)
    evaluation = {
        "schema": "urn:tyche:multiroot-eatf-evaluation-results:1.0",
        "artifact": "EATF-backed multi-root AI-agent evidence corpus",
        "eatf_root": portable_artifact_path(EATF_ROOT),
        "cases_total": total,
        "cases_matched": matched,
        "all_expectations_matched": matched == total,
        "results": case_results,
    }
    (RESULTS / "evaluation-results.json").write_text(
        json.dumps(evaluation, indent=2) + "\n", encoding="utf-8"
    )
    write_csv(case_results)
    write_summary(evaluation)
    write_manifest()
    print(f"{matched}/{total} corpus cases matched expected verdicts")
    print(f"Wrote {RESULTS / 'evaluation-summary.md'}")
    return 0 if matched == total else 1


def resolve_eatf_root() -> Path:
    candidates = []
    if os.environ.get("EATF_ROOT"):
        candidates.append(Path(os.environ["EATF_ROOT"]))
    candidates.append(ARTIFACT_ROOT / "vendor/eatf")

    for candidate in candidates:
        verifier = candidate / "cli/eatf-verify/bin/eatf-verify.js"
        if verifier.exists():
            return candidate
    raise SystemExit(
        "EATF verifier not found. Set EATF_ROOT or unpack/copy EATF under "
        f"{ARTIFACT_ROOT / 'vendor/eatf'}."
    )


def portable_artifact_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ARTIFACT_ROOT.resolve()))
    except ValueError:
        return str(path)


def verify_package(package: dict[str, Any]) -> PackageRecord:
    aep_path = ARTIFACT_ROOT / package["path"]
    start = time.perf_counter()
    proc = subprocess.run(
        ["node", str(EATF_VERIFY), "--json", str(aep_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    if proc.stdout.strip():
        result = json.loads(proc.stdout.splitlines()[-1])
    else:
        result = {
            "valid": False,
            "failureReason": proc.stderr.strip() or f"exit {proc.returncode}",
            "metadata": {},
        }
    return PackageRecord(
        path=str(aep_path),
        valid=bool(result.get("valid")),
        metadata=result.get("metadata") or {},
        failure_reason=result.get("failureReason"),
        size_bytes=aep_path.stat().st_size,
        verify_ms=elapsed_ms,
    )


def write_csv(case_results: list[dict[str, Any]]) -> None:
    with (RESULTS / "evaluation-results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "case_id",
                "title",
                "expected_verdict",
                "verdict",
                "matched_expectation",
                "package_size_bytes",
                "eatf_verify_ms",
                "network_lookups_required",
                "reason_codes",
            ],
        )
        writer.writeheader()
        for result in case_results:
            writer.writerow(
                {
                    "case_id": result["case_id"],
                    "title": result["title"],
                    "expected_verdict": result["expected_verdict"],
                    "verdict": result["verdict"],
                    "matched_expectation": result["matched_expectation"],
                    "package_size_bytes": result["metrics"]["package_size_bytes"],
                    "eatf_verify_ms": result["metrics"]["eatf_verify_ms"],
                    "network_lookups_required": result["metrics"]["network_lookups_required"],
                    "reason_codes": ";".join(result["reason_codes"]),
                }
            )


def write_summary(evaluation: dict[str, Any]) -> None:
    total_package_size = sum(
        result["metrics"]["package_size_bytes"] for result in evaluation["results"]
    )
    total_verify_ms = sum(
        float(result["metrics"]["eatf_verify_ms"]) for result in evaluation["results"]
    )
    lines = [
        "# EATF-Backed Multi-Root Evaluation Summary",
        "",
        f"- Cases: {evaluation['cases_matched']}/{evaluation['cases_total']} matched expected verdicts.",
        f"- EATF root: `{evaluation['eatf_root']}`",
        "- EATF verifier mode: offline JSON CLI.",
        f"- Total package size bytes: {total_package_size}.",
        f"- Total EATF verify ms: {total_verify_ms:.3f}.",
        "- Claim boundary: production-style research artifact; not a legal trust service.",
        "",
        "| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for result in evaluation["results"]:
        lines.append(
            "| {case_id} {title} | {expected} | {observed} | {match} | {size} | {ms:.3f} | {codes} |".format(
                case_id=result["case_id"],
                title=result["title"],
                expected=result["expected_verdict"],
                observed=result["verdict"],
                match="yes" if result["matched_expectation"] else "no",
                size=result["metrics"]["package_size_bytes"],
                ms=float(result["metrics"]["eatf_verify_ms"]),
                codes=", ".join(result["reason_codes"]) or "-",
            )
        )
    (RESULTS / "evaluation-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest() -> None:
    entries: list[dict[str, Any]] = []
    for path in sorted(ARTIFACT_ROOT.rglob("*")):
        if should_manifest(path):
            entries.append(
                {
                    "path": str(path.relative_to(ARTIFACT_ROOT)),
                    "bytes": path.stat().st_size,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            )
    (RESULTS / "artifact-manifest.json").write_text(
        json.dumps({"files": entries}, indent=2) + "\n", encoding="utf-8"
    )


def should_manifest(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name == ".DS_Store" or path.suffix == ".pyc":
        return False
    if "__pycache__" in path.parts:
        return False
    if path == RESULTS / "artifact-manifest.json":
        return False
    return True


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = json.loads(json.dumps(base))
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


if __name__ == "__main__":
    raise SystemExit(main())
