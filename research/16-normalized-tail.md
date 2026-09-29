# Normalization, bad-event tails, and H7\(_\Sigma\)

Status: **Propositions 1--2 and Corollary 3 are proved here.**  They give an exact
unnormalized reformulation of H7\(_\Sigma\) for positive sequential
fiber replacements and sharp counterexamples when the required marginal
weight or denominator comparison is absent.  The comparison with Balaban's
published construction is a source audit.  The history-resolved Yang--Mills
tail estimate isolated in (5.2) remains **open**.

The purpose of this note is narrow.  A small unnormalized component weight
does not make its normalized conditional law close to a regular law.  On the
other hand, H7\(_\Sigma\) does not average conditional probabilities with
counting measure: it weights them by exterior marginals.  For the exact
marginal, conditional normalization cancels.  Keeping these two facts
separate identifies the precise estimate that is missing.

## 1. Pointwise normalization really needs a lower mass

Let \(\mu\) be a finite positive measure on a measurable space \(X\), let
\(E\subset X\), and write

\[
 B=\mu(E),\qquad G=\mu(E^c),\qquad P=\mu(X)=B+G>0.
 \tag{1.1}
\]

### Proposition 1: sharp one-fiber bounds

The normalized bad-event probability is \(B/P\).  Each of the following
bounds is sharp:

\[
 \begin{array}{ll}
 P\ge p_*,\ B\le u
   &\Longrightarrow\quad \displaystyle {B\over P}
        \le \min\{1,u/p_*\},\\[6pt]
 G\ge \ell,\ B\le u
   &\Longrightarrow\quad \displaystyle {B\over P}
        \le {u\over \ell+u},\\[6pt]
 B\le \eta G
   &\Longrightarrow\quad \displaystyle {B\over P}
        \le {\eta\over1+\eta}.
 \end{array}
 \tag{1.2}
\]

In particular, an absolute upper bound \(B\le u\) and strict positivity
\(P>0\), without a quantitative lower bound on \(P\), do not imply any
bound smaller than one on \(B/P\).

**Proof.**  The first inequality is immediate from \(B/P\le u/p_*\).
For the second, \(B/(B+G)\) is increasing in \(B\) and decreasing in
\(G\), so it is at most \(u/(u+\ell)\).  The third follows from
\(B/(B+G)\le\eta/(1+\eta)\).  Equality is obtained by saturating the
displayed hypotheses, so the constants cannot be improved. \(\square\)

The smallest counterexample uses the two-point space
\(X=\{g,b\}\), \(E=\{b\}\), and

\[
 \mu_\varepsilon=\varepsilon\delta_b.
 \tag{1.3}
\]

Then \(\mu_\varepsilon(E)=\varepsilon\to0\) and
\(\mu_\varepsilon(X)>0\), but the normalized bad probability is one.
Thus the statement in CMP **122 I** that the fiber denominators are positive
cannot, by itself, yield a small conditional tail.

## 2. The exact fiber-normalized replacement

All spaces below are standard Borel whenever a disintegration is invoked.
Let \(Y\) be the exterior-field/history space with positive measure \(\nu\).
For each \(y\in Y\), let \(p_y\) and \(q_y\) be finite positive measures on
the fiber \(X_y\), with measurable masses

\[
 P_y=p_y(X_y)>0,\qquad Q_y=q_y(X_y)>0.
 \tag{2.1}
\]

The source-blind fiber replacement used in the introductory \(R\)-prototype is

\[
 r_y(dx)={P_y\over Q_y}q_y(dx)=P_y\widehat q_y(dx),
 \qquad
 \widehat p_y={p_y\over P_y},\quad
 \widehat q_y={q_y\over Q_y}.
 \tag{2.2}
\]

It has the same fiber mass \(P_y\) as \(p_y\).  Let \(E_y\subset X_y\)
be a measurable family of bad sets and put
\(E=\{(x,y):x\in E_y\}\).

### Proposition 2: marginal cancellation

Define measures on the total space by

\[
 M_p(dx,dy)=p_y(dx)\nu(dy),\qquad
 M_r(dx,dy)=r_y(dx)\nu(dy).
 \tag{2.3}
\]

Then

\[
 \begin{aligned}
 \int_Y P_y\widehat p_y(E_y)\,\nu(dy)&=M_p(E),\\
 \int_Y P_y\widehat q_y(E_y)\,\nu(dy)&=M_r(E)
   =\int_Y{P_y\over Q_y}q_y(E_y)\,\nu(dy).
 \end{aligned}
 \tag{2.4}
\]

Consequently, if \(Z=\int P_y\,d\nu\in(0,\infty)\), then

\[
 \int_Y\bigl[\widehat p_y(E_y)+\widehat q_y(E_y)\bigr]
       {P_y\nu(dy)\over Z}
 ={M_p(E)+M_r(E)\over Z}.
 \tag{2.5}
\]

**Proof.**  Substitute the definitions:
\(P_y\widehat p_y(E_y)=p_y(E_y)\) and
\(P_y\widehat q_y(E_y)=P_yq_y(E_y)/Q_y=r_y(E_y)\), then integrate in
\(y\). \(\square\)

This identity is the useful normalization lemma for H7\(_\Sigma\).  It says
that no pointwise lower bound on \(P_y\) or \(Q_y\) is required if the
conditional probabilities are integrated against the **exact preserved
exterior marginal** \(P_y\nu/Z\) and if the estimate is made directly on
the actual pre- and post-replacement bad masses.

It does not say that an unnormalized bound on the raw template \(q_y(E_y)\)
survives the replacement.  Formula (2.4) contains the ratio \(P_y/Q_y\).
The two-point example

\[
 p=\delta_g,qquad q_\varepsilon=\varepsilon\delta_b
 \tag{2.6}
\]

has \(q_\varepsilon(E)=\varepsilon\to0\), but
\(r_\varepsilon=\delta_b\) and hence \(r_\varepsilon(E)=1\).  Strict
positivity of \(Q_\varepsilon\) is again insufficient.  Any route that starts
from a raw-template bound must supply one of the relative estimates

\[
 q_y(E_y)\le b_yQ_y,qquad
 {P_y\over Q_y}\le C_y,qquad\text{or directly}\qquad
 r_y(E_y)\le a_yP_y.
 \tag{2.7}
\]

The first and third formulations are equivalent with \(a_y=b_y\); the
second turns an absolute raw bound into
\(r_y(E_y)\le C_yq_y(E_y)\).

## 3. Sequential histories and the placement sum

At a fixed ultraviolet depth, order all \(R\)-components deterministically
and replace them one at a time, as in research note 11.  Let \(\lambda\)
record the scale, history, placement, and position in this order.  Immediately
before replacement \(\lambda\), let \(M_\lambda\) be the positive current
term and let \(M_\lambda^R\) be the term after replacing that fiber.  Both
have mass \(Z_\lambda\); in the application all terms are ultimately
normalized by the common vacuum mass \(Z\).

Let \(E_\lambda\) be the complement of the regular terminal chart and regular
propagation event used for that component.  If

\[
 \alpha_\lambda(dV_c)
 ={P_\lambda(V_c)\nu_\lambda(dV_c)\over Z},
 \tag{3.1}
\]

then Proposition 2 gives the exact identity

\[
 \int\!\left[
   \widehat p_\lambda(E_\lambda\mid V_c)
  +\widehat q_\lambda(E_\lambda\mid V_c)
 \right]d\alpha_\lambda
 ={M_\lambda(E_\lambda)+M_\lambda^R(E_\lambda)\over Z}.
 \tag{3.2}
\]

### Corollary 3: an unnormalized form of H7\(_\Sigma\)

For positive sequential terms with the exact exterior marginals (3.1),
H7\(_\Sigma\) is equivalent to

\[
 \boxed{
 \sum_{m\ge0}\sum_{\lambda\in\mathscr C_m}
 {M_\lambda(E_\lambda)+M_\lambda^R(E_\lambda)\over Z}<\infty.}
 \tag{3.3}
\]

Moreover, the tail of the series in (3.3) is exactly the H7 contribution to
the physical-versus-stabilized observable telescope.

For a finite signed localized term \(S_\lambda\), disintegrate its total
variation and denote the resulting conditional probability kernel by
\(\widehat s_\lambda(\,\cdot\mid V_c)\).  Using its exact total-variation
exterior marginal, the same calculation gives

\[
 \int \widehat s_\lambda(E_\lambda\mid V_c)
       {d|S_\lambda|_{Y}(V_c)\over Z}
 ={ |S_\lambda|(E_\lambda)\over Z}.
 \tag{3.4}
\]

Thus signed localization does not destroy the identity, but it changes the
measure that must be controlled from a probability marginal to a
total-variation marginal.

Research note 11 permits a convenient majorant
\(\varpi_\lambda\ge\alpha_\lambda\).  Lower domination alone is not enough
to deduce H7 from (3.3).  If instead

\[
 d\varpi_\lambda=r_\lambda d\alpha_\lambda,qquad
 1\le r_\lambda\le C_\lambda,
 \tag{3.5}
\]

then the left side of (3.2) with \(d\varpi_\lambda\) is at most
\(C_\lambda\) times its right side.  Hence a sufficient majorized version is

\[
 \sum_{m,\lambda}{C_\lambda\over Z}
  [M_\lambda(E_\lambda)+M_\lambda^R(E_\lambda)]<\infty.
 \tag{3.6}
\]

The need for the upper bound in (3.5) is sharp.  Take
\(Y=\{a,b\}\), let
\(\alpha_\varepsilon(a)=\varepsilon\),
\(\alpha_\varepsilon(b)=1-\varepsilon\), and let the conditional bad
probability be one at \(a\) and zero at \(b\).  The exact marginal average is
\(\varepsilon\).  The measure
\(\varpi_\varepsilon(a)=1\),
\(\varpi_\varepsilon(b)=1-\varepsilon\) dominates \(\alpha_\varepsilon\),
but its bad-event integral is one.  Therefore the one-sided majorant in
research note 11 must either be chosen exactly, or be accompanied by an upper
Radon--Nikodym bound, before an unnormalized tail estimate can be inserted.

## 4. What the published large-field bounds establish

The following points are direct consequences of Balaban's formulas.

1. CMP **122 I**, Eq. (0.3), printed p. 176, is a restricted-variable fiber
   replacement.  The discussion immediately following it states that the
   densities are positive, the integration domains are nonempty, and the
   denominators are positive.  Eq. (0.4) is the mass-preservation identity.
   This supplies (2.1)--(2.2), but no quantitative lower bound on \(Q_y\).

2. The detailed preparatory transformations through Eq. (1.75), printed
   pp. 193--194, preserve the density.  The next integration changes the
   density and uses integration regions that generally vary from summand to
   summand.  Consequently the exact marginal cancellation must be applied
   **before histories are merged**, with those history-dependent fibers.

3. CMP **122 II**, Eqs. (1.73)--(1.75), printed pp. 379--380, uses positivity
   to bound a normalized \(T_k(X)\)-expectation by a constant times
   \(\sup|F|\).  Taking \(F=\mathbf1_E\) gives only an order-one bound.  It
   does not prove that the regular-event complement has small normalized
   probability.

4. CMP **122 II**, Eqs. (1.79), (1.89), and (1.100), printed pp. 383--390,
   supplies small factors for source-free large-field components and the
   resulting localized \(R\)-activities.  These are useful **unnormalized**
   inputs.  The paper does not mark the terminal-chart event \(E_\lambda\),
   does not state (3.3) for every sequential intermediate term, and does not
   construct the total-variation exterior marginals needed after localization
   and exponentiation.

5. The reverse Faddeev--Popov removal in CMP **122 II**, printed p. 378, is
   again equivalent only after component integration.  It therefore requires
   the same history-resolved treatment; a final source-free activity bound
   cannot simply be read backward as a bound on every earlier physical fiber.

The published work therefore gives more than bare positivity--it gives strong
source-free component suppression--but it does not give either of the two
complete bridges needed here:

- a direct marked estimate of the actual bad masses in (3.3); or
- a raw-template bad-mass estimate together with a uniform control of
  \(P_y/Q_y\) and the sequential history/placement sum.

In particular, no claim that Balaban proved a small normalized tail is made
here.  Conversely, a new proof need not establish a pointwise denominator
lower bound if it proves (3.3) directly.

## 5. The replacement obligation

The exact positive-measure target should be recorded as

\[
 \tag{H7_{\Sigma}'}
 \sum_{m\ge0}\sum_{\lambda\in\mathscr C_m}
 {M_\lambda(E_\lambda)+M_\lambda^R(E_\lambda)\over Z}<\infty,
\]

with a vanishing ultraviolet tail.  For signed localized representations,
replace the two measures by their total variations and use the exact
total-variation marginals, or prove (3.5)--(3.6).

A concrete sufficient estimate is: find nonnegative numbers
\(a_{m,\lambda}\) such that

\[
 M_\lambda(E_\lambda)+M_\lambda^R(E_\lambda)
 \le Za_{m,\lambda},qquad
 \sum_{m,\lambda}a_{m,\lambda}<\infty.
 \tag{5.1}
\]

A termwise sufficient version, before carrying out the fiber normalization,
is

\[
 \begin{aligned}
 p_\lambda(E_\lambda\mid V_c)&\le
   a_\lambda(V_c)P_\lambda(V_c),\\
 q_\lambda(E_\lambda\mid V_c)&\le
   b_\lambda(V_c)Q_\lambda(V_c),
 \end{aligned}
 \qquad
 \sum_{m,\lambda}\int(a_\lambda+b_\lambda)\,d\alpha_\lambda<\infty.
 \tag{5.2}
\]

The weaker but sometimes easier direct-mass route is to use
\(M_\lambda(E)\le M_\lambda(X)\) and the same inequality after replacement.
It closes H7 whenever the **sum of the selected sequential component masses**
is itself summable after history and placement counting.  Whether Balaban's
large-field powers beat that counting in three dimensions is the separate
computation in research note 14.  In four dimensions the published
source-free convergence bounds are not already the common-terminal,
adjacent-depth sequential estimate (5.1).

This is the exact stopping point: H7\(_\Sigma\) does not fail merely because
fiber denominators might be small.  It remains open because the published
construction has not been converted into the marked, sequential,
history-resolved bad-mass series (5.1), nor into the relative fiber bounds
(5.2).
