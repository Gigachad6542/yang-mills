commit 4f867bae0724a1d1e30d79c91a5ce7d93a44ded5
Author: zooatepoo <dwschoolacc@gmail.com>
Date:   Tue Sep 29 00:15:43 2026 -0700

    [T2][proof] Prove symmetric-average H6 lemmas
    
    Transcribe CMP 109 Eq. (0.4) from the primary scan and prove its total-contour-weight rough bound. At the trivial background, prove exact divergence cancellation and the sharp l-infinity, l-one, and l-two current contractions. Prove the literal first-layer image-path bound on an explicit fixed branch-gap event with a concrete SU(2) constant, and exhibit the -I branch-cut obstruction without that event.

diff --git a/research/15-h6-symmetric-average.md b/research/15-h6-symmetric-average.md
new file mode 100644
index 0000000..4642bff
--- /dev/null
++ b/research/15-h6-symmetric-average.md
@@ -0,0 +1,451 @@
# The symmetric CMP 109 average: rough and trivial-background H6 bounds

Status: **the three estimates stated below are proved here.**  The rough bound
is a global unitary-matrix estimate for the stated spectral convention; at the
branch cut, the formula need not be a continuous \(SU(2)\)-valued map.  The
linear current estimates are at the identity background.  The first-layer
path estimate is proved at trivial exterior field on an explicit fixed
branch-gap regular event.  This note does not estimate the probability of the
complement of that event, propagate through curved backgrounds, or prove the
placement-summed H6\(_\Sigma\) bound.

## 1. The formula and the OCR reconstruction

Let \(c=\langle c_-,c_+\rangle\) be a positively oriented coarse bond of
length \(L\) in direction \(\mu\).  For \(x\in B(c_-)\), let
\(x'=x+Le_\mu\), and let \([x,x']\) be the translate of \(c\) starting at
\(x\).  CMP **109**, p. 253, defines \(G(y,x)\) to be the family of shortest
axis-ordered paths from \(y\) to \(x\), one for each ordering of the nonzero
coordinate displacements.  Thus, if \(r\) coordinate displacements are
nonzero, \(|G(y,x)|=r!\); for \(x=y\), use the singleton empty contour.
Write

\[
 \ell(c,x,\Gamma,\Gamma')
 =\Gamma\,[x,x']\,(-\Gamma'),
 \qquad
 \Gamma\in G(c_-,x),\quad
 \Gamma'\in G(c_+,x').
 \tag{1.1}
\]

This is a path from \(c_-\) to \(c_+\).  Put

\[
 w_{c,x,\Gamma,\Gamma'}
 =\frac{L^{-d}}
 {|G(c_-,x)|\,|G(c_+,x')|}.
 \tag{1.2}
\]

Since \(|B(c_-)|=L^d\), these are nonnegative and sum to one.  The
Euclidean-symmetric convex-log average in CMP **109**, Eq. (0.4), is

\[
 \overline U(c)=M(U,c)=
 \exp\!\left\{
  i\!\sum_{x,\Gamma,\Gamma'}
  w_{c,x,\Gamma,\Gamma'}
  \frac1i\log\!\left[
   U(\ell(c,x,\Gamma,\Gamma'))U(c)^{-1}
  \right]
 \right\}U(c).
 \tag{1.3}
\]

The notation \(M(U,c)\) in (0.4) names this explicit bond average.  It is not
the axiomatic finite-set group mean \(M(\{U_j\})\) introduced immediately
afterward and used in Eq. (0.12).

Here \(U(c)\) is the transporter along the straight central path and the
spectral logarithm is the one used in CMP **98**, Eq. (22), with arguments in
\((-\pi,\pi]\).  In particular, for a unitary loop holonomy,

\[
 Z=\frac1i\log U_{\rm loop}
 \quad\hbox{is Hermitian and}\quad
 \|Z\|_{\rm op}\le\pi.
 \tag{1.4}
\]

The local OCR file `cmp109.md` garbles
\(\overline U(c)=M(U,c)=\exp\), \(x\in B(c_-)\), \(L^{-d}\), the prime on
\(x'\), both reciprocal cardinalities, \(1/i\), the union signs, and the final
right factor.  Formula (1.3) records the reconstruction from the primary scan.
In the printed formula the logarithm contains
\(U(\Gamma\cup[x,x']\cup(-\Gamma')\cup(-c))\), which is exactly
\(U(\ell)U(c)^{-1}\).  No claim below depends on any alternative reading of
the garbled OCR.

## 2. A global rough-step bound

For a fine-bond set \(S\), define its total affected contour weight at \(c\) by

\[
 \omega_c(S)=
 \sum_{x,\Gamma,\Gamma'}
 w_{c,x,\Gamma,\Gamma'}
 \mathbf1\{\ell(c,x,\Gamma,\Gamma')\cap S\ne\varnothing\}.
 \tag{2.1}
\]

### Proposition 1: rough support bound for Eq. (0.4)

Let \(U,U'\) be two compact-group gauge fields, represented unitarily, which
agree off \(S\).  If \(S\) is disjoint from the central path \(c\), then

\[
 \|\overline U(c)-\overline U'(c)\|_{\rm op}
 \le \min\{2,\,2\pi\omega_c(S)\}.
 \tag{2.2}
\]

If \(S\) meets \(c\), the universal bound is \(2\).

#### Proof

When \(S\cap c=\varnothing\), the right factor \(U(c)\) is unchanged.  A
summand in (1.3) is unchanged unless its contour \(\ell\) meets \(S\).  By
(1.4), the difference of the two corresponding Hermitian logarithms has
operator norm at most \(2\pi\).  Hence the two Hermitian exponents \(X,X'\)
satisfy

\[
 \|X-X'\|_{\rm op}\le2\pi\omega_c(S).
\]

The Duhamel formula gives
\(\|e^{iX}-e^{iX'}\|_{\rm op}\le\|X-X'\|_{\rm op}\).  The difference of two
unitaries is always at most two, proving (2.2).  If \(S\) meets the central
path, both the loop logarithms and the final factor may change, but both
outputs remain unitary, so the last bound still applies. \(\square\)

Thus the counting variable for the actual four-dimensional average is not the
number of corner contours in CMP **98**, Eq. (42), but the normalized total
weight (2.1) of the symmetric contour triples.

The total weight also has a simple global bound.  In the standard odd-\(L\)
block partition, a fixed fine bond can occur in symmetric radial paths for at
most the \(2d\) coarse bonds incident to its block.  Its normalized weight in
each such radial family is at most one.  If its direction is \(\mu\), at most
\(L\) translated length-\(L\) segments contain it, each with weight \(L^{-d}\).
Consequently, by the union bound,

\[
 \sum_c\omega_c(S)\le(2d+L^{1-d})|S|.
 \tag{2.3}
\]

At most \(|S|\) central transporters meet \(S\), so Proposition 1 implies

\[
 \sum_c\|\overline U(c)-\overline U'(c)\|_{\rm op}
 \le\left[2+2\pi(2d+L^{1-d})\right]|S|.
 \tag{2.4}
\]

## 3. Exact linearization at the trivial background

Denote the nonlinear one-step map (1.3) by \(\mathcal Q\), and put
\(Q_{\rm lin}=D\mathcal Q(1)\).

Let \(U_b(\epsilon)=e^{i\epsilon A_b}\), with \(A\) an antisymmetric
Hermitian fine-bond field.  For an oriented path \(\gamma\), write
\(A(\gamma)\) for the signed sum of \(A_b\) along \(\gamma\).  Linearizing
(1.3) at \(U=1\) gives

\[
 (Q_{\rm lin}A)(c)=\Lambda_{\rm sym}(c_-)+S(A)(c)
                    -\Lambda_{\rm sym}(c_+),
 \tag{3.1}
\]

where

\[
 \begin{aligned}
 \Lambda_{\rm sym}(y)
 &=L^{-d}\sum_{x\in B(y)}
   \frac1{|G(y,x)|}\sum_{\Gamma\in G(y,x)}A(\Gamma),\\
 S(A)(c)
 &=L^{-d}\sum_{x\in B(c_-)}A([x,x']).
 \end{aligned}
 \tag{3.2}
\]

Indeed, the independent \(\Gamma'\)-sum is one in the first endpoint term and
the independent \(\Gamma\)-sum is one in the second.  Translation
\(x\mapsto x'\) identifies the latter with
\(\Lambda_{\rm sym}(c_+)\).  The \(-A(c)\) inside the logarithm cancels the
\(+A(c)\) from the final factor in (1.3).

Use the Hilbert--Schmidt inner product on the Lie algebra and sum over one
orientation of each bond.  For a coarse current \(\tau\), set

\[
 (\operatorname{div}\tau)(y)
 =\sum_{c_-=y}\tau(c)-\sum_{c_+=y}\tau(c).
 \tag{3.3}
\]

Let \(P=Q_{\rm lin}^*\).

### Proposition 2: conserved-current bounds

If \(\operatorname{div}\tau=0\), then the symmetric radial terms in (3.1)
cancel and

\[
 (P\tau)(b)=L^{-d}\sum_c\tau(c)
 \#\{x\in B(c_-):b\subset[x,x']\},
 \tag{3.4}
\]

with the evident orientation sign.  Moreover,

\[
 \operatorname{div}(P\tau)=0,
 \qquad
 \|P\tau\|_\infty\le L^{1-d}\|\tau\|_\infty,
 \qquad
 \|P\tau\|_1\le L\|\tau\|_1,
 \tag{3.5}
\]

and

\[
 \boxed{\ \|P\tau\|_2^2
          \le L^{2-d}\|\tau\|_2^2.\ }
 \tag{3.6}
\]

#### Proof

Pair (3.1) with \(\tau\).  The two endpoint terms give exactly

\[
 \sum_y\langle(\operatorname{div}\tau)(y),
                   \Lambda_{\rm sym}(y)\rangle,
\]

which vanishes.  Taking the adjoint of the remaining straight-segment term
gives (3.4).

The current of \([x,x']\) has divergence \(\delta_x-\delta_{x'}\).  Therefore,
for a fine vertex \(z\in B(y)\),

\[
 (\operatorname{div}P\tau)(z)
 =L^{-d}(\operatorname{div}\tau)(y)=0.
 \tag{3.7}
\]

A fixed fine bond lies in at most \(L\) of the length-\(L\) translated
segments in (3.4).  This proves the sup bound.  Taking absolute values before
summing over fine bonds, and using that there are \(L^d\) segments of length
\(L\) for each coarse bond, gives

\[
 \|P\tau\|_1
 \le L^{-d}L^dL\sum_c\|\tau(c)\|_{\rm HS}
 =L\|\tau\|_1.
\]

For the square bound, let \(I_b\) be the set of pairs \((c,x)\) whose
translated segment contains \(b\).  Cauchy--Schwarz and \(|I_b|\le L\) give

\[
 \begin{aligned}
 \|P\tau\|_2^2
 &\le L^{-2d}\sum_b|I_b|
       \sum_{(c,x)\in I_b}\|\tau(c)\|_{\rm HS}^2\\
 &\le L^{1-2d}\sum_c\sum_{x\in B(c_-)}
       \sum_{b\subset[x,x']}\|\tau(c)\|_{\rm HS}^2\\
 &=L^{1-2d}L^dL\sum_c\|\tau(c)\|_{\rm HS}^2
 =L^{2-d}\|\tau\|_2^2.
 \end{aligned}
\]

This proves (3.5)--(3.6). \(\square\)

In particular, a closed-loop current is conserved.  Iteration at the trivial
background gives

\[
 \|P^m\tau\|_\infty\le L^{(1-d)m}\|\tau\|_\infty,
 \qquad
 \|P^m\tau\|_2^2\le L^{(2-d)m}\|\tau\|_2^2.
 \tag{3.8}
\]

For \(d=4\), the factors are \(L^{-3m}\) and \(L^{-2m}\), respectively.

## 4. A first-layer path bound at trivial exterior

The endpoint estimate (2.2) alone does not bound the length of a lifted path:
the principal logarithm is not uniformly differentiable at holonomies with
eigenvalue \(-1\).  The regular event must keep the interpolation a fixed
distance from that branch locus.  We now state this condition explicitly and
obtain (5.3) of research note 12 with a concrete constant.

Specialize to \(SU(2)\).  If \(H\in SU(2)\) has principal logarithm
\(H=e^{iZ}\), write \(\vartheta(H)=\|Z\|_{\rm op}\in[0,\pi]\).  Fix
\(0<\delta<\pi\), a fine-bond set \(S\), and a configuration \(W\) equal to
the identity off \(S\).  Choose traceless Hermitian bond logarithms

\[
 W_b=e^{iH_b},\qquad \|H_b\|_{\rm op}\le\pi,
\]

and the canonical path \(W_b(t)=e^{itH_b}\) for \(b\in S\), with all other
bonds fixed at one.  Define \(\mathrm{Reg}_\delta(S)\) to consist of the
configurations for which, for every \(t\in[0,1]\) and every loop appearing in
(1.3),

\[
 \vartheta\!\left(
 U_t(\ell(c,x,\Gamma,\Gamma'))U_t(c)^{-1}
 \right)\le\pi-\delta.
 \tag{4.1}
\]

This is an explicit pathwise regular event, not a claim about its probability.
Trivial exterior field alone does not imply (4.1): one noncentral interior
link can make a relative contour holonomy equal, or arbitrarily close, to
\(-1\).  At \(-I\), the stated principal spectral convention gives
\(\log(-I)=i\pi I\), which is not traceless, and the logarithm is not
differentiable there.  Thus an unconditional literal version of (4.4) is
false as a uniform differentiable-path claim; the fixed branch margin is an
essential part of the regular event.

More concretely, choose a noncentral bond for which the total weight of
relative loops containing it once is \(0<\omega<1\), set that bond to \(-I\),
and set all other bonds to \(I\).  At the endpoint those loops contribute
\(\pi I\) to \((1/i)\log\), so the corresponding outer exponential has
determinant \(e^{2\pi i\omega}\).  Approaching the same endpoint through
\(e^{i(\pi-\epsilon)n\cdot\sigma}\) gives traceless logarithms and determinant
one.  Thus Eq. (0.4) is discontinuous as an \(SU(2)\)-valued map at the cut;
the trivial exterior condition by itself cannot supply (5.3).

### Lemma 3: the logarithm derivative on \(SU(2)\)

On the domain \(\vartheta(H)\le\pi-\delta\), the principal logarithm satisfies,
in right-trivialized Hilbert--Schmidt norm,

\[
 \left\|\frac d{dt}\frac1i\log H(t)\right\|_{\rm HS}
 \le C_\delta
 \left\|\frac1i\dot H(t)H(t)^{-1}\right\|_{\rm HS},
 \qquad
 C_\delta=\frac{\pi-\delta}{\sin\delta}.
 \tag{4.2}
\]

#### Proof

Write \(H=e^{iZ}\), with eigenvalues of \(Z\) equal to
\(\pm\vartheta\).  The right-trivialized differential of the exponential has
singular value one in the direction of \(Z\) and
\(\sin\vartheta/\vartheta\) in each perpendicular direction.  Its inverse
therefore has norm at most
\(\vartheta/\sin\vartheta\le(\pi-\delta)/\sin\delta\), with the value at zero
understood by continuity. \(\square\)

For a path \(\ell\), let \(N_b(\ell)\) be the number of traversals of the
unoriented bond underlying \(b\), so immediate backtracking is counted with
multiplicity.  As in (2.3), the radial families contribute at most \(2d\),
and the translated segments contribute at most
\(L\cdot L^{-d}=L^{1-d}\).  Hence

\[
 K_{d,L}:=\sup_b\sum_c\sum_{x,\Gamma,\Gamma'}
 w_{c,x,\Gamma,\Gamma'}
 N_b(\ell(c,x,\Gamma,\Gamma'))
 \le 2d+L^{1-d}.
 \tag{4.3}
\]

The straight central paths have incidence at most one.

### Proposition 4: first-layer path length

For \(W\in\mathrm{Reg}_\delta(S)\), with trivial exterior field and
\(s=|S|\), the path above obeys

\[
 \int_0^1
 \left\|\frac1i\frac d{dt}\mathcal Q(W(t))
                    \mathcal Q(W(t))^{-1}\right\|_1dt
 \le C_0(d,L,\delta)s
 \le C_0(d,L,\delta)(s+L^d),
 \tag{4.4}
\]

where one may take

\[
 C_0(d,L,\delta)
 =\pi\sqrt2\left[
   C_\delta\bigl(2d+1+L^{1-d}\bigr)+1
 \right].
 \tag{4.5}
\]

Thus (4.4) is the first-layer estimate (5.3) of note 12 for the CMP **109**
Eq. (0.4) map at trivial exterior, on the explicit regular event (4.1).  In
the multiscale indexing of that note, this one-step map is the first map
\(Q_m\), not the terminal-level index.

#### Proof

Put

\[
 a_b(t)=\frac1i\dot W_b(t)W_b(t)^{-1},
 \qquad v_b(t)=\|a_b(t)\|_{\rm HS}.
\]

The right-trivialized velocity of a path holonomy is a sum of unitary
conjugates of its bond velocities.  Hence its Hilbert--Schmidt norm is at most
the sum of the \(v_b\)'s along the path.  Lemma 3, followed by the Duhamel
formula for the exponential in (1.3), gives for each coarse bond

\[
 \begin{aligned}
 \left\|\frac1i\dot{\overline U}(c)\overline U(c)^{-1}\right\|_{\rm HS}
 \le{}& C_\delta\sum_{x,\Gamma,\Gamma'}w_{c,x,\Gamma,\Gamma'}
       \sum_{b\in\ell(c,x,\Gamma,\Gamma')}v_b(t)\\
 &+(C_\delta+1)\sum_{b\in c}v_b(t).
 \end{aligned}
 \tag{4.6}
\]

The second line accounts for the inverse central transporter inside every
logarithm and for the final factor \(U(c)\).  Sum (4.6) over \(c\), use (4.3)
and central-path incidence one, and obtain

\[
 \left\|\frac1i\frac d{dt}\mathcal Q(W(t))
                    \mathcal Q(W(t))^{-1}\right\|_1
 \le\left[C_\delta(K_{d,L}+1)+1\right]
      \sum_{b\in S}v_b(t).
 \tag{4.7}
\]

For the canonical path, \(v_b(t)=\|H_b\|_{\rm HS}\le\pi\sqrt2\).  Integrate
(4.7) and sum over the \(s\) moving bonds to get (4.4)--(4.5). \(\square\)

## 5. What remains open

Proposition 1 supplies the global rough estimate for the averaging formula
actually used in the four-dimensional construction.  Proposition 2 supplies
the exact trivial-background conserved-current contraction, including the
quadratic \(L^{2-d}\) factor.  Proposition 4 supplies the first irregular-layer
path bound on a fixed branch-gap event.

None of these statements proves that the normalized true and template fiber
laws put summably small mass on \(\mathrm{Reg}_\delta(S)^c\); that is
H7\(_\Sigma\).  Nor do they bound the conserved-current derivative at a curved
background or sum the squared sensitivities over histories and placements.
Those are the remaining H6\(_\Sigma\) inputs, and they are not upgraded here.
