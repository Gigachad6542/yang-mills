# Averaged \(R\)-bias as a connected correlation

Status: **Propositions 1--3 and the counterexamples are proved here.**
They give an exact covariance representation of the averaged observable
defect without any mutual-absolute-continuity hypothesis, and they show that
gauge invariance and fiber-mass preservation alone give no scale gain.
The placement-summed connected-correlation estimate in (5.2) is **open** for
Balaban's Yang--Mills fibers.  Thus this note supplies a counterexample to an
automatic averaged-H8 argument and a precise replacement obligation; it does
not prove H8\(_\Sigma\).

## 1. From conditional bias to one signed global defect

Fix one step in the deterministic sequential ordering of the
\(R\)-components.  Let \(P\) be the positive measure immediately before this
replacement and \(R\) the positive measure immediately after it, both on the
same terminal configuration space \(\Omega\).  Fiber normalization gives

\[
 P(\Omega)=R(\Omega)=a\in(0,\infty).
 \tag{1.1}
\]

For a bounded terminal test \(F\), the contribution of this replacement to
the normalized observable telescope is

\[
 {1\over Z}\int_\Omega F\,d(R-P),
 \tag{1.2}
\]

where \(Z\) is the common total vacuum mass of the complete density.  If the
fiber variable is \(W\) and the exterior datum is \(V_c\), disintegration of
(1.2) recovers the familiar form

\[
 {1\over Z}\int P_\Lambda(V_c)
 \left[
  \mathbb E_{\widehat q_\Lambda}(F\mid V_c)
 -\mathbb E_{\widehat p_\Lambda}(F\mid V_c)
 \right]\nu(dV_c).
 \tag{1.3}
\]

Equation (1.3) is an **average** of the fixed-exterior biases.  Estimating its
absolute value after integration is potentially weaker than H8\(_\Sigma\),
which inserts an absolute value before that integration.  The following
identity says exactly what cancellation would have to be proved.

## 2. A support-independent covariance identity

### Proposition 1: equal-mass difference equals a covariance

Let \(P,R\) be finite positive measures satisfying (1.1).  Define

\[
 \mu={P+R\over2a},
 \qquad
 h={dR-dP\over dR+dP}.
 \tag{2.1}
\]

The second expression is defined \((P+R)\)-almost everywhere.  Then

\[
 |h|\le1,\qquad \mathbb E_\mu h=0,
 \tag{2.2}
\]

and every bounded real or complex \(F\) satisfies

\[
 {1\over a}\int F\,d(R-P)
 =2\mathbb E_\mu(Fh)
 =2\operatorname{Cov}_\mu(F,h).
 \tag{2.3}
\]

No relation between the supports of \(P\) and \(R\) is required.

**Proof.**  Both measures are absolutely continuous with respect to
\(P+R\).  Their Radon--Nikodym derivatives are nonnegative and sum to one,
so their difference \(h\) lies in \([-1,1]\).  Equal mass gives
\[
 \mathbb E_\mu h
 ={1\over2a}\int d(R-P)=0.
\]
Finally,
\[
 2\mathbb E_\mu(Fh)
 ={1\over a}\int Fh\,d(P+R)
 ={1\over a}\int F\,d(R-P).
\]
The last equality in (2.3) follows from \(\mathbb E_\mu h=0\).
\(\square\)

This identity remains valid when the true and template fiber laws have hard,
unmatched cutoffs.  It is therefore more robust than a likelihood-ratio
interpolation between \(\widehat p_\Lambda\) and
\(\widehat q_\Lambda\).

The first universal bound obtained from (2.3) is

\[
 \left|{1\over a}\int F\,d(R-P)\right|
 \le 2\inf_{c\in\mathbb C}\|F-c\|_\infty
 \tag{2.4}
\]

Keeping the size of the signed defect instead of using only \(|h|\le1\)
gives the sharper total-variation form

\[
 \left|{1\over a}\int F\,d(R-P)\right|
 \le 2\inf_{c\in\mathbb C}\|F-c\|_\infty\,\mathbb E_\mu|h|
 ={\inf_c\|F-c\|_\infty\over a}\,\|R-P\|_{\rm TV}.
 \tag{2.4$'$}
\]

Cauchy--Schwarz also gives

\[
 \left|{1\over a}\int F\,d(R-P)\right|
 \le2\sqrt{\operatorname{Var}_\mu(F)}
       \sqrt{\mathbb E_\mu|h|^2}.
 \tag{2.5}
\]

Thus a scale gain can come either from
\(\mathbb E_\mu|h|=\|R-P\|_{\rm TV}/(2a)\), or from decorrelation of \(F\)
and \(h\).  Neither gain is supplied by gauge symmetry alone.

## 3. Gauge invariance does not kill the covariance

If \(P\) and \(R\) are gauge invariant, then \(\mu\) and \(h\) in (2.1) are
gauge invariant.  A gauge-invariant terminal loop \(F\) is another scalar in
the trivial representation.  There is no representation-theoretic reason for
the covariance of two invariant scalars to vanish.

Strictly, the Radon--Nikodym representative \(h\) is initially defined only
\((P+R)\)-almost everywhere.  For a jointly measurable action of the compact
gauge group, choose the invariant version

\[
 \widetilde h(x)=\int_G h(g\mathbin\cdot x)\,dg.
 \tag{3.0}
\]

Gauge invariance of \(P\) and \(R\) implies
\(\widetilde h=h\) \((P+R)\)-almost everywhere, so this choice leaves every
identity above unchanged.

### Proposition 2: explicit \(SU(2)\) counterexample

For every scale label \(m\), take the common configuration space
\(\Omega=\{I,-I\}\subset SU(2)\), with the conjugation action of \(SU(2)\).
Let

\[
 P_m=\delta_{-I},\qquad R_m=\delta_I,\qquad
 F(U)={1\over2}\operatorname{tr}U.
 \tag{3.1}
\]

Both measures and \(F\) are gauge invariant, the two measures have equal
mass, and the replacement defect is

\[
 \int F\,d(R_m-P_m)=2
 \tag{3.2}
\]

for every \(m\).  In the notation of Proposition 1,
\(\mu_m=\frac12(\delta_I+\delta_{-I})\) and \(h_m=F\), so

\[
 2\operatorname{Cov}_{\mu_m}(F,h_m)=2.
 \tag{3.3}
\]

Thus gauge invariance, positivity, and exact fiber-mass preservation are
compatible with an order-one averaged bias at every scale.

The example is deliberately finite.  It does not model the Wilson action; it
falsifies the proposed **abstract implication** from symmetry and
normalization to a geometric gain.  Tensoring it with any gauge-invariant
exterior probability space leaves (3.2) unchanged, so exterior averaging
alone does not repair the implication.

The conclusion does not depend on singular or disjoint supports.  On the
one-plaquette lattice \(SU(2)^4\) with product Haar measure \(dU\) and the
lattice gauge action, put

\[
 F(U)={1\over2}\operatorname{tr}U(\partial p),\qquad
 dP=(1-tF)dU,\qquad dR=(1+tF)dU,qquad 0<t<1.
 \tag{3.3$'$}
\]

These are full-support, mutually absolutely continuous, gauge-invariant
probability measures.  The plaquette holonomy is Haar distributed,
\(\int F\,dU=0\), and character orthogonality gives
\(\int F^2dU=1/4\).  Hence

\[
 \int F\,d(R-P)=2t\int F^2dU={t\over2},
 \tag{3.3$''$}
\]

again an order-one defect with no scale gain.

There is a related representation-theoretic trap.  If an invariant law acts
on an equivariant vector \(X:\Omega\to\mathfrak{su}(2)\), then
\(\mathbb E X=0\).  But the scalar appearing in an observable bias can pair
two equivariant objects.

### Proposition 3: an invariant scalar survives color averaging

Let \(\mu\) be normalized area measure on the unit sphere in
\(\mathfrak{su}(2)\), with the adjoint action.  Put
\(X(A)=A\) and identify the equivariant covector
\(\xi(A)\) with \(A\) using the invariant inner product.  Then

\[
 \mathbb E_\mu X=0,
 \qquad
 \mathbb E_\mu\langle\xi,X\rangle=1.
 \tag{3.4}
\]

**Proof.**  The first expectation is an invariant vector in the nontrivial
irreducible adjoint representation and hence vanishes.  The second integrand
is \(\langle A,A\rangle=1\). \(\square\)

Accordingly, exterior color averaging may annihilate a naked terminal mean
shift, but it need not annihilate the gauge-invariant contraction of that
shift with the derivative of a terminal loop.  This is exactly why the
flat-background mechanism in research note 11 removes linear
\(\operatorname{Ad}\)-equivariant terms but leaves invariant quadratic and
curvature-coupled terms.

## 4. History and placement bookkeeping

At scale \(m\), let \(\lambda\in\mathscr C_m\) enumerate the history,
placement, and position in the sequential component ordering.  Let
\(P_\lambda,R_\lambda\) be the positive pre- and post-replacement measures.
For this section assume explicitly that

\[
 P_\lambda(\Omega)=R_\lambda(\Omega)=a_\lambda
 \quad\text{for every label }\lambda.
 \tag{4.0}
\]

This labelwise hypothesis holds for the introductory replacement in CMP
**122 I**, Eqs. (0.3)--(0.4), but it has not been verified for the actual
localized procedure described on printed p. 177, whose denominators are
integrals of only parts of the densities.  Task T11 isolates that missing
check.  Subject to (4.0), define
\(\mu_\lambda,h_\lambda\) by (2.1).  The exact scale-\(m\) contribution is

\[
 D_m(F)
 ={2\over Z}\sum_{\lambda\in\mathscr C_m}
 a_\lambda\operatorname{Cov}_{\mu_\lambda}
       (F,h_\lambda).
 \tag{4.1}
\]

This formula is obtained before localization produces signed activities.  If
one works after localization, the corresponding statement must be made for
the Jordan components or an absolute majorant; cancellations may not be
silently transported through a nonlinear history regrouping.

Averaged cancellation can be used in two genuinely different strengths:

\[
 \left|D_m(F)\right|
 = {2\over Z}\left|
 \sum_\lambda a_\lambda
   \operatorname{Cov}_{\mu_\lambda}(F,h_\lambda)\right|,
 \tag{4.2}
\]

which permits cancellation between histories, or the stronger sufficient
bound

\[
 \left|D_m(F)\right|
 \le {2\over Z}\sum_\lambda a_\lambda
 \left|\operatorname{Cov}_{\mu_\lambda}(F,h_\lambda)\right|.
 \tag{4.3}
\]

Equality (4.2) permits cancellation between histories only because the
absolute value is taken after their signed contributions have been summed.
Using it requires a direct estimate of that summed covariance.  The
observable telescope closes if

\[
 \sum_m |D_m(F)|<\infty
 \tag{4.4}
\]

with a tail uniform in ultraviolet depth.  This is an alternative to the
termwise absolute H8\(_\Sigma\) condition, but it must be proved for every
selected terminal test and, for the generating functional, uniformly on the
required complex source domain.

## 5. The exact missing estimate

For one fixed bounded terminal test, a sufficient averaged-H8 input is

\[
 \sum_{m\ge0}{1\over Z}\sum_{\lambda\in\mathscr C_m}
 a_\lambda
 \left|\operatorname{Cov}_{\mu_\lambda}
      (F,h_\lambda)\right|<\infty.
 \tag{5.1}
\]

The scale arithmetic in research note 11 says that a useful termwise target
has one additional geometric factor.  In the notation there, it is enough to
prove a connected estimate of the schematic form

\[
 \boxed{
 \left|\operatorname{Cov}_{\mu_\lambda}
       (F,h_\lambda)\right|
 \le C\,\Delta_\lambda\,\eta_m,
 \qquad \eta_m=O(L^{-m}),}
 \tag{5.2}
\]

together with the stated history/placement majorants.  Condition (5.1) is
already placement-summed, but it takes absolute values term by term.  The
weaker primary target is (4.4), with the \(\lambda\)-sum kept inside the
absolute value as in (4.2).

Formula (5.2) is not a consequence of Cauchy--Schwarz: (2.5) has no small
factor.  It requires a Yang--Mills-specific connected-correlation or
susceptibility estimate.  Possible sufficient mechanisms include:

1. a local covariance inequality whose kernel decays from the
   \(R\)-component to the terminal loop current;
2. a flat-background cancellation plus a uniform susceptibility to the
   geometrically small exterior curvature;
3. a cluster expansion with one marked terminal loop and one marked
   \(R\)-defect, retaining the cancellation before absolute values are taken.

Each mechanism needs information absent from the source-free density bound.
Hard characteristic functions also prevent importing a smooth
likelihood-ratio interpolation without boundary terms or a common-support
argument.

## 6. Comparison with the published construction

- CMP **122 I**, Eq. (0.3), printed p. 176, gives the equal-fiber-mass
  replacement needed for Proposition 1.  Printed p. 177 immediately warns
  that the actual procedure instead uses denominators formed from integrals
  of parts of the densities.  Therefore the labelwise hypothesis (4.0) is
  verified for the prototype but not yet for the localized implementation;
  its history-dependent fibers must be checked before histories are merged.
- CMP **122 I**, pp. 193--194, explicitly changes equality of densities to
  equality only after integration.  This is why the physical and stabilized
  measures in (2.1) are genuinely different.
- CMP **122 II** proves source-free component and polymer bounds.  It does not
  insert a terminal loop together with the \(R\)-defect and prove the
  connected estimate (5.1) or (5.2).
- Printed p. 356 of CMP **122 II** says that loop and averaged-loop
  expectations require further analysis and publication.

The result is therefore a precise failed route, not a negative statement
about the Yang--Mills covariance itself.  Averaging converts the H8 defect
into a connected correlation, which is potentially much smaller than the
fixed-exterior bias.  But the \(SU(2)\) example (3.1) proves that neither
gauge invariance nor normalization supplies that smallness.  The next
mathematical input must be a marked connected-correlation estimate such as
(5.1), together with the labelwise mass issue above.  The Gaussian computation
assigned as research note 19 (assigned, not yet written) tests its expected
power in a model where that estimate can be calculated explicitly.
