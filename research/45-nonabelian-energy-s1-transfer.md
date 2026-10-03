# Non-abelian transfer of note 44 (energy-norm transport) from Balaban's bounds

Status: **derivation from published bounds** (T39). The structure is proved
here. One input, (NA), is obtained from CMP 99 by Cauchy estimates and
Schur's test, but its constants C(L) are not tracked.

## Statement

SU(2), small-field event E_0 (all coarse plaquettes <= ε_0), coarse data at
level m (M = L^m). Write the minimal configuration in the Landau gauge at
the flat background as exp(iηℋ(B)) (CMP 102b Prop. 9; note 36 §2).

**Proposition 1.** Assume (NA) below. Then for B in the small-field domain,

    ||∇ℋ(B)||_2 <= (C_ab + C_1(L) ε_0) M^{-1} ||ℋ(B)||_2,

where C_ab <= 60 is the abelian constant of note 44 (about 4 sharp). For
ε_0 <= 1/C_1(L), image first differences therefore contract by
(C_ab + 1)/L per step, uniformly in the depth, in the energy norm. Second
differences contract by (C_3 + 1) L^{-3/2} in the same way, using note 44
Theorem 3.

**(NA) Background perturbation in the energy norm.** For every background
U on E_0 with plaquettes <= ε_0, the linearized minimizer map H(U) (the
derivative of ℋ at U, CMP 102b (182)) satisfies

    ||∇(H(U) - H_0) B||_2 <= C_1(L) ε_0 M^{-1} ||H_0 B||_2,
    ||(H(U) - H_0) B||_2 <= C_1(L) ε_0 ||H_0 B||_2.

## Proof of Proposition 1 from (NA) and note 44

1. *Mean value.* ℋ(0) = 0 and Dℋ(tB) = H(U_t), where U_t is the
   background at tB. So ℋ(B) = ∫_0^1 H(U_t) B dt = H_0 B + ∫_0^1 (H(U_t) - H_0) B dt.
2. *Abelian part.* At the flat background, H_0 is the abelian minimizer
   map tensored with the identity on su(2) (note 36 §2). By note 44
   Theorem 1, componentwise, ||∇H_0 B|| <= C_ab M^{-1} ||H_0 B||.
3. *Remainder.* By (NA), uniformly in t ∈ [0, 1],
   ||∇∫(H(U_t) - H_0)B dt|| <= C_1 ε_0 M^{-1} ||H_0 B||.
4. *Norms.* By the second half of (NA),
   ||ℋ(B)|| >= (1 - C_1 ε_0) ||H_0 B||.
5. Combine, and absorb (1 - C_1ε_0)^{-1} into the constants. ∎

## Where (NA) comes from

- *Analyticity in the background.* CMP 99 Theorem 3.4: G(U'U) and the
  related operators extend analytically to configurations U'U with
  U' = e^{iηA'}, A' in the small set (3.37), and satisfy all the bounds of
  Theorems 3.1-3.3, which include the derivative bounds (3.42)-(3.47).
  CMP 102b Prop. 9 and (182)-(190) express H(U) and δℋ/δB through these
  operators, with "regularity and decay properties identical to the
  propagator H".
- *Cauchy.* The map A' ↦ H(e^{iηA'}) is analytic on a ball of size α_1 in
  Balaban's norm. The background at hand has size ε_0 in that norm. Cauchy's
  estimate gives ||H(U) - H_0|| <= (ε_0/α_1) sup_{ball} ||H||, in any norm in
  which the supremum is bounded.
- *Schur.* Balaban's bounds are pointwise kernel bounds with exponential
  decay on the coarse scale, for H and for ∇H, with the factor (L^kη)^{-1}
  for each derivative. By Schur's test (row and column ℓ¹ sums of the
  kernel), they give ℓ²-operator bounds with the same scale factors. Since
  H_0 is coercive in energy (note 36 §3, c_1 ≈ 0.6), ||B|| <= C||H_0 B||, and
  this converts the bounds into the relative form stated in (NA).

**What is not tracked.** C_1(L) contains Balaban's constants B_0(L),
B_3(L), which depend on L in an unspecified way. Proposition 1 therefore
needs ε_0 <= 1/C_1(L), a smallness condition on the field domain. It is
compatible with Balaban's scheme (L fixed, then ε_0 and γ small). The
contraction rate itself is the sharp abelian one, (C_ab + 1)/L. This is
better than any sup-norm constant, because the L-dependent constants enter
only multiplied by ε_0.

## Consequence

The transport part of (S1), in the energy norm, holds for SU(2) on the
small-field event, given (NA). (NA) is a Cauchy-plus-Schur consequence of
CMP 99 Theorem 3.4 and CMP 102b Prop. 9. What remains for (S1) as a whole:

- the generated terms, which are (S2) (note 42, via (A_s));
- the large-field regions, handled by the R-operation and (P) (note 39);
- writing Balaban's polymer activities in the energy norm. This is the
  mixed-norm framework proposed in notes 43-44. Analytic remainders stay in
  sup norms; transport and contraction are measured in energy.
