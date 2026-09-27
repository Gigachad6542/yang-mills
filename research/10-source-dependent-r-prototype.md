# A source-dependent fiber-normalized \(R\) prototype

Status: **the abstract fiber theorems and bounds in Sections 2--6 are proved
here**.  Their identification with Balaban's introductory prototype is exact.
Their use in the complete four-dimensional \(R\)-operation requires the open
Yang--Mills inputs listed in Section 8.

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

For global dominated-convergence statements, also assume that each
\(F_{h,j}\) is uniformly bounded, or replace this by a uniform exponential
moment hypothesis.  Define

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
Equivalently, one can call \(q_hP_h(z)/Q_h(z)\) the replaced base density and
retain the same explicit source outside all subsequent integrations.  Mixing
these two conventions obscures the normalization identity.

### Theorem 1: exact source lift and a uniform zero-free polydisc

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

Relative to naively multiplying the unsourced replacement by the source, the
extra correction is independent of the fiber variable \(x\):

\[
 D_h(z,y):=
 \frac{\mathcal R^F_{h,z}[p_h\mid q_h]}
      {e^{G_{h,z}}\mathcal R^F_{h,0}[p_h\mid q_h]}
 =\frac{a_h(z,y)}{b_h(z,y)}.
 \tag{3.3}
\]

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

where the logarithm is the branch fixed by \(\log D_h(0)=0\).  On a polydisc
\(\sum_jr_j\rho_j\le s_0<\log2\), Cauchy's estimate gives

\[
 |\partial^\alpha\log D_h(0,y)|
 \le \alpha!\,2[-\log(2-e^{s_0})]\prod_j\rho_j^{-\alpha_j}.
 \tag{3.5}
\]

If \(|F_{h,j}|\le B_j\) and \(t(z)=\sum_jB_j|z_j|\), the complete local
source ratio \(C_h=\mathcal R^F_{h,z}/\mathcal R^F_{h,0}=e^{G_{h,z}}D_h\)
satisfies

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
for a sequence of source corrections is summability of the fiber influences
\(\sum_kd_{h,k}\).  Without such an estimate, per-step
\(O(|z|d_{h,k})\) corrections may accumulate with ultraviolet depth.

## 5. History sums do not remove the difficulty

Suppose at a fixed configuration the explicit source factor is common and the
unsourced history summands \(r_h\) are positive.  Then

\[
 \frac{\sum_he^{G_z}r_hD_h}{e^{G_z}\sum_hr_h}
 =\sum_h\frac{r_h}{\sum_{h'}r_{h'}}D_h
 \tag{5.1}
\]

is a positive-weighted average.  Hence a common bound
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

Let \(a_h(z,x,y)\) and \(b_h(z,x,y)\) be arbitrary holomorphic integrable
families, set

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

exactly.  If \(a_h(0),b_h(0)>0\) and, pointwise on a common source domain,

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

## 7. Sensitivity audit: what CMP 98 does and does not give

CMP **98**, Proposition 5, proves a functional-derivative bound for the iterated
average on a regular small-field domain, uniform in the lattice spacing.  It
does **not** state a uniform single-bond influence of order
\(L^{-3(K-k)}\), and it supplies no comparable iterated estimate on arbitrary
large-field fibers.

There is already an obstruction in the linearization of its contour average.
The average over \(L^d\) starting points carries a factor \(L^{-d}\), but every
radial contour leaving a block center starts along one of only \(2d\) adjacent
bonds.  By pigeonhole, at least one such hub bond is used by order \(L^d\)
contours and can therefore have order-one one-step weight.  Thus the often
guessed \(L^{-(d-1)}\) influence is at best a generic-position heuristic, not a
uniform estimate.

Iterated locality still says which components can affect a fixed terminal loop.
At a scale \(m\) below the terminal lattice, its pullback occupies order
\(L^{4m}\) fine cells.  Even combining a **heuristic** generic influence
\(L^{-3m}\) with absolute component counting produces \(L^m\), not a summable
upper bound.  Balaban's first large-field factor is
\(\exp[-A(\log g^{-2})^{p}]\); along \(g^{-2}\asymp m\), this is subexponential
in \(m\) and does not repair that crude absolute count.

This calculation shows only that the proposed absolute-value proof does not
close.  It does **not** prove that the true conditional bias diverges.  A useful
bound would need cancellation, a stronger probabilistic estimate, a different
observable/RG geometry, or a comparison norm that avoids summing worst-case
single-bond influences.

## 8. What remains open for the complete \(R\)-operation

The abstract theorem solves the algebraic source lift of Eq. (0.3).  It does not
yet extend Balaban's four-dimensional stability theorem.  The missing inputs
are:

1. identify every detailed localized denominator and template with a positive,
   nonzero fiber pair of the form used above;
2. retain the history/fiber labels through all subsequent localization and
   exponentiation steps;
3. prove a cutoff-uniform fiber-influence or direct marked-polymer bound for the
   selected terminal observables, including large-field configurations;
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
