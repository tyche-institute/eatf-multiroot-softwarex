# Reader check for the v0.1 run report

`w3c/run-report-v01.json` is the v0.1 per-check report of this repository's
evaluation records at commit c421dad, in the reporting format of the W3C
public-agent-conformance group. It was posted to the group's list on
1 November 2026 (https://lists.w3.org/Archives/Public/public-agent-conformance/2026Nov/0000.html)
and accepted there. SHA-256: `0e6086375846a8fc682e264eb9eb64f6f1629d7a514954a3c6d8b39eaf3f7041`.

The workflow `.github/workflows/w3c-report-reader.yml` reads it with the reader
in `agent-evidence-vectors`, pinned in `reader-requirements.txt`, and fails on
anything but `conforms`. Dependabot opens a pull request for each new release
of the reader, so every release is checked against this file before the pin
moves.
