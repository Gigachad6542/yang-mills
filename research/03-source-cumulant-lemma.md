# Analytic source-to-cumulant reduction

Status: **proved here**.

This note records the complex-analytic step needed after the constructive RG has
provided a uniform source estimate.  It prevents a recurring logical shortcut:
pointwise convergence of partition functions at real sources does not by itself
justify convergence of their derivatives at the origin.

## Notation

For a polyradius \(R=(R_1,\ldots,R_q)\), write

\[
 D_R=\{z\in\mathbb C^q:|z_j|<R_j\},\qquad
 R^{-\alpha}=\prod_{j=1}^qR_j^{-\alpha_j},\qquad
 \alpha!=\prod_{j=1}^q\alpha_j!.
\]

If (X_n=(X_{n,1},\ldots,X_{n,q})) is a random vector with exponential
moments near the origin, its normalized generating function and connected
generating function are

\[
 Z_n(z)=\mathbb E e^{z\cdot X_n},\qquad W_n(z)=\log Z_n(z),
\]

and \(\partial^\alpha W_n(0)\) is the joint cumulant with multiplicities
specified by \(\alpha\).

## Theorem A: summable holomorphic increments

Let (W_n:D_R\to\mathbb C) be holomorphic.  Suppose

\[
 \|W_{n+1}-W_n\|_{D_R}\le\delta_n,
 \qquad \sum_{n=0}^\infty\delta_n<\infty.
\]

Then:

1. (W_n\) converges uniformly on (D_R) to a holomorphic function
   (W_\infty\).
2. For every smaller polydisc (D_r) with (0<r_j<R_j), every multi-index
   \(\alpha\), and every (z\in D_r),
   \[
   |\partial^\alpha(W_\infty-W_n)(z)|
   \le \alpha!\prod_{j=1}^q(R_j-r_j)^{-\alpha_j}
       \sum_{k=n}^\infty\delta_k.
   \]
3. In particular, all fixed cumulants \(\partial^\alpha W_n(0)\) converge.  At
   the origin one may use the sharper bound
   \[
   |\partial^\alpha(W_\infty-W_n)(0)|
   \le \alpha!R^{-\alpha}\sum_{k=n}^\infty\delta_k.
   \]

### Proof

The summability hypothesis makes (W_n) uniformly Cauchy, hence it has a uniform
limit (W_\infty).  A locally uniform limit of holomorphic functions of several
complex variables is holomorphic.  For (z\in D_r), the distinguished polytorus

\[
 \{\zeta:|\zeta_j-z_j|=R_j-r_j,\ 1\le j\le q\}
\]

lies in the closure of (D_R) after replacing (R) by an arbitrarily smaller
polyradius and passing to the limit.  The multivariate Cauchy formula applied to
(W_m-W_n) gives

\[
 |\partial^\alpha(W_m-W_n)(z)|
 \le \alpha!\prod_j(R_j-r_j)^{-\alpha_j}
      \|W_m-W_n\|_{D_R}.
\]

The telescoping estimate bounds the final norm by
\(\sum_{k=n}^{m-1}\delta_k\).  Letting (m\to\infty\) proves the second
claim.  Centering the Cauchy polytorus at zero with radii (R_j), again by an
interior approximation if the supremum is over the open polydisc, proves the
third. \(\square\)

## Corollary A.1: geometric RG remainder

If \(\delta_n\le A\vartheta^n\) for (0<\vartheta<1), then

\[
 |\partial^\alpha(W_\infty-W_n)(0)|
 \le \alpha!R^{-\alpha}\frac{A\vartheta^n}{1-\vartheta}.
\]

Thus a geometric bound on connected generating-functional increments gives the
same geometric cutoff error for each fixed cumulant, with the expected analytic
factorial.

## Theorem B: passing from (Z_n) to a logarithm

Let (Z_n:D_R\to\mathbb C) be holomorphic, (Z_n(0)=1), and suppose a single
(0<\eta<1) satisfies

\[
 \|Z_n-1\|_{D_R}\le\eta\quad\text{for every }n.
\]

Then the principal power-series branch (W_n=\log Z_n), normalized by
(W_n(0)=0), is holomorphic on (D_R).  Moreover,

\[
 \|W_n-W_m\|_{D_R}
 \le \frac{1}{1-\eta}\|Z_n-Z_m\|_{D_R}.
\]

Consequently, a summable increment bound for (Z_n) implies Theorem A for
(W_n), with every increment enlarged by at most ((1-\eta)^{-1}).

### Proof

Every value of every (Z_n) lies in the convex disc
\(B(1,\eta)\subset\mathbb C\setminus(-\infty,0]\), so the principal logarithm
is holomorphic there.  For fixed (z), integrate the derivative of the logarithm
along the line segment from (Z_m(z)) to (Z_n(z)):

\[
 \log Z_n(z)-\log Z_m(z)
 =\int_0^1\frac{Z_n(z)-Z_m(z)}
 {(1-s)Z_m(z)+sZ_n(z)}\,ds.
\]

The denominator has modulus at least (1-\eta), which proves the bound. \(\square\)

## Why the complex neighborhood is indispensable

Uniform convergence on a real interval need not imply convergence of derivatives.
For example, (f_n(z)=\sin(nz)/n\) converges uniformly to zero on every bounded
real interval, while (f_n'(0)=1).  It is not locally uniformly bounded on a
fixed complex neighborhood.  Complex-source control is therefore substantive,
not cosmetic.

Likewise (Z_n(0)=1) alone gives no uniform logarithmic domain:
(Z_n(z)=1+nz) has a zero at (-1/n), and derivatives of \(\log Z_n\) diverge.
The RG proof must produce either a zero-free complex domain or (W_n) directly as
a convergent connected-polymer series.

## Application boundary

Theorem A proves an implication only.  It supplies no estimate on
\(W_{n+1}-W_n\), no nonvanishing theorem, and no nondegeneracy of the limiting
covariance.  Those are precisely P4, P5, and P6 in the proof-obligation ledger.
