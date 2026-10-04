# Monte Carlo test in 4D: universality of Balaban-averaged terminal observables

Status: **computation** (T51). Scripts:

- `research/scripts/t51_mc_universality_4d.py` (output `t51_universality.out`);
- `research/scripts/t51_matching.py` (output `t51_matching.out`).

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

## Limits

- Only two refinements (N <= 2, up to 16⁴). The statistics are modest: 200
  measurements per point.
- The terminal 4⁴ lattice is small, and the β values are in the
  crossover/scaling window (β ≈ 2.4-3.3). The test does not reach the deep
  asymptotic regime.
- Only L = 2. Only the plaquette and the 1×2 loop are compared.
