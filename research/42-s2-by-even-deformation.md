# (S2) for a whole RG step by an even complex deformation of the fluctuation coupling

Status:

- **Proved here.**
  - Lemma 1: a Schwarz lemma for even Banach-valued analytic functions.
  - Lemma 2: exact evenness of the deformed RG step in the deformation
    parameter s, and pure transport at s = 0.
  - Theorem 3: the derivative of one full RG step with respect to its input
    data is

        (transport) + R,   ||R|| <= 2M (g p(g))² / α'²,

    **under** the uniformity hypothesis (A_s).
  [Superseded (audit 2026-10-09, T82): for CMP 102, whose fluctuation cutoff is p² (T63 reading, §4), read
  p(g) as p(g)² throughout: the domain is |s| g p² <= α' and ||R|| = O(g² p⁴);
  note 61 uses this form.]
- **Hypothesis (A_s), open.** Balaban's single-step bounds hold, with the
  same constants, when the fluctuation coupling g is replaced by a complex
  coupling sg with |sg| <= α'/p(g).
- **Effect.**
  - Note 31 handled one fluctuation integral by Taylor and Cauchy. This
    note handles the complete step at once: tilted measure, cluster
    expansion, all generated terms. The only cost is the uniformity (A_s).
  - (S2) and the O(g²) part of (S3) of note 29 then hold with constant
    O(g² p(g)²). That is polylogarithmically weaker than O(g²), which is
    harmless:
    - in 3D the g_k² are geometric;
    - in 4D note 29 Theorem 1 uses only sup bounds and the product b̄c̄.
  - In 3D, by the README's chain, M1-3D ⇐ (S1) + (A_s) for CMP 102.
    [Superseded (audit 2026-10-09, T82): the current 3D route is note 61 Theorem 1:
    M1-3D <= (NA♭) + (A_s) + (H4) + (L_s).]

## 1. Lemma 1 (even Schwarz lemma)

Let Ψ be analytic on {|s| < s_0} with values in a Banach space, with
Ψ(-s) = Ψ(s) and ||Ψ(s)|| <= M. Then, for |s| <= 1 < s_0,

    ||Ψ(s) - Ψ(0)|| <= 2M |s|² / s_0².

*Proof.* Ψ(s) - Ψ(0) has only even powers, so Φ(s) := (Ψ(s) - Ψ(0))/s² is
analytic on the disc. On |s| = r < s_0 we have ||Φ|| <= 2M/r². The maximum
principle for Banach-valued analytic functions gives the bound inside. Let
r -> s_0. ∎

## 2. The deformed step

Fix a step of Balaban's RG: background U = U_{k+1}(V'), fluctuation field B
with Gaussian-type measure dB restricted by linear constraints (QB = 0,
gauge fixing) and by symmetric cutoffs χ(|B| <= p(g)). The input data are
the effective-action terms E (polymer activities, analytic on a complex
neighborhood of the small-field set). For s ∈ C \ {0} put

    S_s(B) := (sg)^{-2} [A(U e^{isgB}) - A(U)] + E(U e^{isgB}),
    F(E, s) := -log ∫ dB χ(B) e^{-S_s(B)}.

At s = 1 this is the actual step: the background Wilson term is separated,
and the output is F(E, 1) up to its localization into polymers.

**Lemma 2.**

1. F(E, -s) = F(E, s).
2. As s -> 0, S_s(B) -> ½⟨B, H(U) B⟩ + E(U), where H(U) is the Hessian of A
   at U on the constrained space. Hence F(E, 0) = E(U) + ½ log det H(U) + const,
   and D_E F(E, 0) h = h(U), which is pure transport.

*Proof.*

1. The substitution B -> -B preserves dB, the linear constraints and χ.
   Also S_{-s}(-B) = S_s(B), because (sg)^{-2} is even and the product
   (-s)(-B) = sB.
2. Expand A(Ue^{itB}) = A(U) + t⟨∇A(U), B⟩ + (t²/2)⟨B, H B⟩ + O(t³|B|³).
   The linear term vanishes because U is the constrained minimizer.
   Divide by t² with t = sg, and note E(Ue^{isgB}) -> E(U). ∎

## 3. Theorem 3

**(A_s) Uniform single-step bounds for complex fluctuation coupling.**
There are α' > 0 and M < ∞, independent of k, such that for all complex s
with |s| <= s_0 := α'/(g p(g)) the deformed step is analytic in (E, s) on the
inductive class of inputs, and

    ||D_E F(E, s)|| <= M

in Balaban's polymer norms (input norm to output norm).

**Theorem 3.** Under (A_s),

    D_E F(E, 1) = (transport h ↦ h(U)) + R,   ||R|| <= 2M (g p(g)/α')².

(p(g) is the fluctuation cutoff; for CMP 102 it is p(g)², see §4.)

*Proof.* By Lemma 2, Ψ(s) := D_E F(E, s) is even and analytic for
|s| < s_0, and Ψ(0) is transport. Lemma 1 with |s| = 1 gives
||Ψ(1) - Ψ(0)|| <= 2M/s_0² = 2M (g p(g)/α')². ∎

**The coupling input (S3).** The dependence on the input coupling enters
through the background term g^{-2}A. Differentiating with respect to g^{-2}
at fixed fluctuation coupling is again a derivative of the deformed step,
now in the direction h = A. So the generated part of that dependence is
also O(g² p(g)²) by the same argument, with M replaced by the bound on
D_{g^{-2}} F under (A_s).

## 4. Why (A_s) is plausible, and what it asks

- With |s| <= s_0, the fluctuation exponent satisfies
  |isgB| <= |s| g p(g) <= α' on supp χ. So all evaluations stay in the
  complex neighborhood where Balaban's activities are analytic. These are
  the same domains he already uses (CMP 102, CMP 109: analyticity in the
  fields).
- The deformed action differs from the Gaussian part by the cubic and
  quartic vertices of A, scaled by (sg) and (sg)². On supp χ their size
  relative to the quadratic form is <= C|sg| p(g) <= Cα', which is small. The
  tilt by E(Ue^{isgB}) has the usual small norm. So the cluster expansion
  of the deformed integral has the same small parameters as the actual
  one, uniformly on |s| <= s_0. Equivalently, (A_s) asks that Balaban's
  single-step estimates use the smallness of the fluctuation coupling only
  through |sg| p(g) <= α', not through reality or positivity of s.
- One point needs care. For complex s the quadratic part ½⟨B, HB⟩ is
  unchanged, so the Gaussian measure stays positive. Only the
  interaction is complex. This is exactly the situation of Balaban's
  complex-field estimates, so no positivity is lost in the Gaussian part.
- Large-field regions are not part of this step (they are cut out by χ and
  treated by the R-operation in 4D, and by CMP 102's large-field bounds in
  3D). (A_s) concerns the small-field step only.

*Source support (CMP 102, 3D).* In the renormalization of the interaction
terms (printed pp. 263-264), the field B (27) is bounded by
|B(c)| < 4L²|c - y| g_0 p(g_0) (eq. (28)), "and for g_0 sufficiently small the
number on the right-hand side above is small". The expansion is then
truncated at sixth order, with remainders estimated by analyticity. The
coupling enters these estimates only through the size g_0 p(g_0) of the
fluctuation exponent. That is exactly what (A_s) requires, with
|sg_0| p(g_0) <= α'. Turning this observation into a proof of (A_s) means
checking the remaining uses of the coupling in CMP 102's step, namely the
normalization constants and the large-field characteristic functions. The
latter are outside (A_s), which concerns the small-field step.

*Sharper source fact for 3D (CMP 102 pp. 261-262).* After the scaling
A -> g_0 A in (22), CMP 102 computes the fluctuation integral by:

- expanding v(g_0 A) - g_0^{-2} V(g_0 A) to sixth order in g_0, with
  remainder O(g_0^7 p^{18}(g_0))|Ω_1|;
- the cumulant expansion of the Gaussian integral, again to sixth order,
  giving connected vacuum graphs with at most six vertices and eight legs;
- localization by random-walk expansions with bounds (23)-(25).

Under the deformation g_0 -> s g_0 of the fluctuation coupling, every term up
to sixth order is a polynomial in s, so it is entire and even. Only the
remainder needs an estimate. That estimate is a Taylor-remainder and
cumulant bound, and it holds for complex coupling provided
|s g_0| p^{18/7}(g_0) is small. So in 3D, (A_s) reduces to **one** check:
the remainder bounds of CMP 102 (pp. 261-262) hold for complex coupling with
|s g_0| p(g_0)^{18/7} <= α'. Both are analytic estimates that never use
reality of g_0. The resulting Lipschitz constant in Theorem 3 is
O(g_0² p(g_0)^{36/7}), still polylogarithmically close to O(g_0²).

*Reading report on CMP 102 (T63).* Printed pp. 261-264, eqs. (18)-(33),
`sources/ocr/cmp102uv3.md`.

1. **Gaussian measure and cutoff ((22)).** The fluctuation integral is
   ∫dμ χ exp[v(g_0 A) - g_0^{-2} V(g_0 A)] with χ = Π_b χ(|A(b)| < p²(g_0)).
   dμ is a Gaussian with an exponentially decaying covariance, and it does
   not depend on g_0. χ is a real cutoff on the fluctuation field. Both
   are unchanged by g_0 -> s g_0. Note that the cutoff is p², not p.
2. **Sixth-order expansion.** The integrand v(zA) - z^{-2}V(zA) is analytic
   in z on |z| p(g_0)² <= c, since V starts at third order and the
   function is analytic in zA. Its Taylor remainder after order six is
   bounded by Cauchy's estimate in z. That bound, O(|z|^7 p^{18}) per site,
   uses only |z|. So it holds for complex z = s g_0 with
   |s| g_0 p(g_0)² <= α'.
3. **Cumulant expansion.** It uses formula (3.24) of [8] up to sixth order.
   The formula is analytic in the perturbation and needs only smallness on
   supp χ. The localization by decomposition of unity and the random-walk
   expansions of C^{(0)}, with bound (23), involve only the s-independent
   propagator. The output bounds (24)-(25) follow from (23) and the vertex
   bounds of step 2.
4. **Renormalization ((26)-(33)).** This step:
   - expands the localized terms in the background field ℋ(B), (27)-(30);
   - uses gauge invariance (26) to get (31)-(32), "there are no relevant
     variables";
   - uses the exponential decay of propagators.

   None of these involves the fluctuation coupling. The background
   coupling g_0 multiplies the background term, which (A_s) does not
   deform.
5. **Constants.** Normalization constants such as log σ_0, and Jacobians,
   are independent of the input data E. They drop out of D_E F. In note
   42's formulation, B is not rescaled, so there is no (s g_0)^{#bonds}
   Jacobian.

*Verdict.* No use of the reality or positivity of g_0 was found in the
CMP 102 single-step analysis (pp. 261-264). (A_s) is supported for CMP 102.
Because χ is |A| < p²(g_0), the deformation domain is
|s| g_0 p(g_0)² <= α'. So Theorem 3 gives ||R|| <= 2M (g_0 p(g_0)²/α')² =
O(g_0² p⁴), still polylogarithmically close to O(g_0²). Not checked: the
pages of [7] and [5] that CMP 102 cites for the variational problem and
the propagators, which do not involve the fluctuation coupling.

*Exact form of the deformation (4D and 3D).* Write the Wilson
interaction as

    I_g(B) := g^{-2}[A(Ue^{igB}) - A(U)] - ½⟨B, H B⟩ = g^{-2} Ĩ(gB),

where Ĩ is analytic and starts at cubic order. Then

    s^{-2} I_g(sB) = I_{sg}(B)   exactly.

So the deformed step S_s is Balaban's step with:

- the quadratic (Gaussian) part unchanged;
- the Wilson interaction at complex coupling sg;
- the effective-action terms E evaluated at the complex exponent isgB.

For |sg| p(g) <= α these exponents lie in Balaban's complex analyticity
domains (CMP 109 (1.18), domains U^c(X, α_0, α_1)). (A_s) is therefore
equivalent to this statement: **Balaban's single-step estimates use the
coupling only through bounds on |g| p(g) and on the complex-domain
activities, never through g > 0.** In 3D this was checked above against
CMP 102 pp. 261-262. In 4D, the localization and cluster expansion of the
fluctuation integral (2.13) is deferred by CMP 109 to the next papers
(CMP 109, end of §5: "In the next paper we will construct such localizations
and prove the bounds"). The check of (A_s) for 4D is therefore a reading of
CMP 116/119 for uses of the sign or reality of g. None was found in the
passages read for notes 36-39, but the full check is not done.

*Supporting 4D source fact (CMP 116, printed pp. 15-16).* In estimating
the fluctuation integral for complex configurations U'U (U' = exp(iη A')
with A' complex and small), Balaban writes: "the operators in it are not
symmetric, and the second measure is complex ... For the pair (U, 0) the
operators are symmetric, and the measure is positive, and then the
estimates are simpler. The general case is handled by a perturbative
argument" ((2.15)-(2.16)). So his 4D single-step estimates already allow
complex data, controlled by smallness alone. The s-deformation is milder:
the Gaussian part stays real and positive, and only the interaction I_{sg}
is complex, with |sg| p(g) <= α. This supports (A_s) in 4D. It does not
replace a line-by-line check of CMP 116/119.

*Source check, 4D (CMP 116 Part II §1 and CMP 109 §2; T49).*

- **Part II §1 (CMP 116).** In the localization of the fluctuation-field
  action, g_k enters in three places:
  - the analyticity domains in B, which are {|B| < ε_1 g_k^{-1}} ((1.34));
  - the substitution B' = g_k CB - hD(g_k CB) ((1.19)-(1.20));
  - the prefactor 1/g_k² at V(H_1 B'). That prefactor is cancelled by
    expanding to second order in B', and the zeroth and first orders vanish
    (pp. 9-10).

  This is exactly the identity s^{-2} I_g(sB) = I_{sg}(B) of §4. The
  Gaussian measure dμ_{C^{(k)}} with C^{(k)} = (C* Δ^{(k)} C)^{-1} does not
  depend on g_k (CMP 109 (2.11)-(2.12)). The passages read here use no
  reality or positivity of g_k.
- **CMP 109 p. 266, after (2.9).** Balaban notes that replacing ε_1 by
  (g_k/γ_k) ε_1 in the characteristic function χ_k "has the advantage that
  the functions E^{(j)}, β_j are analytic functions of the effective
  coupling constants". The inductive assumptions are stated for both
  versions: E^{(j)} is "a C^∞-function of g_{j-1} ∈ [0, γ] (or analytic)"
  (p. 270).

  So analyticity in the step coupling is part of Balaban's own inductive
  framework. The radius differs, though:
  - Balaban's variant gives a disc in g_k of radius comparable to γ_k;
  - (A_s) needs radius α'/p(g_k), which is larger by the factor
    1/(g_k p(g_k)).

  For that radius the fluctuation cutoff must be χ(|B| <= p(g_k)), the
  small-field cutoff of the later papers (CMP 119/122), not CMP 109's
  |g_k B| < ε_1.
- **Not checked.** The CMP 109 §§3-5 expansions with this cutoff, and the
  normalization constants. The latter are entire in s and drop out of D_E F.

## 5. Consequences

- **3D.** By the README chain (notes 17, 18, 29), M1-3D ⇐ (S1) + (S2) for
  CMP 102. By Theorem 3, (S2) ⇐ (A_s). (S1) is the transport structure
  behind CMP 109 (0.29) and CMP 102's local expansion. So M1-3D ⇐ (S1) + (A_s).
  [Superseded (audit 2026-10-09, T82): see note 61 Theorem 1 and §6b for the current four inputs.]
  Both are statements about CMP 102's single-step analysis: its irrelevance
  bound, and its uniformity in a complex fluctuation coupling.
- **4D.** In note 29 Theorem 1, b̄ and c̄ come from (S2) and (S3) with
  O(γ² p(γ)²). Since Theorem 1 needs only b̄c̄ small (note 40), this
  suffices for small γ.
- **Relation to note 31.** Note 31's Lemma 2 is the special case of a
  single integral, computed explicitly with the Stein identity.
  Theorem 3 replaces that computation by evenness plus analyticity in s.
