# R0 route (a): a source-dependent R step for one large-field component

Author: Claude, 2026-09-27, answering `CODEX_TO_CLAUDE_NEXT.md`.

Status: formula dictionary and a proved one-component lemma. Every
Yang--Mills input that the lemma does not supply is marked **(Y1)-(Y6)**.

Sources: the OCR text in `/private/tmp/balaban_audit/`: `cmp122i.md` (CMP 122
I), `cmp122ii.md` (CMP 122 II) and `cmp98.md` (CMP 98). The `.real.pdf` files
there are paywall HTML pages, not scans. The OCR drops or garbles most
displayed equations, so every formula below marked *reconstructed* comes from
the surrounding prose and must be checked against a scan.

## 0. Answers in brief

1. **The prototype formula (0.3)** replaces each large-field term by its
   small-field counterpart, multiplied by a ratio of *global* integrals. The
   construction Balaban actually carries out (Sect. 1, Eqs. (1.71)-(1.101)) is
   different: it acts per term and per component, as a *fiberwise* replacement.
   It integrates out \(V_k|_\Lambda\) with \(V_k|_{\Lambda^c}\) fixed, then
   reinserts a normalized, localized small-field factor. I infer from the
   normalization property that this preserves every fiber integral, and hence
   the \(V_k|_{\Lambda^c}\)-marginal of each term. That is stronger than the
   total-integral statement Balaban makes (Section 1).
2. **Sourced numerator and denominator.** With \(F_k=f\circ Q_{k,K}\), both are
   fiber integrals weighted by \(e^{zF_k}\) (Section 2.3). The source passes
   exactly through \(T\), through every gauge-fixing identity, and through the
   reversed Faddeev-Popov step.
3. **Linearity and denominators.** The sourced fiberwise step can be linear in
   the sourced term for a fixed small-field model. Its denominators are nonzero
   whenever \(|z|\operatorname{osc}f<\log2\), with no sensitivity estimate
   needed. It is analytic in \(z\), but in general **not** analytic in the
   outside fields (Section 3).
4. **Sensitivity.** The \(L^{-3(K-k)}\) bound I proposed in the referee report is
   **wrong as a uniform bound**. Averaging (42) runs contours out of the block
   centres. Already in the linearization, some bonds near each centre carry a
   one-step weight of at least about \(1/(2d)\). For irregular configurations
   CMP 98 gives no bound beyond one step. Loop length enters only through
   support and counting (Section 4).
5. **Lemma R0.1** (Section 5) is proved. It needs inputs (Y1)-(Y6).
6. **The reversed Faddeev-Popov step** (CMP 122 II, p. 378) needs no separate
   sourced construction, because \(F_k\) is invariant under every scale-\(k\)
   gauge transformation (Section 6).

**Bottom line.** Route (a) is exact at every step, and its analyticity domain in
\(z\) is independent of the cutoff. It does not by itself give bounds uniform in
\(n\). Each replaced component contributes a factor
\(\rho_z=1+z\,(E_t-E_q)[F_k]+O(z^2\delta^2)\). Crude bounds on the sum of these
first-order biases over the extensively many fine-scale components diverge.
Route (b) faces the same quantity in additive form. The open problem common to
both routes is a cancellation estimate for these biases, (Y6).

## 1. The R formula in CMP 122 I

### 1.1 Prototype (introduction, printed pp. 176-177)

The OCR keeps the prose and drops displays (0.2), (0.3), (0.5) and (0.6)
(`cmp122i.md` lines 36-44). *Reconstructed* from the prose:

- (0.2) \(\rho(V)=\sum_Z\rho(Z,V)\), a sum over large-field regions \(Z\).
- Split \(Z=Z'\cup Z''\). \(Z''\) consists of the components whose small factors
  still control the next steps. \(Z'\) consists of the components that need
  renormalization.
- (0.3)
  \[
  (R\rho)(V)=\sum_Z\rho(Z'',V)\,
  \frac{\int dV'\,\rho(Z,V')}{\int dV'\,\rho(Z'',V')}.
  \]
  The prose says the denominators are positive because the densities are
  positive and the domains nonempty. This gives (0.4),
  \(\int R\rho=\int\rho\).
- (0.5)-(0.6): sum over \(Z'\) at fixed \(Z''\), then write the sum of quotients
  as the exponential of a polymer sum over sets \(X\) disjoint from \(Z''\).

Here **every** field variable is integrated and nothing is held fixed. The
ratio is a number, so (0.3) preserves only the total integral.

**Localized-denominator caveat** (p. 177, line 44). In the actual procedure the
denominators are integrals of *parts* of the densities, localized in
neighbourhoods of \(Z'\). Those parts do not depend on \(Z''\) and are built
from small-field effective actions only.

### 1.2 What the actual construction integrates and holds fixed

- **Components.** \(Z\) is the union of large-field components satisfying (i),
  each contained in a cube of size \(100MR_k\), and (ii), no new large fields
  created inside during the preceding \(N\) steps (lines 58-60).
- **Integration domain** (1.73): \(\Lambda=(\Omega^{c}_{k_0+4+1})\cap Z\). This is
  \(Z'_k\) plus one layer of \(M\)-cubes, a rectangular parallelepiped
  (line 430).
- **Restriction outside \(\Lambda\)** (1.75). A partition of unity
  \(1=\chi_{k,\Lambda}+(1-\chi_{k,\Lambda})\) constrains only
  \(V_k|_{Z\cap\Lambda^c}\), forcing a regular extension into \(\Lambda\). The
  \(1-\chi\) part is large-field and is excluded (lines 438-452). The regular
  extension is built by a generalized axial gauge on \(\partial^+\Lambda\), with
  links inside \(\Lambda\) set to \(1\), followed by the inverse gauge
  transformation. I denote it \(W_0(V_{\Lambda^c})\).
- **First equivalence** (p. 194, lines 454-458). Each term is integrated over
  \(V_k|_\Lambda\). The result is regarded as a function of all of \(V_k\),
  independent of \(V_k|_\Lambda\). \(\Lambda\) differs from term to term. In
  (1.76) all \(\delta\)-functions inside \(\Lambda\) are integrated out, so the
  finer fields in the preimage of \(\Lambda\) become free variables.
  \(V_k|_{\Lambda^c}\) is held fixed.
- **Reinsertion with localized denominators** (1.99)-(1.101), lines 632-648
  (*reconstructed*; the OCR of (1.100) is garbled). For each component \(X_i\)
  with domain \(\Lambda_i\), the fiber-integrated large-field expression is
  multiplied by a quotient. Its numerator is a small-field factor
  \(\exp[-g_k^{-2}A(\zeta_i,U_{k,X_i}(V_k))]\) at the current field. Its
  denominator is the integral of the same factor over
  \(V'_k|_{\Lambda_i}\), including the axial-gauge \(\delta_{G_i}\) and
  \(\chi(\Lambda_i)\) of (1.101), averaged over the \(2^dd!\) coordinate
  reflections and permutations. Here \(\zeta_i\) interpolates from 0 to 1 near
  \(\partial X_i\), and \(U_{k,X_i}\) is the background of (1.74) and (1.79).
  Balaban states a normalization property for the result, and says its changes
  decay exponentially away from the region (line 648).

### 1.3 Why this is a fiberwise replacement (inference)

Write \(V=(W,V_c)\) with \(W=V_k|_{\Lambda}\) and \(V_c=V_k|_{\Lambda^c}\). Let
\(dW\) be normalized Haar measure, as CMP 98 Eq. (10) uses. For a term \(t\),
the first equivalence gives \(\tilde t(V_c)=\int dW\,t(W,V_c)\). The reinsertion
gives \(q(W,V_c)\,\tilde t(V_c)/D(V_c)\). If \(\int R'\rho=\int\rho\) is to hold
for every density, then \(\int dW\,q(W,V_c)=D(V_c)\) for every \(V_c\). So the
denominator must be the fiber integral of the reinserted factor, with the
outside field fixed. Then, for every \(H\) that depends on \(V_c\) only,
\[
\int dV\,H(V_c)\,(R't)(V)=\int dV_c\,H(V_c)\,\tilde t(V_c)=\int dV\,H\,t .
\]
**Conclusion (conditional on (Y1)).** R' preserves the
\(V_k|_{\Lambda^c}\)-marginal of each term. It replaces the conditional law of
\(V_k|_\Lambda\) given \(V_k|_{\Lambda^c}\) by the normalized model \(q\). A
terminal source is affected only through its dependence on \(V_k|_\Lambda\).

## 2. Inserting the terminal source \(F_k=f\circ Q_{k,K}\)

### 2.1 Where the source passes exactly

- **Through \(T\).** \(T\) is the pushforward under the deterministic average
  (referee report, Section 3).
- **Through every change of variables and gauge fixing** that Balaban calls a
  preserved representation (line 454). \(F_k\) is a fixed function of \(V_k\),
  and it is invariant under all scale-\(k\) gauge transformations: \(Q_{k,K}\)
  is gauge covariant (CMP 98 Eq. (11) and the text after (43)), and \(f\)
  depends on traces of closed-loop holonomies.
- **Through the reversed Faddeev-Popov step** (Section 6).
- **Not through the first equivalence** (Section 1.3), unless the construction
  itself is sourced.

### 2.2 Sourced prototype

\[
(R_z\rho)(V)=\sum_Z\rho(Z'',V)\,
\frac{\int dV'\,\rho(Z,V')\,e^{zF_k(V')}}{\int dV'\,\rho(Z'',V')\,e^{zF_k(V')}} .
\]
This preserves \(\int\rho\,e^{zF_k}\) exactly. Because \(F_k\) is nonlocal, the
sourced quotients depend on \(Z''\) through \(F_k\), and the localization in
(0.5) (sets \(X\) disjoint from \(Z''\)) fails as stated.

### 2.3 Sourced fiberwise step (the one to use)

For one component with domain \(\Lambda\), term \(t\) and model \(q\):
\[
N_z(V_c)=\int dW\,t(W,V_c)\,e^{zF_k(W,V_c)},\qquad
D_z(V_c)=\int dW\,q(W,V_c)\,e^{zF_k(W,V_c)},
\]
\[
(R'_zt)(W,V_c)=q(W,V_c)\,\frac{N_z(V_c)}{D_z(V_c)} .
\]
Then \(\int dW\,(R'_zt)\,e^{zF_k}=N_z\) on every fiber. The sourced density after
the step is \(q\,e^{zF_k}N_z/D_z\).

### 2.4 Several components: the source breaks factorization

Balaban factorizes the integrations over the components \(X_1,\dots,X_n\) (line
632). With a terminal source, \(e^{zF_k(W_1,\dots,W_n,V_{\rm rest})}\) couples
the components, so the joint fiber integral does not factorize. Two exact
options:

- apply Section 2.3 one component at a time, in a fixed order; or
- use the joint fiber over \(\bigcup_i\Lambda_i\).

The part that fails to factorize is controlled by mixed second differences
\(F_k(W_i,W_j,\cdot)-F_k(W_i,W^0_j,\cdot)-F_k(W^0_i,W_j,\cdot)+F_k(W^0_i,W^0_j,\cdot)\).
These vanish unless some terminal bond's support meets both \(\Lambda_i\) and
\(\Lambda_j\). See (Y5).

## 3. Linearity, denominators, analyticity

- **Linearity.** \(R'_z\) is linear in the sourced term
  \(\sigma=t\,e^{zF_k}\), because \(\sigma\mapsto q\,e^{zF_k}\int_\Lambda\sigma\,/\,D_z\).
  Its only nonlinearity is the dependence of the model \(q\) on the density's
  own small-field representation, which the unsourced R already has. The
  prototype (2.2) is nonlinear (homogeneous of degree 1), because its
  denominator contains \(\rho(Z'')\).
- **Nonvanishing.** Suppose \(q\ge0\) and \(D_0(V_c)>0\) (Balaban asserts
  positivity and nonempty domains, p. 176, line 40). Put
  \(\delta(V_c)=\operatorname{osc}_WF_k(W,V_c)\). If \(|z|\delta<\log2\), then
  \(D_z\ne0\), and
  \(|D_z|\ge(2-e^{|z|\delta})\,e^{\operatorname{Re}(z)F_k(W_*,V_c)}D_0\) for any
  \(W_*\). Since \(\delta\le\operatorname{osc}f\le2\lVert f\rVert_\infty\), the
  disc \(|z|<\log2/\operatorname{osc}f\) works for every component, every scale
  and every cutoff. No sensitivity estimate is needed here.
- **Analyticity in \(z\).** \(N_z\) and \(D_z\) are entire, because the
  integrands are bounded. So \(R'_zt\) is holomorphic on that disc.
- **Analyticity in the outside fields fails in general.** Take any reference
  \(W_*\) and write \(F_k=F_k(W_*,V_c)+\Delta\). The global factor cancels, and
  \(R'_zt=(R'_0t)\,\rho_z\) with
  \(\rho_z=E_t[e^{z\Delta}]/E_q[e^{z\Delta}]\). Under \(E_t\), \(W\) ranges over
  large-field configurations. For those, \(Q_{k,K}(W,V_c)\) is not covered by
  CMP 98's analyticity (Section 4.1), and the spectral logarithm in (42) jumps
  where a loop holonomy has eigenvalue \(-1\). So \(\rho_z\) is bounded but not
  analytic in \(V_c\). Using \(W_*=W_0(V_c)\), the regular extension of
  Section 1.2, keeps the global factor \(F_k(W_0(V_c),V_c)\) on regular
  configurations. Only the bounded remainder is non-analytic. See (Y4).

## 4. Sensitivity audit (CMP 98)

### 4.1 What CMP 98 proves

- **One-step average (42)** (line 243):
  \[
  \bar U(c)=\exp\Bigl(i\sum_{x\in B(c_-)}L^{-d}\,\tfrac1i\log\bigl[U(\Gamma_{c,x})\,U(c)^{-1}\bigr]\Bigr)\,U(c).
  \]
  Here \(U(c)\) is the transport along the straight central path \(c\) from
  \(c_-\) to \(c_+\). The contour is
  \(\Gamma_{c,x}=\Gamma_{c_-,x}\cup[x,x(c)]\cup\Gamma_{x(c),c_+}\) (text after
  (14), line 80), and log is the spectral logarithm of definition (22). The
  \(k\)-fold average iterates (42).
- **Locality** (line 255): \(U_k(c)\) depends only on bonds in
  \(B_k(c_-)\cup B_k(c_+)\).
- **Covariance** (11), and the verification after (43).
- **Linearization.** For \(U=e^{iA}\) with \(A\) small, the linear term is (14):
  \(\sum_{x\in B(c_-)}L^{-d}A(\Gamma_{c,x})\) (line 91).
- **Regularity and analyticity.** Compositions of averages preserve regularity,
  and \(U_k\) is analytic, on configurations satisfying the regularity condition
  (52), and (176)-(177) for Proposition 10 (lines 935 and 1167). The paper says
  the average is formally defined for all configurations, but controlled only
  on regular ones (line 935).

**Not proved in CMP 98:** any bound on how \(U_k(c)\) depends on a single fine
bond, whether a derivative or an oscillation. In particular there is nothing of
the form \(L^{-(d-1)m}\), and nothing at all for irregular configurations.

### 4.2 Linearized weights

The weights below are rigorous facts about the linear map (14); applying them to
the nonlinear average is heuristic. One step gives weight
\(w_c(b)=L^{-d}\,n_c(b)\) to bond \(b\), where \(n_c(b)\) counts the contours
\(\Gamma_{c,x}\) through \(b\), with orientation.

- **Straight segments.** A bond in direction \(\mu\) lies on at most \(L\)
  segments \([x,x+Le_\mu]\), so its weight is at most \(L^{1-d}\).
- **Radial bonds near the centres.** Every contour starts at \(c_-\). So the
  \(2d\) bonds at \(c_-\) carry all \(L^d\) radial paths between them, and at
  least one has \(|n_c(b)|\ge L^d/(2d)-L\), that is, weight about \(1/(2d)\).
  The same holds at \(c_+\).
- **Totals.** Summed over a block, the radial weights are of order \(dL\), and
  the straight-segment weights of order \(L\).

Consequences:
- The one-step weights range from \(L^{-d}\) up to order 1. No uniform
  \(L^{1-d}\) bound holds, even in the linearization.
- After \(m\) steps, a typical bond has weight around \(L^{-(d-1)m}\). The
  largest weights sit on nested hub spines and decay only like
  \((w_{\max})^m\), where \(w_{\max}\) is the largest one-step weight.
- The \(\ell^1\) norm of the composed weights can be as large as
  \((CdL)^m\). The signed sum, by contrast, is \(L^m\), as scaling requires.

### 4.3 Irregular configurations: what (42) gives rigorously

Spectral logarithms of unitaries are bounded, with eigenvalues in
\((-\pi,\pi]\). Also \(\lVert e^{iX}-e^{iY}\rVert\le\lVert X-Y\rVert\) for
hermitian \(X\) and \(Y\).

- For \(b\) **off the central path** \(c\), changing \(U_b\) arbitrarily changes
  \(\bar U(c)\) by at most \(\min\{2,\ 2\pi\,|n_c(b)|\,L^{-d}\}\).
- For \(b\) **on the central path** \(c\), the change can be of order 1. The
  first-order cancellation that holds for small fields fails once the loops are
  not small.

This bound holds for **every** configuration, but only for one step. At the next
steps the logarithm can jump across the branch cut, so a small change can
produce a jump of size \(2\pi n L^{-d}\), and no decay in \(m\) follows. Decay in
\(m\) needs the intermediate configurations along the propagation to be regular,
and then CMP 98's regular-domain control applies.

### 4.4 Loop length and support

- **Support.** \(F_k\) depends only on scale-\(k\) bonds in \(S(C)\), the pullback
  of \(\bigcup_j\bigcup_{b'\in C_j}\bigl(B_K(b'_-)\cup B_K(b'_+)\bigr)\), by
  iterated locality. A component contributes \(\delta_\Lambda=0\) unless
  \(\Lambda\cap S(C)\neq\emptyset\).
- **Loop length.** \(|\delta\operatorname{Tr}\mathrm{Hol}_C|\le N\sum_{b'\in C}\lVert\delta V_K(b')\rVert\),
  so the effect per affected terminal bond does not depend on \(|C|\). A small
  component affects \(O(1)\) terminal bonds. Loop length enters only through the
  number of components that matter, which is of order
  \(\sum_j|C_j|\,L^{4m}\) at scale \(K-m\).
- **Position.** \(\delta_\Lambda\) depends on where \(\Lambda\) sits relative to
  the nested block centres and central paths (Sections 4.2-4.3), and on whether
  the configurations along the propagation are regular.

### 4.5 Consequence

At scale \(K-m\) the number of R-components per unit volume is of order
\(e^{-p(g_{K-m})}\), with \(p\) polylogarithmic in \(g^{-2}\approx bm\) (CMP 122
I, Eq. (0.1)). Even the generic-position sum
\(\sum_\Lambda\delta_\Lambda\gtrsim L^{m}e^{-p}\) diverges as \(m\to\infty\).
Counting the hub bonds and the \(\ell^1\) weights makes it worse. So summing
\(|\log\rho_z|\le2|z|\delta_\Lambda(1+o(1))\) over components gives no bound
uniform in \(n\). Uniform control would need the first-order biases
\(B_\Lambda=(E_t-E_q)[F_k\mid V_c]\) to be much smaller than \(\delta_\Lambda\).
For example, bounds of second order in the sensitivity would make the generic
sum summable, of order \(L^{-2m}\). That in turn needs a symmetry or cancellation
property of the large-field conditional law relative to the small-field model.
Balaban proves no such property.

## 5. One-component lemma

**Lemma R0.1.** Let \((\Omega_\Lambda,dW)\) and \((\Omega_c,dV_c)\) be
probability spaces, and \(\Omega=\Omega_\Lambda\times\Omega_c\). Let
\(t,q:\Omega\to[0,\infty)\) be measurable with \(\int t<\infty\), and suppose
\(D_0(V_c)=\int q(W,V_c)\,dW\in(0,\infty)\) for every \(V_c\). Let \(F\) be
bounded, measurable and real. Put \(\delta(V_c)=\operatorname{osc}_WF(\cdot,V_c)\)
and \(\bar\delta=\sup\delta\). Define \(N_z\), \(D_z\) and \(R'_z\) as in
Section 2.3, with \(F\) in place of \(F_k\). Then for \(|z|\bar\delta<\log2\):

1. \(D_z(V_c)\neq0\), with the lower bound of Section 3.
2. **Fiberwise exactness.** \(\int(R'_zt)(W,V_c)\,e^{zF(W,V_c)}\,dW=N_z(V_c)\) for
   every \(V_c\). Hence \(\int(R'_zt)\,e^{zF}H=\int t\,e^{zF}H\) for every bounded
   \(H=H(V_c)\).
3. **Factorization.** On \(\{N_0>0\}\), \(R'_zt=(R'_0t)\,\rho_z\) with
   \(\rho_z=E_t[e^{zF}]/E_q[e^{zF}]\). Here \(E_t\) and \(E_q\) are the normalized
   fiber expectations. \(\rho_z\) is holomorphic in \(z\), and
   \[
   |\rho_z-1|\le\frac{2(e^{|z|\delta}-1)}{2-e^{|z|\delta}},\qquad
   |\log\rho_z|\le2\log\frac1{2-e^{|z|\delta}} .
   \]
4. **First order.** \(\rho_z=1+z\,(E_t[F]-E_q[F])+r_z\), with
   \(|r_z|\le C|z|^2\delta^2\) for \(|z|\delta\le\tfrac12\), where \(C\) is an
   absolute constant.
5. **Error of the unsourced step.** For bounded \(H=H(V_c)\):
   \[
   \Bigl|\int(R'_0t-t)\,e^{zF}H\Bigr|\le\lVert H\rVert_\infty\,|z|\,\bar\delta\,e^{|z|\lVert F\rVert_\infty}\int t,
   \qquad
   \Bigl|\int(R'_0t-t)\,F\,H\Bigr|\le\lVert H\rVert_\infty\,\bar\delta\int t .
   \]

*Proof.* (1) Put \(\Delta=F-F(W_*,\cdot)\), so \(|\Delta|\le\delta\). Then
\(\int q\,e^{z\Delta}=D_0(1+u)\) with \(|u|\le e^{|z|\delta}-1<1\).

(2) By the definition,
\(\int dW\,q\,e^{zF}\cdot N_z/D_z=D_z\cdot N_z/D_z=N_z\). Then integrate against
\(H(V_c)\,dV_c\).

(3) \(N_z/N_0=e^{zF(W_*)}E_t[e^{z\Delta}]\) and
\(D_z/D_0=e^{zF(W_*)}E_q[e^{z\Delta}]\). Both expectations lie in
\(\overline{B(1,\eta)}\) with \(\eta=e^{|z|\delta}-1\). This gives
\(|a/b-1|\le|a-b|/|b|\le2\eta/(1-\eta)\). For the logarithm, each principal
logarithm is at most \(-\log(1-\eta)\) in modulus, and the imaginary parts stay
below \(\pi\).

(4) Use \(|e^w-1-w|\le\tfrac12|w|^2e^{|w|}\) in numerator and denominator. The
constant \(F(W_*)\) cancels in \(E_t[\Delta]-E_q[\Delta]\).

(5) The difference equals
\(\int H\,N_0\,\bigl(E_q[e^{zF}]-E_t[e^{zF}]\bigr)\,dV_c\), and
\(|e^{zF(W)}-e^{zF(W')}|\le|z|\,\delta\,e^{|z|\lVert F\rVert_\infty}\). The
\(z\)-derivative at \(0\) is the same computation with \(F\). \(\square\)

**Yang--Mills inputs needed to use R0.1 inside the \(E/R/B\) induction** (none
proved here):

- **(Y1) Identification.** Balaban's (1.100) is \(R'_0\) with
  \(\Lambda=\Lambda_i\), \(t\) the localized large-field expression, and \(q\) the
  localized small-field factor of Section 1.2. In particular, the denominator is
  the fiber integral with \(V_k|_{\Lambda_i^c}\) fixed. This is inferred from the
  normalization property; check it on the scan.
- **(Y2) Positivity.** \(q\ge0\) and \(D_0>0\) on the support. Balaban asserts
  this (p. 176).
- **(Y3) Sensitivity.** A bound on \(\bar\delta_\Lambda\) for
  \(F_k=f\circ Q_{k,K}\) that holds over large-field \(W\). CMP 98 does not
  supply one (Sections 4.1-4.3).
- **(Y4) Non-analytic factors.** The later \(E/R/B\) steps must accept the bounded,
  localized, non-analytic factors \(\rho_z=1+O(|z|\bar\delta_\Lambda)\), in the
  same way they carry the \(\chi\)-functions.
- **(Y5) Several components.** A bound on the order dependence, or joint-fiber
  error, through the mixed second differences of Section 2.4.
- **(Y6) Summability.** Uniformly in \(n\), control over all R-components and
  all scales of \(\sum|B_\Lambda|\), or of
  \(\sum|\log\rho_z|\). Crude bounds diverge (Section 4.5). **This is the main
  obstruction, and it is common to routes (a) and (b).**

## 6. Reversed Faddeev-Popov step (CMP 122 II, printed p. 378)

The text is at `cmp122ii.md` lines 481-491. For the first-class, small-field
components \(X_i\), the gauge-fixing \(\delta_{G_i}(V'_k)\) are removed by a
reversed Faddeev-Popov procedure. This is valid because the characteristic
functions and the effective action are gauge invariant. The result is again
"equivalent, but not equal", in the sense of (1.99) [IV]. The step is the
identity
\[
\int dV\,\delta_{G}(V)\,\Phi(V)\,H(V)=\int dV\,\Phi(V)\,H(V)
\]
for \(\Phi\) and \(H\) invariant under the gauge transformations supported on
\(X_i\) (axial tree gauge, normalized Haar measure). With \(H=e^{zF_k}\) it holds
unchanged, since \(F_k\) is invariant under **all** scale-\(k\) gauge
transformations (Section 2.1).

**Verdict:** no separate sourced construction is needed. The only requirement is
that the source stay exactly gauge invariant. A gauge-fixed or non-invariant
test function would break this step.

## 7. Corrections to my referee report

- **Section 1.4 of the report.** The per-link sensitivity \(L^{-3(K-k)}\) holds
  only for generic positions. It is not a uniform bound (Section 4.2 here). The
  claim that route (a) "looks more promising" is withdrawn. Route (a) is exact
  and has a cutoff-independent \(z\)-disc. Uniform-in-\(n\) control, however,
  runs into the same summability problem (Y6) as route (b).
- **Sections 1.1-1.2 of the report.** Balaban asserts only equality of total
  integrals. The fiberwise structure (Section 1.3 here, conditional on (Y1))
  shows that each first-type step preserves the \(V_k|_{\Lambda^c}\)-marginal of
  each term. The toy model in Section 1.2 of the report is exactly this
  mechanism, and the classification table is unchanged.

## 8. Suggested next steps

1. Check (Y1) on a scan of CMP 122 I, pp. 194 and 200-201, Eqs. (1.99)-(1.101):
   is the denominator the fiber integral with the outside field fixed?
2. Attack (Y6) directly. Can the first-order bias \((E_t-E_q)[F_k\mid V_c]\) be
   shown to be of second order in the sensitivity, for example through a
   reflection symmetry of the fluctuation law about the background \(U_0\) of
   (1.79), up to \(O(g)\) corrections? If not, M1 needs a different observable
   class, or an RG whose large-field step preserves the terminal law exactly.
3. Before any further quantitative work, sharpen (Y3) for Balaban's actual
   contour choice in CMP 96 [2]. That means the precise radial-tree weights and
   the hub-spine sets.
