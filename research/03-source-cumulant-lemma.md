# Analytic source-to-cumulant reduction

Status: **proved here**.

This note isolates the complex-analytic step needed after a constructive RG
estimate. It prevents a recurring shortcut: convergence of partition functions
only at real sources does not justify convergence of their derivatives at the
origin.

## Notation

For a polyradius \(R=(R_1,\ldots,R_q)\), write

\[
 D_R=\{z\in\mathbb C^q:|z_j|<R_j\},\qquad
 R^{-\alpha}=\prod_{j=1}^qR_j^{-\alpha_j},\qquad
 \alpha!=\prod_{j=1}^q\alpha_j!.
\]

For a normalized holomorphic generating function \(F(0)=1\), define

\[
 \kappa_\alpha(F)=\partial^\alpha\operatorname{Log}F(0),
 \qquad |\alpha|\ge1,
\]

whenever the branch normalized by \(\operatorname{Log}F(0)=0\) exists. For a
moment-generating function these are the joint cumulants.

## Theorem A: summable connected increments

Let \(W_n:D_R\to\mathbb C\) be holomorphic and suppose

\[
 \lVert W_{n+1}-W_n\rVert_{D_R}\le\delta_n,
 \qquad \sum_{n=0}^\infty\delta_n<\infty.
\]

Then \(W_n\) converges uniformly to a holomorphic \(W_\infty\). For every
smaller polydisc \(D_r\Subset D_R\), every multi-index \(\alpha\), and every
\(z\in D_r\),

\[
 |\partial^\alpha(W_\infty-W_n)(z)|
 \le \alpha!\prod_{j=1}^q(R_j-r_j)^{-\alpha_j}
      \sum_{k=n}^\infty\delta_k.
\]

At the origin the sharper bound is

\[
 |\partial^\alpha(W_\infty-W_n)(0)|
 \le \alpha!R^{-\alpha}\sum_{k=n}^\infty\delta_k.
\]

### Proof

The summability hypothesis makes \(W_n\) uniformly Cauchy. Its limit is locally
uniform and hence holomorphic. Apply the multivariate Cauchy formula to
\(W_m-W_n\) on coordinate circles centered at \(z\), use the telescoping bound
\(\lVert W_m-W_n\rVert\le\sum_{k=n}^{m-1}\delta_k\), and let
\(m\to\infty\). At boundary radii, first shrink the circles and then take the
monotone limit. \(\square\)

If \(\delta_n\le A\vartheta^n\) with \(0<\vartheta<1\), the cumulant remainder
is at most

\[
 \alpha!R^{-\alpha}\frac{A\vartheta^n}{1-\vartheta}.
\]

## Theorem B: convergence of generating functions is enough

Let \(F_n\) be holomorphic on \(D_R\), let \(F_n(0)=1\), and suppose
\(F_n\to F\) locally uniformly. Then there is a polydisc
\(D_s\Subset D_R\) on which \(F\) and every sufficiently late \(F_n\) are
nonzero. Their normalized logarithms converge locally uniformly there, and

\[
 \kappa_\alpha(F_n)\longrightarrow\kappa_\alpha(F)
\]

for every fixed \(\alpha\).

More quantitatively, if \(F\) is nonzero on \(\overline{D_s}\), put

\[
 m_s=\inf_{\overline{D_s}}|F|,
 \qquad
 \varepsilon_n=\sup_{\overline{D_s}}|F_n-F|,
 \qquad q_n=\varepsilon_n/m_s<1.
\]

Then

\[
 \sup_{D_s}|\operatorname{Log}F_n-\operatorname{Log}F|
 \le-\log(1-q_n),
\]

and

\[
 |\kappa_\alpha(F_n)-\kappa_\alpha(F)|
 \le \alpha!s^{-\alpha}[-\log(1-q_n)].
\]

### Proof

Since \(F(0)=1\), continuity gives a closed polydisc on which \(F\ne0\).
For late \(n\),

\[
 \left|\frac{F_n}{F}-1\right|\le q_n<1.
\]

Hence \(F_n\ne0\) there and the normalized logarithms obey

\[
 \operatorname{Log}F_n-\operatorname{Log}F
 =\log\!\left(1+\frac{F_n-F}{F}\right).
\]

The logarithm power series bounds the norm by
\(\sum_{k\ge1}q_n^k/k=-\log(1-q_n)\). Cauchy's estimate gives the derivative
bound. \(\square\)

The same proof yields a useful relative-Cauchy form. If \(F_n,F_m\) are
nonzero on \(D_R\) and

\[
 q_{nm}=\sup_{D_R}\left|\frac{F_n}{F_m}-1\right|<1,
\]

then

\[
 |\kappa_\alpha(F_n)-\kappa_\alpha(F_m)|
 \le \alpha!R^{-\alpha}[-\log(1-q_{nm})].
\]

## Theorem C: bounded observables give a uniform logarithmic disc

Let \(X_{n,1},\ldots,X_{n,q}\) be random variables with deterministic bounds
\(|X_{n,j}|\le B_j\), uniform in \(n\), and define

\[
 Z_n(z)=\mathbb E\exp\!\left(\sum_jz_jX_{n,j}\right).
\]

Then \(Z_n\) is entire, \(Z_n(0)=1\), and

\[
 |Z_n(z)-1|
 \le \exp\!\left(\sum_jB_j|z_j|\right)-1.
\]

Consequently, any polyradius \(\rho\) satisfying

\[
 S_\rho:=\sum_jB_j\rho_j<\log2
\]

is a cutoff-independent zero-free domain. The normalized logarithm
\(W_n=\operatorname{Log}Z_n\) is holomorphic on \(D_\rho\) and

\[
 \lVert W_n\rVert_{D_\rho}
 \le-\log(2-e^{S_\rho}).
\]

Moreover, if
\(\lVert Z_n-Z_m\rVert_{D_\rho}\le\varepsilon_{nm}\), then

\[
 \lVert W_n-W_m\rVert_{D_\rho}
 \le\frac{\varepsilon_{nm}}{2-e^{S_\rho}}.
\]

### Proof

Boundedness permits differentiation under the expectation on every compact
source set, so \(Z_n\) is entire. With \(w=\sum_jz_jX_{n,j}\),

\[
 |Z_n(z)-1|\le\mathbb E|e^w-1|
 \le\mathbb E(e^{|w|}-1)
 \le e^{\sum_jB_j|z_j|}-1.
\]

On \(D_\rho\) the right side is \(\eta=e^{S_\rho}-1<1\), so the image lies
in the disc \(B(1,\eta)\), away from zero and the principal-log cut. Its log
series has norm at most \(-\log(1-\eta)\). Integrating \(1/w\) along the segment
between \(Z_m(z)\) and \(Z_n(z)\), which stays at distance at least
\(1-\eta=2-e^{S_\rho}\) from zero, proves the last estimate. \(\square\)

Thus P5 in the project ledger is closed for bounded block observables. The open
RG problem is uniform convergence of \(Z_n\), not elementary source analyticity.

## Theorem D: extensive factorial bound

Suppose \(F(0)=1\), \(F\) is nonzero on \(D_R\), and

\[
 \sup_{D_R}|F|\le e^{As}
\]

for \(A,s\ge0\). Then, for \(0<\theta<1\),

\[
 \sup_{D_{\theta R}}|\operatorname{Log}F|
 \le\frac{2\theta}{1-\theta}As,
\]

and hence

\[
 |\kappa_\alpha(F)|
 \le\frac{2\theta}{1-\theta}As\,
      \alpha!(\theta R)^{-\alpha}.
\]

### Proof

Fix \(z\in D_{\theta R}\), put \(w=z/\theta\), and define
\(h(\zeta)=\operatorname{Log}F(\zeta w)\). Then \(h(0)=0\) and
\(\operatorname{Re}h\le As=:B\). For \(B>0\), the function

\[
 g(\zeta)=\frac{h(\zeta)}{2B-h(\zeta)}
\]

maps the unit disc into itself and vanishes at zero. Schwarz's lemma gives
\(|h(\theta)|\le2B\theta/(1-\theta)\). The case \(B=0\) follows from the
maximum principle. Apply the multivariate Cauchy estimate. \(\square\)

## Sharpness and counterexamples

- Real-source convergence is insufficient:
  \(F_n(z)=1+n^{-1/2}\sin(nz)\) converges uniformly to \(1\) on every bounded
  real interval, while \((\log F_n)'(0)=\sqrt n\).
- Normalization or a uniform nonzero basepoint matters:
  \(F_n(z)=z+1/n\to z\), but \((\log F_n)'(0)=n\).
- A full-disc logarithm cannot be inferred across a zero:
  \(F(z)=1-2z\) vanishes at \(1/2\), and its \(k\)-th log derivative at zero is
  \(-(k-1)!2^k\).
- Zero-freeness without a size estimate gives no uniform cumulant bound:
  \(F_n(z)=e^{nz}\) has first cumulant \(n\).
- Local uniform convergence controls each fixed cumulant, not orders growing
  with \(n\): \(F_n(z)=1+nz^n\to1\) locally uniformly on the unit disc, while
  its \(n\)-th log derivative at zero equals \(n\,n!\).

## Application boundary

These theorems are implications. They provide no estimate comparing two lattice
cutoffs and no variance lower bound. Those are P4 and P6 in the project ledger.
