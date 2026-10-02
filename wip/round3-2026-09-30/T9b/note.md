# Lead review T9b: Codex T3, T4, T5 (correctness only)

Commits reviewed: b8e6dd6 `research/13-averaged-bias.md`, ff56fac
`research/14-three-dimensional-m1.md`, 5020a0e `research/16-normalized-tail.md`.
Line numbers refer to the file as committed in those hashes. Checks were run in
`/private/tmp/ym-r3/T9b/checks.py`. CMP 102 pp. 256-257 were checked against the
page images rendered from `sources/papers/Balaban1985-CMP102-UV-stability-3D.pdf`.
CMP 98 and CMP 122 I/II were checked against the OCR files in
`sources/tmp-audit-snapshot-2026-09-28/`.

## Verdict summary

| Item | Verdict |
|---|---|
| 13 Prop 1 (covariance identity; absolute continuity not needed) | correct |
| 13 (2.4), (2.5) | correct; (2.4) has a sharper form (see A3) |
| 13 Prop 2 (SU(2) two-point counterexample) | correct; a full-support strengthening is supplied (D2) |
| 13 Prop 3 (adjoint sphere) | correct |
| 13 (4.1) equal-mass per history label | **needs-fix**: the equal-mass hypothesis per label is proved only for the CMP 122 I prototype (D1) |
| 13 (5.2) | heuristic (schematic), correctly marked open; one wording fix |
| 14 Eqs. (1.1)-(1.3) vs CMP 102 | correct (checked against the page images) |
| 14 "no R-operation in 3D" | correct; add the "very sketchy" caveat and note that (41) is only an inequality |
| 14 Prop 1 (exact transport) | correct; assumes Q_k is Borel measurable |
| 14 Prop 2 (counterfactual series) | correct; **the line 211-214 tail exponent is wrong when H_L>1** |
| 16 Prop 1, (1.3) | correct, and the bounds are attained |
| 16 Prop 2, (2.6), (2.7) | correct |
| 16 Corollary 3 | **needs-fix**: "equivalent" only when varpi = alpha; "exactly the H7 contribution" is wrong (it is an upper bound) |
| 16 one-sided-majorant counterexample | correct |
| 16 section 3 "both have mass Z_lambda" | **needs-fix**: same prototype caveat as 13 (4.1) |

No proposition in the three notes is wrong as a mathematical implication. The
defects are: (a) an unverified equal-mass hypothesis for each history label,
imported from the introductory R-prototype into both 13 and 16; (b) one wrong
exponent in 14; (c) two overstatements in 16 Corollary 3.

## A. research/13 (T3)

A1. Lines 19-43, (1.2)-(1.3): **correct.** For the prototype replacement
r_y = P_y q̂_y, we have int F dR - int F dP = int nu(dV_c) P(V_c)[E_q̂ F - E_p̂ F].

A2. Prop 1, lines 52-95: **correct.** Each step checks: P, R << P+R; the
Radon-Nikodym derivatives dP/d(P+R) and dR/d(P+R) lie in [0,1] and sum to 1
(P+R)-a.e., so |h| <= 1; E_mu h = (R(Ω)-P(Ω))/(2a) = 0; and
2E_mu(Fh) = a^{-1} int F h d(P+R) = a^{-1} int F d(R-P). Complex F is fine with the
bilinear Cov (h is real). Mutual absolute continuity is not needed. Numerical
check on random measures whose supports only partly overlap: error 1e-16.

A3. (2.4), (2.5), lines 102-117: **correct.** Wording fix at line 102 ("are
only"). The same identity gives the sharper universal bound

  |a^{-1} int F d(R-P)| <= 2 inf_c ||F-c||_inf · E_mu|h| = inf_c ||F-c||_inf · ||R-P||_TV / a,

which does contain a smallness factor, namely the fiber total-variation distance.
The statement "neither contains a power of m" is true only because h is
uncontrolled. Replace it with: "Any gain must come from E_mu|h| (the fiber TV
distance) or from decorrelation of F and h. Neither is supplied by symmetry."

A4. Lines 123-126: **minor needs-fix.** For each gauge element g, h∘g = h holds
only (P+R)-a.e. Add: "choose the invariant version h̃(x) = int_G h(g·x) dg (compact
G, jointly measurable action)."

A5. Prop 2, lines 128-157: **correct.** F(±I) = ±1, a = 1, mu = ½(δ_I + δ_{-I}),
h = F, Cov_mu(F,h) = 1, and the defect is 2. The implication it falsifies is
"gauge invariance + positivity + equal mass ⇒ scale gain", and the example does
falsify it. There are two presentational weaknesses. P ⟂ R, and the action is
conjugation on a single holonomy rather than the lattice gauge action. Both are
removed by D2. Lines 159-163 (tensoring with an exterior factor) are correct.

A6. Prop 3, lines 170-186: **correct.** The invariant vector in the irreducible
adjoint representation is 0, and <A,A> = 1 on the unit sphere.

A7. Section 4, (4.1), lines 197-209: **needs-fix.** The identity requires
P_λ(Ω) = R_λ(Ω) for **each** label λ. CMP 122 I, Eq. (0.4), p. 176, gives this
only for the introductory operation. On p. 177 Balaban states that the actual
procedure takes "the denominators equal not [to] the integrals of the whole
densities ... but to the integrals of some parts of these densities". So equal
mass per label is not a published fact for the real construction. Fix: either
(i) prove equal mass for each λ from CMP 122 I section 1 (pp. 193-194 show that
the integrating operation there preserves each term's integral, but the later
renormalization with localized denominators must also be checked), or (ii)
replace (4.1) with the unequal-mass identity D1. D1 adds the mass-transfer term
Σ_λ (a^R_λ - a^P_λ) E_{mu_λ} F / Z. That term does not vanish when only
Σ_λ (a^R_λ - a^P_λ) = 0 is known.

A8. (4.2)-(4.4), (5.1): **correct** (5.1 is sufficient; the factor 2 does not
matter). Lines 276-277 wording: "(5.1) is already placement-summed". The weaker
primary target is (4.4) with the λ-sum taken inside the absolute value, i.e.
|Σ_λ a_λ Cov_λ|. Replace the sentence accordingly.

A9. (5.2): **heuristic.** Whether η_m = O(L^{-m}) suffices depends on the note 11
placement majorants. The note already calls it schematic, so keep that label.

A10. Section 6: the p. 176 Eq. (0.3) and CMP 122 II p. 356 readings are
verified (p. 356: loop variables "deserve detailed analysis and further
publication"). Add the p. 177 caveat (A7). Line 316 points to research note 19,
which does not exist in the repository. Mark it as "assigned, not yet written".

## B. research/14 (T4)

B1. Section 1, lines 12-36: **correct, verified on the page images.** Eq. (1)
ρ0 = exp[-g0^{-2}A - E], g0² = g²ε^{4-d} = g²ε; Eq. (2) ρ_{k+1} = Tρ_k (p. 256);
L^K ε = ε0; Theorem 1 (p. 257) is stated for "the sequence of densities ρ_k,
constructed by the inductive definition (2)"; Eq. (6) reads
∫dU ρ_k = ∫dU T^k ρ0 = ∫dU ρ0 = Z^ε exactly as quoted.

B2. Status lines 3-8: **needs-fix (label).** Add that Theorem 1 is a published
input whose proof Balaban calls "very sketchy" (p. 257), and that he makes "only
few remarks about the easier lower bound". Also state that Prop 1 does **not**
use Theorem 1. It needs only definition (2) and CMP 98 Eq. (10).

B3. Lines 38-42 ("no R-replacement"): **correct.** Source check: section C
(p. 267) says "the density ρ_{k+1} is bounded by a sum of terms obtained by
application of ... T to terms on the right-hand side of (41)". The induction is
an **inequality** pushed through the positive operator T. The densities are never
replaced. The Faddeev-Popov insertion (9) and the decomposition of unity (7) are
exact identities. Add one consequence: CMP 102 gives no exact polymer
representation of ρ_k, only the majorant (41). A 3D adjacent-depth comparison
cannot read an exact expansion from CMP 102. It needs a new one (Dimock-style) or
a bound-only argument.

B4. (2.1): matches CMP 98 Eq. (10), ρ'(V) = ∫dU δ(VŪ^{-1})ρ(U) (checked in the
OCR). **Minor needs-fix:** Eq. (15) of CMP 98 uses a logarithm. State that each
Q_k is taken as a Borel map on all of G^{bonds} (fix a Borel branch of log; the
discontinuity set is Haar-null). Otherwise the δ-kernel and (2.5) are undefined
off the small-field set.

B5. Prop 1 and (2.3)-(2.5): **correct.** ∫dV f(V)δ_G(VQ(U)^{-1}) = f(Q(U)) with
normalized Haar measure. Fubini applies because the integrand is bounded and the
spaces are compact. Iterating gives (2.3). exp(Σ z_α F_α) is bounded for fixed z.
Constant E cancels. Corollary 1 is correct. It holds trivially, since no R-term
exists.

B6. Section 3, lines 122-141: **correct**, with one wording fix. Since
L^{K+1}(ε/L) = ε0, both pushforwards in (3.1) already live on the **same**
terminal lattice T_{ε0}, so "first common terminal lattice" is just the terminal
lattice. Notes 17 and 18 (lines 136, 139) do not exist yet. Mark them as assigned.

B7. Section 4, (4.1)-(4.2): **correct.** (4.3) is a **source reading** and should
carry that label. CMP 122 I p. 176 states the arbitrary power of the bare ε for
the first-step factor. For scale k the relevant input is the CMP 102 regulator
ε1 = g_k p(g_k) with p(g) = b0(1+log g^{-1})^{p0}, p0 > 2 (pp. 257, 267). This
gives a per-plaquette factor exp(-c p(g_k)²), which is superpolynomially small in
g_k² = g²δ_m. So w_m <= C_N δ_m^N holds as a reading. Cite CMP 102 p. 258
("smaller than any positive power of ε") and p. 267 in addition to CMP 122 I.

B8. Prop 2, (4.4)-(4.6): **correct.** The ratio H_L L^{3-N} < 1 is equivalent to
(4.5), and the geometric tail is right. Lines 211-214 are **wrong when H_L > 1**:
at M = K, (H_L L^{3-N})^K = H_L^K (ε/ε0)^{N-3} and H_L^K = (ε0/ε)^{log_L H_L}. The
tail is therefore O(ε^{N-3-log_L H_L}), not O(ε^{N-3}). A numerical check with
L = 2, H_L = 1.5, N = 6 gives exponent 2.415 = N-3-log_2 1.5. Fix: "At M = K the
tail is O(ε^{N-3-log_L H_L}); for H_L = 1 this is O(ε^{N-3})."

## C. research/16 (T5)

C1. Prop 1, (1.2): **correct, and the bounds are attained.** Take B = u, P = p*
(G = p* - u) when u <= p*, or G = 0 otherwise. Take B = u, G = ℓ. Take B = ηG.
(1.3) is correct.

C2. Prop 2, (2.3)-(2.5): **correct.** P_y p̂_y(E_y) = p_y(E_y) and
P_y q̂_y(E_y) = r_y(E_y). This needs measurability of y ↦ p_y(E_y) and
y ↦ q_y(E_y), which the standard-Borel hypothesis on line 72 covers.

C3. (2.6): correct. Q = ε, r = δ_b, r(E) = 1. (2.7): correct; r(E) <= aP iff
q(E) <= aQ, since P > 0. **Typo:** `qquad` without a backslash at lines 142, 152,
228 and 321 (this breaks rendering).

C4. Section 3, lines 167-170 ("Both have mass Z_λ"): **needs-fix**, the same
issue as A7. If the actual R-operation uses partial denominators (CMP 122 I
p. 177), then r_y = (P'_y/Q'_y) q_y with P'_y ≠ P_y. The post-replacement
exterior marginal is then P'_y ν, not P_y ν. The q-term of (3.2) becomes
∫ q̂(E) P ν / Z = ∫ (P_y/P'_y) r_y(E) ν / Z. This is an uncontrolled ratio of
exactly the kind that (2.6) shows to be fatal. State (3.2) and Corollary 3 under
the explicit hypothesis P'_λ = P_λ (equal fiber mass for each label), or add a
bound on P/P'.

C5. Corollary 3, lines 192-205: **needs-fix (two overstatements).**
(i) In note 11, (3.9)-(3.10), H7_Σ is defined with an arbitrary majorant
varpi_λ >= Z^{-1}|P_λ ν_λ|. "Equivalent to (3.3)" holds only for the choice
varpi_λ := α_λ, where the two series agree term by term. For a general admissible
varpi, H7_Σ(varpi) ⇒ (3.3), but the converse fails, as the note's own
counterexample at lines 242-252 shows. Fix: "H7_Σ with varpi_λ = α_λ is
equivalent to (3.3)."
(ii) Line 204, "the tail ... is exactly the H7 contribution", is **wrong**. The
H7 contribution to the telescope is Z^{-1} ∫_{E_λ} F d(M^R_λ - M_λ), and the
tail of (3.3) **bounds** its absolute value after multiplication by sup|F|. Fix:
"bounds, up to the factor sup|F|".

C6. (3.4): correct (the identity is trivial for the disintegration of |S_λ|).
(3.5)-(3.6): correct. The lower bound r_λ >= 1 is not needed for this implication.
Counterexample at lines 242-252: correct. Exact average ε, majorant average 1,
and dvarpi/dα(a) = 1/ε is unbounded.

C7. Section 4: item 3 is verified (CMP 122 II (1.75): a normalized T_k expectation
is <= e^{3 sup|σ|} sup|F|, an order-one bound). Item 1 needs the p. 177 caveat
(C4). Items 2, 4 and 5 were not re-verified in this review.

C8. Section 5: (5.1) is correct. (5.2) is correct but, with its unnormalized
notation p_λ(·|V_c) (normalized in note 11), it is equivalent to (3.3) with the
optimal choice a = p̂(E), b = q̂(E). It is a restatement, not a stronger or easier
estimate. Say so. The direct-mass route (M(E) <= M(X)) is correct as a sufficient
condition when M_λ is the localized component. Lines 343-345 are stale: after
note 14 there are no R-components in 3D, so H7_Σ is vacuous there. Note 14
section 4 is only counterfactual.

## D. Supplements proved in this review

**D1 (unequal-mass covariance identity; proved).** Let P, R be finite positive
measures with masses a_P, a_R, a_P + a_R > 0. Set mu = (P+R)/(a_P+a_R) and
h = d(R-P)/d(R+P). Then for bounded F,

  ∫F d(R-P) = (a_P+a_R) Cov_mu(F,h) + (a_R - a_P) E_mu F.

*Proof.* ∫F d(R-P) = (a_P+a_R) E_mu(Fh), and (a_P+a_R) E_mu h = a_R - a_P. ∎
(Numerical check: error 5e-16.) When a_R = a_P this is Prop 1 of note 13. When
masses match only in total, Σ_λ(a^R_λ - a^P_λ) = 0, the residual
Σ_λ (a^R_λ - a^P_λ)(E_{mu_λ}F - c) is an extra term, for any constant c. It needs
its own estimate.

**D2 (full-support, lattice-gauge-invariant counterexample; proved).** Take the
configuration space G^4 of one plaquette p (G = SU(2), product Haar dU, with the
lattice gauge action). Let F(U) = ½ tr U(∂p), and for 0 < t < 1 let

  P = (1 - tF) dU,  R = (1 + tF) dU.

Both are strictly positive except on a null set, gauge invariant and mutually
absolutely continuous. Since U(∂p) is Haar distributed, ∫F dU = 0, so both have
mass 1. Then ∫F d(R-P) = 2t ∫F² dU = t/2, because ∫|tr V|² dV = 1 on SU(2)
(Monte Carlo value: 1.0003). This defect is order one and independent of any
scale label, so the conclusion of note 13 Prop 2 survives common support and
smooth densities.

**D3 (corrected tail; proved).** See B8: the tail is O(ε^{N-3-log_L H_L}).

## E. Required edits (for the collaboration file)

1. 13, section 4/(4.1) and section 6; 16, section 3 and section 4 item 1: state
   equal mass for each label as a hypothesis (true for the CMP 122 I (0.3)-(0.4)
   prototype, unverified for the p. 177 actual procedure), or use D1.
2. 14, lines 211-214: correct the exponent to N-3-log_L H_L.
3. 16, Corollary 3: "with varpi_λ = α_λ"; replace "exactly" with "bounds, up to sup|F|".
4. 14, status: add the "very sketchy" and lower-bound caveats; note that Prop 1
   is independent of Theorem 1; note that (41) is only an inequality.
5. 14, (2.1): Q_k is Borel on the whole configuration space.
6. 13, line 102: add the TV-sharpened bound; 13, lines 276-277: fix the wording
   about the weaker target; 13, section 3: choose the invariant version of h.
7. 16: fix the `qquad` typos; update lines 343-345 in light of note 14; say that
   (5.2) is a restatement.
8. Dangling references to notes 17, 18 and 19: mark as assigned, not yet written.
