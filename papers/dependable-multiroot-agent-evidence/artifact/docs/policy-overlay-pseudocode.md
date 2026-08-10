# P13 — Policy-overlay decision procedure, derived from code (R1.4i)

Source of truth: `artifact-v0.2/src/eatf_policy_overlay.py` (285 lines), read in full 2026-08-09.
Every rule below cites the implementing lines. ⛔ No lattice-theoretic claims — the verdict rule
is a two-step priority join and is presented as exactly that.

## Verdict algebra (lines 36–41)

```
final_verdict(reasons):
    if ∃ reason with status = fail     → reject
    elif ∃ reason with status = missing → indeterminate
    else                                → accept
```

Three statuses only; `fail` dominates `missing` dominates `pass`. No other combination logic.

## Algorithm 1 — EVALUATE-CASE (lines 66–197)

```
Input:  case (id, verification_time τ, expected_verdict),
        package_records R (from eatf-verify --json),
        policy P (org-a-policy.json)
Output: verdict ∈ {accept, reject, indeterminate}, reason trace, metrics, baseline verdicts

1  reasons ← []
2  for r ∈ R:                                        ▷ package layer (74–80)
3      if r.valid: add(eatf-package-valid, pass)
4      else:       add(eatf-package-invalid, fail) and echo r.failure_reason as fail
5  I ← {r ∈ R : r.role = identity ∧ r.valid}         ▷ (82–87)
6  A ← [r ∈ R : r.role = action ∧ r.valid]
7  for id ∈ I:                                       ▷ identity layer (89–107)
8      id.issuer ∈ P.trusted_identity_issuers         else fail(identity-issuer-untrusted)
9      id.method ∈ P.accepted_identity_methods        else fail(identity-method-unaccepted)
10     rank(id.assurance) ≥ rank(P.min_identity_assurance)
                                                      else fail(⚠ see defect note)
11 seen ← ∅                                          ▷ action layer (109–176)
12 for a ∈ A:
13     TRUSTED-ISSUER(a.issuer, action, a.issued_at, τ, P)   else fail(action-issuer-untrusted)
14     id ← I[a.identity_attestation_id]
15         absent                → fail(identity-hash-missing)
16         id.subject ≠ a.subject → fail(identity-substitution)   ▷ binding check
17         else                  → pass(identity-binding)
18     a.scope ∈ P.accepted_scopes                    else fail(scope-mismatch)
19     (a.subject, a.sequence) ∈ seen → fail(sequence-replay); else insert   ▷ replay
20     if a.requires_live_lookup:
21         P.offline_only → fail(network-dependency-forbidden)
22         else           → missing(network-lookup-required)
23     if P.require_embedded_validation_material:
24         a.validation_material_embedded             else fail(archive-material-insufficient)
25     if P.revocation.required:                      ▷ (154–166)
26         status absent → (P.revocation.missing=reject ? fail : missing)(revocation-missing)
27         age(τ) > P.revocation.max_age_days
                        → (P.revocation.stale=reject ? fail : missing)(revocation-stale)
28         else → pass(revocation-status)
29     a.algorithm_profile ∈ P.accepted_algorithm_profiles → pass
30         else if P.archive_mode ∧ profile ∈ P.archive_algorithm_profiles → pass
31         else → missing(algorithm-unaccepted)       ▷ migration = indeterminate, not reject
32     EVALUATE-BROKER(a, P, reasons)                 ▷ Algorithm 3
33 return final_verdict(reasons), trace, metrics, BASELINES(case, R)
```

## Algorithm 2 — TRUSTED-ISSUER with time cut-offs (lines 200–218)

```
issuer ∈ P.trusted_{role}_issuers                     else untrusted
c ← P.trust_cutoffs[issuer];  no cut-off → trusted
τ < c.after                                           → trusted   ▷ verification before cut-off
c.allow_issued_before_cutoff ∧ issued_at < c.after    → trusted   ▷ grandfathering
otherwise                                             → untrusted
```

## Algorithm 3 — EVALUATE-BROKER (lines 221–250)

```
no broker_id → pass(broker-absent)
broker ∉ P.broker.trusted_brokers                     → fail
rank(broker_assurance) < rank(P.broker.min_assurance) → fail
P.broker.require_exposed_routing ∧ no selected-issuer → fail   ▷ routing must be visible
P.broker.require_validation_material ∧ not embedded   → fail
broker claims an authoritative verdict                → fail   ▷ broker may transport, not decide
else → pass(broker-policy)
```

## Built-in baseline verdicts (lines 253–284) — directly relevant to R3(3)/P6

The artifact **already computes four baseline verdicts per case**, modelling the架 alternatives the
paper argues against:

| baseline | rule (as implemented) |
|---|---|
| `mutable_log` | accept iff the case is flagged mutable-log-only — models "the app log says so" |
| `single_root_registry` | accept iff every issuer = `root-a`, else reject — models one-registry trust |
| `detached_signature` | accept iff all packages valid ∧ all action validation material embedded, else indeterminate |
| `broker_authoritative` | whatever the broker claims; indeterminate if no claim |

These are exactly the "no baseline analogue" comparison points for the scoped-C table: the revision
should *surface* them (per-case table: overlay verdict vs four baselines) — the machinery exists,
the paper just never printed it.

## ⚠ Defect found while deriving (fix in v0.2, disclose in the response letter)

`eatf_policy_overlay.py:107`: the **identity-assurance failure** emits reason code
`identity-method-unaccepted` — a copy-paste of the line-100 code — instead of an
assurance-specific code. Verdicts are unaffected (still `fail`), but the reason trace mislabels
*why*, and reasoned verdicts are part of the paper's claim. v0.2: introduce
`identity-assurance-insufficient`, add a regression case where method passes and assurance fails,
and state the fix in the response letter (fix-rounds guardrail: the fix itself gets adversaried).

Also worth one manuscript sentence: `action_issued_at` falls back to `created_at` (line 113) —
document the fallback rather than leaving it implicit.
