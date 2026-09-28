# Covariant-current reduction for terminal sensitivity

Status: **the abstract conservation and iteration lemmas are proved here.**
The flat-background contraction is the linear lemma of research note 10,
transported by gauge covariance.  The curvature-stable one-step contraction
and the first-irregular-layer path estimate isolated below are open
Yang--Mills inputs.  They are not stated in CMP **98**, Proposition 5.

## 1. Why this is the next H6 question

Research note 11 reduces the observable defect of one complete-
\(R\) fiber replacement to three quantities.  H6 is the deterministic one:
on a regular event, changing a component \(\Lambda\) at scale \(K-m\) should
move each selected gauge-invariant terminal coordinate by

\[
 \Delta_\Lambda
 \le C(|E_\Lambda|+L^d)L^{(1-d)m}.
 \tag{1.1}
\]

At the identity background, note 10 proves the factor \(L^{1-d}\) per step for
a divergence-free loop current.  CMP **98**, Proposition 5, printed p. 42,
proves that the functional derivative of the iterated average is bounded
uniformly in the lattice spacing on its regular domain.  A bounded derivative
is not (1.1): repeated order-one bounds do not yield a geometric gain.

The missing statement is best expressed for the adjoint derivative acting on
gauge-invariant currents.

## 2. Gauge covariance preserves the conserved-current subspace

Let \(\mathcal X_j\) be a smooth local chart of lattice connections at level
\(j\), and let \(\mathcal V_j\) be the corresponding vertex Lie algebra.  At a
background \(U_j\), write

\[
 \Gamma_j(U_j):\mathcal V_j\longrightarrow T_{U_j}\mathcal X_j
\]

for the infinitesimal gauge-action map.  A covector \(\tau_j\) is
**covariantly conserved** when

\[
 \Gamma_j(U_j)^*\tau_j=0.
 \tag{2.1}
\]

This is the intrinsic form of vanishing covariant divergence.

Let \(Q_j:\mathcal X_j\to\mathcal X_{j-1}\) be one gauge-covariant block map.
Its infinitesimal covariance is

\[
 DQ_j(U_j)\,\Gamma_j(U_j)
 =\Gamma_{j-1}(Q_jU_j)\,R_j,
 \tag{2.2}
\]

where \(R_j\) is the induced map on gauge parameters.  The exact form of
\(R_j\) is irrelevant for the following lemma.

### Lemma 1: adjoint derivatives preserve conservation

If \(\tau_{j-1}\) satisfies (2.1) at \(Q_jU_j\), then

\[
 \tau_j:=DQ_j(U_j)^*\tau_{j-1}
 \tag{2.3}
\]

satisfies (2.1) at \(U_j\).

#### Proof

For every \(\phi\in\mathcal V_j\),

\[
 \begin{aligned}
 \langle\tau_j,\Gamma_j(U_j)\phi\rangle
 &=\langle\tau_{j-1},DQ_j(U_j)\Gamma_j(U_j)\phi\rangle\\
 &=\langle\tau_{j-1},
   \Gamma_{j-1}(Q_jU_j)R_j\phi\rangle=0.
 \end{aligned}
\]

\(\square\)

If the terminal test is gauge invariant, its differential is conserved.
Lemma 1 therefore keeps every pulled-back differential in exactly the subspace
on which the cancellation estimate must be proved.  This part is algebraic;
it does not require a small-field expansion.

## 3. The quantitative one-step hypothesis

Equip bond covectors with the sup norm in an \(\operatorname{Ad}\)-invariant
Lie-algebra norm.  Define

\[
 \mathfrak C_j(U_j)=
 \sup_{\substack{\tau\ne0\\
       \Gamma_{j-1}(Q_jU_j)^*\tau=0}}
 \frac{\|DQ_j(U_j)^*\tau\|_\infty}{\|\tau\|_\infty}.
 \tag{3.1}
\]

The exact flat-background lemma of note 10 gives

\[
 \mathfrak C_j(1)\le L^{1-d}.
 \tag{3.2}
\]

Gauge covariance and \(\operatorname{Ad}\)-invariance of the norm extend
(3.2) to pure-gauge backgrounds, provided the local domains and boundary data
are transformed with the background.

The natural regular-background target is

\[
 \boxed{
 \mathfrak C_j(U_j)
 \le L^{1-d}(1+c\,\varkappa_j),
 }
 \tag{3.3}
\]

where \(\varkappa_j\) is a gauge-invariant curvature size on the block and its
one-layer neighborhood.  A weaker uniform bound

\[
 \mathfrak C_j(U_j)\le\theta,qquad
 L^d\theta^2<1,
 \tag{3.4}
\]

is already enough for the quadratic terminal remainder after placement
counting.  In four dimensions the flat value is \(L^{-3}\), while (3.4) only
requires \(\theta<L^{-2}\); there is a full power of margin.

Neither (3.3) nor (3.4) follows from a uniform order-one derivative bound.
They use three additional structures simultaneously: the conserved-current
restriction, the normalized contour averaging, and closeness to a pure-gauge
background measured by curvature rather than by gauge-dependent link size.

## 4. Iteration

### Lemma 2: product contraction

Let \(P_j=DQ_j(U_j)^*\).  Suppose every \(P_j\) maps conserved currents to
conserved currents and

\[
 \|P_j\tau\|_\infty
 \le \alpha(1+r_j)\|\tau\|_\infty,qquad r_j\ge0,
 \tag{4.1}
\]

on that subspace.  Then a conserved terminal covector \(\tau_0\) obeys

\[
 \|P_m\cdots P_1\tau_0\|_\infty
 \le \alpha^m
    \exp\!\left(\sum_{j=1}^m r_j\right)
    \|\tau_0\|_\infty.
 \tag{4.2}
\]

#### Proof

Apply (4.1) successively, using Lemma 1 after each step, and use
\(1+r_j\le e^{r_j}\). \(\square\)

Thus (3.3) with \(\sum_j\varkappa_j\le C\) yields the flat exponent
\(L^{(1-d)m}\) up to a constant.  If only a uniform
\(\mathfrak C_j\le\theta\) is available, the result is \(\theta^m\).

The latter is still useful.  If size-\(s\) components have total placement
weight \(O(\varepsilon_mL^{dm}/s)\), and
\(\Delta_\Lambda\le Cs\theta^m\), then the quadratic term in Lemma 1 of note
11 contributes

\[
 C\varepsilon_m s\,(L^d\theta^2)^m.
 \tag{4.3}
\]

It is geometrically summable under (3.4), after the shape weight absorbs
\(s\).  The corresponding terminal-mean condition is

\[
 |M_\Lambda|\le Cs\theta^m\eta_m,qquad
 \sum_m\varepsilon_m(L^d\theta)^m\eta_m<\infty.
 \tag{4.4}
\]

For \(\theta=L^{1-d}\), (4.3)--(4.4) reduce to the powers in note 11.

## 5. Separating the first irregular layer

The field inside a large-field component need not lie in the regular chart in
which (3.3) is meaningful.  It is enough to isolate one step.

### Lemma 3: one rough step followed by regular contraction

Let \(W(t)\), \(0\le t\le1\), join two fiber configurations on a regular event.
Assume that after the first block map the path is in the regular domain and

\[
 \int_0^1
 \left\|\frac d{dt}Q_1(W(t),V_c)\right\|_1dt
 \le C_0(s+L^d),
 \tag{5.1}
\]

where \(s=|E_\Lambda|\).  Suppose the remaining \(m-1\) adjoint derivatives
obey \(\mathfrak C_j\le\theta\), and the selected terminal coordinate is
gauge invariant and has bounded differential \(C_F\).  Then

\[
 |\Phi_K(W(1),V_c)-\Phi_K(W(0),V_c)|
 \le C_FC_0(s+L^d)\theta^{m-1}.
 \tag{5.2}
\]

#### Proof

Differentiate the terminal coordinate along the once-blocked path.  Pull its
differential back through the remaining \(m-1\) maps.  Lemmas 1--2 bound the
resulting covector in sup norm by \(C_F\theta^{m-1}\).  Pair it with the path
velocity, use \(\ell^\infty\)-\(\ell^1\) duality, and integrate (5.1).
\(\square\)

Because \(L\) is fixed, \(\theta^{m-1}\) differs from \(\theta^m\) only by a
constant.  Thus H6 does not require the large field itself to satisfy every
small-field derivative estimate.  It requires a uniform localized path bound
for the first output and contraction at all later regular levels.  Constructing
such a path without a global logarithm is part of the regular-event definition;
its complement belongs in H7.

## 6. Exact missing local theorem

A sufficient H6 theorem can now be stated without reference to observables or
probability laws.

> **H6-local.**  For every regular background admitted after the first
> large-field blocking step, prove either (3.3) with a summable curvature
> sequence or (3.4) with \(L^d\theta^2<1\), uniformly in domains, histories,
> boundary data, and RG depth.  Prove (5.1) for the first affected layer on a
> regular event whose complement satisfies H7, and apply the estimate to the
> differentials of the selected gauge-invariant terminal coordinate maps.

CMP **98** supplies relevant ingredients:

- locality of the iterated average in the enlarged endpoint blocks;
- analytic small-field expansions in Propositions 3--4;
- a functional derivative bounded independently of the lattice spacing in
  Proposition 5;
- analytic dependence on a regular background in Propositions 6--7.

It does **not** state H6-local.  In particular, Proposition 5 does not give the
conserved-current operator norm (3.1), the relative curvature error in (3.3),
or the first-layer path estimate (5.1).  A proof must expose the contour kernel,
use the covariant Ward identity from Lemma 1 to cancel endpoint/radial pieces,
and bound the residual path dependence by plaquette curvature.  Merely citing
analyticity or a cutoff-independent derivative bound leaves out the geometric
gain.

This is the next deterministic calculation in the \(R\)-observable route.
Even a proof of H6-local would leave H7 and H8, which concern the normalized
fiber laws rather than the averaging map.
