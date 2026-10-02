# Lead review T9a: Codex T1 (f5d76e8) and T2 (4f867ba, research/15)

Status: draft in progress.

## Sources checked
- collaboration/claude-h6-placement-review.md (the five T1 corrections, TASKS.md T1 list)
- git show f5d76e8, git show 4f867ba
- sources/tmp-audit-snapshot-2026-09-28/cmp109.md lines 86-92 (Eq. (0.4) OCR)
- No local primary scan of CMP 109 exists (cmp109.pdf is an Incapsula HTML error page).

## T1 checks (in progress)
1. Lemma 3' : statement and proof correct (Duhamel + ||Z||<=pi).
2. Q_m index, sqrt2, path hypotheses at all t: applied.
3. Normalization / TV form / sequential: applied; see signed-mass issue (pending).
4. Second moment (3.11): applied; equivalence claim checked: (s+1) <= (s+L^d)^2/s <= 2L^{2d}(s+1).
5. C Delta beta term + sentence replacement: applied.

## T2 checks (in progress)

### Computations done (scripts in /private/tmp/ym-r3/T9a)
- check1.py: weights of (1.2) sum to 1 (d=2,L=3,5; d=3,L=3). sup_b sum_c omega_c({b}) = 1.111 (d2L3), 1.080 (d2L5), 1.037 (d3L3); K_{d,L}=1.222,1.160,1.074; claimed bound 2d+L^{1-d} holds (loose by factor ~4-6). Backtracking multiplicity 2 occurs (N_b needed).
- check2.py: exact linearization (finite differences of the nonlinear map at U=1) equals (3.1)-(3.2). div P tau = 0 to 1e-15. Ratios to the bounds in (3.5)-(3.6) max = 1; l2 operator norm^2 on ker(div) equals L^{2-d} exactly; constant current attains all three bounds. Prop 2 correct and sharp.
