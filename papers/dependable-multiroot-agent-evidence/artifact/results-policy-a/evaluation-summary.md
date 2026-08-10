# EATF-Backed Multi-Root Evaluation Summary

- Cases: 192/192 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 3424310.
- Total EATF verify ms: 62982.853.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| M-C1-000-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 19307 | 370.337 | identity-issuer-untrusted |
| M-C1-001-identity-method-unknown C1 × identity-method-unknown @ identity[0] | reject | reject | yes | 19308 | 351.898 | identity-method-unaccepted |
| M-C1-002-identity-assurance-low C1 × identity-assurance-low @ identity[0] | reject | reject | yes | 19293 | 355.906 | identity-assurance-insufficient |
| M-C1-003-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 19416 | 356.201 | - |
| M-C1-004-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[1] | reject | reject | yes | 19307 | 369.522 | identity-issuer-untrusted |
| M-C1-005-identity-method-unknown C1 × identity-method-unknown @ identity[1] | reject | reject | yes | 19308 | 354.048 | identity-method-unaccepted |
| M-C1-006-identity-assurance-low C1 × identity-assurance-low @ identity[1] | reject | reject | yes | 19293 | 353.782 | identity-assurance-insufficient |
| M-C1-007-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[1] | accept | accept | yes | 19416 | 346.041 | - |
| M-C1-008-action-issuer-unknown C1 × action-issuer-unknown @ action[0] | reject | reject | yes | 19287 | 344.268 | action-issuer-untrusted |
| M-C1-009-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 19432 | 362.675 | action-issuer-untrusted |
| M-C1-010-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 19442 | 355.373 | - |
| M-C1-011-binding-dangling-identity C1 × binding-dangling-identity @ action[0] | reject | reject | yes | 19272 | 364.568 | broker-policy-violation, identity-hash-missing |
| M-C1-012-binding-subject-substitution C1 × binding-subject-substitution @ action[0] | reject | reject | yes | 19360 | 345.994 | identity-substitution |
| M-C1-013-scope-unknown C1 × scope-unknown @ action[0] | reject | reject | yes | 19206 | 363.601 | scope-mismatch |
| M-C1-014-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 19393 | 353.873 | network-dependency-forbidden |
| M-C1-015-validation-material-stripped C1 × validation-material-stripped @ action[0] | reject | reject | yes | 19355 | 352.741 | archive-material-insufficient, broker-policy-violation |
| M-C1-016-revocation-missing C1 × revocation-missing @ action[0] | reject | reject | yes | 19201 | 373.313 | revocation-missing |
| M-C1-017-revocation-stale-8d C1 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 19264 | 360.586 | revocation-stale |
| M-C1-018-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 19374 | 373.290 | - |
| M-C1-019-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 19374 | 362.682 | revocation-stale |
| M-C1-020-algorithm-unknown C1 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 19241 | 362.645 | algorithm-unaccepted |
| M-C1-021-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 19285 | 365.878 | - |
| M-C1-022-broker-untrusted C1 × broker-untrusted @ action[0] | reject | reject | yes | 19234 | 357.109 | broker-policy-violation |
| M-C1-023-broker-assurance-low C1 × broker-assurance-low @ action[0] | reject | reject | yes | 19273 | 359.049 | broker-policy-violation |
| M-C1-024-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[0] | accept | accept | yes | 19396 | 380.432 | - |
| M-C1-025-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[0] | reject | reject | yes | 19423 | 349.385 | broker-policy-violation |
| M-C1-026-broker-removed C1 × broker-removed @ action[0] | accept | accept | yes | 19025 | 358.666 | - |
| M-C1-027-action-issuer-unknown C1 × action-issuer-unknown @ action[1] | reject | reject | yes | 19287 | 349.558 | action-issuer-untrusted |
| M-C1-028-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[1] | reject | reject | yes | 19432 | 360.004 | action-issuer-untrusted |
| M-C1-029-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[1] | accept | accept | yes | 19442 | 344.325 | - |
| M-C1-030-binding-dangling-identity C1 × binding-dangling-identity @ action[1] | reject | reject | yes | 19273 | 362.559 | broker-policy-violation, identity-hash-missing |
| M-C1-031-binding-subject-substitution C1 × binding-subject-substitution @ action[1] | reject | reject | yes | 19363 | 365.430 | identity-substitution |
| M-C1-032-scope-unknown C1 × scope-unknown @ action[1] | reject | reject | yes | 19204 | 359.683 | scope-mismatch |
| M-C1-033-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[1] | reject | reject | yes | 19393 | 347.547 | network-dependency-forbidden |
| M-C1-034-validation-material-stripped C1 × validation-material-stripped @ action[1] | reject | reject | yes | 19355 | 363.884 | archive-material-insufficient, broker-policy-violation |
| M-C1-035-revocation-missing C1 × revocation-missing @ action[1] | reject | reject | yes | 19201 | 353.054 | revocation-missing |
| M-C1-036-revocation-stale-8d C1 × revocation-stale-8d @ action[1] | indeterminate | indeterminate | yes | 19264 | 359.525 | revocation-stale |
| M-C1-037-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[1] | accept | accept | yes | 19374 | 346.886 | - |
| M-C1-038-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[1] | indeterminate | indeterminate | yes | 19374 | 378.454 | revocation-stale |
| M-C1-039-algorithm-unknown C1 × algorithm-unknown @ action[1] | indeterminate | indeterminate | yes | 19241 | 342.947 | algorithm-unaccepted |
| M-C1-040-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[1] | accept | accept | yes | 19285 | 341.733 | - |
| M-C1-041-broker-untrusted C1 × broker-untrusted @ action[1] | reject | reject | yes | 19234 | 359.688 | broker-policy-violation |
| M-C1-042-broker-assurance-low C1 × broker-assurance-low @ action[1] | reject | reject | yes | 19273 | 359.751 | broker-policy-violation |
| M-C1-043-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[1] | accept | accept | yes | 19396 | 361.111 | - |
| M-C1-044-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[1] | reject | reject | yes | 19423 | 385.077 | broker-policy-violation |
| M-C1-045-broker-removed C1 × broker-removed @ action[1] | accept | accept | yes | 19025 | 361.271 | - |
| M-C1-046-sequence-replay-duplicate C1 × sequence-replay-duplicate @ case | reject | reject | yes | 24327 | 453.571 | sequence-replay |
| M-C2-000-identity-issuer-unknown C2 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9499 | 177.565 | identity-issuer-untrusted |
| M-C2-001-identity-method-unknown C2 × identity-method-unknown @ identity[0] | reject | reject | yes | 9501 | 175.616 | identity-method-unaccepted |
| M-C2-002-identity-assurance-low C2 × identity-assurance-low @ identity[0] | reject | reject | yes | 9491 | 185.435 | identity-assurance-insufficient |
| M-C2-003-identity-assurance-medium-boundary C2 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9554 | 177.057 | - |
| M-C2-004-action-issuer-unknown C2 × action-issuer-unknown @ action[0] | reject | reject | yes | 9489 | 180.647 | action-issuer-untrusted |
| M-C2-005-action-issuer-retired-after-cutoff C2 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9564 | 182.334 | action-issuer-untrusted |
| M-C2-006-action-issuer-retired-grandfathered C2 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9569 | 176.072 | - |
| M-C2-007-binding-dangling-identity C2 × binding-dangling-identity @ action[0] | reject | reject | yes | 9507 | 174.101 | identity-hash-missing |
| M-C2-008-binding-subject-substitution C2 × binding-subject-substitution @ action[0] | reject | reject | yes | 9528 | 185.258 | identity-substitution |
| M-C2-009-scope-unknown C2 × scope-unknown @ action[0] | reject | reject | yes | 9449 | 177.628 | scope-mismatch |
| M-C2-010-live-lookup-under-offline-policy C2 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9541 | 172.980 | network-dependency-forbidden |
| M-C2-011-validation-material-stripped C2 × validation-material-stripped @ action[0] | reject | reject | yes | 9523 | 182.092 | archive-material-insufficient |
| M-C2-012-revocation-missing C2 × revocation-missing @ action[0] | reject | reject | yes | 9419 | 172.875 | revocation-missing |
| M-C2-013-revocation-stale-8d C2 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9477 | 181.342 | revocation-stale |
| M-C2-014-revocation-boundary-just-fresh C2 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9532 | 179.062 | - |
| M-C2-015-revocation-boundary-just-stale C2 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9532 | 183.472 | revocation-stale |
| M-C2-016-algorithm-unknown C2 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9464 | 190.417 | algorithm-unaccepted |
| M-C2-017-algorithm-pqc-accepted C2 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9483 | 180.634 | - |
| M-C2-018-broker-added-untrusted C2 × broker-added-untrusted @ action[0] | reject | reject | yes | 9681 | 175.681 | broker-policy-violation |
| M-C2-019-sequence-replay-duplicate C2 × sequence-replay-duplicate @ case | reject | reject | yes | 14353 | 268.319 | sequence-replay |
| M-C8-000-identity-issuer-unknown C8 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9504 | 179.495 | identity-issuer-untrusted |
| M-C8-001-identity-method-unknown C8 × identity-method-unknown @ identity[0] | reject | reject | yes | 9506 | 170.808 | identity-method-unaccepted |
| M-C8-002-identity-assurance-low C8 × identity-assurance-low @ identity[0] | reject | reject | yes | 9496 | 180.612 | identity-assurance-insufficient |
| M-C8-003-identity-assurance-medium-boundary C8 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9559 | 173.984 | - |
| M-C8-004-action-issuer-unknown C8 × action-issuer-unknown @ action[0] | reject | reject | yes | 9494 | 184.079 | action-issuer-untrusted |
| M-C8-005-action-issuer-retired-after-cutoff C8 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9569 | 193.041 | action-issuer-untrusted |
| M-C8-006-action-issuer-retired-grandfathered C8 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9574 | 172.307 | - |
| M-C8-007-binding-dangling-identity C8 × binding-dangling-identity @ action[0] | reject | reject | yes | 9513 | 184.319 | identity-hash-missing |
| M-C8-008-binding-subject-substitution C8 × binding-subject-substitution @ action[0] | reject | reject | yes | 9536 | 170.858 | identity-substitution |
| M-C8-009-scope-unknown C8 × scope-unknown @ action[0] | reject | reject | yes | 9452 | 180.764 | scope-mismatch |
| M-C8-010-live-lookup-under-offline-policy C8 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9546 | 178.649 | network-dependency-forbidden |
| M-C8-011-validation-material-stripped C8 × validation-material-stripped @ action[0] | reject | reject | yes | 9528 | 176.130 | archive-material-insufficient |
| M-C8-012-revocation-missing C8 × revocation-missing @ action[0] | reject | reject | yes | 9424 | 170.529 | revocation-missing |
| M-C8-013-revocation-stale-8d C8 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9482 | 175.053 | revocation-stale |
| M-C8-014-revocation-boundary-just-fresh C8 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9537 | 175.942 | - |
| M-C8-015-revocation-boundary-just-stale C8 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9537 | 183.987 | revocation-stale |
| M-C8-016-algorithm-unknown C8 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9469 | 178.864 | algorithm-unaccepted |
| M-C8-017-algorithm-pqc-accepted C8 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9488 | 178.409 | - |
| M-C8-018-broker-added-untrusted C8 × broker-added-untrusted @ action[0] | reject | reject | yes | 9686 | 180.972 | broker-policy-violation |
| M-C8-019-sequence-replay-duplicate C8 × sequence-replay-duplicate @ case | reject | reject | yes | 14368 | 263.242 | sequence-replay |
| P-0001-action-issuer-unknown--algorithm-unknown C1 × action-issuer-unknown + algorithm-unknown | reject | reject | yes | 19454 | 364.705 | action-issuer-untrusted, algorithm-unaccepted |
| P-0002-action-issuer-unknown--validation-material-stripped C1 × action-issuer-unknown + validation-material-stripped | reject | reject | yes | 19568 | 353.940 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0003-action-issuer-unknown--identity-assurance-low C1 × action-issuer-unknown + identity-assurance-low | reject | reject | yes | 19506 | 356.451 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0004-action-issuer-unknown--binding-dangling-identity C1 × action-issuer-unknown + binding-dangling-identity | reject | reject | yes | 19485 | 369.609 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0005-action-issuer-unknown--broker-untrusted C1 × action-issuer-unknown + broker-untrusted | reject | reject | yes | 19447 | 361.016 | action-issuer-untrusted, broker-policy-violation |
| P-0006-action-issuer-unknown--broker-assurance-low C1 × action-issuer-unknown + broker-assurance-low | reject | reject | yes | 19486 | 351.226 | action-issuer-untrusted, broker-policy-violation |
| P-0007-action-issuer-unknown--identity-method-unknown C1 × action-issuer-unknown + identity-method-unknown | reject | reject | yes | 19521 | 372.491 | action-issuer-untrusted, identity-method-unaccepted |
| P-0008-action-issuer-unknown--identity-issuer-unknown C1 × action-issuer-unknown + identity-issuer-unknown | reject | reject | yes | 19520 | 364.656 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0009-action-issuer-unknown--live-lookup-under-offline-policy C1 × action-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19606 | 357.840 | action-issuer-untrusted, network-dependency-forbidden |
| P-0010-action-issuer-unknown--sequence-replay-duplicate C1 × action-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24606 | 439.950 | action-issuer-untrusted, sequence-replay |
| P-0011-action-issuer-unknown--revocation-missing C1 × action-issuer-unknown + revocation-missing | reject | reject | yes | 19414 | 346.111 | action-issuer-untrusted, revocation-missing |
| P-0012-action-issuer-unknown--revocation-boundary-just-fresh C1 × action-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19587 | 350.574 | action-issuer-untrusted |
| P-0013-action-issuer-unknown--scope-unknown C1 × action-issuer-unknown + scope-unknown | reject | reject | yes | 19419 | 357.032 | action-issuer-untrusted, scope-mismatch |
| P-0014-action-issuer-unknown--action-issuer-retired-after-cutoff C1 × action-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19642 | 352.024 | action-issuer-untrusted |
| P-0102-algorithm-unknown--validation-material-stripped C1 × algorithm-unknown + validation-material-stripped | reject | reject | yes | 19522 | 370.924 | algorithm-unaccepted, archive-material-insufficient, broker-policy-violation |
| P-0103-algorithm-unknown--identity-assurance-low C1 × algorithm-unknown + identity-assurance-low | reject | reject | yes | 19460 | 365.151 | algorithm-unaccepted, identity-assurance-insufficient |
| P-0104-algorithm-unknown--binding-dangling-identity C1 × algorithm-unknown + binding-dangling-identity | reject | reject | yes | 19439 | 343.453 | algorithm-unaccepted, broker-policy-violation, identity-hash-missing |
| P-0105-algorithm-unknown--broker-untrusted C1 × algorithm-unknown + broker-untrusted | reject | reject | yes | 19401 | 352.351 | algorithm-unaccepted, broker-policy-violation |
| P-0106-algorithm-unknown--broker-assurance-low C1 × algorithm-unknown + broker-assurance-low | reject | reject | yes | 19440 | 355.603 | algorithm-unaccepted, broker-policy-violation |
| P-0107-algorithm-unknown--identity-method-unknown C1 × algorithm-unknown + identity-method-unknown | reject | reject | yes | 19475 | 349.757 | algorithm-unaccepted, identity-method-unaccepted |
| P-0108-algorithm-unknown--identity-issuer-unknown C1 × algorithm-unknown + identity-issuer-unknown | reject | reject | yes | 19474 | 350.058 | algorithm-unaccepted, identity-issuer-untrusted |
| P-0109-algorithm-unknown--live-lookup-under-offline-policy C1 × algorithm-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19560 | 362.454 | algorithm-unaccepted, network-dependency-forbidden |
| P-0110-algorithm-unknown--sequence-replay-duplicate C1 × algorithm-unknown + sequence-replay-duplicate | reject | reject | yes | 24542 | 438.119 | algorithm-unaccepted, sequence-replay |
| P-0111-algorithm-unknown--revocation-missing C1 × algorithm-unknown + revocation-missing | reject | reject | yes | 19368 | 351.368 | algorithm-unaccepted, revocation-missing |
| P-0112-algorithm-unknown--revocation-boundary-just-fresh C1 × algorithm-unknown + revocation-boundary-just-fresh | indeterminate | indeterminate | yes | 19541 | 354.186 | algorithm-unaccepted |
| P-0113-algorithm-unknown--scope-unknown C1 × algorithm-unknown + scope-unknown | reject | reject | yes | 19373 | 357.386 | algorithm-unaccepted, scope-mismatch |
| P-0114-algorithm-unknown--action-issuer-retired-after-cutoff C1 × algorithm-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19599 | 371.765 | action-issuer-untrusted, algorithm-unaccepted |
| P-0203-validation-material-stripped--identity-assurance-low C1 × validation-material-stripped + identity-assurance-low | reject | reject | yes | 19574 | 344.802 | archive-material-insufficient, broker-policy-violation, identity-assurance-insufficient |
| P-0204-validation-material-stripped--binding-dangling-identity C1 × validation-material-stripped + binding-dangling-identity | reject | reject | yes | 19553 | 343.190 | archive-material-insufficient, broker-policy-violation, identity-hash-missing |
| P-0205-validation-material-stripped--broker-untrusted C1 × validation-material-stripped + broker-untrusted | reject | reject | yes | 19515 | 361.425 | archive-material-insufficient, broker-policy-violation |
| P-0206-validation-material-stripped--broker-assurance-low C1 × validation-material-stripped + broker-assurance-low | reject | reject | yes | 19554 | 363.122 | archive-material-insufficient, broker-policy-violation |
| P-0207-validation-material-stripped--identity-method-unknown C1 × validation-material-stripped + identity-method-unknown | reject | reject | yes | 19589 | 368.134 | archive-material-insufficient, broker-policy-violation, identity-method-unaccepted |
| P-0208-validation-material-stripped--identity-issuer-unknown C1 × validation-material-stripped + identity-issuer-unknown | reject | reject | yes | 19588 | 360.670 | archive-material-insufficient, broker-policy-violation, identity-issuer-untrusted |
| P-0209-validation-material-stripped--live-lookup-under-offline-policy C1 × validation-material-stripped + live-lookup-under-offline-policy | reject | reject | yes | 19674 | 341.244 | archive-material-insufficient, broker-policy-violation, network-dependency-forbidden |
| P-0210-validation-material-stripped--sequence-replay-duplicate C1 × validation-material-stripped + sequence-replay-duplicate | reject | reject | yes | 24693 | 449.967 | archive-material-insufficient, broker-policy-violation, sequence-replay |
| P-0211-validation-material-stripped--revocation-missing C1 × validation-material-stripped + revocation-missing | reject | reject | yes | 19482 | 364.324 | archive-material-insufficient, broker-policy-violation, revocation-missing |
| P-0212-validation-material-stripped--revocation-boundary-just-fresh C1 × validation-material-stripped + revocation-boundary-just-fresh | reject | reject | yes | 19655 | 351.505 | archive-material-insufficient, broker-policy-violation |
| P-0213-validation-material-stripped--scope-unknown C1 × validation-material-stripped + scope-unknown | reject | reject | yes | 19487 | 362.236 | archive-material-insufficient, broker-policy-violation, scope-mismatch |
| P-0214-validation-material-stripped--action-issuer-retired-after-cutoff C1 × validation-material-stripped + action-issuer-retired-after-cutoff | reject | reject | yes | 19713 | 359.968 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0304-identity-assurance-low--binding-dangling-identity C1 × identity-assurance-low + binding-dangling-identity | reject | reject | yes | 19491 | 352.496 | broker-policy-violation, identity-assurance-insufficient, identity-hash-missing |
| P-0305-identity-assurance-low--broker-untrusted C1 × identity-assurance-low + broker-untrusted | reject | reject | yes | 19453 | 353.724 | broker-policy-violation, identity-assurance-insufficient |
| P-0306-identity-assurance-low--broker-assurance-low C1 × identity-assurance-low + broker-assurance-low | reject | reject | yes | 19492 | 357.746 | broker-policy-violation, identity-assurance-insufficient |
| P-0307-identity-assurance-low--identity-method-unknown C1 × identity-assurance-low + identity-method-unknown | reject | reject | yes | 19527 | 345.735 | identity-assurance-insufficient, identity-method-unaccepted |
| P-0308-identity-assurance-low--identity-issuer-unknown C1 × identity-assurance-low + identity-issuer-unknown | reject | reject | yes | 19526 | 356.189 | identity-assurance-insufficient, identity-issuer-untrusted |
| P-0309-identity-assurance-low--live-lookup-under-offline-policy C1 × identity-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19612 | 346.937 | identity-assurance-insufficient, network-dependency-forbidden |
| P-0310-identity-assurance-low--sequence-replay-duplicate C1 × identity-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24612 | 447.213 | identity-assurance-insufficient, sequence-replay |
| P-0311-identity-assurance-low--revocation-missing C1 × identity-assurance-low + revocation-missing | reject | reject | yes | 19420 | 371.310 | identity-assurance-insufficient, revocation-missing |
| P-0312-identity-assurance-low--revocation-boundary-just-fresh C1 × identity-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19593 | 347.338 | identity-assurance-insufficient |
| P-0313-identity-assurance-low--scope-unknown C1 × identity-assurance-low + scope-unknown | reject | reject | yes | 19425 | 364.737 | identity-assurance-insufficient, scope-mismatch |
| P-0314-identity-assurance-low--action-issuer-retired-after-cutoff C1 × identity-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19651 | 355.539 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0405-binding-dangling-identity--broker-untrusted C1 × binding-dangling-identity + broker-untrusted | reject | reject | yes | 19432 | 364.991 | broker-policy-violation, identity-hash-missing |
| P-0406-binding-dangling-identity--broker-assurance-low C1 × binding-dangling-identity + broker-assurance-low | reject | reject | yes | 19471 | 348.443 | broker-policy-violation, identity-hash-missing |
| P-0407-binding-dangling-identity--identity-method-unknown C1 × binding-dangling-identity + identity-method-unknown | reject | reject | yes | 19506 | 341.533 | broker-policy-violation, identity-hash-missing, identity-method-unaccepted |
| P-0408-binding-dangling-identity--identity-issuer-unknown C1 × binding-dangling-identity + identity-issuer-unknown | reject | reject | yes | 19504 | 366.695 | broker-policy-violation, identity-hash-missing, identity-issuer-untrusted |
| P-0409-binding-dangling-identity--live-lookup-under-offline-policy C1 × binding-dangling-identity + live-lookup-under-offline-policy | reject | reject | yes | 19591 | 354.458 | broker-policy-violation, identity-hash-missing, network-dependency-forbidden |
| P-0410-binding-dangling-identity--sequence-replay-duplicate C1 × binding-dangling-identity + sequence-replay-duplicate | reject | reject | yes | 24548 | 468.211 | broker-policy-violation, identity-hash-missing, sequence-replay |
| P-0411-binding-dangling-identity--revocation-missing C1 × binding-dangling-identity + revocation-missing | reject | reject | yes | 19399 | 357.220 | broker-policy-violation, identity-hash-missing, revocation-missing |
| P-0412-binding-dangling-identity--revocation-boundary-just-fresh C1 × binding-dangling-identity + revocation-boundary-just-fresh | reject | reject | yes | 19572 | 362.441 | broker-policy-violation, identity-hash-missing |
| P-0413-binding-dangling-identity--scope-unknown C1 × binding-dangling-identity + scope-unknown | reject | reject | yes | 19404 | 353.187 | broker-policy-violation, identity-hash-missing, scope-mismatch |
| P-0414-binding-dangling-identity--action-issuer-retired-after-cutoff C1 × binding-dangling-identity + action-issuer-retired-after-cutoff | reject | reject | yes | 19630 | 361.470 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0506-broker-untrusted--broker-assurance-low C1 × broker-untrusted + broker-assurance-low | reject | reject | yes | 19433 | 359.191 | broker-policy-violation |
| P-0507-broker-untrusted--identity-method-unknown C1 × broker-untrusted + identity-method-unknown | reject | reject | yes | 19468 | 350.373 | broker-policy-violation, identity-method-unaccepted |
| P-0508-broker-untrusted--identity-issuer-unknown C1 × broker-untrusted + identity-issuer-unknown | reject | reject | yes | 19467 | 345.647 | broker-policy-violation, identity-issuer-untrusted |
| P-0509-broker-untrusted--live-lookup-under-offline-policy C1 × broker-untrusted + live-lookup-under-offline-policy | reject | reject | yes | 19553 | 346.936 | broker-policy-violation, network-dependency-forbidden |
| P-0510-broker-untrusted--sequence-replay-duplicate C1 × broker-untrusted + sequence-replay-duplicate | reject | reject | yes | 24535 | 448.221 | broker-policy-violation, sequence-replay |
| P-0511-broker-untrusted--revocation-missing C1 × broker-untrusted + revocation-missing | reject | reject | yes | 19361 | 355.237 | broker-policy-violation, revocation-missing |
| P-0512-broker-untrusted--revocation-boundary-just-fresh C1 × broker-untrusted + revocation-boundary-just-fresh | reject | reject | yes | 19534 | 367.850 | broker-policy-violation |
| P-0513-broker-untrusted--scope-unknown C1 × broker-untrusted + scope-unknown | reject | reject | yes | 19366 | 352.336 | broker-policy-violation, scope-mismatch |
| P-0514-broker-untrusted--action-issuer-retired-after-cutoff C1 × broker-untrusted + action-issuer-retired-after-cutoff | reject | reject | yes | 19592 | 339.729 | action-issuer-untrusted, broker-policy-violation |
| P-0607-broker-assurance-low--identity-method-unknown C1 × broker-assurance-low + identity-method-unknown | reject | reject | yes | 19507 | 353.682 | broker-policy-violation, identity-method-unaccepted |
| P-0608-broker-assurance-low--identity-issuer-unknown C1 × broker-assurance-low + identity-issuer-unknown | reject | reject | yes | 19506 | 365.578 | broker-policy-violation, identity-issuer-untrusted |
| P-0609-broker-assurance-low--live-lookup-under-offline-policy C1 × broker-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19592 | 358.383 | broker-policy-violation, network-dependency-forbidden |
| P-0610-broker-assurance-low--sequence-replay-duplicate C1 × broker-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24585 | 468.796 | broker-policy-violation, sequence-replay |
| P-0611-broker-assurance-low--revocation-missing C1 × broker-assurance-low + revocation-missing | reject | reject | yes | 19400 | 351.874 | broker-policy-violation, revocation-missing |
| P-0612-broker-assurance-low--revocation-boundary-just-fresh C1 × broker-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19573 | 358.640 | broker-policy-violation |
| P-0613-broker-assurance-low--scope-unknown C1 × broker-assurance-low + scope-unknown | reject | reject | yes | 19405 | 361.295 | broker-policy-violation, scope-mismatch |
| P-0614-broker-assurance-low--action-issuer-retired-after-cutoff C1 × broker-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19631 | 351.713 | action-issuer-untrusted, broker-policy-violation |
| P-0708-identity-method-unknown--identity-issuer-unknown C1 × identity-method-unknown + identity-issuer-unknown | reject | reject | yes | 19541 | 374.775 | identity-issuer-untrusted, identity-method-unaccepted |
| P-0709-identity-method-unknown--live-lookup-under-offline-policy C1 × identity-method-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19627 | 364.296 | identity-method-unaccepted, network-dependency-forbidden |
| P-0710-identity-method-unknown--sequence-replay-duplicate C1 × identity-method-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 428.828 | identity-method-unaccepted, sequence-replay |
| P-0711-identity-method-unknown--revocation-missing C1 × identity-method-unknown + revocation-missing | reject | reject | yes | 19435 | 353.355 | identity-method-unaccepted, revocation-missing |
| P-0712-identity-method-unknown--revocation-boundary-just-fresh C1 × identity-method-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19608 | 362.004 | identity-method-unaccepted |
| P-0713-identity-method-unknown--scope-unknown C1 × identity-method-unknown + scope-unknown | reject | reject | yes | 19440 | 362.236 | identity-method-unaccepted, scope-mismatch |
| P-0714-identity-method-unknown--action-issuer-retired-after-cutoff C1 × identity-method-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19666 | 351.418 | action-issuer-untrusted, identity-method-unaccepted |
| P-0809-identity-issuer-unknown--live-lookup-under-offline-policy C1 × identity-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19626 | 348.264 | identity-issuer-untrusted, network-dependency-forbidden |
| P-0810-identity-issuer-unknown--sequence-replay-duplicate C1 × identity-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 439.032 | identity-issuer-untrusted, sequence-replay |
| P-0811-identity-issuer-unknown--revocation-missing C1 × identity-issuer-unknown + revocation-missing | reject | reject | yes | 19434 | 349.499 | identity-issuer-untrusted, revocation-missing |
| P-0812-identity-issuer-unknown--revocation-boundary-just-fresh C1 × identity-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19607 | 344.188 | identity-issuer-untrusted |
| P-0813-identity-issuer-unknown--scope-unknown C1 × identity-issuer-unknown + scope-unknown | reject | reject | yes | 19439 | 363.598 | identity-issuer-untrusted, scope-mismatch |
| P-0814-identity-issuer-unknown--action-issuer-retired-after-cutoff C1 × identity-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19665 | 358.326 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0910-live-lookup-under-offline-policy--sequence-replay-duplicate C1 × live-lookup-under-offline-policy + sequence-replay-duplicate | reject | reject | yes | 24741 | 439.907 | network-dependency-forbidden, sequence-replay |
| P-0911-live-lookup-under-offline-policy--revocation-missing C1 × live-lookup-under-offline-policy + revocation-missing | reject | reject | yes | 19520 | 354.720 | network-dependency-forbidden, revocation-missing |
| P-0912-live-lookup-under-offline-policy--revocation-boundary-just-fresh C1 × live-lookup-under-offline-policy + revocation-boundary-just-fresh | reject | reject | yes | 19693 | 360.461 | network-dependency-forbidden |
| P-0913-live-lookup-under-offline-policy--scope-unknown C1 × live-lookup-under-offline-policy + scope-unknown | reject | reject | yes | 19525 | 344.334 | network-dependency-forbidden, scope-mismatch |
| P-0914-live-lookup-under-offline-policy--action-issuer-retired-after-cutoff C1 × live-lookup-under-offline-policy + action-issuer-retired-after-cutoff | reject | reject | yes | 19751 | 355.972 | action-issuer-untrusted, network-dependency-forbidden |
| P-1011-sequence-replay-duplicate--revocation-missing C1 × sequence-replay-duplicate + revocation-missing | reject | reject | yes | 24508 | 444.655 | revocation-missing, sequence-replay |
| P-1012-sequence-replay-duplicate--revocation-boundary-just-fresh C1 × sequence-replay-duplicate + revocation-boundary-just-fresh | reject | reject | yes | 24717 | 445.686 | sequence-replay |
| P-1013-sequence-replay-duplicate--scope-unknown C1 × sequence-replay-duplicate + scope-unknown | reject | reject | yes | 24498 | 443.707 | scope-mismatch, sequence-replay |
| P-1014-sequence-replay-duplicate--action-issuer-retired-after-cutoff C1 × sequence-replay-duplicate + action-issuer-retired-after-cutoff | reject | reject | yes | 24787 | 443.273 | action-issuer-untrusted, sequence-replay |
| P-1112-revocation-missing--revocation-boundary-just-fresh C1 × revocation-missing + revocation-boundary-just-fresh | accept | accept | yes | 19554 | 359.732 | - |
| P-1113-revocation-missing--scope-unknown C1 × revocation-missing + scope-unknown | reject | reject | yes | 19333 | 368.015 | revocation-missing, scope-mismatch |
| P-1114-revocation-missing--action-issuer-retired-after-cutoff C1 × revocation-missing + action-issuer-retired-after-cutoff | reject | reject | yes | 19559 | 354.368 | action-issuer-untrusted, revocation-missing |
| P-1213-revocation-boundary-just-fresh--scope-unknown C1 × revocation-boundary-just-fresh + scope-unknown | reject | reject | yes | 19506 | 341.513 | scope-mismatch |
| P-1214-revocation-boundary-just-fresh--action-issuer-retired-after-cutoff C1 × revocation-boundary-just-fresh + action-issuer-retired-after-cutoff | reject | reject | yes | 19732 | 351.288 | action-issuer-untrusted |
| P-1314-scope-unknown--action-issuer-retired-after-cutoff C1 × scope-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19564 | 380.970 | action-issuer-untrusted, scope-mismatch |
