# P6-4D: nondegeneracy from superpolynomial large-field suppression

Status:

- **Proved here.**
  - Proposition 1: an exact variance comparison between the physical
    terminal law ν_N and Balaban's R-modified terminal law ν_N^R.
  - Theorem 2: uniform positive variance for the physical laws, and hence
    nondegeneracy of every subsequential limit (P6-4D). Its inputs are a
    terminal small-field variance bound (V^R) for the R-modified laws and
    an R-bias bound (B-small) that carries Balaban's large-field factor.
- **Mechanism.** Large-field effects are suppressed by
  exp(-c p(γ)²) = exp(-c(log γ^{-1})^{2p_0}) with p_0 > 1. That is
  superpolynomially small in the terminal coupling γ. Gaussian fluctuations
  of a terminal plaquette observable are polynomial in γ. So for small γ the
  R-bias cannot destroy the variance.
- **Open.** (V^R) and (B-small) are hypotheses. (B-small) is the
  quantitative form of note 27's (B-a). The order-of-magnitude statements
  marked "heuristic" are not used in the proofs.

## 1. Variance comparison (proved)

**Proposition 1.** Let ν, ν^R be probability measures on X and
B := ν - ν^R. For bounded real F,

    Var_ν(F) = Var_{ν^R}(F) + B(F²) - B(F)(ν(F) + ν^R(F)),
    Var_ν(F) >= Var_{ν^R}(F) - |B(F²)| - 2||F||_∞ |B(F)|.   (1.1)

*Proof.* Expand ν(F²) - ν(F)², with ν = ν^R + B, and use
ν(F)² - ν^R(F)² = B(F)(ν(F) + ν^R(F)). ∎

## 2. Hypotheses

Fix a terminal observable F, for example the plaquette energy
F = 1 - (1/2) tr U_p of one terminal plaquette.

- **(V^R) terminal small-field variance.** Under H0 (all couplings <= γ,
  terminal coupling g <= γ), inf_N Var_{ν_N^R}(F) >= v(γ) > 0.
  *Heuristic size:* ν^R has density
  exp(-g^{-2}A(U_K(V)) - E_K - ...) with small irrelevant corrections on S
  (CMP 119; CMP 122 II (0.1)). At small g the terminal plaquette fluctuates
  like a Gaussian with variance of order g². So F ~ g² and
  Var(F) ~ c g⁴, giving v(γ) >= c γ⁴ for g comparable to γ.
- **(B-small) R-bias with large-field factor.** For bounded G,
  sup_N |B_N(G)| <= osc(G) b(γ), with b(γ) <= C exp(-c p(γ)²).
  *Source of the factor:* every R-region at depth m carries Balaban's
  large-field factor w_m <= exp(-c p(g_m)²) with g_m <= γ, and
  Σ_m exp(-c p(g_m)²) <= C exp(-c p(γ)²/2) because p(g_m) >= p(γ) and
  p(g_m) grows. (B-small) asks that the complete R-bias series of note 27
  (B-a) inherits this factor. This is the natural form of notes 24-25 once
  (P) and generalized averaged H8 are proved with explicit large-field
  weights.

## 3. Theorem

**Theorem 2.** Assume H0, (V^R) and (B-small), with

    b(γ)(osc(F²) + 2||F||_∞ osc(F)) <= v(γ)/2.   (3.1)

Then inf_N Var_{ν_N}(F) >= v(γ)/2 > 0. Every weak subsequential limit ν of
(ν_N) has Var_ν(F) >= v(γ)/2, so P6-4D holds.

*Proof.* Combine (1.1) with (B-small) applied to G = F² and G = F. Variance
of a fixed continuous function is continuous under weak convergence on the
compact space X. ∎

**When (3.1) holds.** Under the heuristic sizes, v(γ) ~ γ⁴, while
b(γ) <= C exp(-c(log γ^{-1})^{2p_0}) with p_0 > 1 is smaller than any power
of γ. So (3.1) holds for all sufficiently small γ, which is Balaban's regime.
Taking γ small means choosing the terminal scale ε_0 small in physical units
(asymptotic freedom), which M1 permits: the terminal scale is fixed but
arbitrary.

## 4. Place in the programme

Note 27 gives M1-4D convergence from (H0) + (T) + (B). Theorem 2 adds
nondegeneracy from the **quantitative** form of (B) plus the terminal
small-field variance bound (V^R). (V^R) is a statement about Balaban's
terminal effective density alone: Gaussian dominance at small coupling,
with no multiscale comparison. Like note 17's 3D argument it rests on the
terminal representation, but it uses the local Gaussian structure rather than
global density bounds. Global constants exp(±E|T|) would lose a factor
exponential in the terminal volume and could not be compared with b(γ).
