# Exact 2D SU(2) check of the sup-oscillation depth comparison

Status:

- **Computation, exact up to series truncation.** For 2D SU(2) Wilson
  lattice gauge theory with exact holonomy blocking, the adjacent-depth
  terminal log-densities satisfy sup_θ |log f_{N+1} - log f_N| ~ C L^{-2N}.
  The ratios tend to L² for L = 2, 3 and heat-kernel times 1/b with
  b = 2, 4, 8.
- **Proof sketch.** Uniform Bessel-ratio asymptotics. It is not upgraded to
  "proved".

Purpose: the 3D and 4D Gaussian checks (notes 18 §8, 19) could not test the
**sup-oscillation** form of the depth comparison (H3D-1 in note 18, (2.1) in
note 27), because Gaussian log-likelihood ratios are unbounded. This exactly
solvable compact non-abelian model shows that the sup form holds, with the
dimension-6-type rate L^{-2N}, when the continuum limit is a strictly positive
heat kernel.

## 1. Model and exact terminal law

Take the plane, or a disc with free boundary, the Wilson weight
exp(β cos θ_p) per fine plaquette (cos θ = ½ tr U), and β_N = b M², with
M = L^N fine plaquettes per terminal plaquette side, so the terminal
plaquette has fixed physical area. In axial gauge the fine plaquette
holonomies are independent with this class-function law. The holonomy
around a terminal plaquette is an ordered product of conjugates of the M²
fine plaquette holonomies inside it. Its law is therefore the M²-fold
convolution:

    f_M(θ) = Σ_{n>=0} (n+1) c_n(β_M)^{M²} χ_n(θ),   c_n(β) = I_{n+1}(β)/I_1(β),
    χ_n(θ) = sin((n+1)θ)/sin θ.

Distinct terminal plaquettes are independent, so the full terminal law is a
product. Its log-density oscillation is at most (number of terminal
plaquettes) × sup_θ |Δ log f|. This blocking is holonomy decimation, not
Balaban's average; in 2D that is the exactly solvable choice.

## 2. Rate (proof sketch)

1. *Bessel ratio.* Uniformly in n <= β^{1/3},
   log(I_{n+1}(β)/I_1(β)) = -n(n+2)/(2β) + O((n+1)⁴/β²).
   This is the Debye large-argument expansion
   log I_ν(β) = β - ½ log 2πβ - (4ν² - 1)/(8β) + O(ν⁴/β²).
   For larger n the ratio is bounded by exp(-c n²/β) (monotonicity bounds
   for Bessel ratios), so those terms are super-exponentially small after
   the power M².
2. *Coefficients.* Hence c_n(β_M)^{M²} = e^{-n(n+2)/(2b)}(1 + O((n+1)⁴/(b² M²))).
3. *Positive limit.* f_∞ = Σ(n+1)e^{-n(n+2)/(2b)}χ_n is the SU(2) heat kernel
   at time 1/b. It is strictly positive and smooth, with minimum m_b > 0.
4. *Error.* |f_M - f_∞| <= (C/(b²M²)) Σ (n+1)⁶ e^{-n(n+2)/(2b)} = O(M^{-2}),
   uniformly in θ, using |χ_n| <= n+1.
5. *Conclusion.* sup |log f_M - log f_∞| <= C M^{-2}/m_b, so the adjacent
   difference is O(L^{-2N}).

## 3. Numbers

`research/scripts/t22_su2_2d.py` (double precision, b = 2):

| L | N=2 | N=3 | N=4 | N=5 | N=6 | last ratio |
|---|---|---|---|---|---|---|
| 2 | 5.60e-1 | 1.02e-1 | 2.30e-2 | 5.59e-3 | 1.39e-3 | 4.03 |
| 3 | 2.30e-1 | 2.13e-2 | 2.31e-3 | | | 9.20 |

`research/scripts/t22_su2_2d_mp.py` (60-digit precision on a 40-point
θ-grid; b = 4 and b = 8, where the density near θ = π is exponentially
small and double precision fails), L = 2:

| b | N=3 | N=4 | N=5 | ratio sequence |
|---|---|---|---|---|
| 4 | 1.40e-1 | 2.75e-2 | 6.40e-3 | 7.45, 5.09, 4.29 |
| 8 | 2.00e-1 | 3.23e-2 | 6.97e-3 | 9.64, 6.19, 4.63 |

The ratios tend to L² from above. Convergence is slower at shorter
heat-kernel time, because the corrections in step 2 are O((n+1)⁴/(b²M²)) and
the relevant n grow like √b.

## 4. What it shows and does not show

It shows that the sup-oscillation form of the depth comparison is natural
in a compact non-abelian theory: the rate is the dimension-6-type L^{-2N},
and the mechanism is a strictly positive continuum density.

It does not involve averaging blocks, a coupling flow (2D is
superrenormalizable: β ∝ M²), large-field regions, or an R-operation. It
calibrates the hypothesis forms; it is not evidence on the 4D estimates.
