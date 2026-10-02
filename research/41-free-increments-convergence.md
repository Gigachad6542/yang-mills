# (C) of note 22: geometric convergence of the free increments from operator convergence

Status:

- **Proved here.** Proposition 1: a perturbation lemma. If the free step
  operators and their background vertices converge geometrically in an
  exponentially weighted operator norm, and the step propagators are
  uniformly bounded in that norm, then the free increments β_j^0 converge
  geometrically. This is (C) of note 22.
- **Inputs.**
  - (O1) uniform weighted propagator bounds. These are published for the
    trivial background: CMP 95/96 and CMP 99 Theorem 3.3 at U = 1.
  - (O2) geometric convergence of the rescaled free step operators. For the
    composite linear average this is the exact box formula of note 19 (2.1),
    a Riemann sum with error O(L^{-j}). For the Laplacian and gauge-fixing
    parts it is lattice discretization at spacing L^{-j}. (O2) is checked
    here only for the averaging kernels and the weights a_j.
- **Effect.** H0 ⇐ (D) + (S) + (O2) + published inputs (note 22 Prop. D).
  The one remaining free-field input of H0 besides (S) is now an explicit
  convergence statement about Balaban's free operators.

## 1. Setting

At step j, after rescaling the coarse lattice to unit spacing, the free
(U = 1) fluctuation integral has a quadratic form K_j. It includes:

- the gauge-fixed lattice Laplacian on the finest lattice, which has spacing
  L^{-j} in these units;
- the averaging penalty Σ_{i<=j} a_i (L^{i-j})^{d-2} |Q_i A|² (CMP 99 (3.16));
- the ghost part.

Let V_j' and V_j'' be its first and second background derivatives. These are
local operators composed with the averaging maps. The free vacuum
polarization is the background Hessian of ½ log det K_j(U) at U = 1:

    Π_j = ½ Tr(G_j V_j'') - ½ Tr(G_j V_j' G_j V_j'),   G_j = K_j^{-1}.

Here the traces are per unit volume, with block-periodic kernels averaged
over block positions. Then β_j^0 = -½ ∂²_{p_μ p_ν} Π̂_j(0), μ ≠ ν
(CMP 109 (5.37)). Equivalently, β_j^0 is a fixed linear combination of
second moments Σ_y (x-y)_μ (x-y)_ν Π_j(x, y).

**Weighted norm.** For a kernel A(x, y) put

    ||A||_δ := sup_x Σ_y |A(x, y)| e^{δ|x-y|}.

It is submultiplicative, and |second moment of A| <= C_δ ||A||_δ.

## 2. Proposition 1

Assume:

- **(O1)** sup_j ||G_j||_δ <= C_G, sup_j ||V_j'||_δ, ||V_j''||_δ <= C_V;
- **(O2)** there are limits K_∞, V_∞', V_∞'' with
  ||K_j - K_∞||_δ, ||V_j' - V_∞'||_δ, ||V_j'' - V_∞''||_δ <= C_O ϑ^j, ϑ < 1.

Then G_∞ := K_∞^{-1} exists with ||G_∞||_δ <= 2C_G for large j, and

    |β_j^0 - β_∞^0| <= C ϑ^j,   C = C(C_G, C_V, C_O, δ).

*Proof.*

1. *Propagators.* By the resolvent identity,
   G_j - G_l = G_j (K_l - K_j) G_l. With (O1),
   ||G_j - G_l||_δ <= C_G² · 2C_O ϑ^{min(j,l)}. So G_j is Cauchy in ||·||_δ.
   Its limit G_∞ inverts K_∞, and ||G_j - G_∞||_δ <= 2C_G² C_O ϑ^j.
2. *Polarization kernels.* The kernels of G_j V_j'' and of G_j V_j' G_j V_j'
   are products of three or four weighted-bounded factors. A telescoping
   difference with one factor replaced at a time gives
   ||Π_j - Π_∞||_δ <= C' ϑ^j. The trace per unit volume of a block-periodic
   kernel is an average of finitely many diagonal entries, so the same
   bound holds for the kernels whose moments define β.
3. *Moments.* |β_j^0 - β_∞^0| <= C_δ ||Π_j - Π_∞||_δ <= C ϑ^j. ∎

Combined with note 22 Prop. D, this gives (U), and then (W) by Cor. C. The
limit β_∞^0 is forced to equal 2b_0 log L by (S).

## 3. What (O1) and (O2) are

**(O1)** At U = 1, Balaban's propagators have exponential decay uniformly
in the step, with the scale-dependent factors (L^jη)^{...} of CMP 99
(3.42)-(3.47) (Theorem 3.3, specialized to U = 1, which goes back to
CMP 95/96). In rescaled units these become uniform weighted bounds. The
vertices V', V'' are local in the fine lattice, composed with averaging
maps, so they are bounded in ||·||_δ.

**(O2)** has three parts.

1. *Averaging.* By note 19 (2.1), the composite linear average over M = L^j
   fine cells is the exact box formula M^{-4} Σ_{u∈[0,M)^4} Σ_{s,t}. In
   rescaled units it is a Riemann sum for the continuum box average, with
   kernel error O(1/M) = O(L^{-j}) in ||·||_δ. Each level i < j enters the
   penalty with relative weight (L^{i-j})^{d-2}, so the tail of the sum is
   O(L^{-(d-2)j'}) beyond depth j'.
2. *Weights.* a_j = a(1 - L^{-2})/(1 - L^{-2j}) converges to a(1 - L^{-2})
   at rate L^{-2j} (CMP 99, recursion before (3.26)).
3. *Laplacian, gauge fixing and ghosts* on the fine lattice with spacing
   L^{-j}: these are standard discretizations of their continuum limits.
   Acting on functions smooth at the coarse scale they converge at rate
   L^{-j}. Since G_j is smoothing at the coarse scale, the weighted
   convergence required in (O2) holds on the range that matters.

   This last point is stated, not proved. Making it precise needs two
   things:
   - a common space for the operators of different j, since the fine
     lattice changes with j; for example, piecewise-constant extension to
     the continuum, or comparison of the induced coarse-lattice kernels
     only;
   - a two-scale version of (O1): bounds on G_j(K_j - K_∞) that use the
     smoothing of G_j.

   Proposition 1 holds verbatim for the induced coarse-lattice kernels. So
   the second item is the one non-elementary step left in (O2).

So ϑ = L^{-1} is the expected rate. It is consistent with the scalar
calibration of note 23, where the window edge converges.

## 4. Status of H0 after this note

    H0 <= (B), regularity [published]
        + (D) memory decay [notes 29, 31, 40: single-step reduction; open]
        + (S) finite one-loop scheme matching [universal part published]
        + (O2) operator convergence [averaging and weights: done here;
               discretization part: two-scale (O1), stated]
        + (O1) [published].
