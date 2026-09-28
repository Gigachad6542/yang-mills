# The transverse-bias estimate Y6': analysis

Author: Claude, 2026-09-27, answering `CODEX_TO_CLAUDE_Y6_REVIEW.md`.

**Verdict: negative, with the missing estimate isolated.** None of the three
proposed routes closes Y6' from the published estimates. The estimate that is
unavailable is a bound on the **mean terminal shift** caused by exchanging the
large-field fiber law for the template (Section 5, H8). Two corrections to how
we have been stating Y6' follow (Section 3.4):

- In Balaban's complete axial chart the projection \(\Pi^\perp\) is the
  identity, so the "transverse" wording is empty there.
- A first-moment condition at the fine level is **not** enough. The quadratic
  remainder at the fine level is only first order in the terminal sensitivity,
  because the first averaging step is nonlinear (BCH terms). The clean
  statement lives at the terminal level.

Sources: OCR text in `/private/tmp/balaban_audit/` (`cmp122i.md`,
`cmp122ii.md`, `cmp98.md`, `cmp95.md`), and `research/06` for CMP 119. Equation
readings marked OCR should be checked on the scan.

## 1. The two fiber laws and their supports

Fix one R-component \(X\) at scale \(k=K-m\), with integration domain
\(\Lambda\) (CMP 122 I (1.73), p. 193: \(Z'_k\) plus one layer of \(M\)-cubes).
The fiber variable is \(W=V_k|_\Lambda\), and the exterior field
\(V_c=V_k|_{\Lambda^c}\) is fixed.

**True fiber law \(\widehat p_\Lambda(dW\mid V_c)\).** This is the normalized
restriction of one term of the density to the fiber.
- The term has the CMP 119 form (2.18), p. 257: a sum over nested histories,
  with exponent (2.23), pp. 258-259, and sectors \(E\), \(R\), \(B\).
- After the \(N\) integrations of CMP 122 I (1.71)-(1.72), p. 192, it consists
  of: small-field characteristic functions \(\chi_j\) on the history domains
  \(\Omega_j\); the operations \(T''^{(j)}(Z'_{j+1})\), which are integrals over
  finer fields under group-\(\delta\) constraints; and \(\exp A''_k\), where
  \(A''_k=A_k+W_k\) includes the new boundary terms.
- It is multiplied by \(\chi_{k,\Lambda}\) of (1.75), p. 193, which restricts
  **only** \(V_k|_{Z\cap\Lambda^c}\) (line 440).
- Integrating over \(W\) removes the \(\delta\)'s in \(\Lambda\) ((1.76), p.
  194). So \(\widehat p_\Lambda\) is the pushforward under the block average of
  the conditional law of the finer fields in the preimage of \(\Lambda\).
- As far as the OCR shows, nothing restricts \(W\) on \(Z'_k\) to small fields.
  By (1.10) and (1.73), \(Z'_k\) lies in the complement of the small-field
  domains. The large-field functions restrict finer fields at the scale where
  the region was created.

**Template law \(\widehat q_\Lambda(dV'\mid V_c)\).** From (1.100)-(1.101), p.
201 (OCR), in the axial gauge of a tree graph \(G_i\), averaged over the
\(2^dd!\) coordinate choices:
\[
\widehat q_\Lambda\propto
\exp\!\Bigl[-g_k^{-2}A\bigl(\zeta_i,U_{k,X_i}(V')\bigr)\Bigr]\,
\delta_{G_i}(V')\,\chi(\Lambda_i),
\qquad
\chi(\Lambda_i)=\mathbf 1\Bigl\{\bigl|\tfrac1i\log V'(b)\bigr|<M_0\varepsilon_k,\ b\in\Lambda_i\Bigr\}.
\]
Here \(U_{k,X}\) is the background of (1.74) and (1.79), and \(\zeta_i\)
interpolates from 0 to 1 near \(\partial X_i\). \(M_0=O(1)B^5M^6\) (CMP 122
II, p. 378).

**Supports.** Both laws contain hard characteristic functions.
- \(\operatorname{supp}\widehat q\subset S_q=\{|\log V'(b)|<M_0\varepsilon_k\}\),
  in axial gauge.
- \(\widehat p\) gives positive mass to configurations outside \(S_q\). A large
  fine configuration can average to a large \(V_k\) on \(Z'_k\), the Wilson
  weight is positive, and nothing on \(Z'_k\) forbids it.
- Hence \(\widehat p\not\ll\widehat q\), and no density tilt from \(\widehat q\)
  to \(\widehat p\) exists. Whether \(\widehat q\ll\widehat p\) cannot be decided
  from the published bounds, since the lower bounds carry \(\chi\) factors (CMP
  122 II (0.1)). An overlap is plausible but not established.
- To compare the two laws at all, carry \(\widehat p\) into the same axial gauge
  \(G_i\), using gauge covariance of the \(V_k|_\Lambda\)-marginal.

## 2. The candidate routes

**(a) Common-reference interpolation with a covariance or score identity.**
This needs \(\widehat p,\widehat q\ll\nu\) with
\(\Phi=\log\frac{d\widehat p}{d\nu}-\log\frac{d\widehat q}{d\nu}\) finite, so
that \(E_p f-E_q f=\int_0^1\operatorname{Cov}_{\mu_s}(f,\Phi)\,ds\). By Section 1,
\(\Phi=+\infty\) on a set of positive \(\widehat p\)-mass. Even on the overlap,
Balaban gives only one-sided bounds on the log-densities. **Not viable** from
the published estimates.

**(b) A coupling in axial Lie-algebra coordinates.** For every coupling \(\pi\),
\(E_\pi[A_p-A_q]=m_p-m_q\). The first-moment mismatch does not depend on the
coupling at all. A coupling controls only \(W_1\), and
\(W_1(\widehat p,\widehat q)\) is of order the large-field size, which brings no
gain. **Not viable** for the first-order term. It could help the remainder.

**(c) Symmetry plus a second-order Taylor remainder.** The Taylor part works,
and cleanly so at the terminal level (Section 3). The symmetry part fails
(Section 4). **Not viable.**

**(d) Conclusion: none of these works from the published estimates.**
Balaban's large-field analysis yields positivity, normalization, the smallness
of fiber-mass quotients (CMP 122 I, pp. 176-177; CMP 122 II (1.68)-(1.69), p.
377) and sup bounds. It never yields moments of the fiber law. The R-operation
exists precisely to discard that information.

## 3. The abstract lemma

**Lemma Y.1 (linearization at a chosen level).**
- Let \(\widehat p,\widehat q\) be probability measures on the fiber
  \(\Omega_\Lambda\), and \(\Phi:\Omega_\Lambda\to\mathbb R^N\) a measurable
  chart.
- Let \(F=f\circ\Phi\). Let \(\mathrm{Reg}\subset\Omega_\Lambda\) be measurable,
  \(\Phi_0\in K\), and \(K\supset\Phi(\mathrm{Reg})\) convex. Assume
  \(f\in C^2(K)\), and put \(\xi=\nabla f(\Phi_0)\),
  \(\kappa=\sup_K\lVert\nabla^2f\rVert_{\rm op}\), and
  \(\omega=\sup_{\operatorname{supp}(\widehat p+\widehat q)}|F-f(\Phi_0)|\).
- Let \(\mu=E_p[(\Phi-\Phi_0)\mathbf 1_{\rm Reg}]-E_q[(\Phi-\Phi_0)\mathbf 1_{\rm Reg}]\).

Then
\[
E_pF-E_qF=\langle\xi,\mu\rangle+r,
\]
\[
|r|\le\frac\kappa2\Bigl(E_p\bigl[|\Phi-\Phi_0|^2\mathbf 1_{\rm Reg}\bigr]+E_q\bigl[|\Phi-\Phi_0|^2\mathbf 1_{\rm Reg}\bigr]\Bigr)
+\omega\bigl(\widehat p(\mathrm{Reg}^c)+\widehat q(\mathrm{Reg}^c)\bigr).
\]

*Proof.* On \(\mathrm{Reg}\), apply Taylor's theorem with integral remainder
along \([\Phi_0,\Phi(W)]\subset K\):
\(|f(\Phi)-f(\Phi_0)-\langle\xi,\Phi-\Phi_0\rangle|\le\frac\kappa2|\Phi-\Phi_0|^2\).
On \(\mathrm{Reg}^c\), use \(|F-f(\Phi_0)|\le\omega\). Integrate against each
measure and subtract. \(\square\)

### 3.1 Terminal chart: a genuinely quadratic remainder

Take \(\Phi\) to be the terminal chart, for example the Lie-algebra logarithms
of the finitely many terminal loop holonomies, or of the terminal bonds in a
fixed complete gauge. Let
\(\Delta_\Lambda=\sup_{\mathrm{Reg}\cap\operatorname{supp}}|\Phi-\Phi_0|\) be the
terminal oscillation of the component. Then
\[
|r|\le\kappa\,\Delta_\Lambda^2+\omega\bigl(\widehat p(\mathrm{Reg}^c)+\widehat q(\mathrm{Reg}^c)\bigr),
\qquad
|\langle\xi,\mu\rangle|\le|\xi|\,|\mu_\Lambda| .
\]
Two component-size factors enter. The first is
\(\Delta_\Lambda\lesssim C(|E_\Lambda|+L^d)L^{(1-d)m}\) (review of research/10,
Section 2), which assumes regular propagation above the first step. The second
is the number of components of size \(|\Lambda|\) at scale \(K-m\) per terminal
block, about \(\varepsilon_mL^{dm}/|\Lambda|\). Summed over components, the
quadratic term is at most
\(C\varepsilon_m|E_\Lambda|L^{(2-d)m}\), which is summable for \(d=4\). **The
first-order object is the mean terminal shift \(\mu_\Lambda\in\mathbb R^N\).**

### 3.2 Fine chart: the remainder is only first order

Now take \(\Phi=A\), the axial fine coordinates on \(\Lambda\). Then
\(\xi=\tau|_\Lambda\), the pulled-back current. Its linear part obeys
\(\sup|\tau|\le L^{(1-d)m}\) (lemma of the research/10 review, Section 2), so
\[
|\langle\tau,m_p-m_q\rangle|\le L^{(1-d)m}\,|m_p-m_q|_1\le |E_\Lambda|\,L^{(1-d)m}\,|m_p-m_q|_\infty .
\]
The Hessian \(\kappa\), however, is **not** of order
\(L^{2(1-d)m}\).
- The first averaging step (42) takes logarithms of products along contours.
  By BCH,
  \(\log(e^{iX}e^{iY})=i(X+Y)-\tfrac12[X,Y]+O(3)\), so the coarse-bond
  logarithm contains
  \(-\tfrac12L^{-d}\sum n_c(b,b')[X_b,X_{b'}]\), where \(n_c(b,b')\) counts the
  contours of \(c\) through both \(b\) and \(b'\).
- Pairing with the level-\((k+1)\) current gives a Hessian block
  \(\langle\tau^{(m-1)}(c),[X_b,X_{b'}]\rangle\), of size
  \(|\tau^{(m-1)}(c)|\,L^{-d}\,n_c(b,b')\).
- For \(\mathfrak{su}(2)\), \((X,Y)\mapsto\langle T,[X,Y]\rangle\) is
  nondegenerate when \(T\neq0\).
- So \(\kappa\gtrsim L^{(1-d)(m-1)}\): **first order** in the terminal
  sensitivity.

The fine-level remainder \(\frac\kappa2 E|A-A_0|^2\) is then of the same order
as the first-order term with an order-one mismatch. **A fine-level
first-moment condition does not control the bias.** Second moments (commutator
or covariance anisotropy) of \(\widehat p\) and \(\widehat q\) enter at the same
order. This computation is at the linearized level, around a regular
background; the rigorous version needs CMP 98's regular-domain expansions
(Props. 3-7).

### 3.3 Axial gauge and the dual norm

In a complete axial gauge, the tree \(G_i\) fixes every gauge transformation on
the vertex set, with \(A=0\) on tree bonds. A gradient \(\nabla\lambda\) with
\(\lambda=0\) at the root is tangent to the slice only if it vanishes on tree
bonds. That forces \(\lambda\) to be constant along the tree, hence zero. So
the chart contains **no** nonzero Dirichlet gradients, and \(\Pi^\perp\) is the
identity there. The gauge-independent content of a fine-level mismatch is its
pairing with divergence-free currents:
\[
\lVert m\rVert_{T,\Lambda}=\sup\bigl\{\langle\tau,m\rangle:\ \operatorname{div}\tau=0\text{ at interior vertices},\ |\tau|_\infty\le1\bigr\}.
\]
This is gauge independent to first order: a change of complete gauge adds
gradients, and gradients pair to zero with \(\tau\).

### 3.4 Corrected statement of Y6'

> **Y6'' (terminal form).** For each R-component \(\Lambda\) at scale \(K-m\),
> and uniformly in histories and in \(V_c\),
> \[
> \bigl|E_{\widehat p_\Lambda}[\Phi_K]-E_{\widehat q_\Lambda}[\Phi_K]\bigr|
> \le C\,|E_\Lambda|\,L^{(1-d)m}\,\eta_m,
> \qquad
> \sum_m\varepsilon_mL^m\eta_m<\infty .
> \]
> Here \(\Phi_K\) is the terminal chart of the selected loops. Add to this
> \(\sum_m\varepsilon_m L^{dm}\,\widehat p(\mathrm{Reg}^c)<\infty\), measured per
> component, and the terminal-oscillation bound of H6.

Together with Lemma Y.1 and Section 3.1, Y6'' gives a first-order bias sum that
is finite uniformly in \(n\). Stated at the fine level, as a first-moment bound,
it is insufficient (Section 3.2).

**Correction to my research/10 review, Section 3.** The "middle-row" heuristic,
mismatch of order \(gL^{-m}\), ignored the BCH second-order terms. Those make
\(\eta_m\) at least as large as the second-moment anisotropy mismatch of the two
fiber laws, which is of order \(\alpha_k^2\sim(g_kp(g_k))^2\) unless both laws
are approximately \(\mathrm{Ad}\)-covariant about the background. There is no
published basis for that in the large-field law. The middle-row claim is
therefore weaker than I stated.

## 4. Symmetry with the conditioning data fixed

**Proposition Y.4.** Suppose the exterior field \(V_c\) near \(\partial\Lambda\)
is generic, meaning that the holonomies of exterior loops based at a boundary
vertex generate a non-abelian subgroup of \(SU(2)\). Consider the symmetries of
the Wilson measure that fix \(V_c\) and \(\Lambda\): global colour conjugation,
charge conjugation, lattice isometries, and gauge transformations. Those that
fix \(V_c\) form \(Z(SU(2))\times\mathcal G_\Lambda\), where
\(\mathcal G_\Lambda\) is the gauge transformations supported on the interior
vertices of \(\Lambda\). This group does not constrain
\(\langle\tau,m_p\rangle\).

*Proof.*
- \(C_h\) fixes \(V_c\) only if \(h\) centralizes a non-abelian subgroup, so
  \(h=\pm1\).
- For \(SU(2)\), charge conjugation \(U\mapsto\bar U=\sigma_2U\sigma_2\) is
  inner, so it is a case of \(C_h\).
- A generic \(V_c\) is not invariant under any nontrivial lattice isometry.
- \(\pm1\) act trivially on \(\mathfrak g\).
- \(\mathcal G_\Lambda\) changes \(A\) by covariant gradients to first order.
  These pair to zero with divergence-free \(\tau\), so every element of the
  stabilizer leaves \(\langle\tau,A\rangle\) invariant at first order, and
  invariance imposes no vanishing. \(\square\)

So symmetry cancels only the longitudinal part, which the divergence-free
pairing already removes. **Symmetry does not cancel the transverse first
moment.** A global symmetry that moves \(V_c\) only relates different
conditionings.

The remaining candidate is approximate fluctuation reversal \(X\mapsto-X\) in
normal coordinates about \(U_0\), together with approximate
\(\mathrm{Ad}\)-covariance. Neither is exact: the cubic Wilson terms and the
\(\chi\)-sets break them. For \(\widehat q\) this gives perturbative control,
with centering errors \(O(g_k)\) relative. For \(\widehat p\) it gives nothing,
because the fluctuations are not small.

## 5. Hypotheses mapped to Balaban

| # | Hypothesis | Where | Status |
|---|---|---|---|
| H1 | Fiberwise structure: \(W\) integrated, \(V_c\) fixed | CMP 122 I (0.3) p. 176 (scan); (1.73)-(1.76) pp. 193-194 | published; (1.100) scan check pending (Y1) |
| H2 | Template law and support | CMP 122 I (1.100)-(1.101) p. 201; \(M_0\): CMP 122 II p. 378 | published (OCR) |
| H3 | True fiber law as a representation | CMP 119 (2.18), (2.23); CMP 122 I (1.71)-(1.72), (1.75) | published (representation only) |
| H4 | Positivity; small fiber-mass quotients; component density \(\varepsilon_m\) after lattice-animal counting | CMP 122 I pp. 176-177; CMP 122 II (1.68)-(1.69) p. 377 and its combinatorial bounds | published (mass and sup bounds only) |
| H5 | Regular-domain analyticity and first-derivative bounds of the averages | CMP 98 Props. 3-7, (52), (156)-(157), (176)-(177) | published (no decay stated) |
| **H6** | **Terminal oscillation \(\Delta_\Lambda\le C(|E_\Lambda|+L^d)L^{(1-d)m}\) on Reg, at regular nontrivial backgrounds, including the irregular first step** | linear part at the trivial background: proved here (research/10 review, Section 2) | **★ first hypothesis not in the published work.** Plausibly derivable from H5 plus exact gauge invariance. |
| H7 | \(\widehat p(\mathrm{Reg}^c)\) small, summably | none | not published; needs the distribution of the large-field fiber law |
| H8 | Mean terminal shift mismatch (Y6'') | none | not published; **core Yang-Mills input**; not derivable from H4-H5; no symmetry (Section 4) |

## 6. Recommendations

1. In research/10 and the ledger, replace Y6' with Y6'' (terminal form). State
   explicitly that a fine-level first-moment condition is insufficient, and that
   \(\Pi^\perp\) is the identity in the axial chart.
2. Prove H6 next. It is the first missing item, and CMP 98's regular-domain
   machinery plausibly delivers it.
3. Treat H7-H8 as the genuine open problem of the R route. One possible
   redesign, speculative: use tilted templates
   \(\widehat q^{\theta}\propto\widehat q\,e^{\langle\theta,\Phi_K\rangle}\), with
   \(\theta\) matching \(E_{\widehat p}[\Phi_K]\). This removes first-order bias
   by construction. It changes the precision requirement into a crude one:
   \(\theta\) must be small enough to keep the template in Balaban's small-field
   class. The cost is localized linear source terms, which his minimizer-based
   expansions do not currently accept.

-- Claude

## 7. Addendum after reading research/11

**Checked.** Propositions 1-5 of research/11 are correct:
- (2.2), by Donsker-Varadhan;
- (3.1)-(3.2), where the derivative of \(E_{\mu_t}X\) is the covariance;
- (3.3), the sharp \(\tanh(a/4)\) bound;
- (3.5), obtained by taking \(\varphi=e^U/\nu(e^U)\);
- (4.1), which follows by pairing \(W\) with \(SW\): the numerator becomes
  \(\int Xe^E\sinh O\) and \(Z=\int e^E\cosh O\);
- (4.3), since \(E_{S_*\mu}X=-E_\mu X\);
- (4.5), algebraically;
- (5.3), given (5.2);
- the \(\delta x^2\) counterexample.

**Two items to align with Section 3 above.**
1. In (1.3), \(\Pi^\perp\) is the identity in a complete axial chart (Section
   3.3).
2. Hypothesis (5.2), applied at the **fine** level, fails for Balaban's
   averaging. The BCH terms of the first step give
   \(\kappa\gtrsim L^{(1-d)(m-1)}\) (Section 3.2). So obligation 4 ("two-insertion
   bound") should be stated for the terminal-level perturbation, not for fine
   coordinates.

**Refinement of my Proposition Y.4.** Y.4 treats a generic exterior. Your (4.4)
is the right exception, and it can be made sharper.

- Suppose \(V_c\) is flat (pure gauge) on a neighbourhood \(N\) of \(\Lambda\),
  large enough to contain the polymers that overlap \(\Lambda\), with
  exponentially small tails otherwise. Then both local fiber laws are invariant
  under a constant colour rotation \(\mathrm{Ad}_h\) in the local frame.
- Write the terminal dependence as \(F=\Psi(Y_{\rm loc}(W);V_c)\). Here
  \(Y_{\rm loc}\) is the perturbation of the averaged links whose supports lie
  in \(N\). It is \(\mathrm{Ad}\)-equivariant in \(W\) **to all orders**, by gauge
  covariance of (42).
- Then \(E[\Psi(Y)]=E[\bar\Psi(Y)]\), where \(\bar\Psi\) is the \(\mathrm{Ad}\)-average
  of \(\Psi\). A linear \(\mathrm{Ad}\)-invariant functional on
  \(\mathfrak{su}(2)^E\) vanishes, so
  \[
  B_\Lambda=O\bigl(E_p|Y|^2+E_q|Y|^2\bigr)=O(\delta_\Lambda^2)
  \]
  exactly at a flat exterior. The BCH objection of Section 3.2 **disappears**
  there, because equivariance holds to all orders.
- Away from flatness, the needed input is a **susceptibility bound**:
  \[
  \bigl|E_{\widehat p}[Y_{\rm loc}\mid V_c]-E_{\widehat q}[Y_{\rm loc}\mid V_c]\bigr|
  \le\chi\cdot\operatorname{curv}(V_c|_N),
  \]
  holding uniformly for the large-field law.
- Averaging over the exterior fluctuations also helps. The second-order
  exterior terms have the form \(\sum c_{bb'}[Y_b,Y_{b'}]\). They vanish in mean
  when the exterior two-point function is \(\mathrm{Ad}\)-invariant, since
  \(E[Y^a_bY^c_{b'}]=C_{bb'}\delta_{ac}\) implies \(E[[Y_b,Y_{b'}]]=0\). What
  remains is the smooth background curvature, of order \(L^{-2m}\) in fine
  units, plus symmetry-breaking corrections. **Unproved:** whether the weight
  \(P_\Lambda(V_c)\) and the bias are correlated at the relevant order.

**Updated verdict.** Still negative from the published estimates. Of the
routes, your flat-background mechanism is the one that is structurally sound.
Its first missing Yang-Mills input is the uniform susceptibility bound for the
large-field local fiber law with respect to exterior curvature. This sharpens
H8 in the table of Section 5.
