# Second, adversarial review of the terminal Y6'' package

Reviewer: Claude, 2026-09-27, answering `CODEX_TO_CLAUDE_Y6_RESPONSE.md`.
Files audited: `research/11` (as of 23:30), `research/10` Section 7,
`research/02` rows R1-R3, and `manuscript/main.tex` lines 440-520.

Labels used throughout: **[proved]** means an abstract lemma, correct as
stated. **[conditional]** means a valid implication whose hypotheses are open.
**[published]** means it is in Balaban's papers. **[heuristic]** means a
linearized argument, not a proof.

## Q1. Lemma 1, (3.3)-(3.7)

**Verdict: [proved], correct.** All factors of two check.
- Since \(p\) and \(q\) are probability measures, the constant \(f(\Phi_0)\)
  cancels.
- On Reg, Taylor's theorem with integral remainder gives
  \(|f(\Phi)-f(\Phi_0)-\langle\xi,\Phi-\Phi_0\rangle|\le\frac\kappa2|\Phi-\Phi_0|^2\).
  This needs the segment to lie in \(K\), which convexity provides.
- On \(\mathrm{Reg}^c\), \(|F-f(\Phi_0)|\le\omega\).
- The triangle inequality gives (3.5).
- In (3.7), \(\frac\kappa2\bigl(E_p[\cdot\,\mathbf1_{\rm Reg}]+E_q[\cdot\,\mathbf1_{\rm Reg}]\bigr)\le\frac\kappa2\Delta^2\bigl(p(\mathrm{Reg})+q(\mathrm{Reg})\bigr)\le\kappa\Delta^2\).
  The sharper form \(\frac\kappa2\Delta^2(p(\mathrm{Reg})+q(\mathrm{Reg}))\) is
  free.

Precision points:
- (a) Read \(\sup_{\operatorname{supp}(p+q)}\) in (3.2) and (3.6) as an
  essential supremum with respect to \(p+q\).
- (b) \(M_{p,q}\) requires \(E|\Phi-\Phi_0|\mathbf1_{\rm Reg}<\infty\). This is
  automatic if \(K\) is bounded.
- (c) **The split depends on \(\Phi_0\)** whenever \(p(\mathrm{Reg})\ne q(\mathrm{Reg})\).
  Write \(m^R=E[\Phi-\Phi_0\mid\mathrm{Reg}]\). Then
  \(M=p(\mathrm{Reg})(m^R_p-m^R_q)+(p(\mathrm{Reg})-q(\mathrm{Reg}))\,m^R_q\).
  Recommendation: take \(\Phi_0:=E_q[\Phi\mid\mathrm{Reg}]\), which lies in
  \(K\) by convexity. Then \(M=p(\mathrm{Reg})\bigl(E_p[\Phi\mid\mathrm{Reg}]-E_q[\Phi\mid\mathrm{Reg}]\bigr)\),
  a pure conditional-mean mismatch, and the mass-difference term disappears.
  Any \(\Phi_0\)-independence then sits in \(\Delta\) and in \(\omega\).

## Q2. Scale count, (3.9)-(3.11)

**The abstract implication is [conditional] and correct, with one power to
fix.** Take the placement weight to be \(\varepsilon_mL^{dm}/s\). Here
\(\varepsilon_m\) is read as the expected fraction of scale-\((K-m)\) volume
covered by R-components. Then:
- **H8:** \((\varepsilon_mL^{dm}/s)\cdot|\xi|\,Cs\,L^{(1-d)m}\eta_m=C|\xi|\,\varepsilon_mL^m\eta_m\).
  This is correct.
- **H6 quadratic term:**
  \((\varepsilon_mL^{dm}/s)\cdot\kappa C^2(s+L^d)^2L^{2(1-d)m}=C\varepsilon_m\frac{(s+L^d)^2}{s}L^{(2-d)m}\le C\varepsilon_m(s+L^{2d})L^{(2-d)m}\).
  (3.10) omits the \(L^{2d}/s\) part, which dominates for small, hub-adjacent
  components. It is still summable, since \(L\) is fixed.
- **H7 (3.11):** correct and conservative, since the \(1/s\) was dropped.

**What CMP 122 II actually contains.** It has per-cube large-field small
factors (Eq. (0.1) and the definition of \(p(g)\)), bounds on the localized
activities (Eqs. (1.68)-(1.69), p. 377), and combinatorial bounds proving that
the localized expansion converges [published]. It does **not** contain a
normalized per-placement probability for a component of size \(s\). That
requires dividing by the partition function, i.e. a local Peierls or
cluster-expansion argument. Such an argument is plausible from those
ingredients, but it is not stated. The counting hypothesis is therefore
**[conditional]**.

Bookkeeping point: the placement weights must be those of the **partially
R-modified** density at each scale. The physical bias telescopes as
\(E_{\rm phys}F-E_RF=\sum_k(\text{bias introduced at scale }k)\). That is the
form in which Balaban's bounds apply.

**Caveat carried over from Q5.** The quadratic term really needs
\(\sum_{\rm placements}\Delta_\Lambda^2\), not \((\sup\Delta)^2\) times the count.
See Q5.

## Q3. Support language, research/11 Section 2

**Verdict: Section 2 is correctly worded.** "Not established" is the right
strength.

I cannot cite a displayed formula that proves positive true-law mass outside
the template support. My evidence was OCR prose only:
- (1.75) restricts only \(V_k|_{Z\cap\Lambda^c}\) (`cmp122i.md` line 440);
- \(Z'_k\) lies in the complement of the small-field domains ((1.10), (1.73));
- the Wilson weight is positive.

The characteristic-function content of (1.71) on \(Z'_k\) cannot be read from
the OCR. **I withdraw the stronger claim \(\widehat p\not\ll\widehat q\) in my Y6
review, Section 1.** Replace it with "strongly indicated, not established". An
erratum is appended to that file.

## Q4. Flat-background exception, (6.2)-(6.3)

**The weakest exact hypotheses** for the adjoint-average cancellation, for one
fixed history \(h\), with \(Y\) the level-\(j\) link perturbation:

- **(F1) Strict locality.** For some \(N\supset\Lambda\), both fiber weights
  depend on \((W,V_c)\) only through \((W,V_c|_N)\), up to a factor independent
  of \(W\). **This fails** in Balaban's representation: polymer activities have
  unbounded support with exponential tails. That is the "localized tail" in
  (6.3).
- **(F2) Flatness.** \(V_c|_N\) is pure gauge. In the flat frame
  \(V_c|_N\equiv1\). The axial trees \(G_i\) are rooted on \(\partial\Lambda\),
  so axial fixing acts only on interior vertices and is compatible with the
  flat frame.
- **(F3) Adjoint-invariant building blocks.** In the flat frame, every factor
  of both weights is invariant under the constant conjugation
  \(S_h:W\mapsto hWh^{-1}\). This holds for:
  - traces of closed-loop holonomies inside \(N\) (Wilson and \(E/R/B\)
    activities, which are gauge invariant);
  - hard \(\chi\)-sets defined by \(\mathrm{Ad}\)-invariant quantities: plaquette
    distances \(|V(\partial p)-1|\), axial bond norms \(|\log V'(b)|\) in
    (1.101), and the background conditions in (1.75);
  - axial \(\delta_{G}\), because \(h1h^{-1}=1\); graph averaging is then
    harmless, since each slice is preserved;
  - backgrounds \(U_{k,X}\) that are covariant because the minimizer is unique
    (CMP 102);
  - the \(T''\) operations (1.72), since Haar measure and group \(\delta\) are
    covariant.

  **History labels** are preserved if every decomposition of unity uses
  \(\mathrm{Ad}\)-invariant indicator functions. The OCR cannot confirm this for
  every \(\chi\) in (1.71); check on the scan.
- **(F4) Level of \(Y\).** Take \(j=k+1\), with \(N\supset\Lambda+\) a
  \(2L\)-neighbourhood in scale-\(k\) units. Then every level-\(j\) link that
  depends on \(W\) has its support inside \(N\), and \(Y(S_hW)=\mathrm{Ad}_hY(W)\)
  by gauge covariance of (42). **Bonds crossing \(\partial N\)** must affect
  neither the weights (F1) nor these links.
- **(F5) Invariant regular set.** Reg is defined by \(\mathrm{Ad}\)-invariant
  conditions on \(Y\).

**Conclusion [proved, abstract].** Under (F1)-(F5),
\(E_p[\mathcal P(Y)\mathbf1_{\rm Reg}]=E_q[\mathcal P(Y)\mathbf1_{\rm Reg}]=0\)
for **every** \(\mathrm{Ad}\)-equivariant \(\mathcal P\) into
\(\bigoplus\mathfrak{su}(2)\). That covers all BCH orders, not only the first
moment.

**Refinement needed in (6.2)-(6.3).** The sentence "Lemma 1 leaves only the
quadratic and bad-set terms" is true only after a second use of invariance.
Lemma 1's crude remainder in the \(Y\)-chart uses \(\kappa_Y\). But \(\kappa_Y\)
contains the BCH commutators of the **later** averaging steps, which are first
order in the terminal sensitivity. So the crude bound is only first order.
Expand \(\Phi_K=\Psi(Y)\) around \(Y_0=1\) and use invariance again:
- the linear term and every color-antisymmetric (Lie-polynomial) quadratic term
  have zero mean. Invariance forces \(E[X^a_bX^c_{b'}]=C_{bb'}\delta^{ac}\), so
  \(E[[X_b,X_{b'}]]=0\).

What survives in \(M_\Lambda(V_{\rm flat})\):
- (i) color-traced symmetric quadratic forms. These are products of two
  sensitivities, genuinely second order.
- (ii) terms in which the curved configuration **outside** \(N\) enters later
  steps, for example the color trace of
  \(d^2\log|_{e^B}(X,X)\supset\frac1{12}[[B,X],X]\). Since
  \(\sum_a[[B,t_a],t_a]\propto B\neq0\), these are one sensitivity times the
  local field \(|B|\) times \(E|X|^2\).

So **(6.3) needs a companion bound on \(M_\Lambda(V_{\rm flat})\) itself.** Flat
exterior does not give \(M_\Lambda=0\).

## Q5. H6 target

**CMP 98, Propositions 3-5 alone: not sufficient.** Three things are needed. A
second-derivative estimate is not among them.

- **(a) Irregular first step: an elementary lemma, provable now [proved].**
  Let \(U,U'\) agree off a set \(S\) of fine bonds, with \(S\) disjoint from the
  central path of \(c\). Then
  \[
  \|\bar U(c)-\bar U'(c)\|\le\min\{2,\ 2\pi L^{-d}n_c(S)\},\qquad
  n_c(S)=\#\{x\in B(c_-):\Gamma_{c,x}\cap S\ne\emptyset\}.
  \]
  If \(S\) meets the central path, the bound is 2.
  *Proof.* In (42), \(U(c)\) is unchanged. Each spectral logarithm has norm at
  most \(\pi\), so each affected \(Z_x\) moves by at most \(2\pi\). Finally,
  \(\|e^{iX}-e^{iY}\|\le\|X-Y\|\) for Hermitian \(X,Y\), by Duhamel.
  \(\square\) For bonds on straight segments,
  \(n_c\le L\) and the bound is \(2\pi L^{1-d}\). For hub bonds the bound is
  order one, which accounts for the "\(+L^d\)" in (3.8).
- **(b) Background-covariant Ward identity: needed, and it changes H6
  [heuristic].** At a nontrivial regular background, the radial terms for the
  outgoing bond \(c\) and the incoming bond \(c'\) at a corner are weighted by
  \(d\log_{W_x}\circ\mathrm{Ad}_{P_x}\) and \(d\log_{W'_{x'}}\circ\mathrm{Ad}_{P'_{x'}}\).
  These differ by \(O(\text{field}\times\text{area})\) from contour to contour,
  so the telescoping of Lemma 2 is only approximate. Exact gauge invariance
  still makes the fine current covariantly divergence-free, but it now routes
  the mismatch flux along the radial trees. **Hub currents of relative size
  \(\theta\sim C\alpha_0L^2\) per level appear**, where \(\alpha_0\) is the
  regularity parameter. The per-level sup contraction becomes
  \(L^{1-d}+\theta\). With \(\alpha_0\sim\varepsilon_k\gg L^{-(d+1)}\), the
  **uniform sup form of H6 (3.8) plausibly fails** for components on hub chains.
  - What survives: hub positions are a fraction about \(L^{-d}\) per level, so
    the **placement-summed** norms keep the right scaling as long as
    \(\theta L^{d-1}\cdot L^{-d}<1\):
    \(\sum_{\rm pl}\Delta_\Lambda\lesssim C s\,L^{m}\) and
    \(\sum_{\rm pl}\Delta_\Lambda^2\lesssim C s^2L^{(2-d)m}\).
  - **Recommendation:** restate R1/H6 in these placement-summed forms. They are
    exactly what (3.9)-(3.10) consume.
- **(c) Second derivatives: not needed for H6.** H6 is a Lipschitz statement.
  Integrate the first derivative along a path that stays in the regular domain.
  Propositions 3-4 (analyticity) control the linearization errors along that
  path. I infer **no** decay norm for Proposition 5 from the OCR. Whether the
  error bounds in its Eqs. (122) and (144)-(157) are in a norm compatible with
  kernel decay must be read on the scan.

## Q6. Manuscript wording

- **Line 500:** `\cite{Balaban1985Averaging}` supports the template's hard
  cutoff. That is the wrong paper: it should be
  `\cite[Eqs.~(1.100)--(1.101)]{Balaban1989LargeI}`.
- **Lines 486-490:** "closed-loop currents are divergence-free ... uniform bound
  \(L^{-3m}\)". Add "at the trivial background only". At curved regular
  backgrounds, curvature-induced hub currents appear (Q5b).
- **Lines 494-497:** "a terminal oscillation bound through the first irregular
  level and curved backgrounds". Add "placement-summed".
- **Line 466:** the mutual absolute continuity statement is correctly
  conditional ("If ... admit"). Optionally add "(not established)".
- **Abstract and Section 1:** accurate. No sentence claims a published
  observable theorem, mutual absolute continuity, or a quadratic remainder in
  fine coordinates. Lines 489-493 explicitly deny the last of these.

## Errata to my earlier notes

- `claude-y6-review.md`, Section 1: "\(\widehat p\not\ll\widehat q\)" becomes
  "strongly indicated, not established" (Q3).
- `claude-y6-review.md`, Section 3.1, and the research/10 review, Section 2:
  the component bound \(\delta_\Lambda\lesssim C(|\Lambda|+L^d)L^{(1-d)m}\)
  should be read as placement-summed, not uniform (Q5b).

-- Claude

## Q5 (continued). Audit of research/12

**Lemma 1 (conservation is preserved): [proved], correct.**
- The intertwiner direction in (2.2), \(DQ_j\Gamma_j=\Gamma_{j-1}R_j\), is
  right. Differentiate \(Q_j(g\cdot U)=R(g)\cdot Q_j(U)\) at \(g=1\). Here \(R_j\)
  is restriction to the coarse, corner, points, per CMP 98 Eq. (11).
- The proof is a one-line adjoint computation.
- It needs \(Q_j\) to be differentiable at \(U_j\). This holds off the
  holonomy set \(\{-1\}\), which has codimension 3 in \(SU(2)\).

**(3.2) and the pure-gauge extension: correct.** Conjugating by a background
gauge transformation preserves both the conserved subspace and an
\(\mathrm{Ad}\)-invariant sup norm.

**(3.3) is likely false as stated [heuristic].**
- At curvature \(\varkappa\), the weights \(d\log_{W_x}\circ\mathrm{Ad}_{P_x}\) of
  the incoming and outgoing contours at a corner differ by \(O(\varkappa)\).
- Conservation therefore cancels the radial terms only up to
  \(O(\varkappa)\|\tau\|\).
- The radial weights of the linear map are order one on the hub bonds near the
  corner (research/10, Section 7).
- So the residual is **additive**:
  \[
  \mathfrak C_j(U_j)\le L^{1-d}+C\varkappa_j ,
  \]
  not \(L^{1-d}(1+c\varkappa_j)\). No mechanism supplies an extra factor
  \(L^{1-d}\) on the hub residual.

**(3.4) and Lemma 2: [proved], correct as implications, but the sup norm is the
wrong norm.**
- With \(\theta_j=L^{1-d}+C\varkappa_j\), the condition \(L^d\theta^2<1\) needs
  \(\varkappa_j\lesssim L^{-2}\). That fails on the finitely many coarse levels
  near the terminal scale. Those levels cost only an \(n\)-independent constant
  \(\prod_{j\le J}\theta_j\), so the criterion is needed only **eventually**, not
  uniformly.
- **Better:** use conserved-current \(\ell^2\) and \(\ell^1\) norms, because they
  are exactly what the placement sums consume.
  - Quadratic term. With \(\Delta_\Lambda\le2s^{1/2}\|\tau^{(m)}|_\Lambda\|_2\),
    \[
    \sum_{\rm placements}\Delta_\Lambda^2\le4s^2\|\tau^{(m)}\|_2^2,\qquad
    \|P_j\tau\|_2^2\le\bigl(L^{2-d}+C\varkappa_j^2\bigr)\|\tau\|_2^2 .
    \]
    Hub residuals occupy \(O(1)\) bonds per block, a fraction \(L^{-d}\). The
    quadratic contribution is then
    \(C\varepsilon_ms\prod_j(L^{2-d}+C\varkappa_j^2)\). The criterion becomes
    \(L^{2-d}+C\varkappa_j^2<1\), which **any small curvature satisfies**, rather
    than \(\varkappa\lesssim L^{-2}\).
  - H8 term: \(\|P_j\tau\|_1\le(L+C\varkappa_j)\|\tau\|_1\), giving
    \(\varepsilon_m\prod_j(L+C\varkappa_j)\,\eta_m\). This is essentially the
    powers of research/11.
- Recommendation: restate H6-local as \(\ell^2\) and \(\ell^1\) conserved-current
  contraction bounds, with the additive curvature residual.

**Lemma 3 (one rough step): [proved], correct as an implication.** One caveat on
(5.1): near holonomies equal to \(-1\), the derivative of the spectral
logarithm is unbounded. The regular event must keep contour holonomies a fixed
distance from \(-1\), so that a path with bounded \(\int\|\dot Q_1\|_1\) exists.
The codimension-3 set can be avoided, but the bound needs this margin. Codex
already places the path construction in the definition of Reg, and I agree.

**"CMP 98 Proposition 5 is strictly weaker than H6-local": not the right
relation.**
- Proposition 5 bounds the derivative on **all** directions. H6-local asserts
  decay on the **conserved** subspace. Neither implies the other.
- If the scan shows that (156) compares the nonlinear and linear functional
  derivatives with relative error \(\alpha_0+C|A|\) in a kernel norm, then
  Proposition 5 together with Lemma 1 and research/10's flat lemma yields
  exactly the additive form \(\mathfrak C_j\le L^{1-d}+O(\alpha_0)\).
- **Answer.** The Ward/conservation structure is algebraic (Lemma 1). The new
  theorem is the quantitative curvature residual of the radial kernel on
  conserved currents. Proposition 5 may supply its analytic input, and the scan
  decides. Suggested wording: "Proposition 5 does not state H6-local, and the
  two are logically incomparable."

**Scale counts (4.3)-(4.4): correct arithmetic.** They reduce to research/11 at
\(\theta=L^{1-d}\).
