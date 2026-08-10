# EATF-Backed Multi-Root Evaluation Summary

- Cases: 192/192 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 3424310.
- Total EATF verify ms: 63031.155.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| M-C1-000-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 19307 | 356.331 | identity-issuer-untrusted |
| M-C1-001-identity-method-unknown C1 × identity-method-unknown @ identity[0] | reject | reject | yes | 19308 | 361.575 | identity-method-unaccepted |
| M-C1-002-identity-assurance-low C1 × identity-assurance-low @ identity[0] | reject | reject | yes | 19293 | 358.816 | identity-assurance-insufficient |
| M-C1-003-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 19416 | 359.000 | - |
| M-C1-004-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[1] | reject | reject | yes | 19307 | 354.813 | identity-issuer-untrusted |
| M-C1-005-identity-method-unknown C1 × identity-method-unknown @ identity[1] | reject | reject | yes | 19308 | 355.155 | identity-method-unaccepted |
| M-C1-006-identity-assurance-low C1 × identity-assurance-low @ identity[1] | reject | reject | yes | 19293 | 351.343 | identity-assurance-insufficient |
| M-C1-007-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[1] | accept | accept | yes | 19416 | 346.929 | - |
| M-C1-008-action-issuer-unknown C1 × action-issuer-unknown @ action[0] | reject | reject | yes | 19287 | 345.696 | action-issuer-untrusted |
| M-C1-009-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 19432 | 351.314 | action-issuer-untrusted |
| M-C1-010-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 19442 | 360.552 | - |
| M-C1-011-binding-dangling-identity C1 × binding-dangling-identity @ action[0] | reject | reject | yes | 19272 | 355.621 | broker-policy-violation, identity-hash-missing |
| M-C1-012-binding-subject-substitution C1 × binding-subject-substitution @ action[0] | reject | reject | yes | 19360 | 356.575 | identity-substitution |
| M-C1-013-scope-unknown C1 × scope-unknown @ action[0] | reject | reject | yes | 19206 | 371.840 | scope-mismatch |
| M-C1-014-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 19393 | 365.297 | network-dependency-forbidden |
| M-C1-015-validation-material-stripped C1 × validation-material-stripped @ action[0] | reject | reject | yes | 19355 | 339.562 | archive-material-insufficient, broker-policy-violation |
| M-C1-016-revocation-missing C1 × revocation-missing @ action[0] | reject | reject | yes | 19201 | 368.050 | revocation-missing |
| M-C1-017-revocation-stale-8d C1 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 19264 | 346.411 | revocation-stale |
| M-C1-018-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 19374 | 371.239 | - |
| M-C1-019-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 19374 | 350.594 | revocation-stale |
| M-C1-020-algorithm-unknown C1 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 19241 | 370.528 | algorithm-unaccepted |
| M-C1-021-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 19285 | 346.107 | - |
| M-C1-022-broker-untrusted C1 × broker-untrusted @ action[0] | reject | reject | yes | 19234 | 364.673 | broker-policy-violation |
| M-C1-023-broker-assurance-low C1 × broker-assurance-low @ action[0] | reject | reject | yes | 19273 | 372.271 | broker-policy-violation |
| M-C1-024-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[0] | accept | accept | yes | 19396 | 362.624 | - |
| M-C1-025-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[0] | reject | reject | yes | 19423 | 352.770 | broker-policy-violation |
| M-C1-026-broker-removed C1 × broker-removed @ action[0] | accept | accept | yes | 19025 | 348.314 | - |
| M-C1-027-action-issuer-unknown C1 × action-issuer-unknown @ action[1] | reject | reject | yes | 19287 | 346.816 | action-issuer-untrusted |
| M-C1-028-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[1] | reject | reject | yes | 19432 | 344.583 | action-issuer-untrusted |
| M-C1-029-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[1] | accept | accept | yes | 19442 | 353.062 | - |
| M-C1-030-binding-dangling-identity C1 × binding-dangling-identity @ action[1] | reject | reject | yes | 19273 | 362.221 | broker-policy-violation, identity-hash-missing |
| M-C1-031-binding-subject-substitution C1 × binding-subject-substitution @ action[1] | reject | reject | yes | 19363 | 366.282 | identity-substitution |
| M-C1-032-scope-unknown C1 × scope-unknown @ action[1] | reject | reject | yes | 19204 | 380.851 | scope-mismatch |
| M-C1-033-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[1] | reject | reject | yes | 19393 | 360.221 | network-dependency-forbidden |
| M-C1-034-validation-material-stripped C1 × validation-material-stripped @ action[1] | reject | reject | yes | 19355 | 376.801 | archive-material-insufficient, broker-policy-violation |
| M-C1-035-revocation-missing C1 × revocation-missing @ action[1] | reject | reject | yes | 19201 | 362.891 | revocation-missing |
| M-C1-036-revocation-stale-8d C1 × revocation-stale-8d @ action[1] | indeterminate | indeterminate | yes | 19264 | 362.611 | revocation-stale |
| M-C1-037-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[1] | accept | accept | yes | 19374 | 354.624 | - |
| M-C1-038-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[1] | indeterminate | indeterminate | yes | 19374 | 345.483 | revocation-stale |
| M-C1-039-algorithm-unknown C1 × algorithm-unknown @ action[1] | indeterminate | indeterminate | yes | 19241 | 350.064 | algorithm-unaccepted |
| M-C1-040-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[1] | accept | accept | yes | 19285 | 354.545 | - |
| M-C1-041-broker-untrusted C1 × broker-untrusted @ action[1] | reject | reject | yes | 19234 | 377.740 | broker-policy-violation |
| M-C1-042-broker-assurance-low C1 × broker-assurance-low @ action[1] | reject | reject | yes | 19273 | 373.729 | broker-policy-violation |
| M-C1-043-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[1] | accept | accept | yes | 19396 | 362.232 | - |
| M-C1-044-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[1] | reject | reject | yes | 19423 | 363.075 | broker-policy-violation |
| M-C1-045-broker-removed C1 × broker-removed @ action[1] | accept | accept | yes | 19025 | 362.416 | - |
| M-C1-046-sequence-replay-duplicate C1 × sequence-replay-duplicate @ case | reject | reject | yes | 24327 | 440.120 | sequence-replay |
| M-C2-000-identity-issuer-unknown C2 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9499 | 175.607 | identity-issuer-untrusted |
| M-C2-001-identity-method-unknown C2 × identity-method-unknown @ identity[0] | reject | reject | yes | 9501 | 171.237 | identity-method-unaccepted |
| M-C2-002-identity-assurance-low C2 × identity-assurance-low @ identity[0] | reject | reject | yes | 9491 | 183.287 | identity-assurance-insufficient |
| M-C2-003-identity-assurance-medium-boundary C2 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9554 | 173.487 | - |
| M-C2-004-action-issuer-unknown C2 × action-issuer-unknown @ action[0] | reject | reject | yes | 9489 | 177.250 | action-issuer-untrusted |
| M-C2-005-action-issuer-retired-after-cutoff C2 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9564 | 179.382 | action-issuer-untrusted |
| M-C2-006-action-issuer-retired-grandfathered C2 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9569 | 175.198 | - |
| M-C2-007-binding-dangling-identity C2 × binding-dangling-identity @ action[0] | reject | reject | yes | 9507 | 171.849 | identity-hash-missing |
| M-C2-008-binding-subject-substitution C2 × binding-subject-substitution @ action[0] | reject | reject | yes | 9528 | 174.080 | identity-substitution |
| M-C2-009-scope-unknown C2 × scope-unknown @ action[0] | reject | reject | yes | 9449 | 171.688 | scope-mismatch |
| M-C2-010-live-lookup-under-offline-policy C2 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9541 | 180.029 | network-dependency-forbidden |
| M-C2-011-validation-material-stripped C2 × validation-material-stripped @ action[0] | reject | reject | yes | 9523 | 178.106 | archive-material-insufficient |
| M-C2-012-revocation-missing C2 × revocation-missing @ action[0] | reject | reject | yes | 9419 | 192.832 | revocation-missing |
| M-C2-013-revocation-stale-8d C2 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9477 | 183.980 | revocation-stale |
| M-C2-014-revocation-boundary-just-fresh C2 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9532 | 192.845 | - |
| M-C2-015-revocation-boundary-just-stale C2 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9532 | 170.026 | revocation-stale |
| M-C2-016-algorithm-unknown C2 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9464 | 182.117 | algorithm-unaccepted |
| M-C2-017-algorithm-pqc-accepted C2 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9483 | 179.218 | - |
| M-C2-018-broker-added-untrusted C2 × broker-added-untrusted @ action[0] | reject | reject | yes | 9681 | 183.552 | broker-policy-violation |
| M-C2-019-sequence-replay-duplicate C2 × sequence-replay-duplicate @ case | reject | reject | yes | 14353 | 280.090 | sequence-replay |
| M-C8-000-identity-issuer-unknown C8 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9504 | 183.899 | identity-issuer-untrusted |
| M-C8-001-identity-method-unknown C8 × identity-method-unknown @ identity[0] | reject | reject | yes | 9506 | 179.731 | identity-method-unaccepted |
| M-C8-002-identity-assurance-low C8 × identity-assurance-low @ identity[0] | reject | reject | yes | 9496 | 176.565 | identity-assurance-insufficient |
| M-C8-003-identity-assurance-medium-boundary C8 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9559 | 180.059 | - |
| M-C8-004-action-issuer-unknown C8 × action-issuer-unknown @ action[0] | reject | reject | yes | 9494 | 178.836 | action-issuer-untrusted |
| M-C8-005-action-issuer-retired-after-cutoff C8 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9569 | 181.976 | action-issuer-untrusted |
| M-C8-006-action-issuer-retired-grandfathered C8 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9574 | 172.071 | - |
| M-C8-007-binding-dangling-identity C8 × binding-dangling-identity @ action[0] | reject | reject | yes | 9513 | 174.397 | identity-hash-missing |
| M-C8-008-binding-subject-substitution C8 × binding-subject-substitution @ action[0] | reject | reject | yes | 9536 | 175.989 | identity-substitution |
| M-C8-009-scope-unknown C8 × scope-unknown @ action[0] | reject | reject | yes | 9452 | 179.212 | scope-mismatch |
| M-C8-010-live-lookup-under-offline-policy C8 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9546 | 180.479 | network-dependency-forbidden |
| M-C8-011-validation-material-stripped C8 × validation-material-stripped @ action[0] | reject | reject | yes | 9528 | 178.233 | archive-material-insufficient |
| M-C8-012-revocation-missing C8 × revocation-missing @ action[0] | reject | reject | yes | 9424 | 168.566 | revocation-missing |
| M-C8-013-revocation-stale-8d C8 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9482 | 181.141 | revocation-stale |
| M-C8-014-revocation-boundary-just-fresh C8 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9537 | 170.334 | - |
| M-C8-015-revocation-boundary-just-stale C8 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9537 | 181.363 | revocation-stale |
| M-C8-016-algorithm-unknown C8 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9469 | 182.767 | algorithm-unaccepted |
| M-C8-017-algorithm-pqc-accepted C8 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9488 | 184.549 | - |
| M-C8-018-broker-added-untrusted C8 × broker-added-untrusted @ action[0] | reject | reject | yes | 9686 | 174.703 | broker-policy-violation |
| M-C8-019-sequence-replay-duplicate C8 × sequence-replay-duplicate @ case | reject | reject | yes | 14368 | 272.493 | sequence-replay |
| P-0001-action-issuer-unknown--algorithm-unknown C1 × action-issuer-unknown + algorithm-unknown | reject | reject | yes | 19454 | 352.466 | action-issuer-untrusted, algorithm-unaccepted |
| P-0002-action-issuer-unknown--validation-material-stripped C1 × action-issuer-unknown + validation-material-stripped | reject | reject | yes | 19568 | 352.883 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0003-action-issuer-unknown--identity-assurance-low C1 × action-issuer-unknown + identity-assurance-low | reject | reject | yes | 19506 | 352.639 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0004-action-issuer-unknown--binding-dangling-identity C1 × action-issuer-unknown + binding-dangling-identity | reject | reject | yes | 19485 | 362.311 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0005-action-issuer-unknown--broker-untrusted C1 × action-issuer-unknown + broker-untrusted | reject | reject | yes | 19447 | 354.204 | action-issuer-untrusted, broker-policy-violation |
| P-0006-action-issuer-unknown--broker-assurance-low C1 × action-issuer-unknown + broker-assurance-low | reject | reject | yes | 19486 | 363.653 | action-issuer-untrusted, broker-policy-violation |
| P-0007-action-issuer-unknown--identity-method-unknown C1 × action-issuer-unknown + identity-method-unknown | reject | reject | yes | 19521 | 369.121 | action-issuer-untrusted, identity-method-unaccepted |
| P-0008-action-issuer-unknown--identity-issuer-unknown C1 × action-issuer-unknown + identity-issuer-unknown | reject | reject | yes | 19520 | 362.852 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0009-action-issuer-unknown--live-lookup-under-offline-policy C1 × action-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19606 | 362.260 | action-issuer-untrusted, network-dependency-forbidden |
| P-0010-action-issuer-unknown--sequence-replay-duplicate C1 × action-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24606 | 438.209 | action-issuer-untrusted, sequence-replay |
| P-0011-action-issuer-unknown--revocation-missing C1 × action-issuer-unknown + revocation-missing | reject | reject | yes | 19414 | 349.339 | action-issuer-untrusted, revocation-missing |
| P-0012-action-issuer-unknown--revocation-boundary-just-fresh C1 × action-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19587 | 359.091 | action-issuer-untrusted |
| P-0013-action-issuer-unknown--scope-unknown C1 × action-issuer-unknown + scope-unknown | reject | reject | yes | 19419 | 365.702 | action-issuer-untrusted, scope-mismatch |
| P-0014-action-issuer-unknown--action-issuer-retired-after-cutoff C1 × action-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19642 | 355.016 | action-issuer-untrusted |
| P-0102-algorithm-unknown--validation-material-stripped C1 × algorithm-unknown + validation-material-stripped | reject | reject | yes | 19522 | 350.572 | algorithm-unaccepted, archive-material-insufficient, broker-policy-violation |
| P-0103-algorithm-unknown--identity-assurance-low C1 × algorithm-unknown + identity-assurance-low | reject | reject | yes | 19460 | 349.014 | algorithm-unaccepted, identity-assurance-insufficient |
| P-0104-algorithm-unknown--binding-dangling-identity C1 × algorithm-unknown + binding-dangling-identity | reject | reject | yes | 19439 | 365.048 | algorithm-unaccepted, broker-policy-violation, identity-hash-missing |
| P-0105-algorithm-unknown--broker-untrusted C1 × algorithm-unknown + broker-untrusted | reject | reject | yes | 19401 | 338.712 | algorithm-unaccepted, broker-policy-violation |
| P-0106-algorithm-unknown--broker-assurance-low C1 × algorithm-unknown + broker-assurance-low | reject | reject | yes | 19440 | 359.291 | algorithm-unaccepted, broker-policy-violation |
| P-0107-algorithm-unknown--identity-method-unknown C1 × algorithm-unknown + identity-method-unknown | reject | reject | yes | 19475 | 350.743 | algorithm-unaccepted, identity-method-unaccepted |
| P-0108-algorithm-unknown--identity-issuer-unknown C1 × algorithm-unknown + identity-issuer-unknown | reject | reject | yes | 19474 | 343.617 | algorithm-unaccepted, identity-issuer-untrusted |
| P-0109-algorithm-unknown--live-lookup-under-offline-policy C1 × algorithm-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19560 | 355.532 | algorithm-unaccepted, network-dependency-forbidden |
| P-0110-algorithm-unknown--sequence-replay-duplicate C1 × algorithm-unknown + sequence-replay-duplicate | reject | reject | yes | 24542 | 431.052 | algorithm-unaccepted, sequence-replay |
| P-0111-algorithm-unknown--revocation-missing C1 × algorithm-unknown + revocation-missing | reject | reject | yes | 19368 | 361.591 | algorithm-unaccepted, revocation-missing |
| P-0112-algorithm-unknown--revocation-boundary-just-fresh C1 × algorithm-unknown + revocation-boundary-just-fresh | indeterminate | indeterminate | yes | 19541 | 349.248 | algorithm-unaccepted |
| P-0113-algorithm-unknown--scope-unknown C1 × algorithm-unknown + scope-unknown | reject | reject | yes | 19373 | 366.602 | algorithm-unaccepted, scope-mismatch |
| P-0114-algorithm-unknown--action-issuer-retired-after-cutoff C1 × algorithm-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19599 | 354.733 | action-issuer-untrusted, algorithm-unaccepted |
| P-0203-validation-material-stripped--identity-assurance-low C1 × validation-material-stripped + identity-assurance-low | reject | reject | yes | 19574 | 361.702 | archive-material-insufficient, broker-policy-violation, identity-assurance-insufficient |
| P-0204-validation-material-stripped--binding-dangling-identity C1 × validation-material-stripped + binding-dangling-identity | reject | reject | yes | 19553 | 351.529 | archive-material-insufficient, broker-policy-violation, identity-hash-missing |
| P-0205-validation-material-stripped--broker-untrusted C1 × validation-material-stripped + broker-untrusted | reject | reject | yes | 19515 | 349.328 | archive-material-insufficient, broker-policy-violation |
| P-0206-validation-material-stripped--broker-assurance-low C1 × validation-material-stripped + broker-assurance-low | reject | reject | yes | 19554 | 374.132 | archive-material-insufficient, broker-policy-violation |
| P-0207-validation-material-stripped--identity-method-unknown C1 × validation-material-stripped + identity-method-unknown | reject | reject | yes | 19589 | 376.041 | archive-material-insufficient, broker-policy-violation, identity-method-unaccepted |
| P-0208-validation-material-stripped--identity-issuer-unknown C1 × validation-material-stripped + identity-issuer-unknown | reject | reject | yes | 19588 | 357.694 | archive-material-insufficient, broker-policy-violation, identity-issuer-untrusted |
| P-0209-validation-material-stripped--live-lookup-under-offline-policy C1 × validation-material-stripped + live-lookup-under-offline-policy | reject | reject | yes | 19674 | 353.376 | archive-material-insufficient, broker-policy-violation, network-dependency-forbidden |
| P-0210-validation-material-stripped--sequence-replay-duplicate C1 × validation-material-stripped + sequence-replay-duplicate | reject | reject | yes | 24693 | 450.422 | archive-material-insufficient, broker-policy-violation, sequence-replay |
| P-0211-validation-material-stripped--revocation-missing C1 × validation-material-stripped + revocation-missing | reject | reject | yes | 19482 | 370.338 | archive-material-insufficient, broker-policy-violation, revocation-missing |
| P-0212-validation-material-stripped--revocation-boundary-just-fresh C1 × validation-material-stripped + revocation-boundary-just-fresh | reject | reject | yes | 19655 | 373.600 | archive-material-insufficient, broker-policy-violation |
| P-0213-validation-material-stripped--scope-unknown C1 × validation-material-stripped + scope-unknown | reject | reject | yes | 19487 | 359.685 | archive-material-insufficient, broker-policy-violation, scope-mismatch |
| P-0214-validation-material-stripped--action-issuer-retired-after-cutoff C1 × validation-material-stripped + action-issuer-retired-after-cutoff | reject | reject | yes | 19713 | 358.117 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0304-identity-assurance-low--binding-dangling-identity C1 × identity-assurance-low + binding-dangling-identity | reject | reject | yes | 19491 | 350.117 | broker-policy-violation, identity-assurance-insufficient, identity-hash-missing |
| P-0305-identity-assurance-low--broker-untrusted C1 × identity-assurance-low + broker-untrusted | reject | reject | yes | 19453 | 364.651 | broker-policy-violation, identity-assurance-insufficient |
| P-0306-identity-assurance-low--broker-assurance-low C1 × identity-assurance-low + broker-assurance-low | reject | reject | yes | 19492 | 373.363 | broker-policy-violation, identity-assurance-insufficient |
| P-0307-identity-assurance-low--identity-method-unknown C1 × identity-assurance-low + identity-method-unknown | reject | reject | yes | 19527 | 349.455 | identity-assurance-insufficient, identity-method-unaccepted |
| P-0308-identity-assurance-low--identity-issuer-unknown C1 × identity-assurance-low + identity-issuer-unknown | reject | reject | yes | 19526 | 359.104 | identity-assurance-insufficient, identity-issuer-untrusted |
| P-0309-identity-assurance-low--live-lookup-under-offline-policy C1 × identity-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19612 | 358.025 | identity-assurance-insufficient, network-dependency-forbidden |
| P-0310-identity-assurance-low--sequence-replay-duplicate C1 × identity-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24612 | 445.891 | identity-assurance-insufficient, sequence-replay |
| P-0311-identity-assurance-low--revocation-missing C1 × identity-assurance-low + revocation-missing | reject | reject | yes | 19420 | 346.725 | identity-assurance-insufficient, revocation-missing |
| P-0312-identity-assurance-low--revocation-boundary-just-fresh C1 × identity-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19593 | 359.906 | identity-assurance-insufficient |
| P-0313-identity-assurance-low--scope-unknown C1 × identity-assurance-low + scope-unknown | reject | reject | yes | 19425 | 366.691 | identity-assurance-insufficient, scope-mismatch |
| P-0314-identity-assurance-low--action-issuer-retired-after-cutoff C1 × identity-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19651 | 372.380 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0405-binding-dangling-identity--broker-untrusted C1 × binding-dangling-identity + broker-untrusted | reject | reject | yes | 19432 | 361.911 | broker-policy-violation, identity-hash-missing |
| P-0406-binding-dangling-identity--broker-assurance-low C1 × binding-dangling-identity + broker-assurance-low | reject | reject | yes | 19471 | 363.185 | broker-policy-violation, identity-hash-missing |
| P-0407-binding-dangling-identity--identity-method-unknown C1 × binding-dangling-identity + identity-method-unknown | reject | reject | yes | 19506 | 356.542 | broker-policy-violation, identity-hash-missing, identity-method-unaccepted |
| P-0408-binding-dangling-identity--identity-issuer-unknown C1 × binding-dangling-identity + identity-issuer-unknown | reject | reject | yes | 19504 | 359.492 | broker-policy-violation, identity-hash-missing, identity-issuer-untrusted |
| P-0409-binding-dangling-identity--live-lookup-under-offline-policy C1 × binding-dangling-identity + live-lookup-under-offline-policy | reject | reject | yes | 19591 | 357.878 | broker-policy-violation, identity-hash-missing, network-dependency-forbidden |
| P-0410-binding-dangling-identity--sequence-replay-duplicate C1 × binding-dangling-identity + sequence-replay-duplicate | reject | reject | yes | 24548 | 466.357 | broker-policy-violation, identity-hash-missing, sequence-replay |
| P-0411-binding-dangling-identity--revocation-missing C1 × binding-dangling-identity + revocation-missing | reject | reject | yes | 19399 | 349.377 | broker-policy-violation, identity-hash-missing, revocation-missing |
| P-0412-binding-dangling-identity--revocation-boundary-just-fresh C1 × binding-dangling-identity + revocation-boundary-just-fresh | reject | reject | yes | 19572 | 343.666 | broker-policy-violation, identity-hash-missing |
| P-0413-binding-dangling-identity--scope-unknown C1 × binding-dangling-identity + scope-unknown | reject | reject | yes | 19404 | 363.227 | broker-policy-violation, identity-hash-missing, scope-mismatch |
| P-0414-binding-dangling-identity--action-issuer-retired-after-cutoff C1 × binding-dangling-identity + action-issuer-retired-after-cutoff | reject | reject | yes | 19630 | 340.220 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0506-broker-untrusted--broker-assurance-low C1 × broker-untrusted + broker-assurance-low | reject | reject | yes | 19433 | 362.667 | broker-policy-violation |
| P-0507-broker-untrusted--identity-method-unknown C1 × broker-untrusted + identity-method-unknown | reject | reject | yes | 19468 | 348.497 | broker-policy-violation, identity-method-unaccepted |
| P-0508-broker-untrusted--identity-issuer-unknown C1 × broker-untrusted + identity-issuer-unknown | reject | reject | yes | 19467 | 357.368 | broker-policy-violation, identity-issuer-untrusted |
| P-0509-broker-untrusted--live-lookup-under-offline-policy C1 × broker-untrusted + live-lookup-under-offline-policy | reject | reject | yes | 19553 | 360.978 | broker-policy-violation, network-dependency-forbidden |
| P-0510-broker-untrusted--sequence-replay-duplicate C1 × broker-untrusted + sequence-replay-duplicate | reject | reject | yes | 24535 | 446.270 | broker-policy-violation, sequence-replay |
| P-0511-broker-untrusted--revocation-missing C1 × broker-untrusted + revocation-missing | reject | reject | yes | 19361 | 355.718 | broker-policy-violation, revocation-missing |
| P-0512-broker-untrusted--revocation-boundary-just-fresh C1 × broker-untrusted + revocation-boundary-just-fresh | reject | reject | yes | 19534 | 354.506 | broker-policy-violation |
| P-0513-broker-untrusted--scope-unknown C1 × broker-untrusted + scope-unknown | reject | reject | yes | 19366 | 351.232 | broker-policy-violation, scope-mismatch |
| P-0514-broker-untrusted--action-issuer-retired-after-cutoff C1 × broker-untrusted + action-issuer-retired-after-cutoff | reject | reject | yes | 19592 | 352.843 | action-issuer-untrusted, broker-policy-violation |
| P-0607-broker-assurance-low--identity-method-unknown C1 × broker-assurance-low + identity-method-unknown | reject | reject | yes | 19507 | 371.160 | broker-policy-violation, identity-method-unaccepted |
| P-0608-broker-assurance-low--identity-issuer-unknown C1 × broker-assurance-low + identity-issuer-unknown | reject | reject | yes | 19506 | 369.186 | broker-policy-violation, identity-issuer-untrusted |
| P-0609-broker-assurance-low--live-lookup-under-offline-policy C1 × broker-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19592 | 353.891 | broker-policy-violation, network-dependency-forbidden |
| P-0610-broker-assurance-low--sequence-replay-duplicate C1 × broker-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24585 | 443.376 | broker-policy-violation, sequence-replay |
| P-0611-broker-assurance-low--revocation-missing C1 × broker-assurance-low + revocation-missing | reject | reject | yes | 19400 | 348.956 | broker-policy-violation, revocation-missing |
| P-0612-broker-assurance-low--revocation-boundary-just-fresh C1 × broker-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19573 | 350.460 | broker-policy-violation |
| P-0613-broker-assurance-low--scope-unknown C1 × broker-assurance-low + scope-unknown | reject | reject | yes | 19405 | 339.328 | broker-policy-violation, scope-mismatch |
| P-0614-broker-assurance-low--action-issuer-retired-after-cutoff C1 × broker-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19631 | 349.221 | action-issuer-untrusted, broker-policy-violation |
| P-0708-identity-method-unknown--identity-issuer-unknown C1 × identity-method-unknown + identity-issuer-unknown | reject | reject | yes | 19541 | 349.477 | identity-issuer-untrusted, identity-method-unaccepted |
| P-0709-identity-method-unknown--live-lookup-under-offline-policy C1 × identity-method-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19627 | 353.041 | identity-method-unaccepted, network-dependency-forbidden |
| P-0710-identity-method-unknown--sequence-replay-duplicate C1 × identity-method-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 437.194 | identity-method-unaccepted, sequence-replay |
| P-0711-identity-method-unknown--revocation-missing C1 × identity-method-unknown + revocation-missing | reject | reject | yes | 19435 | 373.951 | identity-method-unaccepted, revocation-missing |
| P-0712-identity-method-unknown--revocation-boundary-just-fresh C1 × identity-method-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19608 | 359.177 | identity-method-unaccepted |
| P-0713-identity-method-unknown--scope-unknown C1 × identity-method-unknown + scope-unknown | reject | reject | yes | 19440 | 351.054 | identity-method-unaccepted, scope-mismatch |
| P-0714-identity-method-unknown--action-issuer-retired-after-cutoff C1 × identity-method-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19666 | 369.537 | action-issuer-untrusted, identity-method-unaccepted |
| P-0809-identity-issuer-unknown--live-lookup-under-offline-policy C1 × identity-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19626 | 375.003 | identity-issuer-untrusted, network-dependency-forbidden |
| P-0810-identity-issuer-unknown--sequence-replay-duplicate C1 × identity-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 455.097 | identity-issuer-untrusted, sequence-replay |
| P-0811-identity-issuer-unknown--revocation-missing C1 × identity-issuer-unknown + revocation-missing | reject | reject | yes | 19434 | 347.157 | identity-issuer-untrusted, revocation-missing |
| P-0812-identity-issuer-unknown--revocation-boundary-just-fresh C1 × identity-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19607 | 360.022 | identity-issuer-untrusted |
| P-0813-identity-issuer-unknown--scope-unknown C1 × identity-issuer-unknown + scope-unknown | reject | reject | yes | 19439 | 369.918 | identity-issuer-untrusted, scope-mismatch |
| P-0814-identity-issuer-unknown--action-issuer-retired-after-cutoff C1 × identity-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19665 | 353.928 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0910-live-lookup-under-offline-policy--sequence-replay-duplicate C1 × live-lookup-under-offline-policy + sequence-replay-duplicate | reject | reject | yes | 24741 | 435.700 | network-dependency-forbidden, sequence-replay |
| P-0911-live-lookup-under-offline-policy--revocation-missing C1 × live-lookup-under-offline-policy + revocation-missing | reject | reject | yes | 19520 | 347.674 | network-dependency-forbidden, revocation-missing |
| P-0912-live-lookup-under-offline-policy--revocation-boundary-just-fresh C1 × live-lookup-under-offline-policy + revocation-boundary-just-fresh | reject | reject | yes | 19693 | 351.667 | network-dependency-forbidden |
| P-0913-live-lookup-under-offline-policy--scope-unknown C1 × live-lookup-under-offline-policy + scope-unknown | reject | reject | yes | 19525 | 370.382 | network-dependency-forbidden, scope-mismatch |
| P-0914-live-lookup-under-offline-policy--action-issuer-retired-after-cutoff C1 × live-lookup-under-offline-policy + action-issuer-retired-after-cutoff | reject | reject | yes | 19751 | 340.779 | action-issuer-untrusted, network-dependency-forbidden |
| P-1011-sequence-replay-duplicate--revocation-missing C1 × sequence-replay-duplicate + revocation-missing | reject | reject | yes | 24508 | 433.770 | revocation-missing, sequence-replay |
| P-1012-sequence-replay-duplicate--revocation-boundary-just-fresh C1 × sequence-replay-duplicate + revocation-boundary-just-fresh | reject | reject | yes | 24717 | 453.463 | sequence-replay |
| P-1013-sequence-replay-duplicate--scope-unknown C1 × sequence-replay-duplicate + scope-unknown | reject | reject | yes | 24498 | 462.683 | scope-mismatch, sequence-replay |
| P-1014-sequence-replay-duplicate--action-issuer-retired-after-cutoff C1 × sequence-replay-duplicate + action-issuer-retired-after-cutoff | reject | reject | yes | 24787 | 455.713 | action-issuer-untrusted, sequence-replay |
| P-1112-revocation-missing--revocation-boundary-just-fresh C1 × revocation-missing + revocation-boundary-just-fresh | accept | accept | yes | 19554 | 359.427 | - |
| P-1113-revocation-missing--scope-unknown C1 × revocation-missing + scope-unknown | reject | reject | yes | 19333 | 353.750 | revocation-missing, scope-mismatch |
| P-1114-revocation-missing--action-issuer-retired-after-cutoff C1 × revocation-missing + action-issuer-retired-after-cutoff | reject | reject | yes | 19559 | 347.548 | action-issuer-untrusted, revocation-missing |
| P-1213-revocation-boundary-just-fresh--scope-unknown C1 × revocation-boundary-just-fresh + scope-unknown | reject | reject | yes | 19506 | 358.087 | scope-mismatch |
| P-1214-revocation-boundary-just-fresh--action-issuer-retired-after-cutoff C1 × revocation-boundary-just-fresh + action-issuer-retired-after-cutoff | reject | reject | yes | 19732 | 346.523 | action-issuer-untrusted |
| P-1314-scope-unknown--action-issuer-retired-after-cutoff C1 × scope-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19564 | 346.558 | action-issuer-untrusted, scope-mismatch |
