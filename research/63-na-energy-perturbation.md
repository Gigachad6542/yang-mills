# (NA♭) in the energy norm without CMP 102b (190): a constrained-minimizer perturbation lemma

Status:

- **Proved here.** Lemma 1, an abstract perturbation lemma for
  constrained quadratic minimization: the minimizers move by O(δ) in the
  energy norm when the forms and the constraints move by δ.
- **Conditional on published input only** (CMP 102b (173); §3a). Proposition 2 gives (NA♭) of note 54 in the
  energy-norm form used by note 45 Proposition 1. It needs:
  - (I1) uniform coercivity of the flat-background problem;
  - (I2) a sup bound Cω/M on the fine background deviation;
  - (I3) smallness of the Lagrange-multiplier term.

  It does **not** use the pointwise decay bound CMP 102b (190), whose proof
  Balaban omits (note 54 §4). Nor does it use Schur's test.
- **Effect.** The step of the 3D chain that rested on a proof omitted in
  the source now rests on (I1)-(I3). (I1) is an elementary flat-lattice
  estimate. (I2) is CMP 102b Prop. 9's bounds (19)-(21), or Thm 1.

## 1. Lemma 1 (perturbation of constrained minimizers)

Let X and Y be Hilbert spaces, with the norm on X denoted N. Let a_0 and
a_1 be bounded symmetric bilinear forms on X, and Q_0, Q_1 : X -> Y bounded
linear maps. Assume:

- (i) Q_0 has a right inverse R_0 with N(R_0 y) <= ρ ||y||_Y;
- (ii) |a_0(u, v)| <= C_a N(u)N(v), and a_0(w, w) >= c N(w)² for
  w ∈ ker Q_0;
- (iii) |(a_1 - a_0)(u, v)| <= δ N(u)N(v), and ||(Q_1 - Q_0)u||_Y <= δ N(u).

Put h_i(y) := argmin{a_i(u, u) : Q_i u = y}. Then there are δ_0 > 0 and
K < ∞, depending only on (ρ, C_a, c), such that for δ <= δ_0,

    N(h_1(y) - h_0(y)) <= K δ N(h_0(y))   for all y ∈ Y.

*Proof.*

1. *Right inverse of Q_1.* Put E := (Q_1 - Q_0)R_0. Then ||E|| <= ρδ <= ½,
   and R_1 := R_0 (I + E)^{-1} satisfies Q_1 R_1 = I and N(R_1 y) <= 2ρ||y||.
2. *Kernels.* Define P w := w - R_1 Q_1 w for w ∈ ker Q_0. Then P maps
   ker Q_0 into ker Q_1, and N(Pw - w) <= 2ρδ N(w).
   - *P is onto.* Given z ∈ ker Q_1, put w := z - R_0 Q_0 z ∈ ker Q_0. Then
     P w = z - R_0 Q_0 z + R_1 Q_1 R_0 Q_0 z = z, using Q_1 z = 0 and
     Q_1 R_0 = I + E.
3. *Coercivity on ker Q_1.* For z = P w,

       a_1(z, z) >= a_0(w, w) - |a_0(z - w, z + w)| - δ N(z)²
                 >= [c - 2ρδ C_a (2 + 2ρδ) - δ(1 + 2ρδ)²] N(w)²
                 >= (c/2) N(w)² >= (c/4) N(z)²

   for small δ, since N(z) <= (1 + 2ρδ) N(w).
4. *The difference.* Let u_i := h_i(y) and d := u_1 - u_0. Then
   Q_1 d = (Q_0 - Q_1) u_0 =: e, with ||e|| <= δ N(u_0). Write
   d = R_1 e + z with z ∈ ker Q_1.
   - Optimality of u_1 gives a_1(u_1, z') = 0 for all z' ∈ ker Q_1. With
     z' = z this reads a_1(z, z) = -a_1(u_0, z) - a_1(R_1 e, z).
   - Write z = P w. Optimality of u_0 gives a_0(u_0, w) = 0, so
     |a_0(u_0, z)| = |a_0(u_0, z - w)| <= 2ρδ C_a N(u_0) N(w).
   - Also |(a_1 - a_0)(u_0, z)| <= δ N(u_0) N(z), and
     |a_1(R_1 e, z)| <= (C_a + δ) 2ρδ N(u_0) N(z).

   By step 3, (c/4) N(z)² <= C' δ N(u_0) N(z). So
   N(d) <= N(R_1 e) + N(z) <= (2ρ + 4C'/c) δ N(u_0). ∎

## 2. The setting of (NA♭)

- X: the fine fluctuation fields (su(2)-valued 1-forms on the fine torus).
  The norm is

      N(A)² := ||D_♭ A||² + M^{-2} ||A||²,

  where D_♭ is the covariant difference at the flat background U♭ (note 54
  §2 normal form).
- a_U: the second variation of the Wilson action at the background U,
  plus the Lagrange-multiplier term, as below.
- Q_U: the linearized covariant average at U, together with the gauge
  condition (Landau relative to U). Y has the quotient norm
  ||y||_Y := inf{N(u) : Q_♭ u = y}, so (i) holds with ρ = 1 + η for any
  η > 0.
- H(U)B = h_U(B), the derivative of the minimizer map (CMP 102b (182)). By
  the Euler-Lagrange equations, the linearization of a constrained
  minimizer is the minimizer of the Hessian of the Lagrangian on the
  linearized constraint set.

**Inputs.**

- **(I1) Flat coercivity, uniform in M.**
  - |a_♭(u, v)| <= C_a N(u)N(v), and a_♭(w, w) >= c N(w)² on ker Q_♭.
  - Ingredients: the exact lattice identity
    ||D_♭A||² = ||d_♭A||² + ||d_♭*A||² at a flat background (Fourier in each
    twisted sector, note 54 §2); the gauge condition d_♭*A = 0; and a block
    Poincaré inequality M^{-2}||A||² <= C_P ||D_♭A||² on fields with zero
    block averages.
  - In the untwisted sector the constant fields are excluded by the
    averaging constraint. In twisted sectors there are no zero modes.
  - The bound ||H(U♭) y|| <= C M^{d/2} |y|, used in Proposition 2 step 2,
    is part of (I1): the minimal extension is no larger than the
    block-constant extension, up to a constant, by coercivity.
  - All constants are scale invariant, hence uniform in M.
  - Proved in Lemma 3 (§2a).
- **(I2) Fine background deviation.** In the global gauge of note 57, the
  fine background U = U_k(V) satisfies U = e^{ia'} U♭ with
  |a'|_∞ <= C ω/M in fine units, where ω = dist(V, Flat) <= d n_0 √ε_0.
  Source: CMP 102b Prop. 9, conditions (19)-(21), which bound ℋ(B) in
  scaled sup norms; or Thm 1 for minimal configurations.
- **(I3) Multiplier term.** At a constrained minimizer, the Hessian of the
  Lagrangian contains λ · D²Q_U. Here λ is the multiplier, of the size of
  the background current, O(ε_0) in scaled units. So this term is a bounded
  form of size O(ε_0) relative to N.

## 2a. Lemma 3 ((I1), flat coercivity)

At a flat background U♭ (note 54 normal form), on the fine torus with
composite block size M:

- (a) ||D_♭A||² = ||d_♭A||² + ||d_♭*A||² exactly, where
  ||D_♭A||² = Σ_{x,μ,ν} |∇_{♭,μ} A_ν(x)|².
- (b) If Q_♭ A = 0 (Balaban's composite linear average at U♭), then
  M^{-2} ||A||² <= C_P ||D_♭ A||², with C_P independent of M.
- (c) There is a right inverse R of Q_♭ with N(R y) <= C M^{d/2-1} |y|_{ℓ²}
  and ||R y|| <= C M^{d/2} |y|.
- (d) On {Q_♭ A = 0, d_♭*A = 0}, a_♭(A, A) = ||d_♭A||² >= c N(A)², with
  c = 1/(1 + C_P). Moreover, N(H(U♭) y) <= C M^{d/2-1}|y| and
  ||H(U♭) y|| <= C M^{d/2}|y|.

*Proof.*

1. *(a).* In the normal form the problem splits into a neutral sector and
   twisted charged sectors (note 54 §2). In each sector, after Fourier
   transform, the forward differences are multiplication by complex
   numbers r_μ(p), and they commute. Also (dA)_{μν} = r_μ Â_ν - r_ν Â_μ and
   d*A = Σ_μ r̄_μ Â_μ. The complex Lagrange identity
   (Σ_μ|r_μ|²)(Σ_ν|Â_ν|²) = Σ_{μ<ν}|r_μÂ_ν - r_νÂ_μ|² + |Σ_μ r̄_μÂ_μ|²
   gives (a) mode by mode.
2. *(b).* Let P_0 be the projection onto fields that are covariantly
   constant on each M-block. On a block, the flat background is pure
   gauge. So the standard lattice Poincaré inequality on a cube of side M
   gives ||A - P_0A|| <= C M ||D_♭A||.
   - Q_♭ restricted to block-constant fields is a coarse operator whose
     symbol is bounded below. This is the alias-0 positivity of note 47
     §3 / note 44 step 4. So ||P_0A|| <= C M^{d/2} |Q_♭ P_0 A|.
   - If Q_♭A = 0, then |Q_♭P_0A| = |Q_♭(P_0A - A)| <= C M^{-d/2} ||A - P_0A||.
   - Hence ||A|| <= C M ||D_♭A||.
3. *(c).* Let S be the smooth extension: S y is the block-constant
   extension of y, mollified at scale M. Then ||D_♭ S y|| <= C M^{d/2-1}|y|
   and ||S y|| <= C M^{d/2}|y|. The coarse operator Q_♭S has a symbol
   bounded below, by the same alias-0 argument, so it is invertible with
   a bounded inverse. Put R := S (Q_♭ S)^{-1}.
4. *(d).* By (a), on {d_♭*A = 0}, ||D_♭A||² = ||d_♭A||². With (b),
   N(A)² <= (1 + C_P) ||d_♭A||². For H(U♭)y:
   - a_♭(H y) <= a_♭(R y) <= N(R y)² <= C M^{d-2}|y|², since H y minimizes;
   - H y - R y ∈ ker Q_♭, so by (b),
     ||H y|| <= ||R y|| + C M (||D_♭ H y|| + ||D_♭ R y||) <= C M^{d/2}|y|.

   Here R y is first projected onto the gauge slice, which changes it only
   by a gradient and does not increase ||D_♭ ·||. ∎

So (I1) is proved, up to the standard Poincaré inequality on cubes and the
alias-0 positivity already proved in notes 44 and 47. Proposition 2 then
rests on (I2) and (I3) only.

## 3. Proposition 2 ((NA♭), energy form)

Under (I1)-(I3), for ω and ε_0 small enough,

    N((H(U) - H(U♭)) B) <= K (ω + ε_0) N(H(U♭) B).

Consequently, with Theorem 2 of note 54 (transport at flat backgrounds),

    ||∇_{U♭}(H(U) - H(U♭)) B|| <= K (ω + ε_0)(C_ab + C) M^{-1} ||H(U♭) B||,
    ||(H(U) - H(U♭)) B|| <= K (ω + ε_0)(C_ab + C) ||H(U♭) B||,

which is (NA♭) with C_1(L) ω(ε_0) replaced by K(C_ab + C)(ω + ε_0).

*Proof.* Check (iii) of Lemma 1 with δ = C(ω + ε_0).

1. *Forms.* a_U - a_♭ consists of:
   - terms ⟨D_♭A, [a', A']⟩ with |a'|_∞ <= Cω/M, bounded by
     C(ω/M) ||D_♭A|| ||A'|| <= Cω N(A) N(A');
   - terms ⟨[a', A], [a', A']⟩, bounded by (Cω/M)² ||A|| ||A'|| <= Cω² N N;
   - the background-curvature term ⟨F_U, [A, A']⟩ of the second variation,
     with |F_U| <= Cω/M² (fine units, from (I2)), bounded by
     (Cω/M²) ||A|| ||A'|| <= Cω N(A) N(A'); [Audit 2026-10-09, T82.]
   - the (I3) term, O(ε_0) N N.
2. *Constraints.* The linearized averages differ by parallel transport
   along contours of length <= CM, so by at most CM · Cω/M = Cω per
   contour. Hence |(Q_U - Q_♭) A|(c) <= Cω M^{-d} Σ_{block} |A|. To bound
   the quotient norm, use the preimage H(U♭) y. By Theorem 2 of note 54 and
   the scaling ||H(U♭) y|| ~ M^{d/2} |y|, this gives
   N(H(U♭) y) <= C M^{d/2 - 1} |y|_{ℓ²}. So
   ||(Q_U - Q_♭) A||_Y <= C M^{d/2-1} · Cω M^{-d/2} ||A|| <= Cω N(A).
   The gauge conditions differ in the same way.
3. *Conclusion.* Lemma 1 gives the first display. The consequences follow:
   - ||∇_{U♭} u|| <= N(u) and ||u|| <= M N(u);
   - N(H(U♭)B) <= (C_ab + C) M^{-1} ||H(U♭) B||, by note 54 Theorem 2 (the
     potential version) and the definition of N. ∎

## 3a. Source status of (I2) and (I3)

- **(I2)** is CMP 102b (173), printed p. 305 (OCR line 862). The minimizer
  ℋ(B) relative to the background V_0 satisfies the regularity conditions
  (19)-(21) with ε_2 = B_5 ε_1, where B_5 is an absolute constant depending
  on d and L. (19) is a sup bound on ℋ and its differences in scaled units,
  |A| < ε_2 (L^jη)^{-1}. In the fully small-field region this makes the
  fine-link deviation from the background O(ε_2/M) in fine units.
  - Here V_0 = V♭ is flat with arbitrary holonomy, which is allowed by
    Prop. 9 (orbits V'V_0), and ε_1 ~ ω = dist(V, Flat) (note 57).
  - Unlike (190), the bound (173) is derived in the text, from Sects. C and
    F of the same paper.
- **(I3)** At the flat background the minimizer is unconstrained, and its
  multiplier vanishes. The multiplier is a linear function of the
  minimizer's Euler-Lagrange residual. That residual is analytic in B,
  with the same scaled sup bounds. So |λ| = O(ε_2) = O(ω) in scaled units,
  and the term λ·D²Q is O(ω) relative to N.

So (NA♭), in the energy form of Proposition 2, rests on:
- Lemma 1 and Lemma 3 (proved here);
- note 54 Theorem 2 and note 57 (proved);
- CMP 102b (173) (published, derived in the source).

## 4. Effect on the 3D chain

(H1) of note 61 now rests on:

- note 54 Theorem 2 (proved);
- note 57 (proved, Codex);
- Proposition 2 here, given (I1)-(I3).

It no longer rests on CMP 102b (190) or on Schur's test. The remaining
inputs are the elementary flat estimate (I1), CMP 102b's sup bounds (I2),
and (I3). Note 54's caveat n_0 > O(1)M concerned CMP 99's local
regularity cubes, and it is no longer needed for this route.
