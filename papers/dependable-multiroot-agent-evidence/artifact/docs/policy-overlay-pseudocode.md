# Policy-overlay decision procedure

Full pseudocode for the multi-root policy layer, derived line by line from
`src/eatf_policy_overlay.py` (295 lines). The paper prints a condensed form as
Algorithm 1; this document gives all three procedures and cites the
implementing lines, so that a reader can check the description against the
source without reading the source first.

The verdict rule is a two-step priority join over reason statuses — nothing
more elaborate is claimed or implemented.

## Verdict algebra (lines 36–48)

```
final_verdict(reasons):
    if ∃ reason with status = fail      → reject
    elif ∃ reason with status = missing → indeterminate
    else                                → accept
```

Three statuses only: `fail` dominates `missing`, which dominates `pass`. Note
that a package-layer failure and a policy violation both yield `reject`; what
distinguishes them is the reason trace, not the verdict.

## Algorithm 1 — EVALUATE-CASE (lines 66–199)

```
Input:  case (id, verification_time τ, expected_verdict),
        package_records R (from eatf-verify --json),
        policy P (a relying-party policy document)
Output: verdict ∈ {accept, reject, indeterminate}, reason trace, metrics,
        baseline verdicts

1  reasons ← []
2  for r ∈ R:                                        ▷ package layer (74–80)
3      if r.valid: add(eatf-package-valid, pass)
4      else:       add(eatf-package-invalid, fail) and echo r.failure_reason as fail
5  I ← {r ∈ R : r.role = identity ∧ r.valid}         ▷ (82–87)
6  A ← [r ∈ R : r.role = action ∧ r.valid]
7  for id ∈ I:                                       ▷ identity layer (89–109)
8      id.issuer ∈ P.trusted_identity_issuers         else fail(identity-issuer-untrusted)
9      id.method ∈ P.accepted_identity_methods        else fail(identity-method-unaccepted)
10     rank(id.assurance) ≥ rank(P.min_identity_assurance)
                                                      else fail(identity-assurance-insufficient)
11 seen ← ∅                                          ▷ action layer (111–178)
12 for a ∈ A:
13     TRUSTED-ISSUER(a.issuer, action, a.issued_at, τ, P)   else fail(action-issuer-untrusted)
14     id ← I[a.identity_attestation_id]
15         absent                 → fail(identity-hash-missing)
16         id.subject ≠ a.subject → fail(identity-substitution)   ▷ binding check
17         else                   → pass(identity-binding)
18     a.scope ∈ P.accepted_scopes                    else fail(scope-mismatch)
19     (a.subject, a.sequence) ∈ seen → fail(sequence-replay); else insert   ▷ replay
20     if a.requires_live_lookup:
21         P.offline_only → fail(network-dependency-forbidden)
22         else           → missing(network-lookup-required)
23     if P.require_embedded_validation_material:
24         a.validation_material_embedded             else fail(archive-material-insufficient)
25     if P.revocation.required:                      ▷ (156–168)
26         status absent → (P.revocation.missing = reject ? fail : missing)(revocation-missing)
27         age(τ) > P.revocation.max_age_days
                        → (P.revocation.stale = reject ? fail : missing)(revocation-stale)
28         else → pass(revocation-status)
29     a.algorithm_profile ∈ P.accepted_algorithm_profiles → pass
30         else if P.archive_mode ∧ profile ∈ P.archive_algorithm_profiles → pass
31         else → missing(algorithm-unaccepted)       ▷ migration = indeterminate, not reject
32     EVALUATE-BROKER(a, P, reasons)                 ▷ Algorithm 3
33 return final_verdict(reasons), trace, metrics, BASELINES(case, R)
```

Line 115: `action_issued_at` falls back to `created_at` when the attribute is
absent, so a package that omits an explicit issuance time is still evaluated
against the trust cut-offs rather than skipped.

## Algorithm 2 — TRUSTED-ISSUER with time cut-offs (lines 202–220)

```
issuer ∈ P.trusted_{role}_issuers                     else untrusted
c ← P.trust_cutoffs[issuer];  no cut-off → trusted
τ < c.after                                           → trusted   ▷ verification before cut-off
c.allow_issued_before_cutoff ∧ issued_at < c.after    → trusted   ▷ grandfathering
otherwise                                             → untrusted
```

## Algorithm 3 — EVALUATE-BROKER (lines 223–252)

```
no broker_id → pass(broker-absent)
broker ∉ P.broker.trusted_brokers                     → fail
rank(broker_assurance) < rank(P.broker.min_assurance) → fail
P.broker.require_exposed_routing ∧ no selected-issuer → fail   ▷ routing must be visible
P.broker.require_validation_material ∧ not embedded   → fail
broker claims an authoritative verdict                → fail   ▷ broker may transport, not decide
else → pass(broker-policy)
```

## Built-in baseline verdicts (lines 255–294)

Alongside its own verdict the evaluator computes four deliberately weaker
models per case, so that the overlay's discrimination can be compared with
simpler alternatives on identical evidence. Table 2 of the paper reports the
outcome.

| baseline | rule (as implemented) |
|---|---|
| `mutable_log` | accept iff the case is flagged mutable-log-only — models "the application log says so" |
| `single_root_registry` | accept iff every issuer is the single registry root, else reject |
| `detached_signature` | accept iff all packages are valid ∧ all action validation material is embedded, else indeterminate |
| `broker_authoritative` | whatever the broker claims; indeterminate when no claim is made |

Two of these were corrected in v0.2: as written in v0.1 the mutable-log model
tested a flag no case set and the single-root model compared against an issuer
name no case used, so both were vacuous on this corpus. The source documents
the previous behaviour in comments.

## Scope of what the reason trace covers

The overlay decides on attributes carried in each package's `metadata.json`.
The EATF package layer signs the action payload (`canonical.bin`) and records
its digest; it does not bind `metadata.json`. The corpus therefore exercises
policy decisions over declared attributes, with package-layer integrity checked
separately. The paper states this in §Validation and §Limitations.
