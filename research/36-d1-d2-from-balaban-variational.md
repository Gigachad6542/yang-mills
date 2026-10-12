# (D1) and (D2) of note 34 from Balaban's variational theory (CMP 102b, CMP 99)

Status:

- **Source reading (published input).**
  - CMP 102b Theorem 1 (existence, uniqueness and regularity of minimal
    configurations) and Proposition 9 (analyticity, linear term H, decay of
    δℋ/δB);
  - CMP 99 Theorem 3.11 (Δ_a positive definite) and (3.16) (the
    level-weighted Q*aQ form).
- **Proved here, abelian case.**
  - (D1) holds with the explicit constant c_1 = 1/(2Λ), where Λ is the
    supremum of the block-flux covariance multiplier. It is uniform in the
    level by scale invariance (§3, computation).
  - (D2) holds with the sup-norm constant s_L of note 35.
- **Derivation sketch, non-abelian (conditional reduction).**
  - (D2) on E_0 with s_L^{NA} <= s_L^{ab}(1 + Cε_0) + Cε_0, from Prop. 9 by
    linearization at the flat configuration.
  - (D1) on E_0 with c_1^{NA} >= c_1^{ab} - Cε_0, from Theorem 1 uniqueness
    and a second-variation argument.

  Two steps are sketched and not carried out: the localization of Prop. 9
  to a cube (Prop. 9 is stated for coarse fields that are small globally,
  in a fixed gauge), and the uniformity of the third-order remainder.
- **Effect.** The non-abelian (PA) on the ε_0-small event (note 34) now
  rests on published variational results plus two exact abelian constants.
  It needs s_L < 1 - η, which note 35's computed rows (lower bounds for s_L)
  suggest for L >= 4 but do not establish.

## 1. What CMP 102b provides

*Theorem 1 (CMP 102b p. 279).* Suppose a coarse configuration V satisfies
|(dV)(p') - 1| < ε_1 on every coarse plaquette, with ε_1 <= a_1. Then:

- there is a minimal orbit of the Wilson action on the fiber of fine fields
  with averages V;
- it is the unique critical orbit in the small-field space (6);
- on every cube □ of size 2M L^j η (M >= M(ε_1)) there is a gauge in which
  |A| < B_3 M ε_1 (L^jη)^{-1} and |∇_η A| < B_3 M ε_1 (L^jη)^{-2}, with
  higher-derivative bounds (9)-(10).

The constants depend on d and L only, uniformly in the number of steps k.

So the fine curvature in scale-j units is O(ε_1). This is (D2) with **some**
constant C(d, L). The theorem does not give the size of that constant. Note
35 shows it is about s_L = O(1), not O(L^{-2}): it exceeds 1 for L = 2, 3,
and the computed rows (lower bounds for s_L) are below 1 for L >= 4.

*Proposition 9 (CMP 102b p. 309).* Let V = V'V_0 with V' = e^{iB} small.
Then U_k(V'V_0) U_k(V_0)^{-1} = exp(iη ℋ(B)) in the Landau gauge. Here ℋ is
analytic in B and in the background, its expansion starts with the linear
term H_0 B (equations (179)-(180)), and δℋ/δB has the decay of the
propagator H (equation (190)). It is gauge covariant (181).

*CMP 99, Theorem 3.11 and (3.16).* Δ_a = Δ + DRD* + Q*aQ is positive
definite, with

    ⟨A, Q*aQ A⟩ = a Σ_j (L^jη)^{d-2} |Q_j(U) A|².

In d = 4 the weight (L^jη)^{d-2} makes |φ_j|² scale invariant, where
φ_j = (L^jη) Q_j A is the level-j angle.

## 2. (D2), non-abelian, from Proposition 9

Take V_0 = 1 (flat), which satisfies (7) trivially. Then V = e^{iB}, and
the minimal configuration is exp(iηℋ(B)) with ℋ(B) = H_0 B + O(|B|²).

At V_0 = 1, H_0 is the flat linear minimizer operator of CMP 95/96. It acts
componentwise on su(2) and is exactly the abelian minimizer of note 35,
tensored with the identity on su(2).

1. *Linear part.* The level-j image angle of exp(iηH_0B) is G(d'B) (note 35)
   in each su(2) component. On the exact coarse fluxes d'B the
   exact-restricted row norm bounds the Euclidean norm as well: apply the
   optimal scalar extension componentwise. So the linear part is
   <= s_L^{ab} sup |d'B|.
2. *Coarse angles.* ϑ' = |d'B| + O(|B|²).
3. *Remainder.* The O(|B|²) terms of ℋ and of the image angle are bounded
   by C|B|² <= Cε_0 sup ϑ', in a local axial gauge where |B| <= Cε_0. This
   uses Theorem 1's gauge on a cube and the gauge covariance (181).
4. *Localization (sketched).* Prop. 9 needs B small globally. Changing V
   outside a cube of size R around p changes the image angle at p by an
   amount that decays like e^{-δR}, by (190) integrated along the segment
   between the two configurations, which stays in the small-field domain on
   E_0. The weight e^{-δ dist} in (D2) absorbs this.

*Holonomy caveat (note 54).* Step 4 and the use of Prop. 9 at V_0 = 1 assume
that E_0 configurations are globally small in one gauge. On the torus this
fails for nontrivial holonomy. The replacement:

- use note 54 Lemma 3 (dist(V, Flat) <= ω(ε_0) in a suitable gauge);
- apply Prop. 9 at the flat background V_0 = V♭, which satisfies (7) with zero
  curvature;
- step 4 is then not needed.

The cost is twofold:

- ε_0 is replaced by ω(ε_0) in the remainders;
- the linear part at V♭ is the twisted abelian map on the charged
  components (note 54 §1).

Its sup-norm constant equals s_L^{ab} up to wrap-around corrections
O(e^{-δ n_0}), because unimodular phases do not change |kernel|. This was not
recomputed with the exact-flux LP of note 35.

Hence on E_0, s_L^{NA} <= s_L^{ab}(1 + Cε_0) + Cε_0, with the weighted form
of note 35. For L >= 4 the computed rows give about 0.88 including the
observed m-growth [T53: for L = 4 a larger row, 0.881 at m = 1, n0 = 6, gives
about 0.97-1.01 with the m-growth; only L >= 5 stays below 1; in twisted
sectors s_L^{ab} must be the maximum over sectors (note 35 §5)], but they are lower bounds for s_L^{ab}, so the chain
lemma's condition s_L < 1 - η for small ε_0 is suggested, not established.
[Audit 2026-10-09, T82.]

## 3. (D1), abelian: exact constant

In the Gaussian theory with action ½||F||², let Φ_j be the level-j block
fluxes. Minimizing over fine fields with given Φ_j,
S_j(W) = ½ Φ_jᵀ C_j^{-1} Φ_j, where C_j is the covariance of Φ_j. So

    S_j(W) - S_{j+1}(CW) = ½ φᵀ Cov(Φ_j | Φ_{j+1})^{-1} φ,
    φ = Φ_j - E[Φ_j | Φ_{j+1}].

This is the Gaussian chain rule for quadratic forms. Since
Cov(Φ_j | Φ_{j+1}) <= C_j as operators, and the operator norm of C_j on
ℓ²(coarse plaquettes) is Λ_j := sup_K λ_max(C^{(M)}(K)) (note 19 (2.5),
β = 1), we get

    S_j(W) - S_{j+1}(CW) >= |φ|_2² / (2Λ_j) >= |φ|_∞² / (2Λ_j).

By 4D scale invariance Λ_j converges as M = L^j grows. The computed values
are in §5.

## 4. (D1), non-abelian, from Theorem 1 (sketch)

Let W be in the fiber over V = CW, both on E_0, and let U(W), U(V) be the
minimizers. Then S_j(W) - S_{j+1}(V) = A(U(W)) - A(U(V)).

1. U(W) satisfies the constraints of the V-problem, and U(V) is the unique
   critical point there (Theorem 1).
2. In Balaban's linearizing coordinates for the averaging (CMP 102b
   Prop. 3), the fiber is a linear space {A' : Q_{j+1}A' = 0}.
3. Along this space the first variation of A at U(V) vanishes, by (178).
   The second variation is the abelian quadratic form plus O(ε_0) by
   (3.137) of CMP 99. The third-order terms are O(ε_0)|A'|².
4. Hence S_j(W) - S_{j+1}(V) >= (c_1^{ab} - Cε_0)|φ_j|². Here φ_j is the
   level-j image angle of A', and c_1^{ab} is the §3 constant applied to
   the linearized fluxes.

What is sketched here is the uniformity of the O(ε_0) terms over the
non-local fiber. Balaban's bounds hold with constants depending only on
(d, L), which is the needed uniformity, but the statement in exactly this
form is not printed.

## 5. Computation of Λ (abelian (D1))

Script: `research/scripts/t28_d1_abelian.py` (output `.out`). Coarse torus
6⁴, sup over all coarse momenta.

| L | M = L^j | Λ_j | c_1 = 1/(2Λ_j) |
|---|---|---|---|
| 2 | 2 | 0.8750 | 0.571 |
| 2 | 4 | 0.8438 | 0.593 |
| 2 | 8 | 0.8359 | 0.598 |
| 3 | 3 | 0.8519 | 0.587 |
| 3 | 9 | 0.8354 | 0.599 |
| 3 | 27 | 0.8336 | 0.600 |

The script reproduces all rows except M = 27, which comes from an earlier run of the same computation (heavy). Λ_j
decreases with M toward about 0.835, so c_1 ≈ 0.6 uniformly in the level.
The maximum sits at the smallest nonzero coarse momenta.

**Use in note 34.** In the abelian theory take φ_j to be the level-j flux
residual Φ_j - E[Φ_j | Φ_{j+1}] itself. Then Lemma 1 holds with C_F = 1
(the angle is the flux), and (D1) holds with c_1 = 0.6 by §3. With note 35's
s_L, Theorem 3 of note 34 would apply for L >= 4 if the computed rows
(lower bounds for s_L) gave s_L itself. For example:

- L = 5: s ≈ 0.6 including the m-growth; with η = 0.3, ρ = 0.7/0.6 ≈ 1.17;
- L = 4: s ≈ 0.85; with η = 0.1, ρ ≈ 1.06. [T53: superseded; the largest
  L = 4 row found is 0.881 at m = 1 (note 35 §5), about 0.97-1.01 with the
  m-growth, so ρ > 1 is not suggested for L = 4.]

The abelian (PA) was already proved, without these inputs, in note 26
Prop. 2. The point of this section is that the non-abelian route of note 34
has its abelian limit under quantitative control.
