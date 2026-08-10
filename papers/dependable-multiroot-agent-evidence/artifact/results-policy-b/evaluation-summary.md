# EATF-Backed Multi-Root Evaluation Summary

- Cases: 152/192 matched expected verdicts.
- EATF root: `vendor/eatf`
- EATF verifier mode: offline JSON CLI.
- Total package size bytes: 3424310.
- Total EATF verify ms: 62855.946.
- Claim boundary: production-style research artifact; not a legal trust service.

| Case | Expected | Observed | Match | Size bytes | EATF verify ms | Reason codes |
|---|---:|---:|---:|---:|---:|---|
| M-C1-000-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 19307 | 358.669 | identity-issuer-untrusted |
| M-C1-001-identity-method-unknown C1 × identity-method-unknown @ identity[0] | reject | reject | yes | 19308 | 353.082 | identity-method-unaccepted |
| M-C1-002-identity-assurance-low C1 × identity-assurance-low @ identity[0] | reject | accept | no | 19293 | 379.787 | - |
| M-C1-003-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 19416 | 360.550 | - |
| M-C1-004-identity-issuer-unknown C1 × identity-issuer-unknown @ identity[1] | reject | reject | yes | 19307 | 352.495 | identity-issuer-untrusted |
| M-C1-005-identity-method-unknown C1 × identity-method-unknown @ identity[1] | reject | reject | yes | 19308 | 369.169 | identity-method-unaccepted |
| M-C1-006-identity-assurance-low C1 × identity-assurance-low @ identity[1] | reject | accept | no | 19293 | 352.162 | - |
| M-C1-007-identity-assurance-medium-boundary C1 × identity-assurance-medium-boundary @ identity[1] | accept | accept | yes | 19416 | 359.557 | - |
| M-C1-008-action-issuer-unknown C1 × action-issuer-unknown @ action[0] | reject | reject | yes | 19287 | 346.866 | action-issuer-untrusted |
| M-C1-009-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 19432 | 344.116 | action-issuer-untrusted |
| M-C1-010-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 19442 | 340.480 | - |
| M-C1-011-binding-dangling-identity C1 × binding-dangling-identity @ action[0] | reject | reject | yes | 19272 | 362.305 | broker-policy-violation, identity-hash-missing |
| M-C1-012-binding-subject-substitution C1 × binding-subject-substitution @ action[0] | reject | reject | yes | 19360 | 352.653 | identity-substitution |
| M-C1-013-scope-unknown C1 × scope-unknown @ action[0] | reject | accept | no | 19206 | 364.690 | - |
| M-C1-014-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 19393 | 350.849 | network-dependency-forbidden |
| M-C1-015-validation-material-stripped C1 × validation-material-stripped @ action[0] | reject | reject | yes | 19355 | 371.352 | archive-material-insufficient, broker-policy-violation |
| M-C1-016-revocation-missing C1 × revocation-missing @ action[0] | reject | indeterminate | no | 19201 | 368.994 | revocation-missing |
| M-C1-017-revocation-stale-8d C1 × revocation-stale-8d @ action[0] | indeterminate | accept | no | 19264 | 359.989 | - |
| M-C1-018-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 19374 | 345.674 | - |
| M-C1-019-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[0] | indeterminate | accept | no | 19374 | 351.128 | - |
| M-C1-020-algorithm-unknown C1 × algorithm-unknown @ action[0] | indeterminate | accept | no | 19241 | 347.841 | - |
| M-C1-021-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 19285 | 364.762 | - |
| M-C1-022-broker-untrusted C1 × broker-untrusted @ action[0] | reject | reject | yes | 19234 | 359.257 | broker-policy-violation |
| M-C1-023-broker-assurance-low C1 × broker-assurance-low @ action[0] | reject | accept | no | 19273 | 358.471 | - |
| M-C1-024-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[0] | accept | accept | yes | 19396 | 357.786 | - |
| M-C1-025-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[0] | reject | reject | yes | 19423 | 356.738 | broker-policy-violation |
| M-C1-026-broker-removed C1 × broker-removed @ action[0] | accept | accept | yes | 19025 | 342.356 | - |
| M-C1-027-action-issuer-unknown C1 × action-issuer-unknown @ action[1] | reject | reject | yes | 19287 | 349.872 | action-issuer-untrusted |
| M-C1-028-action-issuer-retired-after-cutoff C1 × action-issuer-retired-after-cutoff @ action[1] | reject | reject | yes | 19432 | 344.996 | action-issuer-untrusted |
| M-C1-029-action-issuer-retired-grandfathered C1 × action-issuer-retired-grandfathered @ action[1] | accept | accept | yes | 19442 | 348.328 | - |
| M-C1-030-binding-dangling-identity C1 × binding-dangling-identity @ action[1] | reject | reject | yes | 19273 | 351.755 | broker-policy-violation, identity-hash-missing |
| M-C1-031-binding-subject-substitution C1 × binding-subject-substitution @ action[1] | reject | reject | yes | 19363 | 372.826 | identity-substitution |
| M-C1-032-scope-unknown C1 × scope-unknown @ action[1] | reject | accept | no | 19204 | 352.484 | - |
| M-C1-033-live-lookup-under-offline-policy C1 × live-lookup-under-offline-policy @ action[1] | reject | reject | yes | 19393 | 356.456 | network-dependency-forbidden |
| M-C1-034-validation-material-stripped C1 × validation-material-stripped @ action[1] | reject | reject | yes | 19355 | 363.471 | archive-material-insufficient, broker-policy-violation |
| M-C1-035-revocation-missing C1 × revocation-missing @ action[1] | reject | indeterminate | no | 19201 | 355.092 | revocation-missing |
| M-C1-036-revocation-stale-8d C1 × revocation-stale-8d @ action[1] | indeterminate | accept | no | 19264 | 351.745 | - |
| M-C1-037-revocation-boundary-just-fresh C1 × revocation-boundary-just-fresh @ action[1] | accept | accept | yes | 19374 | 362.089 | - |
| M-C1-038-revocation-boundary-just-stale C1 × revocation-boundary-just-stale @ action[1] | indeterminate | accept | no | 19374 | 342.895 | - |
| M-C1-039-algorithm-unknown C1 × algorithm-unknown @ action[1] | indeterminate | accept | no | 19241 | 355.988 | - |
| M-C1-040-algorithm-pqc-accepted C1 × algorithm-pqc-accepted @ action[1] | accept | accept | yes | 19285 | 352.551 | - |
| M-C1-041-broker-untrusted C1 × broker-untrusted @ action[1] | reject | reject | yes | 19234 | 374.567 | broker-policy-violation |
| M-C1-042-broker-assurance-low C1 × broker-assurance-low @ action[1] | reject | accept | no | 19273 | 366.870 | - |
| M-C1-043-broker-assurance-medium-boundary C1 × broker-assurance-medium-boundary @ action[1] | accept | accept | yes | 19396 | 362.955 | - |
| M-C1-044-broker-claims-authoritative-verdict C1 × broker-claims-authoritative-verdict @ action[1] | reject | reject | yes | 19423 | 362.257 | broker-policy-violation |
| M-C1-045-broker-removed C1 × broker-removed @ action[1] | accept | accept | yes | 19025 | 363.314 | - |
| M-C1-046-sequence-replay-duplicate C1 × sequence-replay-duplicate @ case | reject | reject | yes | 24327 | 453.205 | sequence-replay |
| M-C2-000-identity-issuer-unknown C2 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9499 | 184.842 | identity-issuer-untrusted |
| M-C2-001-identity-method-unknown C2 × identity-method-unknown @ identity[0] | reject | reject | yes | 9501 | 172.090 | identity-method-unaccepted |
| M-C2-002-identity-assurance-low C2 × identity-assurance-low @ identity[0] | reject | accept | no | 9491 | 182.031 | - |
| M-C2-003-identity-assurance-medium-boundary C2 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9554 | 187.090 | - |
| M-C2-004-action-issuer-unknown C2 × action-issuer-unknown @ action[0] | reject | reject | yes | 9489 | 184.562 | action-issuer-untrusted |
| M-C2-005-action-issuer-retired-after-cutoff C2 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9564 | 185.555 | action-issuer-untrusted |
| M-C2-006-action-issuer-retired-grandfathered C2 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9569 | 174.707 | - |
| M-C2-007-binding-dangling-identity C2 × binding-dangling-identity @ action[0] | reject | reject | yes | 9507 | 171.507 | identity-hash-missing |
| M-C2-008-binding-subject-substitution C2 × binding-subject-substitution @ action[0] | reject | reject | yes | 9528 | 186.172 | identity-substitution |
| M-C2-009-scope-unknown C2 × scope-unknown @ action[0] | reject | accept | no | 9449 | 178.025 | - |
| M-C2-010-live-lookup-under-offline-policy C2 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9541 | 174.968 | network-dependency-forbidden |
| M-C2-011-validation-material-stripped C2 × validation-material-stripped @ action[0] | reject | reject | yes | 9523 | 178.166 | archive-material-insufficient |
| M-C2-012-revocation-missing C2 × revocation-missing @ action[0] | reject | indeterminate | no | 9419 | 169.425 | revocation-missing |
| M-C2-013-revocation-stale-8d C2 × revocation-stale-8d @ action[0] | indeterminate | accept | no | 9477 | 181.276 | - |
| M-C2-014-revocation-boundary-just-fresh C2 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9532 | 177.695 | - |
| M-C2-015-revocation-boundary-just-stale C2 × revocation-boundary-just-stale @ action[0] | indeterminate | accept | no | 9532 | 188.236 | - |
| M-C2-016-algorithm-unknown C2 × algorithm-unknown @ action[0] | indeterminate | accept | no | 9464 | 172.375 | - |
| M-C2-017-algorithm-pqc-accepted C2 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9483 | 173.055 | - |
| M-C2-018-broker-added-untrusted C2 × broker-added-untrusted @ action[0] | reject | reject | yes | 9681 | 178.641 | broker-policy-violation |
| M-C2-019-sequence-replay-duplicate C2 × sequence-replay-duplicate @ case | reject | reject | yes | 14353 | 268.839 | sequence-replay |
| M-C8-000-identity-issuer-unknown C8 × identity-issuer-unknown @ identity[0] | reject | reject | yes | 9504 | 179.115 | identity-issuer-untrusted |
| M-C8-001-identity-method-unknown C8 × identity-method-unknown @ identity[0] | reject | reject | yes | 9506 | 190.658 | identity-method-unaccepted |
| M-C8-002-identity-assurance-low C8 × identity-assurance-low @ identity[0] | reject | accept | no | 9496 | 171.110 | - |
| M-C8-003-identity-assurance-medium-boundary C8 × identity-assurance-medium-boundary @ identity[0] | accept | accept | yes | 9559 | 180.901 | - |
| M-C8-004-action-issuer-unknown C8 × action-issuer-unknown @ action[0] | reject | reject | yes | 9494 | 175.911 | action-issuer-untrusted |
| M-C8-005-action-issuer-retired-after-cutoff C8 × action-issuer-retired-after-cutoff @ action[0] | reject | reject | yes | 9569 | 186.683 | action-issuer-untrusted |
| M-C8-006-action-issuer-retired-grandfathered C8 × action-issuer-retired-grandfathered @ action[0] | accept | accept | yes | 9574 | 179.823 | - |
| M-C8-007-binding-dangling-identity C8 × binding-dangling-identity @ action[0] | reject | reject | yes | 9513 | 185.520 | identity-hash-missing |
| M-C8-008-binding-subject-substitution C8 × binding-subject-substitution @ action[0] | reject | reject | yes | 9536 | 172.694 | identity-substitution |
| M-C8-009-scope-unknown C8 × scope-unknown @ action[0] | reject | accept | no | 9452 | 173.193 | - |
| M-C8-010-live-lookup-under-offline-policy C8 × live-lookup-under-offline-policy @ action[0] | reject | reject | yes | 9546 | 187.238 | network-dependency-forbidden |
| M-C8-011-validation-material-stripped C8 × validation-material-stripped @ action[0] | reject | reject | yes | 9528 | 179.137 | archive-material-insufficient |
| M-C8-012-revocation-missing C8 × revocation-missing @ action[0] | reject | indeterminate | no | 9424 | 178.158 | revocation-missing |
| M-C8-013-revocation-stale-8d C8 × revocation-stale-8d @ action[0] | indeterminate | accept | no | 9482 | 185.797 | - |
| M-C8-014-revocation-boundary-just-fresh C8 × revocation-boundary-just-fresh @ action[0] | accept | accept | yes | 9537 | 189.448 | - |
| M-C8-015-revocation-boundary-just-stale C8 × revocation-boundary-just-stale @ action[0] | indeterminate | accept | no | 9537 | 177.614 | - |
| M-C8-016-algorithm-unknown C8 × algorithm-unknown @ action[0] | indeterminate | accept | no | 9469 | 183.860 | - |
| M-C8-017-algorithm-pqc-accepted C8 × algorithm-pqc-accepted @ action[0] | accept | accept | yes | 9488 | 175.511 | - |
| M-C8-018-broker-added-untrusted C8 × broker-added-untrusted @ action[0] | reject | reject | yes | 9686 | 182.247 | broker-policy-violation |
| M-C8-019-sequence-replay-duplicate C8 × sequence-replay-duplicate @ case | reject | reject | yes | 14368 | 268.975 | sequence-replay |
| P-0001-action-issuer-unknown--algorithm-unknown C1 × action-issuer-unknown + algorithm-unknown | reject | reject | yes | 19454 | 348.970 | action-issuer-untrusted |
| P-0002-action-issuer-unknown--validation-material-stripped C1 × action-issuer-unknown + validation-material-stripped | reject | reject | yes | 19568 | 349.933 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0003-action-issuer-unknown--identity-assurance-low C1 × action-issuer-unknown + identity-assurance-low | reject | reject | yes | 19506 | 360.986 | action-issuer-untrusted |
| P-0004-action-issuer-unknown--binding-dangling-identity C1 × action-issuer-unknown + binding-dangling-identity | reject | reject | yes | 19485 | 359.614 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0005-action-issuer-unknown--broker-untrusted C1 × action-issuer-unknown + broker-untrusted | reject | reject | yes | 19447 | 356.110 | action-issuer-untrusted, broker-policy-violation |
| P-0006-action-issuer-unknown--broker-assurance-low C1 × action-issuer-unknown + broker-assurance-low | reject | reject | yes | 19486 | 356.633 | action-issuer-untrusted |
| P-0007-action-issuer-unknown--identity-method-unknown C1 × action-issuer-unknown + identity-method-unknown | reject | reject | yes | 19521 | 356.538 | action-issuer-untrusted, identity-method-unaccepted |
| P-0008-action-issuer-unknown--identity-issuer-unknown C1 × action-issuer-unknown + identity-issuer-unknown | reject | reject | yes | 19520 | 343.249 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0009-action-issuer-unknown--live-lookup-under-offline-policy C1 × action-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19606 | 344.633 | action-issuer-untrusted, network-dependency-forbidden |
| P-0010-action-issuer-unknown--sequence-replay-duplicate C1 × action-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24606 | 436.852 | action-issuer-untrusted, sequence-replay |
| P-0011-action-issuer-unknown--revocation-missing C1 × action-issuer-unknown + revocation-missing | reject | reject | yes | 19414 | 350.296 | action-issuer-untrusted, revocation-missing |
| P-0012-action-issuer-unknown--revocation-boundary-just-fresh C1 × action-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19587 | 353.133 | action-issuer-untrusted |
| P-0013-action-issuer-unknown--scope-unknown C1 × action-issuer-unknown + scope-unknown | reject | reject | yes | 19419 | 363.333 | action-issuer-untrusted |
| P-0014-action-issuer-unknown--action-issuer-retired-after-cutoff C1 × action-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19642 | 368.516 | action-issuer-untrusted |
| P-0102-algorithm-unknown--validation-material-stripped C1 × algorithm-unknown + validation-material-stripped | reject | reject | yes | 19522 | 354.152 | archive-material-insufficient, broker-policy-violation |
| P-0103-algorithm-unknown--identity-assurance-low C1 × algorithm-unknown + identity-assurance-low | reject | accept | no | 19460 | 364.358 | - |
| P-0104-algorithm-unknown--binding-dangling-identity C1 × algorithm-unknown + binding-dangling-identity | reject | reject | yes | 19439 | 358.592 | broker-policy-violation, identity-hash-missing |
| P-0105-algorithm-unknown--broker-untrusted C1 × algorithm-unknown + broker-untrusted | reject | reject | yes | 19401 | 356.324 | broker-policy-violation |
| P-0106-algorithm-unknown--broker-assurance-low C1 × algorithm-unknown + broker-assurance-low | reject | accept | no | 19440 | 341.003 | - |
| P-0107-algorithm-unknown--identity-method-unknown C1 × algorithm-unknown + identity-method-unknown | reject | reject | yes | 19475 | 351.666 | identity-method-unaccepted |
| P-0108-algorithm-unknown--identity-issuer-unknown C1 × algorithm-unknown + identity-issuer-unknown | reject | reject | yes | 19474 | 369.788 | identity-issuer-untrusted |
| P-0109-algorithm-unknown--live-lookup-under-offline-policy C1 × algorithm-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19560 | 362.084 | network-dependency-forbidden |
| P-0110-algorithm-unknown--sequence-replay-duplicate C1 × algorithm-unknown + sequence-replay-duplicate | reject | reject | yes | 24542 | 460.493 | sequence-replay |
| P-0111-algorithm-unknown--revocation-missing C1 × algorithm-unknown + revocation-missing | reject | indeterminate | no | 19368 | 347.213 | revocation-missing |
| P-0112-algorithm-unknown--revocation-boundary-just-fresh C1 × algorithm-unknown + revocation-boundary-just-fresh | indeterminate | accept | no | 19541 | 348.014 | - |
| P-0113-algorithm-unknown--scope-unknown C1 × algorithm-unknown + scope-unknown | reject | accept | no | 19373 | 370.984 | - |
| P-0114-algorithm-unknown--action-issuer-retired-after-cutoff C1 × algorithm-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19599 | 359.586 | action-issuer-untrusted |
| P-0203-validation-material-stripped--identity-assurance-low C1 × validation-material-stripped + identity-assurance-low | reject | reject | yes | 19574 | 361.012 | archive-material-insufficient, broker-policy-violation |
| P-0204-validation-material-stripped--binding-dangling-identity C1 × validation-material-stripped + binding-dangling-identity | reject | reject | yes | 19553 | 350.746 | archive-material-insufficient, broker-policy-violation, identity-hash-missing |
| P-0205-validation-material-stripped--broker-untrusted C1 × validation-material-stripped + broker-untrusted | reject | reject | yes | 19515 | 350.786 | archive-material-insufficient, broker-policy-violation |
| P-0206-validation-material-stripped--broker-assurance-low C1 × validation-material-stripped + broker-assurance-low | reject | reject | yes | 19554 | 350.360 | archive-material-insufficient, broker-policy-violation |
| P-0207-validation-material-stripped--identity-method-unknown C1 × validation-material-stripped + identity-method-unknown | reject | reject | yes | 19589 | 348.369 | archive-material-insufficient, broker-policy-violation, identity-method-unaccepted |
| P-0208-validation-material-stripped--identity-issuer-unknown C1 × validation-material-stripped + identity-issuer-unknown | reject | reject | yes | 19588 | 338.742 | archive-material-insufficient, broker-policy-violation, identity-issuer-untrusted |
| P-0209-validation-material-stripped--live-lookup-under-offline-policy C1 × validation-material-stripped + live-lookup-under-offline-policy | reject | reject | yes | 19674 | 356.972 | archive-material-insufficient, broker-policy-violation, network-dependency-forbidden |
| P-0210-validation-material-stripped--sequence-replay-duplicate C1 × validation-material-stripped + sequence-replay-duplicate | reject | reject | yes | 24693 | 448.995 | archive-material-insufficient, broker-policy-violation, sequence-replay |
| P-0211-validation-material-stripped--revocation-missing C1 × validation-material-stripped + revocation-missing | reject | reject | yes | 19482 | 353.786 | archive-material-insufficient, broker-policy-violation, revocation-missing |
| P-0212-validation-material-stripped--revocation-boundary-just-fresh C1 × validation-material-stripped + revocation-boundary-just-fresh | reject | reject | yes | 19655 | 358.610 | archive-material-insufficient, broker-policy-violation |
| P-0213-validation-material-stripped--scope-unknown C1 × validation-material-stripped + scope-unknown | reject | reject | yes | 19487 | 353.362 | archive-material-insufficient, broker-policy-violation |
| P-0214-validation-material-stripped--action-issuer-retired-after-cutoff C1 × validation-material-stripped + action-issuer-retired-after-cutoff | reject | reject | yes | 19713 | 337.724 | action-issuer-untrusted, archive-material-insufficient, broker-policy-violation |
| P-0304-identity-assurance-low--binding-dangling-identity C1 × identity-assurance-low + binding-dangling-identity | reject | reject | yes | 19491 | 356.027 | broker-policy-violation, identity-hash-missing |
| P-0305-identity-assurance-low--broker-untrusted C1 × identity-assurance-low + broker-untrusted | reject | reject | yes | 19453 | 359.311 | broker-policy-violation |
| P-0306-identity-assurance-low--broker-assurance-low C1 × identity-assurance-low + broker-assurance-low | reject | accept | no | 19492 | 357.862 | - |
| P-0307-identity-assurance-low--identity-method-unknown C1 × identity-assurance-low + identity-method-unknown | reject | reject | yes | 19527 | 364.126 | identity-method-unaccepted |
| P-0308-identity-assurance-low--identity-issuer-unknown C1 × identity-assurance-low + identity-issuer-unknown | reject | reject | yes | 19526 | 337.049 | identity-issuer-untrusted |
| P-0309-identity-assurance-low--live-lookup-under-offline-policy C1 × identity-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19612 | 350.699 | network-dependency-forbidden |
| P-0310-identity-assurance-low--sequence-replay-duplicate C1 × identity-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24612 | 436.407 | sequence-replay |
| P-0311-identity-assurance-low--revocation-missing C1 × identity-assurance-low + revocation-missing | reject | indeterminate | no | 19420 | 364.202 | revocation-missing |
| P-0312-identity-assurance-low--revocation-boundary-just-fresh C1 × identity-assurance-low + revocation-boundary-just-fresh | reject | accept | no | 19593 | 353.469 | - |
| P-0313-identity-assurance-low--scope-unknown C1 × identity-assurance-low + scope-unknown | reject | accept | no | 19425 | 352.999 | - |
| P-0314-identity-assurance-low--action-issuer-retired-after-cutoff C1 × identity-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19651 | 365.418 | action-issuer-untrusted |
| P-0405-binding-dangling-identity--broker-untrusted C1 × binding-dangling-identity + broker-untrusted | reject | reject | yes | 19432 | 351.528 | broker-policy-violation, identity-hash-missing |
| P-0406-binding-dangling-identity--broker-assurance-low C1 × binding-dangling-identity + broker-assurance-low | reject | reject | yes | 19471 | 346.161 | broker-policy-violation, identity-hash-missing |
| P-0407-binding-dangling-identity--identity-method-unknown C1 × binding-dangling-identity + identity-method-unknown | reject | reject | yes | 19506 | 346.881 | broker-policy-violation, identity-hash-missing, identity-method-unaccepted |
| P-0408-binding-dangling-identity--identity-issuer-unknown C1 × binding-dangling-identity + identity-issuer-unknown | reject | reject | yes | 19504 | 353.214 | broker-policy-violation, identity-hash-missing, identity-issuer-untrusted |
| P-0409-binding-dangling-identity--live-lookup-under-offline-policy C1 × binding-dangling-identity + live-lookup-under-offline-policy | reject | reject | yes | 19591 | 353.493 | broker-policy-violation, identity-hash-missing, network-dependency-forbidden |
| P-0410-binding-dangling-identity--sequence-replay-duplicate C1 × binding-dangling-identity + sequence-replay-duplicate | reject | reject | yes | 24548 | 451.340 | broker-policy-violation, identity-hash-missing, sequence-replay |
| P-0411-binding-dangling-identity--revocation-missing C1 × binding-dangling-identity + revocation-missing | reject | reject | yes | 19399 | 343.214 | broker-policy-violation, identity-hash-missing, revocation-missing |
| P-0412-binding-dangling-identity--revocation-boundary-just-fresh C1 × binding-dangling-identity + revocation-boundary-just-fresh | reject | reject | yes | 19572 | 356.169 | broker-policy-violation, identity-hash-missing |
| P-0413-binding-dangling-identity--scope-unknown C1 × binding-dangling-identity + scope-unknown | reject | reject | yes | 19404 | 351.769 | broker-policy-violation, identity-hash-missing |
| P-0414-binding-dangling-identity--action-issuer-retired-after-cutoff C1 × binding-dangling-identity + action-issuer-retired-after-cutoff | reject | reject | yes | 19630 | 355.139 | action-issuer-untrusted, broker-policy-violation, identity-hash-missing |
| P-0506-broker-untrusted--broker-assurance-low C1 × broker-untrusted + broker-assurance-low | reject | reject | yes | 19433 | 338.284 | broker-policy-violation |
| P-0507-broker-untrusted--identity-method-unknown C1 × broker-untrusted + identity-method-unknown | reject | reject | yes | 19468 | 355.918 | broker-policy-violation, identity-method-unaccepted |
| P-0508-broker-untrusted--identity-issuer-unknown C1 × broker-untrusted + identity-issuer-unknown | reject | reject | yes | 19467 | 352.468 | broker-policy-violation, identity-issuer-untrusted |
| P-0509-broker-untrusted--live-lookup-under-offline-policy C1 × broker-untrusted + live-lookup-under-offline-policy | reject | reject | yes | 19553 | 353.108 | broker-policy-violation, network-dependency-forbidden |
| P-0510-broker-untrusted--sequence-replay-duplicate C1 × broker-untrusted + sequence-replay-duplicate | reject | reject | yes | 24535 | 435.157 | broker-policy-violation, sequence-replay |
| P-0511-broker-untrusted--revocation-missing C1 × broker-untrusted + revocation-missing | reject | reject | yes | 19361 | 371.138 | broker-policy-violation, revocation-missing |
| P-0512-broker-untrusted--revocation-boundary-just-fresh C1 × broker-untrusted + revocation-boundary-just-fresh | reject | reject | yes | 19534 | 355.248 | broker-policy-violation |
| P-0513-broker-untrusted--scope-unknown C1 × broker-untrusted + scope-unknown | reject | reject | yes | 19366 | 344.754 | broker-policy-violation |
| P-0514-broker-untrusted--action-issuer-retired-after-cutoff C1 × broker-untrusted + action-issuer-retired-after-cutoff | reject | reject | yes | 19592 | 367.664 | action-issuer-untrusted, broker-policy-violation |
| P-0607-broker-assurance-low--identity-method-unknown C1 × broker-assurance-low + identity-method-unknown | reject | reject | yes | 19507 | 363.884 | identity-method-unaccepted |
| P-0608-broker-assurance-low--identity-issuer-unknown C1 × broker-assurance-low + identity-issuer-unknown | reject | reject | yes | 19506 | 358.593 | identity-issuer-untrusted |
| P-0609-broker-assurance-low--live-lookup-under-offline-policy C1 × broker-assurance-low + live-lookup-under-offline-policy | reject | reject | yes | 19592 | 351.527 | network-dependency-forbidden |
| P-0610-broker-assurance-low--sequence-replay-duplicate C1 × broker-assurance-low + sequence-replay-duplicate | reject | reject | yes | 24585 | 443.043 | sequence-replay |
| P-0611-broker-assurance-low--revocation-missing C1 × broker-assurance-low + revocation-missing | reject | indeterminate | no | 19400 | 354.498 | revocation-missing |
| P-0612-broker-assurance-low--revocation-boundary-just-fresh C1 × broker-assurance-low + revocation-boundary-just-fresh | reject | accept | no | 19573 | 355.282 | - |
| P-0613-broker-assurance-low--scope-unknown C1 × broker-assurance-low + scope-unknown | reject | accept | no | 19405 | 360.297 | - |
| P-0614-broker-assurance-low--action-issuer-retired-after-cutoff C1 × broker-assurance-low + action-issuer-retired-after-cutoff | reject | reject | yes | 19631 | 361.269 | action-issuer-untrusted |
| P-0708-identity-method-unknown--identity-issuer-unknown C1 × identity-method-unknown + identity-issuer-unknown | reject | reject | yes | 19541 | 352.555 | identity-issuer-untrusted, identity-method-unaccepted |
| P-0709-identity-method-unknown--live-lookup-under-offline-policy C1 × identity-method-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19627 | 357.813 | identity-method-unaccepted, network-dependency-forbidden |
| P-0710-identity-method-unknown--sequence-replay-duplicate C1 × identity-method-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 434.410 | identity-method-unaccepted, sequence-replay |
| P-0711-identity-method-unknown--revocation-missing C1 × identity-method-unknown + revocation-missing | reject | reject | yes | 19435 | 366.895 | identity-method-unaccepted, revocation-missing |
| P-0712-identity-method-unknown--revocation-boundary-just-fresh C1 × identity-method-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19608 | 356.853 | identity-method-unaccepted |
| P-0713-identity-method-unknown--scope-unknown C1 × identity-method-unknown + scope-unknown | reject | reject | yes | 19440 | 357.886 | identity-method-unaccepted |
| P-0714-identity-method-unknown--action-issuer-retired-after-cutoff C1 × identity-method-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19666 | 356.251 | action-issuer-untrusted, identity-method-unaccepted |
| P-0809-identity-issuer-unknown--live-lookup-under-offline-policy C1 × identity-issuer-unknown + live-lookup-under-offline-policy | reject | reject | yes | 19626 | 348.352 | identity-issuer-untrusted, network-dependency-forbidden |
| P-0810-identity-issuer-unknown--sequence-replay-duplicate C1 × identity-issuer-unknown + sequence-replay-duplicate | reject | reject | yes | 24630 | 450.181 | identity-issuer-untrusted, sequence-replay |
| P-0811-identity-issuer-unknown--revocation-missing C1 × identity-issuer-unknown + revocation-missing | reject | reject | yes | 19434 | 368.819 | identity-issuer-untrusted, revocation-missing |
| P-0812-identity-issuer-unknown--revocation-boundary-just-fresh C1 × identity-issuer-unknown + revocation-boundary-just-fresh | reject | reject | yes | 19607 | 347.358 | identity-issuer-untrusted |
| P-0813-identity-issuer-unknown--scope-unknown C1 × identity-issuer-unknown + scope-unknown | reject | reject | yes | 19439 | 345.996 | identity-issuer-untrusted |
| P-0814-identity-issuer-unknown--action-issuer-retired-after-cutoff C1 × identity-issuer-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19665 | 362.921 | action-issuer-untrusted, identity-issuer-untrusted |
| P-0910-live-lookup-under-offline-policy--sequence-replay-duplicate C1 × live-lookup-under-offline-policy + sequence-replay-duplicate | reject | reject | yes | 24741 | 429.099 | network-dependency-forbidden, sequence-replay |
| P-0911-live-lookup-under-offline-policy--revocation-missing C1 × live-lookup-under-offline-policy + revocation-missing | reject | reject | yes | 19520 | 359.120 | network-dependency-forbidden, revocation-missing |
| P-0912-live-lookup-under-offline-policy--revocation-boundary-just-fresh C1 × live-lookup-under-offline-policy + revocation-boundary-just-fresh | reject | reject | yes | 19693 | 355.988 | network-dependency-forbidden |
| P-0913-live-lookup-under-offline-policy--scope-unknown C1 × live-lookup-under-offline-policy + scope-unknown | reject | reject | yes | 19525 | 371.080 | network-dependency-forbidden |
| P-0914-live-lookup-under-offline-policy--action-issuer-retired-after-cutoff C1 × live-lookup-under-offline-policy + action-issuer-retired-after-cutoff | reject | reject | yes | 19751 | 358.109 | action-issuer-untrusted, network-dependency-forbidden |
| P-1011-sequence-replay-duplicate--revocation-missing C1 × sequence-replay-duplicate + revocation-missing | reject | reject | yes | 24508 | 453.953 | revocation-missing, sequence-replay |
| P-1012-sequence-replay-duplicate--revocation-boundary-just-fresh C1 × sequence-replay-duplicate + revocation-boundary-just-fresh | reject | reject | yes | 24717 | 453.399 | sequence-replay |
| P-1013-sequence-replay-duplicate--scope-unknown C1 × sequence-replay-duplicate + scope-unknown | reject | reject | yes | 24498 | 454.329 | sequence-replay |
| P-1014-sequence-replay-duplicate--action-issuer-retired-after-cutoff C1 × sequence-replay-duplicate + action-issuer-retired-after-cutoff | reject | reject | yes | 24787 | 468.818 | action-issuer-untrusted, sequence-replay |
| P-1112-revocation-missing--revocation-boundary-just-fresh C1 × revocation-missing + revocation-boundary-just-fresh | accept | accept | yes | 19554 | 367.594 | - |
| P-1113-revocation-missing--scope-unknown C1 × revocation-missing + scope-unknown | reject | indeterminate | no | 19333 | 368.682 | revocation-missing |
| P-1114-revocation-missing--action-issuer-retired-after-cutoff C1 × revocation-missing + action-issuer-retired-after-cutoff | reject | reject | yes | 19559 | 349.961 | action-issuer-untrusted, revocation-missing |
| P-1213-revocation-boundary-just-fresh--scope-unknown C1 × revocation-boundary-just-fresh + scope-unknown | reject | accept | no | 19506 | 353.431 | - |
| P-1214-revocation-boundary-just-fresh--action-issuer-retired-after-cutoff C1 × revocation-boundary-just-fresh + action-issuer-retired-after-cutoff | reject | reject | yes | 19732 | 364.721 | action-issuer-untrusted |
| P-1314-scope-unknown--action-issuer-retired-after-cutoff C1 × scope-unknown + action-issuer-retired-after-cutoff | reject | reject | yes | 19564 | 361.902 | action-issuer-untrusted |
