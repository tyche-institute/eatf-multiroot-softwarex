# EATF-Backed Multi-Root Evaluation Summary

- Cases: 192/192 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 3424310.
- Total EATF verify ms: 62806.563.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| M-C1-000-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 19307 | 356.351 | identity-issuer-untrusted |
| M-C1-001-identity-method-unknown C1 × identity-method-unknown @ identity[0] | reject | reject | yes | 19308 | 361.768 | identity-method-unaccepted |
| M-C1-002-identity-assurance-low C1 × identity-assurance-low @ identity[0] | reject | reject | yes | 19293 | 357.524 | identity-assurance-insufficient |
| M-C1-003-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 19416 | 375.798 | - |
| M-C1-004-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[1] | reject | reject | yes | 19307 | 347.467 | identity-issuer-untrusted |
| M-C1-005-identity-method-unknown C1 × identity-method-unknown @ identity[1] | reject | reject | yes | 19308 | 363.835 | identity-method-unaccepted |
| M-C1-006-identity-assurance-low C1 × identity-assurance-low @ identity[1] | reject | reject | yes | 19293 | 363.666 | identity-assurance-insufficient |
| M-C1-007-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[1] | accept | accept | yes | 19416 | 354.094 | - |
| M-C1-008-action-issuer-unknown C1 × action-issuer-unknown @ action[0] | reject | reject | yes | 19287 | 370.960 | action-issuer-untrusted |
| M-C1-009-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 19432 | 360.029 | action-issuer-untrusted |
| M-C1-010-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 19442 | 352.855 | - |
| M-C1-011-binding-dangling-identity C1 × binding-dangling-identity @ action[0] | reject | reject | yes | 19272 | 353.558 | broker-policy-violation, identity-hash-missing |
| M-C1-012-binding-subject-substitution C1 × binding-subject-substitution @ action[0] | reject | reject | yes | 19360 | 342.818 | identity-substitution |
| M-C1-013-scope-unknown C1 × scope-unknown @ action[0] | reject | reject | yes | 19206 | 353.497 | scope-mismatch |
| M-C1-014-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 19393 | 351.799 | network-dependency-forbidden |
| M-C1-015-validation-material-stripped C1 × validation-material-stripped @ action[0] | reject | reject | yes | 19355 | 349.500 | archive-material-insufficient, broker-policy-violation |
| M-C1-016-revocation-missing C1 × revocation-missing @ action[0] | reject | reject | yes | 19201 | 356.118 | revocation-missing |
| M-C1-017-revocation-stale-8d C1 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 19264 | 365.446 | revocation-stale |
| M-C1-018-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 19374 | 360.869 | - |
| M-C1-019-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 19374 | 346.123 | revocation-stale |
| M-C1-020-algorithm-unknown C1 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 19241 | 353.768 | algorithm-unaccepted |
| M-C1-021-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 19285 | 349.731 | - |
| M-C1-022-broker-untrusted C1 × broker-untrusted @ action[0] | reject | reject | yes | 19234 | 358.694 | broker-policy-violation |
| M-C1-023-broker-assurance-low C1 × broker-assurance-low @ action[0] | reject | reject | yes | 19273 | 339.990 | broker-policy-violation |
| M-C1-024-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[0] | accept | accept | yes | 19396 | 361.925 | - |
| M-C1-025-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[0] | reject | reject | yes | 19423 | 348.498 | broker-policy-violation |
| M-C1-026-broker-removed C1 × broker-removed @ action[0] | accept | accept | yes | 19025 | 357.433 | - |
| M-C1-027-action-issuer-unknown C1 × action-issuer-unknown @ action[1] | reject | reject | yes | 19287 | 353.757 | action-issuer-untrusted |
| M-C1-028-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[1] | reject | reject | yes | 19432 | 349.984 | action-issuer-untrusted |
| M-C1-029-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[1] | accept | accept | yes | 19442 | 348.742 | - |
| M-C1-030-binding-dangling-identity C1 × binding-dangling-identity @ action[1] | reject | reject | yes | 19273 | 358.621 | broker-policy-violation, identity-hash-missing |
| M-C1-031-binding-subject-substitution C1 × binding-subject-substitution @ action[1] | reject | reject | yes | 19363 | 358.275 | identity-substitution |
| M-C1-032-scope-unknown C1 × scope-unknown @ action[1] | reject | reject | yes | 19204 | 360.829 | scope-mismatch |
| M-C1-033-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[1] | reject | reject | yes | 19393 | 357.750 | network-dependency-forbidden |
| M-C1-034-validation-material-stripped C1 × validation-material-stripped @ action[1] | reject | reject | yes | 19355 | 343.326 | archive-material-insufficient, broker-policy-violation |
| M-C1-035-revocation-missing C1 × revocation-missing @ action[1] | reject | reject | yes | 19201 | 374.769 | revocation-missing |
| M-C1-036-revocation-stale-8d C1 × revocation-stale-8d @ action[1] | indeterminate | indeterminate | yes | 19264 | 356.837 | revocation-stale |
| M-C1-037-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[1] | accept | accept | yes | 19374 | 366.796 | - |
| M-C1-038-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[1] | indeterminate | indeterminate | yes | 19374 | 361.279 | revocation-stale |
| M-C1-039-algorithm-unknown C1 × algorithm-unknown @ action[1] | indeterminate | indeterminate | yes | 19241 | 367.158 | algorithm-unaccepted |
| M-C1-040-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[1] | accept | accept | yes | 19285 | 367.756 | - |
| M-C1-041-broker-untrusted C1 × broker-untrusted @ action[1] | reject | reject | yes | 19234 | 346.122 | broker-policy-violation |
| M-C1-042-broker-assurance-low C1 × broker-assurance-low @ action[1] | reject | reject | yes | 19273 | 343.693 | broker-policy-violation |
| M-C1-043-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[1] | accept | accept | yes | 19396 | 371.379 | - |
| M-C1-044-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[1] | reject | reject | yes | 19423 | 359.284 | broker-policy-violation |
| M-C1-045-broker-removed C1 × broker-removed @ action[1] | accept | accept | yes | 19025 | 358.397 | - |
| M-C1-046-sequence-replay-duplicate C1 × sequence-replay-duplicate @ case | reject | reject | yes | 24327 | 436.165 | sequence-replay |
| M-C2-000-identity-issuer-unknown C2 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9499 | 172.188 | identity-issuer-untrusted |
| M-C2-001-identity-method-unknown C2 × identity-method-unknown @ identity[0] | reject | reject | yes | 9501 | 171.699 | identity-method-unaccepted |
| M-C2-002-identity-assurance-low C2 × identity-assurance-low @ identity[0] | reject | reject | yes | 9491 | 180.464 | identity-assurance-insufficient |
| M-C2-003-identity-assurance-medium-boundary C2 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9554 | 182.957 | - |
| M-C2-004-action-issuer-unknown C2 × action-issuer-unknown @ action[0] | reject | reject | yes | 9489 | 181.575 | action-issuer-untrusted |
| M-C2-005-action-issuer-retired-after-cutoff C2 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9564 | 179.372 | action-issuer-untrusted |
| M-C2-006-action-issuer-retired-grandfathered C2 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9569 | 174.031 | - |
| M-C2-007-binding-dangling-identity C2 × binding-dangling-identity @ action[0] | reject | reject | yes | 9507 | 177.445 | identity-hash-missing |
| M-C2-008-binding-subject-substitution C2 × binding-subject-substitution @ action[0] | reject | reject | yes | 9528 | 178.582 | identity-substitution |
| M-C2-009-scope-unknown C2 × scope-unknown @ action[0] | reject | reject | yes | 9449 | 172.448 | scope-mismatch |
| M-C2-010-live-lookup-under-offline-policy C2 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9541 | 173.884 | network-dependency-forbidden |
| M-C2-011-validation-material-stripped C2 × validation-material-stripped @ action[0] | reject | reject | yes | 9523 | 181.050 | archive-material-insufficient |
| M-C2-012-revocation-missing C2 × revocation-missing @ action[0] | reject | reject | yes | 9419 | 183.257 | revocation-missing |
| M-C2-013-revocation-stale-8d C2 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9477 | 176.255 | revocation-stale |
| M-C2-014-revocation-boundary-just-fresh C2 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9532 | 180.536 | - |
| M-C2-015-revocation-boundary-just-stale C2 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9532 | 183.666 | revocation-stale |
| M-C2-016-algorithm-unknown C2 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9464 | 191.208 | algorithm-unaccepted |
| M-C2-017-algorithm-pqc-accepted C2 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9483 | 185.801 | - |
| M-C2-018-broker-added-untrusted C2 × broker-added-untrusted @ action[0] | reject | reject | yes | 9681 | 178.993 | broker-policy-violation |
| M-C2-019-sequence-replay-duplicate C2 × sequence-replay-duplicate @ case | reject | reject | yes | 14353 | 277.423 | sequence-replay |
| M-C8-000-identity-issuer-unknown C8 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9504 | 175.837 | identity-issuer-untrusted |
| M-C8-001-identity-method-unknown C8 × identity-method-unknown @ identity[0] | reject | reject | yes | 9506 | 183.989 | identity-method-unaccepted |
| M-C8-002-identity-assurance-low C8 × identity-assurance-low @ identity[0] | reject | reject | yes | 9496 | 180.547 | identity-assurance-insufficient |
| M-C8-003-identity-assurance-medium-boundary C8 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9559 | 175.211 | - |
| M-C8-004-action-issuer-unknown C8 × action-issuer-unknown @ action[0] | reject | reject | yes | 9494 | 177.361 | action-issuer-untrusted |
| M-C8-005-action-issuer-retired-after-cutoff C8 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9569 | 180.741 | action-issuer-untrusted |
| M-C8-006-action-issuer-retired-grandfathered C8 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9574 | 176.407 | - |
| M-C8-007-binding-dangling-identity C8 × binding-dangling-identity @ action[0] | reject | reject | yes | 9513 | 183.877 | identity-hash-missing |
| M-C8-008-binding-subject-substitution C8 × binding-subject-substitution @ action[0] | reject | reject | yes | 9536 | 172.773 | identity-substitution |
| M-C8-009-scope-unknown C8 × scope-unknown @ action[0] | reject | reject | yes | 9452 | 176.661 | scope-mismatch |
| M-C8-010-live-lookup-under-offline-policy C8 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9546 | 172.464 | network-dependency-forbidden |
| M-C8-011-validation-material-stripped C8 × validation-material-stripped @ action[0] | reject | reject | yes | 9528 | 181.226 | archive-material-insufficient |
| M-C8-012-revocation-missing C8 × revocation-missing @ action[0] | reject | reject | yes | 9424 | 177.402 | revocation-missing |
| M-C8-013-revocation-stale-8d C8 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9482 | 176.472 | revocation-stale |
| M-C8-014-revocation-boundary-just-fresh C8 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9537 | 187.348 | - |
| M-C8-015-revocation-boundary-just-stale C8 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9537 | 190.854 | revocation-stale |
| M-C8-016-algorithm-unknown C8 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9469 | 178.030 | algorithm-unaccepted |
| M-C8-017-algorithm-pqc-accepted C8 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9488 | 177.984 | - |
| M-C8-018-broker-added-untrusted C8 × broker-added-untrusted @ action[0] | reject | reject | yes | 9686 | 174.389 | broker-policy-violation |
| M-C8-019-sequence-replay-duplicate C8 × sequence-replay-duplicate @ case | reject | reject | yes | 14368 | 271.166 | sequence-replay |
| P-0001-action-issuer-unknown--algorithm-unknown C1 × action-issuer-unknown + algorithm-unknown | reject | reject | yes | 19454 | 350.155 | action-issuer-untrusted, algorithm-unaccepted |
| P-0002-action-issuer-unknown--validation-material-stripped C1 × action-issuer-unknown + validation-material-stripped | reject | reject | yes | 19568 | 354.532 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0003-action-issuer-unknown--identity-assurance-low C1 × action-issuer-unknown + identity-assurance-low | reject | reject | yes | 19506 | 356.126 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0004-action-issuer-unknown--binding-dangling-identity C1 × action-issuer-unknown + binding-dangling-identity | reject | reject | yes | 19485 | 356.308 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0005-action-issuer-unknown--broker-untrusted C1 × action-issuer-unknown + broker-untrusted | reject | reject | yes | 19447 | 348.735 | action-issuer-untrusted, broker-policy-violation |
| P-0006-action-issuer-unknown--broker-assurance-low C1 × action-issuer-unknown + broker-assurance-low | reject | reject | yes | 19486 | 350.743 | action-issuer-untrusted, broker-policy-violation |
| P-0007-action-issuer-unknown--identity-method-unknown C1 × action-issuer-unknown + identity-method-unknown | reject | reject | yes | 19521 | 370.327 | action-issuer-untrusted, identity-method-unaccepted |
| P-0008-action-issuer-unknown--identity-issuer-unknown C1 × action-issuer-unknown + identity-issuer-unknown | reject | reject | yes | 19520 | 350.755 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0009-action-issuer-unknown--live-lookup-under-offline-policy C1 × action-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19606 | 366.107 | action-issuer-untrusted, network-dependency-forbidden |
| P-0010-action-issuer-unknown--sequence-replay-duplicate C1 × action-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24606 | 442.140 | action-issuer-untrusted, sequence-replay |
| P-0011-action-issuer-unknown--revocation-missing C1 × action-issuer-unknown + revocation-missing | reject | reject | yes | 19414 | 359.400 | action-issuer-untrusted, revocation-missing |
| P-0012-action-issuer-unknown--revocation-boundary-just-fresh C1 × action-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19587 | 360.742 | action-issuer-untrusted |
| P-0013-action-issuer-unknown--scope-unknown C1 × action-issuer-unknown + scope-unknown | reject | reject | yes | 19419 | 352.634 | action-issuer-untrusted, scope-mismatch |
| P-0014-action-issuer-unknown--action-issuer-retired-after-cutoff C1 × action-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19642 | 356.988 | action-issuer-untrusted |
| P-0102-algorithm-unknown--validation-material-stripped C1 × algorithm-unknown + validation-material-stripped | reject | reject | yes | 19522 | 363.661 | algorithm-unaccepted, archive-material-insufficient, broker-policy-violation |
| P-0103-algorithm-unknown--identity-assurance-low C1 × algorithm-unknown + identity-assurance-low | reject | reject | yes | 19460 | 359.856 | algorithm-unaccepted, identity-assurance-insufficient |
| P-0104-algorithm-unknown--binding-dangling-identity C1 × algorithm-unknown + binding-dangling-identity | reject | reject | yes | 19439 | 374.991 | algorithm-unaccepted, broker-policy-violation, identity-hash-missing |
| P-0105-algorithm-unknown--broker-untrusted C1 × algorithm-unknown + broker-untrusted | reject | reject | yes | 19401 | 359.627 | algorithm-unaccepted, broker-policy-violation |
| P-0106-algorithm-unknown--broker-assurance-low C1 × algorithm-unknown + broker-assurance-low | reject | reject | yes | 19440 | 358.180 | algorithm-unaccepted, broker-policy-violation |
| P-0107-algorithm-unknown--identity-method-unknown C1 × algorithm-unknown + identity-method-unknown | reject | reject | yes | 19475 | 371.019 | algorithm-unaccepted, identity-method-unaccepted |
| P-0108-algorithm-unknown--identity-issuer-unknown C1 × algorithm-unknown + identity-issuer-unknown | reject | reject | yes | 19474 | 354.353 | algorithm-unaccepted, identity-issuer-untrusted |
| P-0109-algorithm-unknown--live-lookup-under-offline-policy C1 × algorithm-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19560 | 350.742 | algorithm-unaccepted, network-dependency-forbidden |
| P-0110-algorithm-unknown--sequence-replay-duplicate C1 × algorithm-unknown + sequence-replay-duplicate | reject | reject | yes | 24542 | 448.264 | algorithm-unaccepted, sequence-replay |
| P-0111-algorithm-unknown--revocation-missing C1 × algorithm-unknown + revocation-missing | reject | reject | yes | 19368 | 369.511 | algorithm-unaccepted, revocation-missing |
| P-0112-algorithm-unknown--revocation-boundary-just-fresh C1 × algorithm-unknown + revocation-boundary-just-fresh | indeterminate | indeterminate | yes | 19541 | 353.874 | algorithm-unaccepted |
| P-0113-algorithm-unknown--scope-unknown C1 × algorithm-unknown + scope-unknown | reject | reject | yes | 19373 | 338.238 | algorithm-unaccepted, scope-mismatch |
| P-0114-algorithm-unknown--action-issuer-retired-after-cutoff C1 × algorithm-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19599 | 351.034 | action-issuer-untrusted, algorithm-unaccepted |
| P-0203-validation-material-stripped--identity-assurance-low C1 × validation-material-stripped + identity-assurance-low | reject | reject | yes | 19574 | 339.759 | archive-material-insufficient, broker-policy-violation, identity-assurance-insufficient |
| P-0204-validation-material-stripped--binding-dangling-identity C1 × validation-material-stripped + binding-dangling-identity | reject | reject | yes | 19553 | 369.071 | archive-material-insufficient, broker-policy-violation, identity-hash-missing |
| P-0205-validation-material-stripped--broker-untrusted C1 × validation-material-stripped + broker-untrusted | reject | reject | yes | 19515 | 371.678 | archive-material-insufficient, broker-policy-violation |
| P-0206-validation-material-stripped--broker-assurance-low C1 × validation-material-stripped + broker-assurance-low | reject | reject | yes | 19554 | 347.663 | archive-material-insufficient, broker-policy-violation |
| P-0207-validation-material-stripped--identity-method-unknown C1 × validation-material-stripped + identity-method-unknown | reject | reject | yes | 19589 | 348.351 | archive-material-insufficient, broker-policy-violation, identity-method-unaccepted |
| P-0208-validation-material-stripped--identity-issuer-unknown C1 × validation-material-stripped + identity-issuer-unknown | reject | reject | yes | 19588 | 362.369 | archive-material-insufficient, broker-policy-violation, identity-issuer-untrusted |
| P-0209-validation-material-stripped--live-lookup-under-offline-policy C1 × validation-material-stripped + live-lookup-under-offline-policy | reject | reject | yes | 19674 | 350.512 | archive-material-insufficient, broker-policy-violation, network-dependency-forbidden |
| P-0210-validation-material-stripped--sequence-replay-duplicate C1 × validation-material-stripped + sequence-replay-duplicate | reject | reject | yes | 24693 | 435.077 | archive-material-insufficient, broker-policy-violation, sequence-replay |
| P-0211-validation-material-stripped--revocation-missing C1 × validation-material-stripped + revocation-missing | reject | reject | yes | 19482 | 348.086 | archive-material-insufficient, broker-policy-violation, revocation-missing |
| P-0212-validation-material-stripped--revocation-boundary-just-fresh C1 × validation-material-stripped + revocation-boundary-just-fresh | reject | reject | yes | 19655 | 339.608 | archive-material-insufficient, broker-policy-violation |
| P-0213-validation-material-stripped--scope-unknown C1 × validation-material-stripped + scope-unknown | reject | reject | yes | 19487 | 363.978 | archive-material-insufficient, broker-policy-violation, scope-mismatch |
| P-0214-validation-material-stripped--action-issuer-retired-after-cutoff C1 × validation-material-stripped + action-issuer-retired-after-cutoff | reject | reject | yes | 19713 | 348.409 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0304-identity-assurance-low--binding-dangling-identity C1 × identity-assurance-low + binding-dangling-identity | reject | reject | yes | 19491 | 357.972 | broker-policy-violation, identity-assurance-insufficient, identity-hash-missing |
| P-0305-identity-assurance-low--broker-untrusted C1 × identity-assurance-low + broker-untrusted | reject | reject | yes | 19453 | 353.643 | broker-policy-violation, identity-assurance-insufficient |
| P-0306-identity-assurance-low--broker-assurance-low C1 × identity-assurance-low + broker-assurance-low | reject | reject | yes | 19492 | 348.924 | broker-policy-violation, identity-assurance-insufficient |
| P-0307-identity-assurance-low--identity-method-unknown C1 × identity-assurance-low + identity-method-unknown | reject | reject | yes | 19527 | 343.447 | identity-assurance-insufficient, identity-method-unaccepted |
| P-0308-identity-assurance-low--identity-issuer-unknown C1 × identity-assurance-low + identity-issuer-unknown | reject | reject | yes | 19526 | 354.996 | identity-assurance-insufficient, identity-issuer-untrusted |
| P-0309-identity-assurance-low--live-lookup-under-offline-policy C1 × identity-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19612 | 369.729 | identity-assurance-insufficient, network-dependency-forbidden |
| P-0310-identity-assurance-low--sequence-replay-duplicate C1 × identity-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24612 | 456.022 | identity-assurance-insufficient, sequence-replay |
| P-0311-identity-assurance-low--revocation-missing C1 × identity-assurance-low + revocation-missing | reject | reject | yes | 19420 | 347.287 | identity-assurance-insufficient, revocation-missing |
| P-0312-identity-assurance-low--revocation-boundary-just-fresh C1 × identity-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19593 | 354.697 | identity-assurance-insufficient |
| P-0313-identity-assurance-low--scope-unknown C1 × identity-assurance-low + scope-unknown | reject | reject | yes | 19425 | 352.282 | identity-assurance-insufficient, scope-mismatch |
| P-0314-identity-assurance-low--action-issuer-retired-after-cutoff C1 × identity-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19651 | 367.207 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0405-binding-dangling-identity--broker-untrusted C1 × binding-dangling-identity + broker-untrusted | reject | reject | yes | 19432 | 350.360 | broker-policy-violation, identity-hash-missing |
| P-0406-binding-dangling-identity--broker-assurance-low C1 × binding-dangling-identity + broker-assurance-low | reject | reject | yes | 19471 | 352.721 | broker-policy-violation, identity-hash-missing |
| P-0407-binding-dangling-identity--identity-method-unknown C1 × binding-dangling-identity + identity-method-unknown | reject | reject | yes | 19506 | 345.002 | broker-policy-violation, identity-hash-missing, identity-method-unaccepted |
| P-0408-binding-dangling-identity--identity-issuer-unknown C1 × binding-dangling-identity + identity-issuer-unknown | reject | reject | yes | 19504 | 358.581 | broker-policy-violation, identity-hash-missing, identity-issuer-untrusted |
| P-0409-binding-dangling-identity--live-lookup-under-offline-policy C1 × binding-dangling-identity + live-lookup-under-offline-policy | reject | reject | yes | 19591 | 345.356 | broker-policy-violation, identity-hash-missing, network-dependency-forbidden |
| P-0410-binding-dangling-identity--sequence-replay-duplicate C1 × binding-dangling-identity + sequence-replay-duplicate | reject | reject | yes | 24548 | 448.354 | broker-policy-violation, identity-hash-missing, sequence-replay |
| P-0411-binding-dangling-identity--revocation-missing C1 × binding-dangling-identity + revocation-missing | reject | reject | yes | 19399 | 356.693 | broker-policy-violation, identity-hash-missing, revocation-missing |
| P-0412-binding-dangling-identity--revocation-boundary-just-fresh C1 × binding-dangling-identity + revocation-boundary-just-fresh | reject | reject | yes | 19572 | 365.009 | broker-policy-violation, identity-hash-missing |
| P-0413-binding-dangling-identity--scope-unknown C1 × binding-dangling-identity + scope-unknown | reject | reject | yes | 19404 | 339.115 | broker-policy-violation, identity-hash-missing, scope-mismatch |
| P-0414-binding-dangling-identity--action-issuer-retired-after-cutoff C1 × binding-dangling-identity + action-issuer-retired-after-cutoff | reject | reject | yes | 19630 | 357.307 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0506-broker-untrusted--broker-assurance-low C1 × broker-untrusted + broker-assurance-low | reject | reject | yes | 19433 | 361.050 | broker-policy-violation |
| P-0507-broker-untrusted--identity-method-unknown C1 × broker-untrusted + identity-method-unknown | reject | reject | yes | 19468 | 361.270 | broker-policy-violation, identity-method-unaccepted |
| P-0508-broker-untrusted--identity-issuer-unknown C1 × broker-untrusted + identity-issuer-unknown | reject | reject | yes | 19467 | 352.597 | broker-policy-violation, identity-issuer-untrusted |
| P-0509-broker-untrusted--live-lookup-under-offline-policy C1 × broker-untrusted + live-lookup-under-offline-policy | reject | reject | yes | 19553 | 342.766 | broker-policy-violation, network-dependency-forbidden |
| P-0510-broker-untrusted--sequence-replay-duplicate C1 × broker-untrusted + sequence-replay-duplicate | reject | reject | yes | 24535 | 450.694 | broker-policy-violation, sequence-replay |
| P-0511-broker-untrusted--revocation-missing C1 × broker-untrusted + revocation-missing | reject | reject | yes | 19361 | 349.129 | broker-policy-violation, revocation-missing |
| P-0512-broker-untrusted--revocation-boundary-just-fresh C1 × broker-untrusted + revocation-boundary-just-fresh | reject | reject | yes | 19534 | 364.749 | broker-policy-violation |
| P-0513-broker-untrusted--scope-unknown C1 × broker-untrusted + scope-unknown | reject | reject | yes | 19366 | 355.166 | broker-policy-violation, scope-mismatch |
| P-0514-broker-untrusted--action-issuer-retired-after-cutoff C1 × broker-untrusted + action-issuer-retired-after-cutoff | reject | reject | yes | 19592 | 352.644 | action-issuer-untrusted, broker-policy-violation |
| P-0607-broker-assurance-low--identity-method-unknown C1 × broker-assurance-low + identity-method-unknown | reject | reject | yes | 19507 | 346.540 | broker-policy-violation, identity-method-unaccepted |
| P-0608-broker-assurance-low--identity-issuer-unknown C1 × broker-assurance-low + identity-issuer-unknown | reject | reject | yes | 19506 | 359.911 | broker-policy-violation, identity-issuer-untrusted |
| P-0609-broker-assurance-low--live-lookup-under-offline-policy C1 × broker-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19592 | 360.052 | broker-policy-violation, network-dependency-forbidden |
| P-0610-broker-assurance-low--sequence-replay-duplicate C1 × broker-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24585 | 459.491 | broker-policy-violation, sequence-replay |
| P-0611-broker-assurance-low--revocation-missing C1 × broker-assurance-low + revocation-missing | reject | reject | yes | 19400 | 375.287 | broker-policy-violation, revocation-missing |
| P-0612-broker-assurance-low--revocation-boundary-just-fresh C1 × broker-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19573 | 357.480 | broker-policy-violation |
| P-0613-broker-assurance-low--scope-unknown C1 × broker-assurance-low + scope-unknown | reject | reject | yes | 19405 | 354.383 | broker-policy-violation, scope-mismatch |
| P-0614-broker-assurance-low--action-issuer-retired-after-cutoff C1 × broker-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19631 | 343.436 | action-issuer-untrusted, broker-policy-violation |
| P-0708-identity-method-unknown--identity-issuer-unknown C1 × identity-method-unknown + identity-issuer-unknown | reject | reject | yes | 19541 | 347.767 | identity-issuer-untrusted, identity-method-unaccepted |
| P-0709-identity-method-unknown--live-lookup-under-offline-policy C1 × identity-method-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19627 | 351.542 | identity-method-unaccepted, network-dependency-forbidden |
| P-0710-identity-method-unknown--sequence-replay-duplicate C1 × identity-method-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 439.046 | identity-method-unaccepted, sequence-replay |
| P-0711-identity-method-unknown--revocation-missing C1 × identity-method-unknown + revocation-missing | reject | reject | yes | 19435 | 366.371 | identity-method-unaccepted, revocation-missing |
| P-0712-identity-method-unknown--revocation-boundary-just-fresh C1 × identity-method-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19608 | 356.465 | identity-method-unaccepted |
| P-0713-identity-method-unknown--scope-unknown C1 × identity-method-unknown + scope-unknown | reject | reject | yes | 19440 | 367.875 | identity-method-unaccepted, scope-mismatch |
| P-0714-identity-method-unknown--action-issuer-retired-after-cutoff C1 × identity-method-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19666 | 360.108 | action-issuer-untrusted, identity-method-unaccepted |
| P-0809-identity-issuer-unknown--live-lookup-under-offline-policy C1 × identity-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19626 | 361.899 | identity-issuer-untrusted, network-dependency-forbidden |
| P-0810-identity-issuer-unknown--sequence-replay-duplicate C1 × identity-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 443.576 | identity-issuer-untrusted, sequence-replay |
| P-0811-identity-issuer-unknown--revocation-missing C1 × identity-issuer-unknown + revocation-missing | reject | reject | yes | 19434 | 357.771 | identity-issuer-untrusted, revocation-missing |
| P-0812-identity-issuer-unknown--revocation-boundary-just-fresh C1 × identity-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19607 | 357.525 | identity-issuer-untrusted |
| P-0813-identity-issuer-unknown--scope-unknown C1 × identity-issuer-unknown + scope-unknown | reject | reject | yes | 19439 | 340.966 | identity-issuer-untrusted, scope-mismatch |
| P-0814-identity-issuer-unknown--action-issuer-retired-after-cutoff C1 × identity-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19665 | 352.769 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0910-live-lookup-under-offline-policy--sequence-replay-duplicate C1 × live-lookup-under-offline-policy + sequence-replay-duplicate | reject | reject | yes | 24741 | 434.519 | network-dependency-forbidden, sequence-replay |
| P-0911-live-lookup-under-offline-policy--revocation-missing C1 × live-lookup-under-offline-policy + revocation-missing | reject | reject | yes | 19520 | 350.995 | network-dependency-forbidden, revocation-missing |
| P-0912-live-lookup-under-offline-policy--revocation-boundary-just-fresh C1 × live-lookup-under-offline-policy + revocation-boundary-just-fresh | reject | reject | yes | 19693 | 348.412 | network-dependency-forbidden |
| P-0913-live-lookup-under-offline-policy--scope-unknown C1 × live-lookup-under-offline-policy + scope-unknown | reject | reject | yes | 19525 | 341.327 | network-dependency-forbidden, scope-mismatch |
| P-0914-live-lookup-under-offline-policy--action-issuer-retired-after-cutoff C1 × live-lookup-under-offline-policy + action-issuer-retired-after-cutoff | reject | reject | yes | 19751 | 358.690 | action-issuer-untrusted, network-dependency-forbidden |
| P-1011-sequence-replay-duplicate--revocation-missing C1 × sequence-replay-duplicate + revocation-missing | reject | reject | yes | 24508 | 433.093 | revocation-missing, sequence-replay |
| P-1012-sequence-replay-duplicate--revocation-boundary-just-fresh C1 × sequence-replay-duplicate + revocation-boundary-just-fresh | reject | reject | yes | 24717 | 443.942 | sequence-replay |
| P-1013-sequence-replay-duplicate--scope-unknown C1 × sequence-replay-duplicate + scope-unknown | reject | reject | yes | 24498 | 459.467 | scope-mismatch, sequence-replay |
| P-1014-sequence-replay-duplicate--action-issuer-retired-after-cutoff C1 × sequence-replay-duplicate + action-issuer-retired-after-cutoff | reject | reject | yes | 24787 | 445.451 | action-issuer-untrusted, sequence-replay |
| P-1112-revocation-missing--revocation-boundary-just-fresh C1 × revocation-missing + revocation-boundary-just-fresh | accept | accept | yes | 19554 | 368.053 | - |
| P-1113-revocation-missing--scope-unknown C1 × revocation-missing + scope-unknown | reject | reject | yes | 19333 | 357.784 | revocation-missing, scope-mismatch |
| P-1114-revocation-missing--action-issuer-retired-after-cutoff C1 × revocation-missing + action-issuer-retired-after-cutoff | reject | reject | yes | 19559 | 357.362 | action-issuer-untrusted, revocation-missing |
| P-1213-revocation-boundary-just-fresh--scope-unknown C1 × revocation-boundary-just-fresh + scope-unknown | reject | reject | yes | 19506 | 342.336 | scope-mismatch |
| P-1214-revocation-boundary-just-fresh--action-issuer-retired-after-cutoff C1 × revocation-boundary-just-fresh + action-issuer-retired-after-cutoff | reject | reject | yes | 19732 | 367.569 | action-issuer-untrusted |
| P-1314-scope-unknown--action-issuer-retired-after-cutoff C1 × scope-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19564 | 360.325 | action-issuer-untrusted, scope-mismatch |
