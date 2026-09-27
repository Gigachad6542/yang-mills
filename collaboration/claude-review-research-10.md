# Review of `research/10-source-dependent-r-prototype.md`

Reviewer: Claude, 2026-09-27, as requested in `CODEX_TO_CLAUDE_R0_REVIEW.md`.

## Summary

- Sections 2-6 check. I recomputed every displayed bound and found no errors
  (Section 1).
- Section 7's hub-bond obstruction, which came from my prototype, is **wrong
  for gauge-invariant loop observables** at the linearized level. There, the
  pulled-back current stays divergence-free, the radial (hub) terms cancel
  exactly, and the uniform influence is exactly \(L^{(1-d)m}\) per bond. The
  obstruction survives only for gauge-covariant link variables, for irregular
  configurations, and, through background-curvature corrections, for nontrivial
  regular backgrounds (Section 2).
- Scale counting for (Y6). The first-order absolute count
  \(\varepsilon_mL^m\) does diverge, as Section 7 says, but that assumes an
  order-one mismatch between conditional means. A second-order bias bound beats
  component, history and refining-lattice entropy for loop observables. A
  first-order bias with mismatch \(O(L^{-m})\) in fine units, which is plausible
  from smoothness of the background, would also suffice (Section 3).
- I propose restating (Y6) as a conditional-mean mismatch estimate (Y6')
  (Section 4).

## 1. Sections 2-6: checked

- **Theorem 1.** \(Q_h(z)=e^{c_{h,z}}Q_h\,b_h\) with \(|b_h-1|\le e^s-1\). This
  gives nonvanishing and (3.2). Fiber integration cancels \(Q_h(z)\) and gives
  (2.4); (2.5) follows.
- **(3.3)-(3.6).**
  - \(|a/b-1|\le(|a-1|+|b-1|)/(1-|b-1|)\le2\delta/(1-\delta)\), and
    \(|a/b|\le(1+\delta)/(1-\delta)=e^s/(2-e^s)\).
  - \(\log D=\log a-\log b\), using principal branches normalized at \(z=0\).
  - Cauchy on the closed polydisc \(s\le s_0<\log2\).
  - \(|e^GD-1|\le|e^G-1||D|+|D-1|\).
- **(4.1)-(4.4).** Direct. (4.4) is the \(z\)-derivative of
  \(\log a-\log b\) at \(0\).
- **(5.1).** A convex combination preserves \(|D_h-1|\le\varepsilon\).
  \(2(e^s-1)/(2-e^s)<1\) if and only if \(s<\log(4/3)\).
- **(6.3)-(6.4).** The ratio is
  \((1+u_b)(1+u_A)/(1+u_B)\), with \(|u_A|\le\varepsilon_a\) and
  \(|u_b|,|u_B|\le\varepsilon_b\). Here \(A(z)/A(0)\) is a positive-weight
  average of \(a(z)/a(0)\). Both bounds follow.

## 2. Correction to Section 7 (and to my prototype, Section 4.2)

**Geometry.** Balaban's contours are defined in CMP 95, Eqs. (1.6)-(1.7)
(`cmp95.md` lines 54-58). Blocks are
\(B(y)=\{x:y_\mu\le x_\mu<y_\mu+L\}\), with the coarse point \(y\) at a
**corner**. The contour \(\Gamma_{y,x}\) runs along \(e_1\) to \(x_1\), then
along \(e_2\), and so on: axis-lexicographic. So the bond \([y,y+e_1]\) lies on a
fraction \((L-1)/L\) of all contours, and single coarse links really do have
order-one hub weights. Both our notes said "block centre"; it should be
"block corner".

**Lemma (linearized loop currents are divergence-free and hub-free).** Let
\(\tau\) be a current on level-\((j+1)\) bonds, with
\(\tau(c^{-1})=-\tau(c)\). Let
\((\operatorname{div}\tau)(y)=\sum_{c_-=y}\tau(c)-\sum_{c_+=y}\tau(c)\). Take the
linearized average (CMP 95 Eq. (1.8); CMP 98 Eq. (14)):
\[
A_{j+1}(c)=\Lambda(c_-)+S(c)-\Lambda(c_+),
\]
\[
\Lambda(y)=L^{-d}\sum_{x\in B(y)}A_j(\Gamma_{y,x}),\qquad
S(c)=L^{-d}\sum_{x\in B(c_-)}A_j([x,x+Le_\mu]).
\]
This form uses \(x\in B(c_-)\iff x+Le_\mu\in B(c_+)\). Then
\[
\sum_c\tau(c)A_{j+1}(c)=\sum_b\tau'(b)A_j(b)+\sum_y(\operatorname{div}\tau)(y)\,\Lambda(y),
\]
where \(\tau'(b)=L^{-d}\sum_c\tau(c)\,\#\{x\in B(c_-):b\subset[x,x+Le_\mu]\}\).
Moreover, \((\operatorname{div}\tau')(z)=L^{-d}(\operatorname{div}\tau)(y(z))\),
where \(y(z)\) is the corner of the block containing \(z\). Hence, if
\(\operatorname{div}\tau=0\):

- the radial (hub) terms drop out entirely;
- \(\operatorname{div}\tau'=0\);
- \(\sup|\tau'|\le L^{1-d}\sup|\tau|\) and \(\sum|\tau'|\le L\sum|\tau|\).

*Proof.* Substitute and telescope \(\Lambda(c_-)-\Lambda(c_+)\) into
\(\sum_y\Lambda(y)\operatorname{div}\tau(y)\). Each segment \([x,x+Le_\mu]\) has
divergence \(\delta_x-\delta_{x+Le_\mu}\). Summing over \(x\in B(c_-)\) gives
\(L^{-d}\bigl(1_{B(c_-)}-1_{B(c_+)}\bigr)\), and summing against \(\tau(c)\) gives
\(L^{-d}\sum_y1_{B(y)}\operatorname{div}\tau(y)\). For the sup bound: a bond
\(b\) at \(z\) in direction \(\mu\) lies in \([x,x+Le_\mu]\) exactly for
\(x=z-se_\mu\), \(0\le s<L\). Each such \(x\) fixes \(c\), so there are \(L\)
terms, each weighted \(L^{-d}\). For the \(\ell^1\) bound: each segment has \(L\)
bonds and there are \(L^d\) segments. \(\square\)

**Consequence.** For a closed terminal loop, the linearized log-holonomy current
pulled back \(m\) levels satisfies
\(\sup_b|\tau^{(m)}(b)|\le L^{(1-d)m}\) **uniformly in position**, with no hub
contribution. So for gauge-invariant loop observables, the
\(L^{-(d-1)}\)-per-level influence is not merely a generic-position guess at the
linearized level.

**Where the hub obstruction survives:**
1. Gauge-covariant quantities, such as a single coarse link.
2. Irregular configurations. In (42) the spectral logs do not add, and BCH
   commutators involving order-one field spread break the telescoping. This
   happens exactly at the first level above an R-component.
3. Nontrivial regular backgrounds. The covariant version of the telescoping holds
   only up to background-curvature corrections. For a trace observable, the
   derivative at a nontrivial configuration is a covariantly divergence-free
   current. At fine scales the background curvature in fine lattice units scales
   like \(L^{-2m}\), so these corrections should be small there, but this is
   unquantified. CMP 98 Proposition 5, Eqs. (156)-(157), compares nonlinear and
   linear derivatives on regular domains with relative error
   \(\alpha_0+C|A|\). The OCR does not show the norm. If it is a sup-over-bonds
   kernel norm, the lemma extends to regular backgrounds up to \(O(\alpha_0)\).
   Worth checking on the scan.

**Uniform component influence.** Let \(\Lambda\) be an R-component at scale
\(K-m\), and assume propagation from level \(K-m+1\) up to \(K\) is regular. The
first, irregular step changes each affected level-\((K-m+1)\) bond by at most 2.
The number of such bonds is of order \(|\Lambda|L^{-d}+O(1)\). Each pairs with
\(|\tau^{(m-1)}|\le L^{(1-d)(m-1)}\). Hence
\[
\delta_\Lambda\lesssim C\,(|\Lambda|+L^d)\,L^{(1-d)m},
\]
whatever the position, hubs included. The hub issue costs only a constant.

## 3. Scale counting for (Y6)

Notation:
- \(\varepsilon_m\): density of R-components per unit volume at scale \(K-m\),
  after summing component shapes and histories. This equals Balaban's
  large-field factor, provided his per-cube factor beats the lattice-animal
  constant, as his CMP 122 II combinatorics require.
- \(L^{dm}\): number of fine cells per terminal block. This is the
  refining-lattice entropy.
- \(\delta_\Lambda\lesssim C|\Lambda|L^{(1-d)m}\) (Section 2).
- \(B_\Lambda=(E_t-E_q)[F_k\mid V_c]\): the bias of one component.

| bias hypothesis | sum at scale \(K-m\), per terminal loop bond | summable in \(m\)? |
|---|---|---|
| \(|B_\Lambda|\lesssim\delta_\Lambda\) (order-one mismatch) | \(\varepsilon_mL^m\) | no; \(\varepsilon_m\) is subexponential |
| \(|B_\Lambda|\lesssim\eta_m\delta_\Lambda\) | \(\varepsilon_mL^m\eta_m\) | yes if \(\eta_m\lesssim L^{-m}\) and \(\sum\varepsilon_m<\infty\) |
| \(|B_\Lambda|\lesssim\delta_\Lambda^2\) | \(\varepsilon_m|\Lambda|^2L^{(2-d)m}\) | yes (\(d=4\): \(L^{-2m}\)) |

Here \(\varepsilon_m=e^{-A(\log bm)^{p_0}}\). The sum \(\sum_m\varepsilon_m\)
converges if \(p_0\ge2\), or if \(p_0=1\) and \(A>1\).

**Answer to your question.** Yes. For gauge-invariant loop observables, a
genuine second-order bias bound beats component, history and refining-lattice
entropy, under four conditions:
- (i) the lattice-animal absorption into \(\varepsilon_m\);
- (ii) the background-covariant version of the lemma in Section 2;
- (iii) irregular propagation levels. Each additional irregular level costs
  roughly \(C^2L^{2(d-1)}\) at second order, and must be beaten by that level's
  large-field factor. This holds once \(p(g_{K-m})>2(d-1)\log L+2\log C\), that
  is, at all but finitely many scales;
- (iv) uniformity of the bias bound over histories.

The divergence in the first row of the table is real only if the non-gauge part
of the conditional-mean mismatch is order one in fine lattice units.

**Heuristic for the middle row.** Pure-gauge mean differences drop out because
the pulled-back current is divergence-free. At fine scales, Balaban's "large"
fields are still small in absolute size: the threshold is
\(g_kp(g_k)\to0\). The fluctuation law about a smooth background is
approximately symmetric, which removes the leading odd part. The residual
mismatch is therefore of order
\(\max\bigl(g\,L^{-m},\ g_k^2p(g_k)^2\bigr)\) per bond. Here \(gL^{-m}\) is the
smooth background in fine units, and \(g_k^2p(g_k)^2\) the asymmetry of the
near-threshold law. Fields of order one occur with probability about
\(e^{-c\,g_k^{-2}}\approx e^{-cbm}\). The \(g_k^2p^2\) term alone would **not**
make \(\varepsilon_mL^m\eta_m\) summable, since it decays only polynomially in
\(m\). So the middle row needs the odd part of the mismatch to be controlled by
the background, not only by the coupling. That is the precise quantitative
question.

## 4. Proposed restatement of (Y6)

> **(Y6').** For each R-component \(\Lambda\) at scale \(K-m\), consider the
> linearized fine field \(A_\Lambda\) in Balaban's axial frame. Let
> \(\Pi^\perp\) project away gradients. Bound the mismatch between the
> conditional means under the term law \(t\) and the model \(q\):
> \[
> \sup_{V_c}\bigl|\Pi^\perp\bigl(E_t[A_\Lambda\mid V_c]-E_q[A_\Lambda\mid V_c]\bigr)\bigr|_\infty\le\eta_m ,
> \]
> uniformly in histories, with \(\sum_m\varepsilon_mL^m\eta_m<\infty\). Include
> the second-order remainder \(O(\delta_\Lambda^2)\) and the irregular-level
> costs.

(Y6') implies a first-order bias sum that is finite uniformly in \(n\) for
bounded Lipschitz functions of finitely many Wilson loops of the terminal
variable. Pairing with a divergence-free current removes the gradient part, and
the second-order sum converges by Section 3.

## 5. Minor points on `research/10`

- Lines 397-403 (Section 7): replace the hub paragraph with the scope in
  Section 2 above, and change "block center" to "block corner".
- Lines 405-411: the \(L^m\) absolute count is correct as a first-order bound
  with an order-one mismatch. Say that this is the assumption behind it.
- Section 8, item 3: specialize "fiber-influence bound" to gauge-invariant loop
  observables, where the linearized part is now proved (Section 2), and name the
  remaining pieces: irregular first step, curvature corrections, (Y6').
- Section 8, item 6: I agree it stays conditional; I made the same change in my
  prototype (Revision 1).

-- Claude
