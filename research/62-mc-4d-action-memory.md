# Monte Carlo, 4D: does the terminal theory forget an irrelevant action term? (inconclusive at N <= 2)

Status: **computation** (T58, 4D part). Scripts:

- `research/scripts/t58_mc_action_universality.py` (masked-staple heat
  bath);
- `research/scripts/t58_matching.py` (output `t58_matching.out`);
- raw data in `t58_4d.out` and, for Wilson, `t51_universality.out`.

This is the 4D counterpart of note 59. The result is **inconclusive**.

## Setup

- SU(2), d = 4, terminal lattice 4⁴, L = 2. Depths N = 1 (8⁴) and N = 2
  (16⁴).
- Actions: Wilson, and tree-level Symanzik (c_0 = 5/3, c_1 = -1/12).
- In 4D the bare coupling must be matched. At each depth, β is tuned
  separately for each action so that the terminal plaquette P takes a
  common value. The terminal 1×2 loop W12 is then compared at that P.
- Statistics: 150 thermalization updates, 200 measurements. Errors come
  from Gaussian resampling of the quadratic interpolations.

## Results

| N | P | β (Symanzik) | β (Wilson) | W12_sym - W12_wil |
|---|---|---|---|---|
| 1 | 0.583 | 1.940 | 2.613 | -0.0086(24) |
| 1 | 0.621 | 2.039 | 2.727 | -0.0075(18) |
| 1 | 0.660 | 2.158 | 2.877 | -0.0073(17) |
| 2 | 0.608 | 2.315 | 2.994 | -0.0068(18) |
| 2 | 0.645 | 2.427 | 3.110 | -0.0057(21) |
| 2 | 0.681 | 2.562 | 3.268 | -0.0051(17) |

## Reading

1. **There is a gap at both depths.** At matched P the two actions differ
   in W12 by about 3-4σ at N = 1 and about 3σ at N = 2.
2. **The decay from N = 1 to N = 2 is not established.** At comparable P,
   the gap goes from about -0.0075 to about -0.0057, a ratio of 1.3 ± 0.6.
   A dimension-6 (L^{-2}) rate predicts about 4. The data neither confirm
   nor exclude it.
3. **Where the residual sits.** Note 56 found that Wilson's curve W12(P)
   barely moves from N = 1 to N = 2: the difference is 0.000(2). The
   Symanzik curve moves by about +0.002 over the same step. So if
   universality holds, the remaining gap of about 0.006 has to close in
   later steps, through one or both curves.
4. **Possible reasons for slow decay.**
   - At β_W ≈ 2.6-3.3 the theory is not deep in the asymptotic regime.
   - Logarithmic (anomalous-dimension) corrections to the L^{-2} rate.
   - Finite-volume effects on the small 4⁴ terminal lattice, which may
     differ between actions.
   - Statistics.

   A third depth (N = 3, 32⁴) is needed for both actions.

## Consequence

This computation gives no evidence against memory decay. But unlike the 3D
test (note 59), it does not yet show it in 4D. Extending T54 (Codex) to the
Symanzik action at N = 3 would decide it. With the masked-staple code this
costs about 11 h per β at 32⁴ on one core.
