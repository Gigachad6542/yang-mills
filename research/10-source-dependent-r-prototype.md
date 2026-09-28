# A source-dependent fiber-normalized \(R\) prototype

Status: **the abstract fiber theorems and bounds in Sections 2--6 and the
linearized closed-loop current lemma in Section 7 are proved here**.  Their
identification with Balaban's introductory prototype and linear averaging
formula is exact.  Their use in the complete four-dimensional \(R\)-operation
requires the open Yang--Mills inputs listed in Section 8.

This note incorporates the independent derivation in
`collaboration/claude-r0-prototype.md`, with two corrections from the journal
page image: Eq. (0.3) is already a restricted-variable, hence fiberwise,
integral, and the full sourced output must include the explicit source factor.

## 1. What CMP 122 I actually normalizes

CMP **122 I**, Eq. (0.2), writes

\[
 \rho(V)=\sum_Z\rho(Z,V),
\]

and decomposes \(Z=Z'\cup Z''\).  The scan of printed p. 176 gives

\[
 (R\rho)(V)=\sum_Z\rho(Z'',V)
 \frac{\int dV|_{Z'}\,\rho(Z,V)}
      {\int dV|_{Z'}\,\rho(Z'',V)}.
 \tag{1.1}
\]

The notation \(dV|_{Z'}\) means integration over the variables restricted to
\(Z'\), with the exterior variables held fixed.  Thus the introductory
operation is a sum of fiber-normalized replacements, not merely a ratio of
global integrals.  Fiber integration gives Eq. (0.4), preservation of the full
mass.

This stronger reading does not identify the physical observable law.  The
conditional distribution on each fiber is replaced, the region \(Z'\) varies
with the term/history, and Balaban immediately warns on p. 177 that the actual
denominators use localized parts of the densities.  The detailed construction
on pp. 193--194 likewise uses term-dependent integration regions and changes
equality to equivalence.  The complete operation also contains the later
equivalent-but-not-equal reverse Faddeev--Popov step.

## 2. Multi-source fiber replacement

Let \(H\) be a finite or countable history set.  For each \(h\in H\), let
\(y\) denote exterior data with measure \(\nu_h(dy)\), let
\(\kappa_h(y,dx)\) be a fiber kernel, and let \(p_h,q_h\ge0\) be measurable.
Assume, almost everywhere,

\[
 0<P_h(y):=\int p_h(x,y)\,\kappa_h(y,dx)<\infty,
 \qquad
 0<Q_h(y):=\int q_h(x,y)\,\kappa_h(y,dx)<\infty,
 \tag{2.1}
\]

and

\[
 M:=\sum_h\int P_h(y)\,\nu_h(dy)<\infty.
\]

Let \(F_{h,1},\ldots,F_{h,m}\) be real observables representing the same
selected physical terminal tests in the coordinates of history \(h\).  Put

\[
 G_{h,z}(x,y)=\sum_{j=1}^m z_jF_{h,j}(x,y).
\]

Suppose that there are measurable fiber centers \(c_{h,j}(y)\) and constants
\(r_j\ge0\), independent of \(h,y\), such that on the union of the supports of
\(p_h\) and \(q_h\),

\[
 |F_{h,j}(x,y)-c_{h,j}(y)|\le r_j.
 \tag{2.2}
\]

For the summed identity and differentiation across \(h,y\), assume in addition
that each \(F_{h,j}\) is uniformly bounded.  A locally uniform exponential
moment dominating all source derivatives would be an admissible replacement,
but is not needed for the bounded terminal observables used here.  Define

\[
 \begin{aligned}
 P_h(z,y)&=\int e^{G_{h,z}(x,y)}p_h(x,y)\,\kappa_h(y,dx),\\
 Q_h(z,y)&=\int e^{G_{h,z}(x,y)}q_h(x,y)\,\kappa_h(y,dx),\\
 \mathcal R^{F}_{h,z}[p_h\mid q_h](x,y)
 &=e^{G_{h,z}(x,y)}q_h(x,y)\frac{P_h(z,y)}{Q_h(z,y)}.
 \end{aligned}
 \tag{2.3}
\]

The explicit factor \(e^{G_{h,z}}\) is part of the **full sourced density**.
One may factor it as
\(e^{G_{h,z}}\widetilde p_{h,z}\), where
\(\widetilde p_{h,z}=q_hP_h(z)/Q_h(z)\), but this is a source-dependent base
correction.  Moreover, \(e^{G_{h,z}}\) must remain inside every later
integration over variables on which \(G_{h,z}\) depends.  Mixing the full-density
and factored conventions obscures the normalization identity.

### Theorem 1: exact source lift and a uniform zero-free domain

Let

\[
 s(z)=\sum_{j=1}^m r_j|z_j|.
\]

If \(s(z)<\log2\), then \(P_h(z,y)\) and \(Q_h(z,y)\) are nonzero and
\(\mathcal R^F_{h,z}\) is holomorphic in \(z\).  Moreover,

\[
 \int \mathcal R^F_{h,z}[p_h\mid q_h](x,y)\,\kappa_h(y,dx)
 =P_h(z,y).
 \tag{2.4}
\]

Consequently, for every bounded exterior/history test \(\psi_h(y)\),

\[
 \sum_h\int \psi_h(y)\int\mathcal R^F_{h,z}\,d\kappa_h\,d\nu_h
 =\sum_h\int \psi_h(y)\int e^{G_{h,z}}p_h\,d\kappa_h\,d\nu_h.
 \tag{2.5}
\]

Thus this termwise source lift preserves the full generating function and all
of its joint derivatives exactly.  It reduces at \(z=0\) to the ordinary
fiber-normalized replacement

\[
 \mathcal R^F_{h,0}[p_h\mid q_h]=q_h\frac{P_h}{Q_h}.
\]

The set \(s(z)<\log2\) is a weighted complete Reinhardt
\(\ell^1\)-domain.  In particular, every polydisc with
\(\sum_jr_j\rho_j<\log2\) lies inside it.

## 3. Quantitative distortion bounds

Normalize \(p_h\) and \(q_h\) on a fixed fiber to probability laws
\(\widehat p_h=p_h/P_h\) and \(\widehat q_h=q_h/Q_h\).  Set

\[
 c_{h,z}(y)=\sum_jz_jc_{h,j}(y),
 \qquad g_{h,z}=G_{h,z}-c_{h,z},
\]

and

\[
 a_h(z,y)=\mathbb E_{\widehat p_h}e^{g_{h,z}},
 \qquad
 b_h(z,y)=\mathbb E_{\widehat q_h}e^{g_{h,z}}.
\]

Since \(|g_{h,z}|\le s(z)\),

\[
 |a_h-1|,|b_h-1|\le\delta(s):=e^s-1<1.
 \tag{3.1}
\]

In particular,

\[
 |Q_h(z,y)|\ge
 Q_h(y)e^{\operatorname{Re}c_{h,z}(y)}(2-e^{s(z)}),
 \tag{3.2}
\]

and the same lower bound holds with \(P_h\) in place of \(Q_h\).

Relative to naively multiplying the unsourced replacement by the source, define
the fiber scalar

\[
 D_h(z,y):=
 \frac{P_h(z,y)/P_h(y)}{Q_h(z,y)/Q_h(y)}
 =\frac{a_h(z,y)}{b_h(z,y)}.
 \tag{3.3}
\]

Where \(q_h(x,y)>0\), this equals the density ratio
\(\mathcal R^F_{h,z}/(e^{G_{h,z}}\mathcal R^F_{h,0})\).  Definition (3.3)
remains meaningful where both densities vanish and avoids a spurious \(0/0\).

It obeys

\[
 \begin{aligned}
 |D_h-1|&\le
 \frac{2(e^s-1)}{2-e^s},\\
 |D_h|&\le\frac{e^s}{2-e^s},\\
 |\log D_h|&\le2[-\log(2-e^s)],
 \end{aligned}
 \tag{3.4}
\]

where
\(\log D_h:=\operatorname{Log}a_h-\operatorname{Log}b_h\), with each principal
branch taken in the disc around one, so that \(\log D_h(0)=0\).  On a polydisc
\(\sum_jr_j\rho_j\le s_0<\log2\), Cauchy's estimate gives

\[
 |\partial^\alpha\log D_h(0,y)|
 \le \alpha!\,2[-\log(2-e^{s_0})]\prod_j\rho_j^{-\alpha_j}.
 \tag{3.5}
\]

If \(|F_{h,j}|\le B_j\) and \(t(z)=\sum_jB_j|z_j|\), define the complete local
source factor \(C_h=e^{G_{h,z}}D_h\).  It agrees with
\(\mathcal R^F_{h,z}/\mathcal R^F_{h,0}\) wherever the unsourced replacement is
positive and satisfies

\[
 |C_h|\le e^t\frac{e^s}{2-e^s},
 \qquad
 |C_h-1|\le
 (e^t-1)\frac{e^s}{2-e^s}
 +\frac{2(e^s-1)}{2-e^s}.
 \tag{3.6}
\]

### Proof of Theorem 1 and the bounds

Equations (3.1) follow from
\(|e^w-1|\le e^{|w|}-1\).  Hence both normalized moment-generating functions
lie in the disc centered at one of radius \(e^s-1<1\), proving nonvanishing and
(3.2).  Fiber integration in (2.3) cancels \(Q_h(z,y)\) and proves (2.4);
summing proves (2.5).  Boundedness gives holomorphy by dominated convergence.

For (3.4), use

\[
 \left|\frac{a}{b}-1\right|
 \le\frac{|a-1|+|b-1|}{1-|b-1|},
\]

and \(|a/b|\le(1+\delta)/(1-\delta)\).  The power series for the principal
logarithm gives \(|\log w|\le-\log(1-\delta)\) when \(|w-1|\le\delta<1\);
apply it separately to \(a\) and \(b\).  Equations (3.5)--(3.6) then follow
from multivariable Cauchy and the triangle inequality. \(\square\)

## 4. What the unsourced operation loses

For one real test \(F\), the exact one-fiber error of the source-blind
replacement is

\[
 \int F\,\mathcal R^F_{h,0}\,d\kappa_h-
 \int Fp_h\,d\kappa_h
 =P_h\left(\mathbb E_{\widehat q_h}F-
            \mathbb E_{\widehat p_h}F\right).
 \tag{4.1}
\]

Therefore

\[
 \left|\int F(\mathcal R^F_{h,0}-p_h)\,d\kappa_h\right|
 \le P_h\operatorname{osc}_{\operatorname{supp}(p_h+q_h)}F.
 \tag{4.2}
\]

After summing and normalizing by \(M\), the bias is at most the essential
supremum of the fiber oscillation.  The general bounded-test estimate is only
\(2\lVert F\rVert_\infty\).

If \(F=f\circ\tau_h\), where \(f\) is \(L_f\)-Lipschitz on a terminal metric
space and

\[
 d_h(y)=\operatorname{diam}\tau_h(\operatorname{fiber}(h,y)),
\]

then

\[
 \operatorname{osc}_{\rm fiber}F\le L_fd_h(y).
 \tag{4.3}
\]

Also,

\[
 \partial_{z_j}\log D_h(0,y)
 =\mathbb E_{\widehat p_h}F_{h,j}
  -\mathbb E_{\widehat q_h}F_{h,j}.
 \tag{4.4}
\]

Thus the source correction inserts exactly the conditional expectation missing
from the ordinary \(R\)-step.  If the terminal observable is fiber-independent,
then its fiber radius is zero, \(D_h\equiv1\), and the ordinary operation already
commutes with that source.

For one real \(F\), choosing the midpoint of its essential fiber range gives
\(r=\operatorname{osc}_{\rm fiber}(F)/2\), improving the source disc by a
factor of two over an uncentered norm bound.  A sufficient elementary condition
for a compatible history-resolved composition is a common summable envelope,
for example
\(\sum_k\sup_{h,y}d_{h,k}<\infty\).  A weighted variant can be used if its
weights are retained through the history sum.  Without such an estimate,
per-step \(O(|z|d_{h,k})\) corrections may accumulate with ultraviolet depth.

## 5. History sums do not remove the difficulty

Suppose at a common pointwise configuration the explicit source factor is
common, the unsourced history summands \(r_h\) are positive, and
\(0<\sum_hr_h<\infty\).  Then

\[
 \frac{\sum_he^{G_z}r_hD_h}{e^{G_z}\sum_hr_h}
 =\sum_h\frac{r_h}{\sum_{h'}r_{h'}}D_h
 \tag{5.1}
\]

is a positively weighted average.  Hence a common bound
\(|D_h-1|\le\varepsilon\) passes through the history sum.  The elementary
bound (3.4) gives \(\varepsilon<1\), and therefore a zero-free complete-density
ratio, on the smaller domain

\[
 s<\log(4/3).
\]

This argument needs a common envelope.  Nonvanishing of each denominator, or
smallness modulo a different history-dependent constant, does not control the
sum.  It also does not handle unmatched histories.

Exact scalar preservation composes only if every step retains the complete
history-resolved analytic family and its pairing with the appropriate template.
The operation is representation-dependent and generally nonlinear after
histories are combined:

\[
 q_1\frac{P_1}{Q_1}+q_2\frac{P_2}{Q_2}
 \ne(q_1+q_2)\frac{P_1+P_2}{Q_1+Q_2}.
 \tag{5.2}
\]

Once histories are merged, the fiber/template data required at the next step
are lost.  Moreover, zero-free denominators give no spatial locality or polymer
decay for \(\log D_h\).

## 6. The correct sequential induction statement

After one sourced step the input is no longer necessarily a pure exponential
times a positive source-free density.  The following general form is therefore
the appropriate algebraic induction.

Let \(a_h(z,x,y)\) and \(b_h(z,x,y)\) be \(L^1(d\kappa_h)\)-valued
holomorphic families; equivalently, pointwise holomorphy together with local
\(L^1\) domination on every compact source set suffices.  Assume
\(0<A_h(0,y),B_h(0,y)<\infty\), and set

\[
 A_h(z,y)=\int a_h(z,x,y)d\kappa_h,
 \qquad
 B_h(z,y)=\int b_h(z,x,y)d\kappa_h,
\]

and, whenever \(B_h(z,y)\ne0\), define

\[
 \mathfrak R_z[a_h\mid b_h](x,y)
 =b_h(z,x,y)\frac{A_h(z,y)}{B_h(z,y)}.
 \tag{6.1}
\]

Then

\[
 \int\mathfrak R_z[a_h\mid b_h]d\kappa_h=A_h(z,y)
 \tag{6.2}
\]

exactly.  If \(a_h(0,x,y),b_h(0,x,y)>0\) on the points where the ratios below
are used and, pointwise on a common source domain,

\[
 \left|\frac{a_h(z)}{a_h(0)}-1\right|\le\varepsilon_a<1,
 \qquad
 \left|\frac{b_h(z)}{b_h(0)}-1\right|\le\varepsilon_b<1,
\]

then

\[
 \left|\frac{\mathfrak R_z}{\mathfrak R_0}\right|
 \le\frac{(1+\varepsilon_a)(1+\varepsilon_b)}{1-\varepsilon_b},
 \tag{6.3}
\]

and

\[
 \left|\frac{\mathfrak R_z}{\mathfrak R_0}-1\right|
 \le\frac{\varepsilon_a+2\varepsilon_b+\varepsilon_a\varepsilon_b}
          {1-\varepsilon_b}.
 \tag{6.4}
\]

These follow by writing the ratio as the product of the pointwise template
ratio, the normalized \(A\)-ratio, and the inverse normalized \(B\)-ratio.

## 7. Closed-loop cancellation and the actual sensitivity gap

CMP **98**, Proposition 5, proves a functional-derivative bound for the iterated
average on a regular small-field domain, uniform in the lattice spacing.  It
does not by itself state the source-sensitive estimate needed here.  The
linearized contour geometry can nevertheless be analyzed exactly, and gauge
invariance removes an apparent hub-bond obstruction for closed loops.

CMP **95**, Eqs. (1.6)--(1.8), takes the coarse point \(y\) at a **corner** of
the block \(B(y)\) and uses axis-ordered contours \(\Gamma_{y,x}\).  A single
coarse link therefore does have order-one radial weights near that corner.
Write the one-step linearized average as

\[
 (QA)(c)=\Lambda(c_-)+S(c)-\Lambda(c_+),
 \tag{7.1}
\]

where

\[
 \Lambda(y)=L^{-d}\sum_{x\in B(y)}A(\Gamma_{y,x}),\qquad
 S(c)=L^{-d}\sum_{x\in B(c_-)}A([x,x+Le_\mu]).
 \tag{7.2}
\]

Here \(c=\langle y,y+Le_\mu\rangle\).  For an antisymmetric current \(\tau\)
on oriented coarse bonds define

\[
 (\operatorname{div}\tau)(y)
 =\sum_{c_-=y}\tau(c)-\sum_{c_+=y}\tau(c).
\]

### Lemma 2: a divergence-free current has no radial hub term

Pairing (7.1) with \(\tau\) gives

\[
 \sum_c\tau(c)(QA)(c)
 =\sum_b\tau'(b)A(b)
  +\sum_y(\operatorname{div}\tau)(y)\Lambda(y),
 \tag{7.3}
\]

where

\[
 \tau'(b)=L^{-d}\sum_c\tau(c)\,
 \#\{x\in B(c_-):b\subset[x,x+Le_\mu]\}.
 \tag{7.4}
\]

If \(\operatorname{div}\tau=0\), then

\[
 \operatorname{div}\tau'=0,\qquad
 \lVert\tau'\rVert_\infty\le L^{1-d}\lVert\tau\rVert_\infty,\qquad
 \lVert\tau'\rVert_1\le L\lVert\tau\rVert_1.
 \tag{7.5}
\]

### Proof

The two \(\Lambda\)-terms telescope after summing over coarse bonds and give the
last term in (7.3), which vanishes for a divergence-free current.  A straight
segment \([x,x+Le_\mu]\) has divergence
\(\delta_x-\delta_{x+Le_\mu}\).  Summing its contribution over
\(x\in B(c_-)\), and then over \(c\), gives

\[
 (\operatorname{div}\tau')(z)
 =L^{-d}(\operatorname{div}\tau)(y(z)),
\]

where \(y(z)\) is the corner of the block containing \(z\).  Finally, a fine
bond in direction \(\mu\) lies in at most \(L\) of the straight segments in
(7.4), each weighted by \(L^{-d}\), proving the sup bound.  There are \(L^d\)
segments of length \(L\) per coarse bond, proving the \(\ell^1\) bound.
\(\square\)

The linearized current of a closed terminal loop is divergence-free.  Iterating
Lemma 2 therefore gives the **uniform**, not merely generic-position, estimate

\[
 \lVert\tau^{(m)}\rVert_\infty
 \le L^{(1-d)m}\lVert\tau\rVert_\infty.
 \tag{7.6}
\]

This proves the \(L^{-3m}\) single-bond influence in \(d=4\) at the trivial-field
linearization for closed-loop tests.  It does not prove the nonlinear
large-field estimate.  Three interfaces remain:

1. the first level above an \(R\)-component may contain irregular fields, where
   the spectral logarithms and Baker--Campbell--Hausdorff terms are not governed
   by the linear telescoping argument;
2. at a nontrivial regular background, the derivative of a loop is
   covariantly divergence-free and curvature corrections must be quantified;
3. the source correction depends on the difference between the true and model
   conditional means, not only on the oscillation of the terminal test.

Conditional on regular propagation after the first affected level, the natural
component influence has the form

\[
 \delta_\Lambda\lesssim
 C(|\Lambda|+L^d)L^{(1-d)m}.
 \tag{7.7}
\]

The factor \(L^{dm}\) counting possible fine cells then turns a first-order
absolute bias \(O(\delta_\Lambda)\) with an order-one conditional-mean mismatch
into a bound of order

\[
 \varepsilon_mL^m,
 \tag{7.8}
\]

per terminal loop bond.  Here \(\varepsilon_m\) denotes the large-field
component density after lattice-animal and history summation.  For large \(m\),
Balaban's first suppression factor behaves like
\(\varepsilon_m=\exp[-A(\log(bm))^{p_0}]\), which is subexponential and cannot
beat \(L^m\).  This shows that an order-one first-order mismatch estimate does
not close; it does not show that the true bias diverges.

If instead the conditional-mean mismatch supplies a factor
\(\eta_m\), the first-order sum is bounded by
\(\varepsilon_mL^m\eta_m\).  A second-order estimate
\(O(\delta_\Lambda^2)\) gives
\[
 \varepsilon_m|\Lambda|^2L^{(2-d)m},
 \tag{7.9}
\]
which is geometrically summable in \(d=4\), subject to uniform control of
component shapes, histories, and additional irregular levels.

A precise replacement for the earlier vague summability request is therefore:

> **Y6'.**  In Balaban's local axial frame, let \(\Pi^\perp\) remove gradient
> directions.  For every \(R\)-component \(\Lambda\) at scale \(K-m\), prove,
> uniformly in exterior fields and histories,
> \[
> \left\|\Pi^\perp\left(
> \mathbb E_{\widehat p_\Lambda}[A_\Lambda\mid V_c]
> -\mathbb E_{\widehat q_\Lambda}[A_\Lambda\mid V_c]\right)\right\|_\infty
> \le\eta_m,
> \]
> with \(\sum_m\varepsilon_mL^m\eta_m<\infty\), and control the quadratic
> remainder by (7.9), including all irregular-level costs.

Establishing Y6' is a Yang--Mills estimate; the linear current lemma only
identifies the gauge-invariant direction in which it is needed.

## 8. What remains open for the complete \(R\)-operation

The abstract theorem solves the algebraic source lift of Eq. (0.3).  It does not
yet extend Balaban's four-dimensional stability theorem.  The missing inputs
are:

1. identify every detailed localized denominator and template with a positive,
   nonzero fiber pair of the form used above;
2. retain the history/fiber labels through all subsequent localization and
   exponentiation steps;
3. extend Lemma 2 from the trivial-field linearization to the irregular first
   level and regular curved backgrounds, and prove Y6' (or a direct
   marked-polymer substitute) for the selected terminal loop observables;
4. control several components, mixed fiber differences, and unmatched
   histories without losing the common source disc;
5. show that the source corrections fit the analytic/local \(E/R/B\) density
   class with a gain beating lattice-animal and refining-lattice entropy;
6. verify term by term that the final reverse Faddeev--Popov equivalence remains
   source-preserving.  Gauge invariance makes this plausible, but the published
   statement alone is not an observable theorem.

The key distinction is now exact: nonvanishing denominators and source
normalization are elementary consequences of bounded fiber oscillation;
uniform localization and summability of the resulting history-dependent source
activities are the hard Yang--Mills problem.
