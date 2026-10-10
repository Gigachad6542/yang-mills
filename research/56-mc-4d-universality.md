# Monte Carlo test in 4D: universality of Balaban-averaged terminal observables

Status: **computation** (T51). Scripts:

- `research/scripts/t51_mc_universality_4d.py` (output `t51_universality.out`);
- `research/scripts/t51_matching.py` (output `t51_matching.out`).
- T54 (third depth N = 3 and the 2×2 loop, section "Third depth" below):
  `research/scripts/t54_mc_checkpointed.py` (outputs `t54_n{N}_b{β}.out`),
  `research/scripts/t54_matching.py` (output `t54_matching.out`).

This is numerical evidence for the 4D coupling flow (H0) and for M1-4D. It
is not a proof.

## Question

In 4D the bare coupling must be tuned with the depth (asymptotic freedom).
M1-4D with (H0) claims that a coupling β_N exists such that the terminal
law of the N-fold averaged field converges. A testable consequence is
universality: if β_N is fixed at each depth by holding one terminal
observable fixed, every other terminal observable must converge too. The
step β_N - β_{N-1} must also approach the one-loop value
8 b_0 log 2 = 0.2575 (SU(2), β = 4/g², L = 2).

## Setup

- Model: SU(2), Wilson action, d = 4, on the lattice (Z/(4·2^N))^4 for
  N = 0, 1, 2 (4⁴, 8⁴, 16⁴).
- Sampling: heat bath plus over-relaxation, 150 thermalization updates and
  200 measurements, one every 2 updates.
- Terminal map: N applications of Balaban's average (CMP 98 (42), corner
  blocks) to the terminal lattice 4⁴.
- Observables: the averaged plaquette P and the 1×2 loop W12.
- Checks: the d-dimensional code reproduces the 3D average of t50 exactly,
  and gauge covariance holds in 4D to 3e-15.
- Matching: P(β) and W12(β) are interpolated quadratically in β at each N.
  Errors come from 2000 Gaussian resamplings.

## Results

Raw data:

| N | lattice | β | P | W12 |
|---|---|---|---|---|
| 0 | 4⁴ | 2.4 / 2.5 / 2.6 | 0.6335 / 0.6545 / 0.6720 | 0.4333 / 0.4618 / 0.4863 |
| 1 | 8⁴ | 2.6 / 2.7 / 2.8 / 2.9 | 0.5782 / 0.6125 / 0.6418 / 0.6647 | 0.3527 / 0.3934 / 0.4303 / 0.4591 |
| 2 | 16⁴ | 2.85 / 3.0 / 3.15 / 3.3 | 0.5502 / 0.6106 / 0.6553 / 0.6865 | 0.3240 / 0.3919 / 0.4463 / 0.4854 |

At fixed terminal plaquette P:

| P | β_0 | β_1 | β_2 | W12(N=1) - W12(N=0) | W12(N=2) - W12(N=1) | β_1 - β_0 | β_2 - β_1 |
|---|---|---|---|---|---|---|---|
| 0.62 | — | 2.723 | 3.029 | — | +0.0007(19) | — | 0.305(3) |
| 0.64 | 2.429 | 2.794 | 3.093 | -0.0144(24) | -0.0005(19) | 0.365(5) | 0.299(3) |
| 0.66 | 2.529 | 2.877 | 3.168 | -0.0163(19) | -0.0017(17) | 0.348(5) | 0.290(4) |

## What this shows

1. **Universality emerges with depth.**
   - N = 0 (no averaging) and N = 1 disagree by 6-8σ in W12 at equal P.
   - N = 1 and N = 2 agree within errors at all three matching points.

   The differences fell by at least a factor of 8: from about 0.015 to at
   most 0.002, consistent with zero. One matching condition (P) therefore
   fixes the other terminal observable, as M1-4D with (H0) predicts.
2. **The coupling step approaches asymptotic freedom.** At fixed P, the step
   β_N - β_{N-1} falls from 0.35-0.37 (N: 0 -> 1) to 0.29-0.31 (1 -> 2). It
   also decreases as β grows at fixed N (0.305, 0.299, 0.290). Both trends
   point toward the one-loop value 0.2575. The remainder is of the size
   expected from higher-order and scheme terms at β ≈ 3. This is the
   numerical counterpart of (S) and (C) (notes 47-50): a finite universal
   step 2b_0 log L plus corrections that decay with depth.
3. **Agreement with the 3D picture** (note 55). The terminal fields defined
   by Balaban's iterated average have well-defined limits. In 4D this holds
   once the coupling flow is matched.

## Third depth (N = 3, 32⁴) and the 2×2 loop (T54)

The same Monte Carlo (checkpointed driver `t54_mc_checkpointed.py`, same
update scheme, 150 + 400 updates, 200 measurements) was run again at every
depth with fresh seeds, adding the terminal 2×2 loop W22, and at the new
depth N = 3 on 32⁴ (β = 3.30, 3.40, 3.50; about 4.2 h each). Raw data
(`t54_n*.out`):

| N | lattice | β | P | W12 | W22 |
|---|---|---|---|---|---|
| 0 | 4⁴ | 2.4 / 2.5 / 2.6 | 0.6367 / 0.6567 / 0.6714 | 0.4378 / 0.4648 / 0.4858 | 0.2436 / 0.2735 / 0.2974 |
| 1 | 8⁴ | 2.6 / 2.7 / 2.8 / 2.9 | 0.5795 / 0.6126 / 0.6424 / 0.6654 | 0.3540 / 0.3937 / 0.4307 / 0.4600 | 0.1722 / 0.2073 / 0.2424 / 0.2718 |
| 2 | 16⁴ | 2.85 / 3.0 / 3.15 / 3.3 | 0.5541 / 0.6105 / 0.6540 / 0.6872 | 0.3277 / 0.3923 / 0.4449 / 0.4869 | 0.1555 / 0.2107 / 0.2612 / 0.3025 |
| 3 | 32⁴ | 3.3 / 3.4 / 3.5 | 0.6152 / 0.6418 / 0.6704 | 0.3995 / 0.4286 / 0.4665 | 0.2219 / 0.2438 / 0.2857 |

Errors on P are 0.0006-0.0014, on W12 0.0008-0.0020, on W22 0.0012-0.0028.
The N = 0, 1, 2 points agree with note 56's first runs within errors.

At fixed terminal plaquette P (`t54_matching.out`; differences between
consecutive depths, value(error)):

| P | N | β step β_N - β_{N-1} | W12(N) - W12(N-1) | W22(N) - W22(N-1) |
|---|---|---|---|---|
| 0.64 | 0 → 1 | 0.378(5) | -0.0146(22) | -0.0092(30) |
| 0.66 | 0 → 1 | 0.355(6) | -0.0165(19) | -0.0141(23) |
| 0.62 | 1 → 2 | 0.308(3) | +0.0009(18) | +0.0060(24) |
| 0.64 | 1 → 2 | 0.304(3) | +0.0000(19) | +0.0046(24) |
| 0.66 | 1 → 2 | 0.298(4) | -0.0009(18) | +0.0027(23) |
| 0.62 | 2 → 3 | 0.288(5) | +0.0006(24) | +0.0026(28) |
| 0.64 | 2 → 3 | 0.297(5) | -0.0011(25) | -0.0021(31) |
| 0.66 | 2 → 3 | 0.292(4) | -0.0000(22) | +0.0013(28) |

Matched couplings at P = 0.64: β_0 = 2.415(4), β_1 = 2.793(2),
β_2 = 3.097(3), β_3 = 3.394(4) (the extrapolated guess was 3.37-3.40).

What this adds:

1. **The third depth confirms universality for W12.** The 2 → 3
   differences are zero within 0.0025 at all three matching points, the same
   as 1 → 2, after the 7-9σ disagreement between N = 0 and N = 1.
2. **The 2×2 loop converges as well.** W22 shows the same pattern: 3-6σ
   apart between N = 0 and N = 1, 1.2-2.5σ at 1 → 2 (all positive,
   +0.003 to +0.006), and within 1σ at 2 → 3. The 1 → 2 residual is larger
   for the larger loop, as expected for a finite-depth correction that
   decays with N; with these errors it is not significant at 2 → 3.
3. **The β step keeps decreasing toward the one-loop value.** At fixed P,
   0.36-0.38 (0 → 1), 0.30-0.31 (1 → 2), 0.29-0.30 (2 → 3), against
   8 b_0 log 2 = 0.2575. The decrease from 1 → 2 to 2 → 3 is 0.020, 0.007,
   0.006 at P = 0.62, 0.64, 0.66 (3.4σ, 1.2σ, 1.1σ), in the direction
   predicted by asymptotic freedom (the two-loop correction to the step is
   positive and of order g², so it shrinks as β grows). The
   remaining gap of about 0.035 is of the size of the higher-order and
   scheme terms at β ≈ 3.3.

Status: **computation**. This is evidence for (H0) and M1-4D at three
refinements, not a proof.

## Limits

- Three refinements at most (N <= 3, up to 32⁴; N = 3 has only three β
  values, so its quadratic interpolation is exact through the data). The
  statistics are modest: 200 measurements per point.
- The terminal 4⁴ lattice is small, and the β values are in the
  crossover/scaling window (β ≈ 2.4-3.3). The test does not reach the deep
  asymptotic regime.
- Only L = 2. Only the plaquette, the 1×2 loop and (T54) the 2×2 loop are compared.
