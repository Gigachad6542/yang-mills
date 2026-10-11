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
- **Not checked.** The normalization constants, which are entire in s and
  drop out of D_E F; and the localization and cluster expansion of the
  fluctuation integral (2.13), which CMP 109 leaves to the next paper
  (p. 298). The CMP 109 §§3-5 expansions are checked below (T55).

*Source check, 4D (CMP 109 §§3-5; T55).* Printed pp. 269-298, read from the
page images. In §§3-5 the fluctuation-field action of step k has two parts:

- the Wilson part P^{(k)}(g_k, U_{k+1}, B);
- the curly bracket of (2.12). For each earlier scale j <= k it contains
  E^{(j)}(U_k(exp iB'V^{(k)})) - E^{(j)}(U_k(V^{(k)})) and the counterterm
  β_j(g_{j-1})(A(U_j(exp iB'V^{(k)})) - A(U_k(V^{(k)}))) of (4.38), which
  enters with a minus sign ((1.6)).

The deformation g_k -> s g_k of this note changes neither the inputs
E^{(j)} nor the earlier β_j(g_{j-1}), j <= k. Only B' changes. Every place
where g_k enters §§3-5:

1. **P^{(k)}, p. 269, (3.1).** Balaban only states that it is analytic in
   B and bounded by a second-order polynomial in B with O(ε_1) coefficients,
   so it is a small perturbation of dμ_{C^{(k)}}. Its localization is
   deferred (p. 270). It is the term I_{sg} checked in CMP 116 Part II §1
   above. Size only.
2. **B' = g_k CB - hD̃(g_k CB), p. 270, (3.2).** This is the only place g_k
   enters the curly bracket. After the deformation,
   B' = s g_k CB - hD̃(s g_k CB). This is analytic in s, and
   |B'| <= C|s g_k| p(g_k) <= Cα' on supp χ(|B| <= p(g_k)).
3. **First localization and the t_□-derivative, pp. 270-273, (3.3)-(3.17).**
   B' enters only through H_k(B') in δH_j ((3.8)). The bounds (3.9) and
   (3.17) are linear in |ζ_□H_k(B')|. The Cauchy integral (3.15) in t_□
   needs only that H_j(B(t)) satisfies (3.14). Balaban gets this by taking
   ε_1 small (p. 273), that is, from the size of B'. Under the deformation,
   ε_1 is replaced by Cα'. (The decay of δH_j/δB used in (3.9) is
   Proposition 9, (190) of CMP 102b; see note 39.)
4. **Gauge changes, pp. 273-276, (3.18)-(3.31).** The bounds are
   O(1)Mα_0. (3.29) allows G^c-valued gauge transformations. g_k does not
   enter.
5. **Fifth-order expansion and Lemma 4, pp. 277-280, (3.32)-(3.54).** These
   are:
   - the expansion (3.34) in the background field B and its remainder
     (3.35);
   - analyticity on U_j^c(X, α_0, α_1), (3.36);
   - Lemma 4 ((3.53)), stated for an arbitrary complex perturbation with
     values in g^c and size < α_3 (Balaban also calls it B', p. 279, but it
     is a perturbation of the background field, not the B' of (3.2));
   - the Cauchy estimate (3.54).

   The factor that restores the constant E_0 is O(1)α_2^{-1}ε_1, from the
   t_□-derivative (p. 280). That is again the size of B'. Size only.
6. **§4, background derivatives and Ward identities, pp. 281-288,
   (4.1)-(4.30).** These are:
   - Cauchy integrals (4.3) and the size bound (4.5);
   - the Ward identities (4.8)-(4.15), from invariance under g^c-valued λ
     with complex B (pp. 283-284), where (4.14) is algebraic
     (semisimplicity);
   - the derivative bounds (4.16)-(4.23);
   - algebra and a lattice Taylor formula, (4.24)-(4.30).

   g_k does not enter.
7. **E^{(2)} and the vacuum polarization, pp. 289-291, (4.32)-(4.37).** By
   Schur's lemma ((4.32)-(4.33)), E^{(2)}_{ab} is proportional to δ_{ab}.
   This holds for a complex coefficient too. (4.36) is a size bound, and
   (4.37) defines Π := Σ_X E^{(2)}(X, x, y). g_k does not enter.
8. **Counterterm cancellation, pp. 291-292, (4.38)-(4.45).** The scale-j
   counterterm (4.38) expands into (4.42) and (4.44); the term (4.45)
   vanishes. β_j(g_{j-1}) is *defined* as the coefficient in the
   corresponding expansion of Π^{(j)} (p. 292; (5.42) with the superscript
   (j), p. 298). So the two groups of terms cancel identically. The
   cancellation is an identity between input data and holds for every
   complex B'. Its prefactor is the earlier β_j(g_{j-1}), not g_k.
9. **§5, β from Π, pp. 292-298, (5.1)-(5.44).** §5 uses:
   - Euclidean covariance (5.2)-(5.6);
   - gauge invariance (5.9), (5.21);
   - the decay (5.10), |Π_μν(x-y)| <= O(1)E_0 exp(-δ_1|x-y|);
   - analyticity for |Im p| < δ_1 ((5.11));
   - the Laurent decomposition (5.17)-(5.24);
   - Taylor coefficients and their symmetries (5.25)-(5.36);
   - β = Σ_x Π_μν(x) x_μ x_ν for μ ≠ ν ((5.42)).

   (5.43)-(5.44) are a regrouping and a size bound. The printed exponent in
   (5.44) is missing its minus sign.

*The generated marginal coefficient.* After the deformation, the
coefficient produced by step k is β(s) = Σ_x Π_μν(x; s) x_μ x_ν ((5.42)),
built from the deformed output. It is complex for non-real s. CMP 109
mentions reality once, on p. 295, after (5.29) and (5.30): g_μν, a and b are
real for real z. That holds at real coupling and is never used afterwards:
- (5.31)-(5.42) are identities between Taylor coefficients and hold over C;
- the cancellation on p. 298 is an identity;
- (5.43)-(5.44) is a size bound.

Reality and positivity of β matter only for the flow of the couplings
between steps, which Balaban says the dependence of β_j on g_{j-1} governs
(p. 298). That flow is outside §§3-5 and outside the single step of (A_s).
In this note the marginal coefficient of the deformed output is one
component of F(E, s), and (A_s) needs only a bound on its size.

**Verdict (T55): no use of reality found in CMP 109 §§3-5.** g_k enters
only through P^{(k)} ((3.1)) and B' ((3.2)), and every estimate uses only
the size of B' (ε_1 in CMP 109, Cα' under the deformation). The generated
marginal coefficient enters only through algebraic identities and size
bounds.

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
