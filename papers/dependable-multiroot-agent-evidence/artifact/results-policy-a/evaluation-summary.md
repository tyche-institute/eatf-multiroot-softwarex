# EATF-Backed Multi-Root Evaluation Summary

- Cases: 192/192 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 3424310.
- Total EATF verify ms: 62857.370.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| M-C1-000-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 19307 | 362.850 | identity-issuer-untrusted |
| M-C1-001-identity-method-unknown C1 × identity-method-unknown @ identity[0] | reject | reject | yes | 19308 | 368.112 | identity-method-unaccepted |
| M-C1-002-identity-assurance-low C1 × identity-assurance-low @ identity[0] | reject | reject | yes | 19293 | 354.944 | identity-assurance-insufficient |
| M-C1-003-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 19416 | 346.435 | - |
| M-C1-004-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[1] | reject | reject | yes | 19307 | 338.122 | identity-issuer-untrusted |
| M-C1-005-identity-method-unknown C1 × identity-method-unknown @ identity[1] | reject | reject | yes | 19308 | 352.630 | identity-method-unaccepted |
| M-C1-006-identity-assurance-low C1 × identity-assurance-low @ identity[1] | reject | reject | yes | 19293 | 353.875 | identity-assurance-insufficient |
| M-C1-007-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[1] | accept | accept | yes | 19416 | 366.277 | - |
| M-C1-008-action-issuer-unknown C1 × action-issuer-unknown @ action[0] | reject | reject | yes | 19287 | 351.282 | action-issuer-untrusted |
| M-C1-009-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 19432 | 360.693 | action-issuer-untrusted |
| M-C1-010-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 19442 | 355.055 | - |
| M-C1-011-binding-dangling-identity C1 × binding-dangling-identity @ action[0] | reject | reject | yes | 19272 | 360.996 | broker-policy-violation, identity-hash-missing |
| M-C1-012-binding-subject-substitution C1 × binding-subject-substitution @ action[0] | reject | reject | yes | 19360 | 340.463 | identity-substitution |
| M-C1-013-scope-unknown C1 × scope-unknown @ action[0] | reject | reject | yes | 19206 | 349.718 | scope-mismatch |
| M-C1-014-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 19393 | 344.350 | network-dependency-forbidden |
| M-C1-015-validation-material-stripped C1 × validation-material-stripped @ action[0] | reject | reject | yes | 19355 | 354.803 | archive-material-insufficient, broker-policy-violation |
| M-C1-016-revocation-missing C1 × revocation-missing @ action[0] | reject | reject | yes | 19201 | 341.675 | revocation-missing |
| M-C1-017-revocation-stale-8d C1 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 19264 | 369.511 | revocation-stale |
| M-C1-018-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 19374 | 360.564 | - |
| M-C1-019-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 19374 | 355.393 | revocation-stale |
| M-C1-020-algorithm-unknown C1 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 19241 | 362.799 | algorithm-unaccepted |
| M-C1-021-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 19285 | 353.307 | - |
| M-C1-022-broker-untrusted C1 × broker-untrusted @ action[0] | reject | reject | yes | 19234 | 359.501 | broker-policy-violation |
| M-C1-023-broker-assurance-low C1 × broker-assurance-low @ action[0] | reject | reject | yes | 19273 | 353.769 | broker-policy-violation |
| M-C1-024-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[0] | accept | accept | yes | 19396 | 371.997 | - |
| M-C1-025-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[0] | reject | reject | yes | 19423 | 359.702 | broker-policy-violation |
| M-C1-026-broker-removed C1 × broker-removed @ action[0] | accept | accept | yes | 19025 | 362.805 | - |
| M-C1-027-action-issuer-unknown C1 × action-issuer-unknown @ action[1] | reject | reject | yes | 19287 | 364.462 | action-issuer-untrusted |
| M-C1-028-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[1] | reject | reject | yes | 19432 | 363.436 | action-issuer-untrusted |
| M-C1-029-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[1] | accept | accept | yes | 19442 | 357.020 | - |
| M-C1-030-binding-dangling-identity C1 × binding-dangling-identity @ action[1] | reject | reject | yes | 19273 | 347.333 | broker-policy-violation, identity-hash-missing |
| M-C1-031-binding-subject-substitution C1 × binding-subject-substitution @ action[1] | reject | reject | yes | 19363 | 354.599 | identity-substitution |
| M-C1-032-scope-unknown C1 × scope-unknown @ action[1] | reject | reject | yes | 19204 | 355.095 | scope-mismatch |
| M-C1-033-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[1] | reject | reject | yes | 19393 | 359.690 | network-dependency-forbidden |
| M-C1-034-validation-material-stripped C1 × validation-material-stripped @ action[1] | reject | reject | yes | 19355 | 345.061 | archive-material-insufficient, broker-policy-violation |
| M-C1-035-revocation-missing C1 × revocation-missing @ action[1] | reject | reject | yes | 19201 | 347.871 | revocation-missing |
| M-C1-036-revocation-stale-8d C1 × revocation-stale-8d @ action[1] | indeterminate | indeterminate | yes | 19264 | 351.876 | revocation-stale |
| M-C1-037-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[1] | accept | accept | yes | 19374 | 355.100 | - |
| M-C1-038-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[1] | indeterminate | indeterminate | yes | 19374 | 349.836 | revocation-stale |
| M-C1-039-algorithm-unknown C1 × algorithm-unknown @ action[1] | indeterminate | indeterminate | yes | 19241 | 373.101 | algorithm-unaccepted |
| M-C1-040-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[1] | accept | accept | yes | 19285 | 370.696 | - |
| M-C1-041-broker-untrusted C1 × broker-untrusted @ action[1] | reject | reject | yes | 19234 | 369.368 | broker-policy-violation |
| M-C1-042-broker-assurance-low C1 × broker-assurance-low @ action[1] | reject | reject | yes | 19273 | 352.761 | broker-policy-violation |
| M-C1-043-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[1] | accept | accept | yes | 19396 | 364.984 | - |
| M-C1-044-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[1] | reject | reject | yes | 19423 | 346.261 | broker-policy-violation |
| M-C1-045-broker-removed C1 × broker-removed @ action[1] | accept | accept | yes | 19025 | 352.905 | - |
| M-C1-046-sequence-replay-duplicate C1 × sequence-replay-duplicate @ case | reject | reject | yes | 24327 | 430.573 | sequence-replay |
| M-C2-000-identity-issuer-unknown C2 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9499 | 178.894 | identity-issuer-untrusted |
| M-C2-001-identity-method-unknown C2 × identity-method-unknown @ identity[0] | reject | reject | yes | 9501 | 171.058 | identity-method-unaccepted |
| M-C2-002-identity-assurance-low C2 × identity-assurance-low @ identity[0] | reject | reject | yes | 9491 | 177.577 | identity-assurance-insufficient |
| M-C2-003-identity-assurance-medium-boundary C2 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9554 | 173.699 | - |
| M-C2-004-action-issuer-unknown C2 × action-issuer-unknown @ action[0] | reject | reject | yes | 9489 | 188.307 | action-issuer-untrusted |
| M-C2-005-action-issuer-retired-after-cutoff C2 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9564 | 183.622 | action-issuer-untrusted |
| M-C2-006-action-issuer-retired-grandfathered C2 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9569 | 182.218 | - |
| M-C2-007-binding-dangling-identity C2 × binding-dangling-identity @ action[0] | reject | reject | yes | 9507 | 178.539 | identity-hash-missing |
| M-C2-008-binding-subject-substitution C2 × binding-subject-substitution @ action[0] | reject | reject | yes | 9528 | 169.990 | identity-substitution |
| M-C2-009-scope-unknown C2 × scope-unknown @ action[0] | reject | reject | yes | 9449 | 169.906 | scope-mismatch |
| M-C2-010-live-lookup-under-offline-policy C2 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9541 | 177.715 | network-dependency-forbidden |
| M-C2-011-validation-material-stripped C2 × validation-material-stripped @ action[0] | reject | reject | yes | 9523 | 170.657 | archive-material-insufficient |
| M-C2-012-revocation-missing C2 × revocation-missing @ action[0] | reject | reject | yes | 9419 | 181.446 | revocation-missing |
| M-C2-013-revocation-stale-8d C2 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9477 | 173.462 | revocation-stale |
| M-C2-014-revocation-boundary-just-fresh C2 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9532 | 185.119 | - |
| M-C2-015-revocation-boundary-just-stale C2 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9532 | 188.261 | revocation-stale |
| M-C2-016-algorithm-unknown C2 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9464 | 172.455 | algorithm-unaccepted |
| M-C2-017-algorithm-pqc-accepted C2 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9483 | 192.208 | - |
| M-C2-018-broker-added-untrusted C2 × broker-added-untrusted @ action[0] | reject | reject | yes | 9681 | 175.833 | broker-policy-violation |
| M-C2-019-sequence-replay-duplicate C2 × sequence-replay-duplicate @ case | reject | reject | yes | 14353 | 266.136 | sequence-replay |
| M-C8-000-identity-issuer-unknown C8 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9504 | 182.062 | identity-issuer-untrusted |
| M-C8-001-identity-method-unknown C8 × identity-method-unknown @ identity[0] | reject | reject | yes | 9506 | 172.825 | identity-method-unaccepted |
| M-C8-002-identity-assurance-low C8 × identity-assurance-low @ identity[0] | reject | reject | yes | 9496 | 180.442 | identity-assurance-insufficient |
| M-C8-003-identity-assurance-medium-boundary C8 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9559 | 182.450 | - |
| M-C8-004-action-issuer-unknown C8 × action-issuer-unknown @ action[0] | reject | reject | yes | 9494 | 180.863 | action-issuer-untrusted |
| M-C8-005-action-issuer-retired-after-cutoff C8 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9569 | 172.241 | action-issuer-untrusted |
| M-C8-006-action-issuer-retired-grandfathered C8 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9574 | 176.969 | - |
| M-C8-007-binding-dangling-identity C8 × binding-dangling-identity @ action[0] | reject | reject | yes | 9513 | 170.093 | identity-hash-missing |
| M-C8-008-binding-subject-substitution C8 × binding-subject-substitution @ action[0] | reject | reject | yes | 9536 | 177.108 | identity-substitution |
| M-C8-009-scope-unknown C8 × scope-unknown @ action[0] | reject | reject | yes | 9452 | 176.762 | scope-mismatch |
| M-C8-010-live-lookup-under-offline-policy C8 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9546 | 171.059 | network-dependency-forbidden |
| M-C8-011-validation-material-stripped C8 × validation-material-stripped @ action[0] | reject | reject | yes | 9528 | 171.280 | archive-material-insufficient |
| M-C8-012-revocation-missing C8 × revocation-missing @ action[0] | reject | reject | yes | 9424 | 174.544 | revocation-missing |
| M-C8-013-revocation-stale-8d C8 × revocation-stale-8d @ action[0] | indeterminate | indeterminate | yes | 9482 | 181.005 | revocation-stale |
| M-C8-014-revocation-boundary-just-fresh C8 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9537 | 181.855 | - |
| M-C8-015-revocation-boundary-just-stale C8 × revocation-boundary-just-stale @ action[0] | indeterminate | indeterminate | yes | 9537 | 178.529 | revocation-stale |
| M-C8-016-algorithm-unknown C8 × algorithm-unknown @ action[0] | indeterminate | indeterminate | yes | 9469 | 180.320 | algorithm-unaccepted |
| M-C8-017-algorithm-pqc-accepted C8 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9488 | 178.474 | - |
| M-C8-018-broker-added-untrusted C8 × broker-added-untrusted @ action[0] | reject | reject | yes | 9686 | 180.476 | broker-policy-violation |
| M-C8-019-sequence-replay-duplicate C8 × sequence-replay-duplicate @ case | reject | reject | yes | 14368 | 260.106 | sequence-replay |
| P-0001-action-issuer-unknown--algorithm-unknown C1 × action-issuer-unknown + algorithm-unknown | reject | reject | yes | 19454 | 355.006 | action-issuer-untrusted, algorithm-unaccepted |
| P-0002-action-issuer-unknown--validation-material-stripped C1 × action-issuer-unknown + validation-material-stripped | reject | reject | yes | 19568 | 363.652 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0003-action-issuer-unknown--identity-assurance-low C1 × action-issuer-unknown + identity-assurance-low | reject | reject | yes | 19506 | 354.345 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0004-action-issuer-unknown--binding-dangling-identity C1 × action-issuer-unknown + binding-dangling-identity | reject | reject | yes | 19485 | 355.990 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0005-action-issuer-unknown--broker-untrusted C1 × action-issuer-unknown + broker-untrusted | reject | reject | yes | 19447 | 354.151 | action-issuer-untrusted, broker-policy-violation |
| P-0006-action-issuer-unknown--broker-assurance-low C1 × action-issuer-unknown + broker-assurance-low | reject | reject | yes | 19486 | 380.597 | action-issuer-untrusted, broker-policy-violation |
| P-0007-action-issuer-unknown--identity-method-unknown C1 × action-issuer-unknown + identity-method-unknown | reject | reject | yes | 19521 | 362.950 | action-issuer-untrusted, identity-method-unaccepted |
| P-0008-action-issuer-unknown--identity-issuer-unknown C1 × action-issuer-unknown + identity-issuer-unknown | reject | reject | yes | 19520 | 369.583 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0009-action-issuer-unknown--live-lookup-under-offline-policy C1 × action-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19606 | 371.611 | action-issuer-untrusted, network-dependency-forbidden |
| P-0010-action-issuer-unknown--sequence-replay-duplicate C1 × action-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24606 | 434.573 | action-issuer-untrusted, sequence-replay |
| P-0011-action-issuer-unknown--revocation-missing C1 × action-issuer-unknown + revocation-missing | reject | reject | yes | 19414 | 348.892 | action-issuer-untrusted, revocation-missing |
| P-0012-action-issuer-unknown--revocation-boundary-just-fresh C1 × action-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19587 | 344.457 | action-issuer-untrusted |
| P-0013-action-issuer-unknown--scope-unknown C1 × action-issuer-unknown + scope-unknown | reject | reject | yes | 19419 | 350.718 | action-issuer-untrusted, scope-mismatch |
| P-0014-action-issuer-unknown--action-issuer-retired-after-cutoff C1 × action-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19642 | 357.715 | action-issuer-untrusted |
| P-0102-algorithm-unknown--validation-material-stripped C1 × algorithm-unknown + validation-material-stripped | reject | reject | yes | 19522 | 353.266 | algorithm-unaccepted, archive-material-insufficient, broker-policy-violation |
| P-0103-algorithm-unknown--identity-assurance-low C1 × algorithm-unknown + identity-assurance-low | reject | reject | yes | 19460 | 350.153 | algorithm-unaccepted, identity-assurance-insufficient |
| P-0104-algorithm-unknown--binding-dangling-identity C1 × algorithm-unknown + binding-dangling-identity | reject | reject | yes | 19439 | 347.151 | algorithm-unaccepted, broker-policy-violation, identity-hash-missing |
| P-0105-algorithm-unknown--broker-untrusted C1 × algorithm-unknown + broker-untrusted | reject | reject | yes | 19401 | 358.815 | algorithm-unaccepted, broker-policy-violation |
| P-0106-algorithm-unknown--broker-assurance-low C1 × algorithm-unknown + broker-assurance-low | reject | reject | yes | 19440 | 353.959 | algorithm-unaccepted, broker-policy-violation |
| P-0107-algorithm-unknown--identity-method-unknown C1 × algorithm-unknown + identity-method-unknown | reject | reject | yes | 19475 | 348.253 | algorithm-unaccepted, identity-method-unaccepted |
| P-0108-algorithm-unknown--identity-issuer-unknown C1 × algorithm-unknown + identity-issuer-unknown | reject | reject | yes | 19474 | 355.675 | algorithm-unaccepted, identity-issuer-untrusted |
| P-0109-algorithm-unknown--live-lookup-under-offline-policy C1 × algorithm-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19560 | 339.855 | algorithm-unaccepted, network-dependency-forbidden |
| P-0110-algorithm-unknown--sequence-replay-duplicate C1 × algorithm-unknown + sequence-replay-duplicate | reject | reject | yes | 24542 | 443.805 | algorithm-unaccepted, sequence-replay |
| P-0111-algorithm-unknown--revocation-missing C1 × algorithm-unknown + revocation-missing | reject | reject | yes | 19368 | 344.057 | algorithm-unaccepted, revocation-missing |
| P-0112-algorithm-unknown--revocation-boundary-just-fresh C1 × algorithm-unknown + revocation-boundary-just-fresh | indeterminate | indeterminate | yes | 19541 | 352.251 | algorithm-unaccepted |
| P-0113-algorithm-unknown--scope-unknown C1 × algorithm-unknown + scope-unknown | reject | reject | yes | 19373 | 359.560 | algorithm-unaccepted, scope-mismatch |
| P-0114-algorithm-unknown--action-issuer-retired-after-cutoff C1 × algorithm-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19599 | 365.948 | action-issuer-untrusted, algorithm-unaccepted |
| P-0203-validation-material-stripped--identity-assurance-low C1 × validation-material-stripped + identity-assurance-low | reject | reject | yes | 19574 | 371.654 | archive-material-insufficient, broker-policy-violation, identity-assurance-insufficient |
| P-0204-validation-material-stripped--binding-dangling-identity C1 × validation-material-stripped + binding-dangling-identity | reject | reject | yes | 19553 | 350.860 | archive-material-insufficient, broker-policy-violation, identity-hash-missing |
| P-0205-validation-material-stripped--broker-untrusted C1 × validation-material-stripped + broker-untrusted | reject | reject | yes | 19515 | 360.183 | archive-material-insufficient, broker-policy-violation |
| P-0206-validation-material-stripped--broker-assurance-low C1 × validation-material-stripped + broker-assurance-low | reject | reject | yes | 19554 | 354.852 | archive-material-insufficient, broker-policy-violation |
| P-0207-validation-material-stripped--identity-method-unknown C1 × validation-material-stripped + identity-method-unknown | reject | reject | yes | 19589 | 357.951 | archive-material-insufficient, broker-policy-violation, identity-method-unaccepted |
| P-0208-validation-material-stripped--identity-issuer-unknown C1 × validation-material-stripped + identity-issuer-unknown | reject | reject | yes | 19588 | 360.625 | archive-material-insufficient, broker-policy-violation, identity-issuer-untrusted |
| P-0209-validation-material-stripped--live-lookup-under-offline-policy C1 × validation-material-stripped + live-lookup-under-offline-policy | reject | reject | yes | 19674 | 347.654 | archive-material-insufficient, broker-policy-violation, network-dependency-forbidden |
| P-0210-validation-material-stripped--sequence-replay-duplicate C1 × validation-material-stripped + sequence-replay-duplicate | reject | reject | yes | 24693 | 434.515 | archive-material-insufficient, broker-policy-violation, sequence-replay |
| P-0211-validation-material-stripped--revocation-missing C1 × validation-material-stripped + revocation-missing | reject | reject | yes | 19482 | 367.863 | archive-material-insufficient, broker-policy-violation, revocation-missing |
| P-0212-validation-material-stripped--revocation-boundary-just-fresh C1 × validation-material-stripped + revocation-boundary-just-fresh | reject | reject | yes | 19655 | 360.137 | archive-material-insufficient, broker-policy-violation |
| P-0213-validation-material-stripped--scope-unknown C1 × validation-material-stripped + scope-unknown | reject | reject | yes | 19487 | 360.365 | archive-material-insufficient, broker-policy-violation, scope-mismatch |
| P-0214-validation-material-stripped--action-issuer-retired-after-cutoff C1 × validation-material-stripped + action-issuer-retired-after-cutoff | reject | reject | yes | 19713 | 366.334 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0304-identity-assurance-low--binding-dangling-identity C1 × identity-assurance-low + binding-dangling-identity | reject | reject | yes | 19491 | 369.229 | broker-policy-violation, identity-assurance-insufficient, identity-hash-missing |
| P-0305-identity-assurance-low--broker-untrusted C1 × identity-assurance-low + broker-untrusted | reject | reject | yes | 19453 | 355.248 | broker-policy-violation, identity-assurance-insufficient |
| P-0306-identity-assurance-low--broker-assurance-low C1 × identity-assurance-low + broker-assurance-low | reject | reject | yes | 19492 | 370.509 | broker-policy-violation, identity-assurance-insufficient |
| P-0307-identity-assurance-low--identity-method-unknown C1 × identity-assurance-low + identity-method-unknown | reject | reject | yes | 19527 | 360.296 | identity-assurance-insufficient, identity-method-unaccepted |
| P-0308-identity-assurance-low--identity-issuer-unknown C1 × identity-assurance-low + identity-issuer-unknown | reject | reject | yes | 19526 | 345.173 | identity-assurance-insufficient, identity-issuer-untrusted |
| P-0309-identity-assurance-low--live-lookup-under-offline-policy C1 × identity-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19612 | 353.060 | identity-assurance-insufficient, network-dependency-forbidden |
| P-0310-identity-assurance-low--sequence-replay-duplicate C1 × identity-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24612 | 443.459 | identity-assurance-insufficient, sequence-replay |
| P-0311-identity-assurance-low--revocation-missing C1 × identity-assurance-low + revocation-missing | reject | reject | yes | 19420 | 352.900 | identity-assurance-insufficient, revocation-missing |
| P-0312-identity-assurance-low--revocation-boundary-just-fresh C1 × identity-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19593 | 369.154 | identity-assurance-insufficient |
| P-0313-identity-assurance-low--scope-unknown C1 × identity-assurance-low + scope-unknown | reject | reject | yes | 19425 | 359.012 | identity-assurance-insufficient, scope-mismatch |
| P-0314-identity-assurance-low--action-issuer-retired-after-cutoff C1 × identity-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19651 | 344.311 | action-issuer-untrusted, identity-assurance-insufficient |
| P-0405-binding-dangling-identity--broker-untrusted C1 × binding-dangling-identity + broker-untrusted | reject | reject | yes | 19432 | 344.151 | broker-policy-violation, identity-hash-missing |
| P-0406-binding-dangling-identity--broker-assurance-low C1 × binding-dangling-identity + broker-assurance-low | reject | reject | yes | 19471 | 354.110 | broker-policy-violation, identity-hash-missing |
| P-0407-binding-dangling-identity--identity-method-unknown C1 × binding-dangling-identity + identity-method-unknown | reject | reject | yes | 19506 | 369.075 | broker-policy-violation, identity-hash-missing, identity-method-unaccepted |
| P-0408-binding-dangling-identity--identity-issuer-unknown C1 × binding-dangling-identity + identity-issuer-unknown | reject | reject | yes | 19504 | 354.790 | broker-policy-violation, identity-hash-missing, identity-issuer-untrusted |
| P-0409-binding-dangling-identity--live-lookup-under-offline-policy C1 × binding-dangling-identity + live-lookup-under-offline-policy | reject | reject | yes | 19591 | 357.526 | broker-policy-violation, identity-hash-missing, network-dependency-forbidden |
| P-0410-binding-dangling-identity--sequence-replay-duplicate C1 × binding-dangling-identity + sequence-replay-duplicate | reject | reject | yes | 24548 | 443.833 | broker-policy-violation, identity-hash-missing, sequence-replay |
| P-0411-binding-dangling-identity--revocation-missing C1 × binding-dangling-identity + revocation-missing | reject | reject | yes | 19399 | 348.974 | broker-policy-violation, identity-hash-missing, revocation-missing |
| P-0412-binding-dangling-identity--revocation-boundary-just-fresh C1 × binding-dangling-identity + revocation-boundary-just-fresh | reject | reject | yes | 19572 | 367.998 | broker-policy-violation, identity-hash-missing |
| P-0413-binding-dangling-identity--scope-unknown C1 × binding-dangling-identity + scope-unknown | reject | reject | yes | 19404 | 352.870 | broker-policy-violation, identity-hash-missing, scope-mismatch |
| P-0414-binding-dangling-identity--action-issuer-retired-after-cutoff C1 × binding-dangling-identity + action-issuer-retired-after-cutoff | reject | reject | yes | 19630 | 348.836 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0506-broker-untrusted--broker-assurance-low C1 × broker-untrusted + broker-assurance-low | reject | reject | yes | 19433 | 365.865 | broker-policy-violation |
| P-0507-broker-untrusted--identity-method-unknown C1 × broker-untrusted + identity-method-unknown | reject | reject | yes | 19468 | 357.694 | broker-policy-violation, identity-method-unaccepted |
| P-0508-broker-untrusted--identity-issuer-unknown C1 × broker-untrusted + identity-issuer-unknown | reject | reject | yes | 19467 | 359.811 | broker-policy-violation, identity-issuer-untrusted |
| P-0509-broker-untrusted--live-lookup-under-offline-policy C1 × broker-untrusted + live-lookup-under-offline-policy | reject | reject | yes | 19553 | 363.168 | broker-policy-violation, network-dependency-forbidden |
| P-0510-broker-untrusted--sequence-replay-duplicate C1 × broker-untrusted + sequence-replay-duplicate | reject | reject | yes | 24535 | 456.808 | broker-policy-violation, sequence-replay |
| P-0511-broker-untrusted--revocation-missing C1 × broker-untrusted + revocation-missing | reject | reject | yes | 19361 | 368.180 | broker-policy-violation, revocation-missing |
| P-0512-broker-untrusted--revocation-boundary-just-fresh C1 × broker-untrusted + revocation-boundary-just-fresh | reject | reject | yes | 19534 | 374.214 | broker-policy-violation |
| P-0513-broker-untrusted--scope-unknown C1 × broker-untrusted + scope-unknown | reject | reject | yes | 19366 | 365.167 | broker-policy-violation, scope-mismatch |
| P-0514-broker-untrusted--action-issuer-retired-after-cutoff C1 × broker-untrusted + action-issuer-retired-after-cutoff | reject | reject | yes | 19592 | 356.579 | action-issuer-untrusted, broker-policy-violation |
| P-0607-broker-assurance-low--identity-method-unknown C1 × broker-assurance-low + identity-method-unknown | reject | reject | yes | 19507 | 346.046 | broker-policy-violation, identity-method-unaccepted |
| P-0608-broker-assurance-low--identity-issuer-unknown C1 × broker-assurance-low + identity-issuer-unknown | reject | reject | yes | 19506 | 351.921 | broker-policy-violation, identity-issuer-untrusted |
| P-0609-broker-assurance-low--live-lookup-under-offline-policy C1 × broker-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19592 | 354.825 | broker-policy-violation, network-dependency-forbidden |
| P-0610-broker-assurance-low--sequence-replay-duplicate C1 × broker-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24585 | 443.994 | broker-policy-violation, sequence-replay |
| P-0611-broker-assurance-low--revocation-missing C1 × broker-assurance-low + revocation-missing | reject | reject | yes | 19400 | 354.579 | broker-policy-violation, revocation-missing |
| P-0612-broker-assurance-low--revocation-boundary-just-fresh C1 × broker-assurance-low + revocation-boundary-just-fresh | reject | reject | yes | 19573 | 354.568 | broker-policy-violation |
| P-0613-broker-assurance-low--scope-unknown C1 × broker-assurance-low + scope-unknown | reject | reject | yes | 19405 | 354.405 | broker-policy-violation, scope-mismatch |
| P-0614-broker-assurance-low--action-issuer-retired-after-cutoff C1 × broker-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19631 | 362.294 | action-issuer-untrusted, broker-policy-violation |
| P-0708-identity-method-unknown--identity-issuer-unknown C1 × identity-method-unknown + identity-issuer-unknown | reject | reject | yes | 19541 | 345.694 | identity-issuer-untrusted, identity-method-unaccepted |
| P-0709-identity-method-unknown--live-lookup-under-offline-policy C1 × identity-method-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19627 | 351.492 | identity-method-unaccepted, network-dependency-forbidden |
| P-0710-identity-method-unknown--sequence-replay-duplicate C1 × identity-method-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 454.949 | identity-method-unaccepted, sequence-replay |
| P-0711-identity-method-unknown--revocation-missing C1 × identity-method-unknown + revocation-missing | reject | reject | yes | 19435 | 360.127 | identity-method-unaccepted, revocation-missing |
| P-0712-identity-method-unknown--revocation-boundary-just-fresh C1 × identity-method-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19608 | 356.523 | identity-method-unaccepted |
| P-0713-identity-method-unknown--scope-unknown C1 × identity-method-unknown + scope-unknown | reject | reject | yes | 19440 | 356.843 | identity-method-unaccepted, scope-mismatch |
| P-0714-identity-method-unknown--action-issuer-retired-after-cutoff C1 × identity-method-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19666 | 352.630 | action-issuer-untrusted, identity-method-unaccepted |
| P-0809-identity-issuer-unknown--live-lookup-under-offline-policy C1 × identity-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19626 | 355.828 | identity-issuer-untrusted, network-dependency-forbidden |
| P-0810-identity-issuer-unknown--sequence-replay-duplicate C1 × identity-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 452.696 | identity-issuer-untrusted, sequence-replay |
| P-0811-identity-issuer-unknown--revocation-missing C1 × identity-issuer-unknown + revocation-missing | reject | reject | yes | 19434 | 347.711 | identity-issuer-untrusted, revocation-missing |
| P-0812-identity-issuer-unknown--revocation-boundary-just-fresh C1 × identity-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19607 | 364.249 | identity-issuer-untrusted |
| P-0813-identity-issuer-unknown--scope-unknown C1 × identity-issuer-unknown + scope-unknown | reject | reject | yes | 19439 | 349.669 | identity-issuer-untrusted, scope-mismatch |
| P-0814-identity-issuer-unknown--action-issuer-retired-after-cutoff C1 × identity-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19665 | 373.204 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0910-live-lookup-under-offline-policy--sequence-replay-duplicate C1 × live-lookup-under-offline-policy + sequence-replay-duplicate | reject | reject | yes | 24741 | 442.392 | network-dependency-forbidden, sequence-replay |
| P-0911-live-lookup-under-offline-policy--revocation-missing C1 × live-lookup-under-offline-policy + revocation-missing | reject | reject | yes | 19520 | 359.662 | network-dependency-forbidden, revocation-missing |
| P-0912-live-lookup-under-offline-policy--revocation-boundary-just-fresh C1 × live-lookup-under-offline-policy + revocation-boundary-just-fresh | reject | reject | yes | 19693 | 366.127 | network-dependency-forbidden |
| P-0913-live-lookup-under-offline-policy--scope-unknown C1 × live-lookup-under-offline-policy + scope-unknown | reject | reject | yes | 19525 | 352.385 | network-dependency-forbidden, scope-mismatch |
| P-0914-live-lookup-under-offline-policy--action-issuer-retired-after-cutoff C1 × live-lookup-under-offline-policy + action-issuer-retired-after-cutoff | reject | reject | yes | 19751 | 362.012 | action-issuer-untrusted, network-dependency-forbidden |
| P-1011-sequence-replay-duplicate--revocation-missing C1 × sequence-replay-duplicate + revocation-missing | reject | reject | yes | 24508 | 448.331 | revocation-missing, sequence-replay |
| P-1012-sequence-replay-duplicate--revocation-boundary-just-fresh C1 × sequence-replay-duplicate + revocation-boundary-just-fresh | reject | reject | yes | 24717 | 440.024 | sequence-replay |
| P-1013-sequence-replay-duplicate--scope-unknown C1 × sequence-replay-duplicate + scope-unknown | reject | reject | yes | 24498 | 431.885 | scope-mismatch, sequence-replay |
| P-1014-sequence-replay-duplicate--action-issuer-retired-after-cutoff C1 × sequence-replay-duplicate + action-issuer-retired-after-cutoff | reject | reject | yes | 24787 | 429.661 | action-issuer-untrusted, sequence-replay |
| P-1112-revocation-missing--revocation-boundary-just-fresh C1 × revocation-missing + revocation-boundary-just-fresh | accept | accept | yes | 19554 | 365.073 | - |
| P-1113-revocation-missing--scope-unknown C1 × revocation-missing + scope-unknown | reject | reject | yes | 19333 | 357.126 | revocation-missing, scope-mismatch |
| P-1114-revocation-missing--action-issuer-retired-after-cutoff C1 × revocation-missing + action-issuer-retired-after-cutoff | reject | reject | yes | 19559 | 372.458 | action-issuer-untrusted, revocation-missing |
| P-1213-revocation-boundary-just-fresh--scope-unknown C1 × revocation-boundary-just-fresh + scope-unknown | reject | reject | yes | 19506 | 343.549 | scope-mismatch |
| P-1214-revocation-boundary-just-fresh--action-issuer-retired-after-cutoff C1 × revocation-boundary-just-fresh + action-issuer-retired-after-cutoff | reject | reject | yes | 19732 | 378.050 | action-issuer-untrusted |
| P-1314-scope-unknown--action-issuer-retired-after-cutoff C1 × scope-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19564 | 352.186 | action-issuer-untrusted, scope-mismatch |
