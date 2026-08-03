# EATF-Backed Multi-Root Evaluation Summary

- Cases: 10/10 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 103322.
- Total EATF verify ms: 7316.678.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| C1 multi-root success | accept | accept | yes | 19004 | 1372.126 | - |
| C2 non-brokered success | accept | accept | yes | 9347 | 671.616 | - |
| C3 identity substitution | reject | reject | yes | 9361 | 642.836 | identity-hash-missing |
| C4 broker downgrade | reject | reject | yes | 9536 | 676.915 | archive-material-insufficient, broker-policy-violation |
| C5 issuer distrust after cutoff | reject | reject | yes | 9327 | 646.571 | action-issuer-untrusted |
| C6 stale revocation evidence | indeterminate | indeterminate | yes | 9306 | 653.501 | revocation-stale |
| C7 cross-policy replay | reject | reject | yes | 9353 | 677.710 | scope-mismatch |
| C8 offline validation | accept | accept | yes | 9352 | 665.498 | - |
| C9 lookup dependency | reject | reject | yes | 9333 | 644.514 | network-dependency-forbidden |
| C10 algorithm migration | indeterminate | indeterminate | yes | 9403 | 665.391 | algorithm-unaccepted |
