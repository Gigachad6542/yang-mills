# Transverse conditional means and quadratic \(R\)-bias

Status: **the probability lemmas, counterexamples, and scale reduction below
are proved here**. The conditional entropy, score, reflection, susceptibility,
and second-derivative estimates needed to apply them to Balaban's complete
\(R\)-operation are open.

## 1. The quantity left after source normalization

Fix one history, one exterior field, and one \(R\)-component \(\Lambda\). In
the notation of research note 10, normalize the two fiber densities to
probability laws

\[
 \mu=\widehat p_\Lambda,\qquad \nu=\widehat q_\Lambda.
\]

The source-blind replacement changes the conditional expectation of a terminal
test \(F_m\) by

\[
 B_\Lambda(F_m)=\mathbb E_\nu F_m-\mathbb E_\mu F_m.
 \tag{1.1}
\]

Equivalently, the first derivative of the exact source correction has the
opposite sign:

\[
 \partial_z\log D_\Lambda(0)
 =\mathbb E_\mu F_m-\mathbb E_\nu F_m.
 \tag{1.2}
\]

Let \(A_\Lambda\) denote a Lie-algebra coordinate in a local axial frame and
let \(\Pi^\perp\) remove infinitesimal gradient directions. The proposed Y6'
input is

\[
 \left\|\Pi^\perp\left(
   \mathbb E_\mu A_\Lambda-\mathbb E_\nu A_\Lambda
 \right)\right\|_\infty\le\eta_m,
 \qquad
 \sum_m\varepsilon_mL^m\eta_m<\infty.
 \tag{1.3}
\]

The large-field factor \(\varepsilon_m\) controls the mass of a history term.
It does not control the mean of the **normalized** conditional law in (1.1).
The lemmas below identify the additional input needed to control that mean.

## 2. Entropy does not create a geometric factor

### Proposition 1: entropy--subgaussian mean bound

Let \(X\) be real and suppose its centered moment-generating function under
\(\nu\) satisfies

\[
 \log\mathbb E_\nu e^{t(X-\mathbb E_\nu X)}
 \le \frac{\sigma^2t^2}{2},\qquad t\in\mathbb R.
 \tag{2.1}
\]

For every \(\mu\ll\nu\),

\[
 \left|\mathbb E_\mu X-\mathbb E_\nu X\right|
 \le\sqrt{2\sigma^2D(\mu\Vert\nu)}.
 \tag{2.2}
\]

#### Proof

The entropy variational inequality gives, for \(t>0\),

\[
 t(\mathbb E_\mu X-\mathbb E_\nu X)
 \le D(\mu\Vert\nu)+\frac{\sigma^2t^2}{2}.
\]

Optimize in \(t\) and repeat for \(-X\). \(\square\)

If \(\nu(dx)=Z^{-1}e^{-V(x)}dx\) on a convex fiber with
\(\nabla^2V\ge\kappa I\), then Bakry--Émery gives
\(\sigma^2\le\kappa^{-1}\) for a unit coordinate. Thus (2.2) yields the
required \(O(L^{-m})\) mean only after the new estimate

\[
 D(\mu\Vert\nu)=O(\kappa L^{-2m}).
 \tag{2.3}
\]

This scale is sharp: for two unit-variance Gaussians with means \(0\) and \(a\),
the entropy is \(a^2/2\) and (2.2) is an equality. Conditioning a Gaussian on
a large-field event gives a second warning. The event may have small mass while
the normalized conditional mean is order one, or larger. Large-field
suppression alone is therefore not an entropy estimate of the form (2.3).

## 3. A density tilt transfers the burden to a score estimate

### Proposition 2: interpolation identity

Assume

\[
 d\mu=\frac{e^U}{\nu(e^U)}d\nu,\qquad
 d\mu_t=\frac{e^{tU}}{\nu(e^{tU})}d\nu,\quad 0\le t\le1.
\]

Then

\[
 \mathbb E_\mu X-\mathbb E_\nu X
 =\int_0^1\operatorname{Cov}_{\mu_t}(X,U)\,dt.
 \tag{3.1}
\]

If every \(\mu_t\) satisfies a Poincaré inequality with constant \(C_t\), and
\(X\) is a unit Euclidean coordinate, then

\[
 \left|\mathbb E_\mu X-\mathbb E_\nu X\right|
 \le\int_0^1 C_t
       \left(\mathbb E_{\mu_t}|\nabla U|^2\right)^{1/2}dt.
 \tag{3.2}
\]

#### Proof

Differentiate \(\mathbb E_{\mu_t}X\) to obtain (3.1). Cauchy--Schwarz and the
two Poincaré inequalities for \(X\) and \(U\) give (3.2). \(\square\)

A usual Poincaré or Brascamp--Lieb inequality does not permit replacing
\(\nabla U\) by \(\Pi^\perp\nabla U\) merely because the tested coordinate is
transverse. Cross-Hessian terms can carry a longitudinal score into a
transverse mean. That replacement requires a product decomposition, an
invariant transverse subspace for the covariance operator, or a genuinely
directional covariance inequality.

There is also a sharp zeroth-order version. If
\(\operatorname{osc}U\le a\), then

\[
 \lVert\mu-\nu\rVert_{\rm TV}\le\tanh(a/4),\qquad
 |\mathbb E_\mu f-\mathbb E_\nu f|
 \le\operatorname{osc}(f)\tanh(a/4).
 \tag{3.3}
\]

Here \(\lVert\mu-\nu\rVert_{\rm TV}=\sup_A|\mu(A)-\nu(A)|\), so a real
bounded test obeys
\(|\mathbb E_\mu f-\mathbb E_\nu f|\le\operatorname{osc}(f)
\lVert\mu-\nu\rVert_{\rm TV}\).
The extremizer is a two-point likelihood ratio whose two values have ratio
\(e^a\). Hence this route still needs
\(\operatorname{osc}\log(d\mu/d\nu)=O(L^{-m})\).

### Proposition 3: Stein identity and transverse leakage

Suppose a law \(\nu\) on a Euclidean fiber has a Stein kernel \(\tau\):

\[
 \mathbb E_\nu[(A-\mathbb E_\nu A)\varphi(A)]
 =\mathbb E_\nu[\tau(A)\nabla\varphi(A)].
 \tag{3.4}
\]

For the tilt in Proposition 2,

\[
 \mathbb E_\mu A-\mathbb E_\nu A
 =\mathbb E_\mu[\tau\nabla U].
 \tag{3.5}
\]

Consequently,

\[
 \Pi^\perp(\mathbb E_\mu A-\mathbb E_\nu A)
 =\mathbb E_\mu[\Pi^\perp\tau\Pi^\perp\nabla U]
  +\mathbb E_\mu[\Pi^\perp\tau(1-\Pi^\perp)\nabla U].
 \tag{3.6}
\]

#### Proof

Use \(\varphi=e^U/\nu(e^U)\) in (3.4). \(\square\)

For a Gaussian with precision \(K\), (3.5) is the exact Schwinger--Dyson
identity \(\Delta m=K^{-1}\mathbb E_\mu\nabla U\). Formula (3.6) shows both
requirements explicitly: a small transverse score and control of longitudinal
to transverse mixing. Integration by parts does not manufacture either one.
Hard characteristic-function boundaries add flux terms and may make \(U\)
infinite, so (3.5) cannot be applied to Balaban's fiber pair without a new
support-compatible interpolation or explicit boundary analysis.

## 4. The symmetry route

### Proposition 4: odd-density defect

Let \(S\) be a measurable involution preserving a reference measure \(\lambda\).
Suppose \(X\circ S=-X\), \(E\circ S=E\), and \(O\circ S=-O\). For

\[
 d\mu=Z^{-1}e^{E+O}d\lambda,\qquad
 d\bar\mu=\bar Z^{-1}e^E\cosh(O)d\lambda,
\]

one has

\[
 \mathbb E_\mu X=\mathbb E_{\bar\mu}[X\tanh O].
 \tag{4.1}
\]

In particular, if \(|X|\le M\) and \(|O|\le a\), then

\[
 |\mathbb E_\mu X|\le M\tanh a.
 \tag{4.2}
\]

#### Proof

Pair a point with its image under \(S\). The \(X\cosh O\) contribution and the
\(\sinh O\) contribution to the normalization vanish by parity, leaving (4.1).
\(\square\)

More intrinsically,

\[
 |\mathbb E_\mu X|
 \le M\lVert\mu-S_*\mu\rVert_{\rm TV}.
 \tag{4.3}
\]

Thus exact invariance of both fiber laws makes both odd means vanish. An
approximate reflection defect \(O(L^{-m})\) is also sufficient.

Suppose instead that the conditioning/background datum is \(h\),
\(S_*\mu_h=\mu_{-h}\), and the same holds for \(\nu_h\). If the two mean maps
vanish at \(h=0\) and have derivative norms bounded by \(C_\mu,C_\nu\), then

\[
 \left|\mathbb E_{\mu_h}X-\mathbb E_{\nu_h}X\right|
 \le(C_\mu+C_\nu)|h|.
 \tag{4.4}
\]

This identifies a plausible mechanism for (1.3): exact cancellation at a flat
or pure-gauge background, followed by a uniform susceptibility estimate in a
background whose curvature contribution is geometrically small. A global
symmetry that changes the fixed exterior field or the history label is not
enough.

There is a useful paired-history relaxation. If histories \(h,h^*\) have
weights \(w,w^*\) and first-order biases \(b,b^*\), and

\[
 |w-w^*|\le\theta(w+w^*),\quad |b|,|b^*|\le M,\quad |b+b^*|\le r,
\]

then their normalized combined bias is at most

\[
 \theta M+\frac r2.
 \tag{4.5}
\]

This follows by writing
\(wb+w^*b^*=\frac12(w+w^*)(b+b^*)+\frac12(w-w^*)(b-b^*)\).
It allows a reflected-history pairing even when a termwise symmetry fails.

## 5. Exact reduction to a mean term and a quadratic remainder

### Proposition 5: transverse Taylor reduction

Assume that on the union of the two fiber supports,

\[
 F_m(A)=F_0+\ell_m(\Pi^\perp A)+R_m(A),
 \tag{5.1}
\]

with

\[
 \lVert\ell_m\rVert_1\le C_1\delta_\Lambda,\qquad
 |R_m(A)|\le C_2\delta_\Lambda^2W(A),\qquad
 \mathbb E_\mu W+\mathbb E_\nu W\le M_2.
 \tag{5.2}
\]

Then

\[
 \boxed{
 |B_\Lambda(F_m)|
 \le C_1\delta_\Lambda
 \left\|\Pi^\perp(\mathbb E_\mu A-\mathbb E_\nu A)\right\|_\infty
 +C_2M_2\delta_\Lambda^2.}
 \tag{5.3}
\]

#### Proof

Take expectations in (5.1), subtract, use \(\ell^1\)-\(\ell^\infty\) duality,
and bound the two remainders separately. \(\square\)

There is also a symmetry-only version. If \(\mu,\nu\) are \(S\)-invariant and

\[
 |F_m(A)+F_m(SA)-2F_0|
 \le C\delta_\Lambda^2W(A),
\]

then averaging \(F_m\) with \(F_m\circ S\) gives

\[
 |B_\Lambda(F_m)|
 \le\frac C2\delta_\Lambda^2
      (\mathbb E_\mu W+\mathbb E_\nu W).
 \tag{5.4}
\]

First-derivative control does **not** imply the quadratic remainder in (5.2).
On \([-1,1]\), let
\(\mu=(\delta_{-1}+\delta_1)/2\), \(\nu=\delta_0\), and
\(F_\delta(x)=\delta x^2\). The laws have the same mean and
\(\operatorname{osc}F_\delta=\delta\), but their expectation difference is
\(\delta\), not \(O(\delta^2)\). A two-insertion or second-Fréchet-derivative
estimate for the pulled-back loop observable is a separate theorem.

## 6. Scale count

The linear closed-loop lemma in research note 10 gives, conditionally on
regular propagation above the first affected level,

\[
 \delta_\Lambda
 \lesssim C(|\Lambda|+L^d)L^{(1-d)m}.
 \tag{6.1}
\]

Inserting (1.3) into (5.3), and then counting \(L^{dm}\) possible fine cells per
terminal block, gives the two scale contributions

\[
 \varepsilon_mL^m\eta_m
 \quad\hbox{and}\quad
 \varepsilon_m|\Lambda|^2L^{(2-d)m},
 \tag{6.2}
\]

up to fixed powers associated with the bounded component diameter. The first
is summable precisely under the weighted Y6' condition. The second is
geometrically summable in \(d=4\), provided component shapes and histories have
already been absorbed into \(\varepsilon_m\), the moment \(M_2\) is uniform, and
irregular-level costs are controlled.

Thus a valid proof may take either of two forms:

1. a transverse conditional-mean estimate with
   \(\sum_m\varepsilon_mL^m\eta_m<\infty\); or
2. exact cancellation of the projected first moment plus the genuinely
   quadratic observable estimate (5.2).

## 7. Audit against the published construction

The introductory CMP **122 I** formula identifies \(p=\rho(Z,V)\) and
\(q=\rho(Z'',V)\) on a restricted-variable fiber (Eq. (0.3), printed p. 176).
It proves positivity of their fiber masses, not closeness of their normalized
conditional laws. The actual denominator uses localized small-field parts
(p. 177), and the integration fiber varies by term/history (pp. 193--194).

CMP **119**, Section 1, builds the complete density with hard small-field and
large-field characteristic functions and repeated decompositions of unity
(printed pp. 246--253); Eq. (2.18) then sums over the resulting histories.
Consequently, mutual absolute continuity of \(\mu\) and \(\nu\), a finite
log-density tilt, and the absence of boundary flux cannot be assumed. They
would have to be proved for a refined pairing or replaced by the coupling or
reflection route.

CMP **98**, Proposition 5, controls a first functional derivative of the
iterated averaging map on a regular small-field domain. Even after combining
that estimate with the divergence-free loop-current cancellation, it supplies
neither:

- a comparison of the two conditional fiber laws;
- a transverse entropy, score, or susceptibility estimate;
- control of hard characteristic-function boundary terms;
- nor the second-derivative estimate in (5.2).

The exact additional Yang--Mills obligations are therefore:

1. construct common local axial coordinates, or an intrinsic replacement, on
   the relevant supports, including the first irregular level;
2. prove one of the sharp small inputs isolated above: conditional entropy
   \(O(L^{-2m})\), transverse score/odd defect \(O(L^{-m})\), or exact
   flat-background cancellation with \(O(L^{-m})\) susceptibility response;
3. control longitudinal-to-transverse covariance mixing and all cutoff-boundary
   flux terms;
4. prove a two-insertion bound for the nonlinear average and terminal loop,
   including mixed derivatives for several components;
5. retain these estimates uniformly through component shapes, exterior fields,
   histories, and the final history sum.

The strongest presently motivated route is exact cancellation at a flat or
pure-gauge background, possibly after pairing reflected histories, followed by
a uniform conditional susceptibility bound showing that only geometrically
small background curvature breaks the cancellation. This is a precise target,
not a consequence of the published source-free bounds.
