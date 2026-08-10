# EATF-Backed Multi-Root Evaluation Summary

- Cases: 10/10 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 103322.
- Total EATF verify ms: 1958.414.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| C1 multi-root success | accept | accept | yes | 19004 | 359.234 | - |
| C2 non-brokered success | accept | accept | yes | 9347 | 169.378 | - |
| C3 identity substitution | reject | reject | yes | 9361 | 183.472 | identity-hash-missing |
| C4 broker downgrade | reject | reject | yes | 9536 | 189.158 | archive-material-insufficient, broker-policy-violation |
| C5 issuer distrust after cutoff | reject | reject | yes | 9327 | 174.187 | action-issuer-untrusted |
| C6 stale revocation evidence | indeterminate | indeterminate | yes | 9306 | 179.544 | revocation-stale |
| C7 cross-policy replay | reject | reject | yes | 9353 | 172.965 | scope-mismatch |
| C8 offline validation | accept | accept | yes | 9352 | 174.875 | - |
| C9 lookup dependency | reject | reject | yes | 9333 | 182.629 | network-dependency-forbidden |
| C10 algorithm migration | indeterminate | indeterminate | yes | 9403 | 172.972 | algorithm-unaccepted |
