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

## 5. Consequences

- **3D.** By the README chain (notes 17, 18, 29), M1-3D ⇐ (S1) + (S2) for
  CMP 102. By Theorem 3, (S2) ⇐ (A_s). (S1) is the transport structure
  behind CMP 109 (0.29) and CMP 102's local expansion. So M1-3D ⇐ (S1) + (A_s).
  Both are statements about CMP 102's single-step analysis: its irrelevance
  bound, and its uniformity in a complex fluctuation coupling.
- **4D.** In note 29 Theorem 1, b̄ and c̄ come from (S2) and (S3) with
  O(γ² p(γ)²). Since Theorem 1 needs only b̄c̄ small (note 40), this
  suffices for small γ.
- **Relation to note 31.** Note 31's Lemma 2 is the special case of a
  single integral, computed explicitly with the Stein identity.
  Theorem 3 replaces that computation by evenness plus analyticity in s.
