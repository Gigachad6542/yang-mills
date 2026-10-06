# Monte Carlo: the terminal observables forget an irrelevant term in the bare action (3D)

Status: **computation** (T58). Script:
`research/scripts/t58_mc_action_universality.py` (output `.out`). Wilson
data are from note 55 (`t50_mc_terminal_convergence.out`). This is
numerical evidence for the memory-decay mechanism ((S1)-(S3) of note 29,
(D) of note 22), not a proof.

## Question

Two bare actions with the same classical continuum limit should give the
same limit of the terminal Balaban-averaged observables. The first is the
Wilson action. The second is the tree-level Symanzik action: c_0 = 5/3 on
plaquettes, c_1 = -1/12 on 1×2 rectangles, so c_0 + 8c_1 = 1. They differ
by an irrelevant (dimension-6) term. In 3D the bare scaling
β_N = β_0 L^N is exact for both, so no coupling matching is needed. The
differences at equal depth should therefore vanish as N grows. Their decay
rate measures how fast the RG forgets the irrelevant perturbation.

## Setup

- SU(2), d = 3, L = 2, n_0 = 4, β_0 = 4, depths N = 0..3 (fine lattices up
  to 32³).
- Each configuration is mapped N times through Balaban's average to the
  terminal 4³ lattice.
- Symanzik runs: heat bath plus over-relaxation with rectangle staples,
  using an 8-colour update ordering. Checks:
  - the Wilson limit agrees with t51 to 1e-15;
  - the exact staple counts are 4 (plaquette) and 6 (rectangle);
  - colour classes are independent.
- Symanzik statistics: 150 thermalization updates and 200 measurements,
  one every 2 updates. The Wilson runs (note 55) used 200 and 400.

## Results

| N | P (Wilson) | P (Symanzik) | ΔP | W12 (Wilson) | W12 (Symanzik) | ΔW12 |
|---|---|---|---|---|---|---|
| 0 | 0.7292 | 0.8119 | 0.0826(16) | 0.5497 | 0.6642 | 0.1146(33) |
| 1 | 0.8183 | 0.8532 | 0.0350(10) | 0.6564 | 0.7121 | 0.0556(21) |
| 2 | 0.8504 | 0.8648 | 0.0144(13) | 0.7057 | 0.7271 | 0.0214(34) |
| 3 | 0.8627 | 0.8718 | 0.0091(14) | 0.7251 | 0.7419 | 0.0167(37) |

The successive ratios are:

- ΔP: 2.36, 2.43, 1.6 ± 0.3;
- ΔW12: 2.06, 2.60, 1.3 ± 0.4.

## What this shows

1. **The difference between the actions is forgotten.** It shrinks by a
   factor of about 9 in P and 7 in W12 over three steps. Through N = 2 the
   per-step ratio is about 2.4, close to L = 2. That is σ ≈ 1, the O(g²ε_N)
   rate of a superrenormalizable theory. The dimension-6 term itself would
   give L² = 4, but in the terminal observables it mixes with the
   O(g² a) corrections it induces. At N = 3 the ratio, 1.6 ± 0.3 (P) and
   1.3 ± 0.4 (W12), is within 1-2σ of 2. The statistics there are thin.
2. **Same limit.** The Symanzik sequence converges faster. Its N = 3 value
   P = 0.8718(12) already matches the extrapolated Wilson limit
   0.8727 (note 55). Two-parameter extrapolations of the three Symanzik
   points give 0.876-0.880 for P and 0.749-0.762 for W12, against 0.873 and
   0.740 for Wilson. The extrapolation uncertainty is of order 0.01, which
   is larger than the gap.
3. **Relation to the theory.** (S1)-(S3) of note 29 predict that an
   irrelevant perturbation of the input data is transported with factor
   θ < 1 per step, after its O(g²) generated part is accounted for. The
   observed geometric decay of the action dependence is the nonperturbative
   counterpart.

## Limits

- Only 3D, L = 2, one coupling (β_0 = 4), and N <= 3. The N = 3 differences
  have 15-20% errors.
- In 4D the same test needs β-matching at each depth, as in note 56. With
  the present numpy code it costs about 35 s per sweep at 16⁴, so it was not
  run.
