# Four-dimensional Gaussian power counting for a rooted even defect

Status:

- **Proved exactly:** the block-flux identity (2.1), the Fourier aliasing
  formula (2.5), the Gaussian insertion identities (3.3)--(3.4), the
  placement-sum identity (3.8), and the fixed-exterior formulas
  (5.1)--(5.4).
- **Computation with an analytic scaling derivation:** at a registered local
  placement, the fine-to-terminal flux covariance is \(M^{-2}\), and the
  connected covariance of a terminal small loop with one even quadratic
  defect is \(M^{-4}=L^{-4m}\).  The fitted exponent is \(3.940907\) on
  \(M=4,8,16,32\), \(3.979797\) on \(M=8,16,32\), and \(3.992215\) on the
  final pair.  The missing step for a completely analytic theorem is a
  pointwise convergence proof for the discrete Hodge projection of the
  rescaled nonsmooth block kernel.
- **Correction to the proposed fixed-exterior conclusion:** for bounded
  exterior means, the terminal shift is generically \(M^{-2}\), not order
  one, while the centered/averaged response is \(M^{-4}\).  What does not
  decay is the normalized *local fiber shift*, or the supremum over the
  unbounded exterior field.  An order-one terminal shift requires exterior
  means of order \(M^2\).  Thus the literal claim that the same terminal
  observable has an order-one shift at every bounded fixed exterior field is
  false in this model.
- **Numerical verification:** the real-space covariance obtained from an
  eigendecomposition of \(d^*d\) agrees with (2.5) to at most
  \(3.4\times10^{-16}\).  No pseudoinverse is used.

Here \(M=L^m\), so the powers of \(M\) below are exactly the powers in the
depth \(m\) requested by T8.

## 1. Model and Fourier conventions

Let the fine torus be

\[
 \Lambda_n=(\mathbb Z/n\mathbb Z)^4,
 \qquad n=n_0M,
 \qquad M=L^m,
\]

and let \(A\) be a real noncompact \(U(1)\) one-form.  For
\(a=(\mu,\nu)\), \(\mu<\nu\), write \(F_a=(dA)_{\mu\nu}\).  The Gaussian
action is

\[
 S(A)={\beta\over2}\sum_{x\in\Lambda_n}\sum_a F_a(x)^2,
 \qquad \beta=g^{-2}.
 \tag{1.1}
\]

Gauge zero modes cause no problem for flux observables.  Put

\[
 r_j(p)=e^{ip_j}-1,
 \qquad
 R_{(\mu\nu),j}(p)
 =r_\mu(p)\delta_{\nu j}-r_\nu(p)\delta_{\mu j}.
 \tag{1.2}
\]

For \(p\ne0\), the fine-flux covariance is \(\beta^{-1}P_2(p)\), where

\[
 P_2(p)={R(p)R(p)^*\over |r(p)|^2},
 \qquad P_2(0)=0.
 \tag{1.3}
\]

This is the orthogonal projection of two-forms onto the exact two-forms.  In
particular \(P_2^2=P_2=P_2^*\), and its rank is three at every nonzero
momentum.

## 2. Exact propagation through the linear block map

Let \(Q\) be the linearization of Balaban's average in research note 10,
(7.1)--(7.2).  The radial paths cancel after applying the coarse exterior
derivative.  Iterating \(m\) times gives the exact identity

\[
 \Phi_a(Y):=(d_cQ^mA)_a(Y)
 ={1\over M^4}
 \sum_{u\in[0,M)^4}\sum_{s,t=0}^{M-1}
 F_a(MY+u+s e_\mu+t e_\nu).
 \tag{2.1}
\]

Thus the answer is independent of whether the radial contour is axis ordered
forward or backward.  Define

\[
 D_M(q)=\sum_{s=0}^{M-1}e^{-iqs}.
 \tag{2.2}
\]

The Fourier multiplier of (2.1) is

\[
 \widehat w_a(p)
 =M^{-4}\left(\prod_{j=0}^3D_M(p_j)\right)
 D_M(p_\mu)D_M(p_\nu).
 \tag{2.3}
\]

Let \(K\in(2\pi/n_0)\mathbb Z_{n_0}^4\) be a terminal momentum, and set

\[
 p_\ell={K+2\pi\ell\over M},
 \qquad \ell\in[0,M)^4.
 \tag{2.4}
\]

With unnormalized Fourier transforms on both tori, the six-by-six terminal
flux covariance is

\[
 \boxed{
 C_{ab}^{(M)}(K)
 ={1\over\beta M^4}
 \sum_{\ell\in[0,M)^4}
 (P_2)_{ab}(p_\ell)\,
 \overline{\widehat w_a(p_\ell)}
 \widehat w_b(p_\ell).}
 \tag{2.5}
\]

Equations (2.1) and (2.5) are checked independently in Section 6.

## 3. One rooted even defect

Fix a terminal plaquette \(X=\Phi_a(Y)\), and a fine plaquette
\(Z=F_b(z)\).  Their cross covariance is

\[
 c_b^{(M)}(z)
 ={1\over\beta n^4}\sum_p
 e^{ip\cdot(MY-z)}
 \overline{\widehat w_a(p)}(P_2)_{ab}(p).
 \tag{3.1}
\]

There is a parity point that must be stated first:

\[
 \operatorname{Cov}(X,Z^2)=0.
 \tag{3.2}
\]

The terminal flux is odd and the defect is even.  The nonzero gauge-invariant
small-loop test is \(W_t=\cos(tX)\), or equivalently its leading plaquette
energy \(X^2\).  Wick's formula gives the exact identities

\[
 \operatorname{Cov}(X^2,Z^2)=2c_b^{(M)}(z)^2,
 \tag{3.3}
\]

and

\[
 \boxed{
 \operatorname{Cov}(\cos(tX),Z^2)
 =-t^2e^{-t^2\operatorname{Var}(X)/2}
 c_b^{(M)}(z)^2.}
 \tag{3.4}
\]

Subtracting \(\mathbb E Z^2\) from the defect does not change either
covariance.  For the hypercubic local action defect

\[
 H_{4,z}={\beta\over2}\sum_b F_b(z)^2,
 \tag{3.5}
\]

one sums (3.4) over the six orientations and multiplies by \(\beta/2\).

### The scale

In real space, the kernel in (2.1) is a product of two triangular kernels in
the \(\mu,\nu\) directions and two boxes in the transverse directions:

\[
 w_{a,M}(x)=M^{-4}T_M(x_\mu)T_M(x_\nu)
 \mathbf1_M(x_\rho)\mathbf1_M(x_\sigma),
 \tag{3.6}
\]

where \(T_M=\mathbf1_M*\mathbf1_M\).  Its amplitude is \(M^{-2}\).
Equivalently, after writing \(k=Mp\), (2.3) has the exact rescaled form

\[
 \widehat w_a(k/M)=M^2W_{a,M}(k),
 \qquad
 c_b^{(M)}(z)=\beta^{-1}M^{-2}G_{ab,M}(z/M-Y).
 \tag{3.7}
\]

The discrete Hodge projector is an order-zero multiplier.  Its continuum
limit applied to the triangle--triangle--box--box profile is finite and is
nonzero at the registered placements used below.  This gives the analytic
power count \(c_M\sim M^{-2}\), hence (3.4) is \(M^{-4}\).  The scripts
establish the nonzero limit and the exponent numerically; they do not supply
a stand-alone pointwise singular-integral convergence proof at every edge of
the block kernel.

There is an important marginality check.  Since \(P_2\) is a projection,
Parseval gives the exact identity

\[
 \sum_{z,b}\beta\,c_b^{(M)}(z)^2=\operatorname{Var}(X).
 \tag{3.8}
\]

Thus a single rooted \(F^2\) insertion is \(M^{-4}\), but its \(O(M^4)\)
placements sum to order one.  The translation-summed \(F^2\) defect is
marginal, as it must be in four dimensions.  The rooted calculation by
itself is therefore not a summability theorem for all component placements.

## 4. Numerical power

Take \(n_0=2\), \(\beta=1\), \(a=b=(0,1)\), \(Y=0\), and, for even \(M\),

\[
 z_M=(M-1,M-1,M/2,M/2).
 \tag{4.1}
\]

This is one of the maximum-magnitude placements for \(M=2,4,8,16\), up to
reflections and translations.  The exact Fourier sums give:

| \(M\) | \(c_M\) | \(M^2c_M\) | \(\operatorname{Var}(X)\) | \(|\operatorname{Cov}(\cos X,F_{01}(z_M)^2)|\) | ratio |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.171875000e-1 | 0.468750000 | 0.190104167 | 1.248768639e-2 | |
| 4 | 3.431509322e-2 | 0.549041492 | 0.126852084 | 1.105159055e-3 | 11.2994 |
| 8 | 8.985428941e-3 | 0.575067452 | 0.110128770 | 7.641233474e-5 | 14.4631 |
| 16 | 2.269421658e-3 | 0.580971944 | 0.105766677 | 4.884987402e-6 | 15.6423 |
| 32 | 5.687304727e-4 | 0.582380004 | 0.104656808 | 3.069637274e-7 | 15.9139 |

The response ratios tend to \(2^4=16\).  A log--log fit on
\(M=4,8,16,32\) gives exponent \(3.940907\); the last three points give
\(3.979797\), and the last ratio gives \(3.992215\).  Independently,
\(M^2c_M\to0.582\ldots\).  Hence the actual power is the proposed

\[
 L^{-4m}.
 \tag{4.2}
\]

The table is produced by `research/scripts/t8_gauss4d.py`.

## 5. Fixed exterior data: exact correction to the premise

Let \(X,Z\) now denote a conditional jointly Gaussian pair at fixed exterior
data, with conditional means \(\bar x,\bar z\), centered variance
\(V=\operatorname{Var}(X)\), and centered covariance \(c\).  Direct
differentiation of the Gaussian characteristic function gives

\[
 \operatorname{Cov}(e^{itX},Z^2\mid\mathrm{ext})
 =(2it\bar zc-t^2c^2)e^{it\bar x-t^2V/2},
 \tag{5.1}
\]

and therefore

\[
 \boxed{
 \operatorname{Cov}(\cos(tX),Z^2\mid\mathrm{ext})
 =e^{-t^2V/2}
 \left[-2t\bar zc\sin(t\bar x)-t^2c^2\cos(t\bar x)\right].}
 \tag{5.2}
\]

At a centered or symmetry-averaged exterior, the term linear in \(c\)
vanishes and (5.2) has the \(M^{-4}\) gain.  At a generic bounded exterior,
it is only \(M^{-2}\).  This is precisely the extra cancellation that is lost
when the exterior average in research note 13 is replaced by a pointwise
absolute value.

The normalized local fiber shift itself need not be small.  In one Gaussian
fiber coordinate, let

\[
 p_h=N(h,s^2),
 \qquad
 dq_h={e^{-\lambda Z^2/2}\,dp_h\over p_h(e^{-\lambda Z^2/2})}.
\]

Then

\[
 q_h=N\left({h\over1+\lambda s^2},
             {s^2\over1+\lambda s^2}\right),
 \qquad
 \mathbb E_{q_h}Z-\mathbb E_{p_h}Z
 =-{\lambda s^2h\over1+\lambda s^2}.
 \tag{5.3}
\]

For \(h=s^2=\lambda=1\), the mean shift is \(-1/2\), and the local loop shift
is

\[
 \mathbb E_{q_1}\cos Z-\mathbb E_{p_1}\cos Z
 =e^{-1/4}\cos(1/2)-e^{-1/2}\cos1
 =0.355752072\ldots,
 \tag{5.4}
\]

independently of \(m\).  Exact block propagation multiplies its linear
terminal effect by a coefficient \(a_M\asymp M^{-2}\).  Consequently:

- for \(h=0\), the terminal shift is \(O(M^{-4})\);
- for a fixed nonzero bounded \(h\), it is generically \(O(M^{-2})\);
- no estimate uniform in the noncompact exterior field can decay: choosing
  \(h_M\asymp a_M^{-1}\asymp M^2\) leaves an order-one terminal shift.

For \(a_M=M^{-2}\), \(s^2=\lambda=1\), and exterior loop phase \(0.7\), the script
`research/scripts/t8_fixed_exterior.py` gives terminal shifts

| \(M\) | \(h=0\) | \(h=1\) | \(h=M^2\) |
|---:|---:|---:|---:|
| 2 | 1.16739412e-2 | 1.04250333e-1 | 4.81620284e-1 |
| 4 | 7.45822914e-4 | 2.19131983e-2 | 4.90597153e-1 |
| 8 | 4.66779887e-5 | 5.14836048e-3 | 4.91164406e-1 |
| 16 | 2.91762471e-6 | 1.26551171e-3 | 4.91199883e-1 |
| 32 | 1.82352522e-7 | 3.15014986e-4 | 4.91202101e-1 |
| 64 | 1.13970364e-8 | 7.86683421e-5 | 4.91202240e-1 |

This proves the useful fixed-exterior statement, but also prevents the
stronger false formulation: exact propagation does not permit an order-one
terminal shift at one fixed bounded exterior background.

## 6. Independent real-space checks

The script `research/scripts/t8_kernel_check.py` constructs \(Q\) directly
from radial paths and compares \(d_cQA\) with (2.1) on random real fields.

| fine side | \(L\) | radial order | maximum error |
|---:|---:|:---|---:|
| 4 | 2 | forward | 1.33e-15 |
| 4 | 2 | reverse | 1.33e-15 |
| 6 | 3 | forward | 3.11e-15 |
| 6 | 3 | reverse | 2.22e-15 |

For the covariance check, `research/scripts/t8_brute_check.py` forms the
dense real-space matrix \(d^*d\), diagonalizes it, discards only eigenvalues
below \(10^{-10}\lambda_{\max}\), and evaluates

\[
 (d_cQ^m)(d^*d)^+(d_cQ^m)^*/\beta
\]

from the retained eigenpairs.  The notation \((d^*d)^+\) describes the
spectral inverse; the code does **not** call `pinv`.

| \(n_0\) | \(L\) | radial order | retained rank | expected rank | max Fourier--real error |
|---:|---:|:---|---:|---:|---:|
| 3 | 1 | forward | 240 | 240 | 3.33e-16 |
| 2 | 2 | forward | 765 | 765 | 1.65e-16 |
| 2 | 2 | reverse | 765 | 765 | 1.65e-16 |

The expected fine-lattice physical rank is
\(3(n^4-1)\).  The unblocked \(n_0=3\) case checks genuinely complex Fourier
phases and off-diagonal orientation entries; the \(L=2\) cases check the
exact block propagation.

## 7. Consequences and limits

1. The Gaussian model realizes the mechanism proposed after research note
   13: exterior averaging/centering kills the term linear in the propagated
   influence, and the surviving even connected response contains two
   factors \(M^{-2}\).
2. The gain is local.  Equation (3.8) shows why the placement sum of a
   dimension-four defect is marginal in four dimensions.  A proof of the
   Yang--Mills \(R\)-bias still needs its activity weights and cancellations.
3. A pointwise fixed-exterior estimate cannot simply be assigned the
   \(M^{-4}\) power.  At bounded generic backgrounds it has only \(M^{-2}\),
   and the noncompact model has no decaying uniform exterior supremum.
4. This calculation has no non-Abelian commutators, large-field regions,
   hard cutoffs, running coupling, or signed history expansion.  It tests
   the geometric propagation and Gaussian connected-correlation mechanism,
   not the complete Robs hypothesis.

To reproduce all numbers, run

```text
python3 research/scripts/t8_gauss4d.py
python3 research/scripts/t8_fixed_exterior.py
python3 research/scripts/t8_kernel_check.py
python3 research/scripts/t8_brute_check.py
```
