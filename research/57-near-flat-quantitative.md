# A quantitative near-flat lemma on an SU(2) lattice torus

Status:

- **Proved.**  On \(\Lambda_n=(\mathbb Z/n\mathbb Z)^d\), \(d\ge2\), if
  every plaquette satisfies
  \(\|U(\partial p)-1\|_{\rm op}\le\varepsilon\), then

  \[
  \inf_{g,\,F\ \mathrm{flat}}\max_b\|U_b^g-F_b\|_{\rm op}
  \le d\,n\sqrt{\varepsilon}.
  \tag{0.1}
  \]

  Thus note 54's modulus may be chosen
  \(\omega_n(\varepsilon)\le d n\sqrt\varepsilon\).  For \(d=1\) every
  configuration is flat, so the left side is zero.
- **Sharp exponent.**  A constant-link family with two orthogonal SU(2)
  axes has plaquette defect \(O(\alpha^2)\) but distance \(\Omega(\alpha)\)
  from the flat configurations.  Consequently the exponent \(1/2\) in
  (0.1) cannot be replaced uniformly by any larger exponent, even for fixed
  \(n\).

The proof is finite-dimensional and elementary.  A complete axial gauge
reduces the connection to \(d\) cycle holonomies plus an error bounded by
the number of elementary plaquette swaps.  Those cycle holonomies almost
commute.  The special quaternion geometry of SU(2) then gives a commuting
tuple within the square root of their commutator defect.

## 1. Conventions and statement

Write a positive oriented bond as \((x,\mu)\), where
\(x\in\{0,\ldots,n-1\}^d\), \(1\le\mu\le d\), and addition of vertices is
modulo \(n\).  Put

\[
 P_{\mu\nu}(x)
 =U_\mu(x)U_\nu(x+e_\mu)
  U_\mu(x+e_\nu)^{-1}U_\nu(x)^{-1}.
 \tag{1.1}
\]

The norm is the operator norm in the defining two-dimensional
representation.  We use the gauge convention

\[
 U^g(x,y)=g(x)U(x,y)g(y)^{-1}.
 \tag{1.2}
\]

For differences of SU(2) matrices this operator norm equals the normalized
Hilbert--Schmidt norm; the unnormalized Hilbert--Schmidt norm is larger by
\(\sqrt2\).  If \(\vartheta(A,B)\in[0,\pi]\) is geodesic distance, then
\(\|A-B\|_{\rm op}=2\sin(\vartheta(A,B)/2)\), so
\(\|A-B\|_{\rm op}\le\vartheta(A,B)\le(\pi/2)\|A-B\|_{\rm op}\).

A configuration \(F\) is flat when all its plaquettes are one.  Define

\[
 d_\infty(U,{\rm Flat})
 :=\inf_{g,\,F\ \mathrm{flat}}\max_b\|U_b^g-F_b\|_{\rm op}.
 \tag{1.3}
\]

**Theorem 1 (quantitative near-flat lemma).**  If

\[
 \max_{x,\mu<\nu}\|P_{\mu\nu}(x)-1\|_{\rm op}
 \le\varepsilon,
 \tag{1.4}
\]

then, for \(d\ge2\),

\[
 d_\infty(U,{\rm Flat})\le d n\sqrt\varepsilon.
 \tag{1.5}
\]

The estimate is meaningful without an extra smallness hypothesis.  When
\(n\sqrt\varepsilon\ge1\), it follows from the diameter two of SU(2).  The
content is the regime \(n\sqrt\varepsilon\le1\).

## 2. Plaquette moves and complete axial gauge

An elementary positive plaquette move interchanges two adjacent positive
steps \(\mu\nu\) and \(\nu\mu\), with the base points adjusted in the
usual way.  If two paths \(q,q'\) with the same endpoints differ by one
such move, then (1.1), unitary invariance of the norm, and (1.4) give

\[
 \|U(q)-U(q')\|_{\rm op}\le\varepsilon.
 \tag{2.1}
\]

Telescoping therefore gives

\[
 \|U(q)-U(q')\|_{\rm op}\le N\varepsilon
 \tag{2.2}
\]

whenever \(q\) is changed into \(q'\) by \(N\) elementary moves.  This is
the only nonabelian Stokes estimate needed below; all conjugating factors
are unitary and hence cost nothing.

For \(x=(x_1,\ldots,x_d)\), let \(q_x\) be the coordinate-ordered path
from zero to \(x\): first take \(x_1\) steps in direction 1, then \(x_2\)
steps in direction 2, and so on.  The union of the resulting distinguished
bonds is

\[
 T=\{(x,\mu):x_\mu<n-1,\ x_\nu=0\text{ for every }\nu>\mu\}.
 \tag{2.3}
\]

It is a spanning tree: every \(q_x\) lies in \(T\), and
\(|T|=\sum_{\mu=1}^d n^{\mu-1}(n-1)=n^d-1\).  Set

\[
 g(x)=U(q_x).
 \tag{2.4}
\]

This is a function on the finite quotient, hence a legitimate periodic
gauge transformation.  The torus-cycle data remain in the seam holonomies
below; no cycle is gauged away.  The theorem concerns globally periodic
SU(2) link fields.  Twisted SO(3) or 't Hooft boundary conditions are a
different hypothesis.

Then every distinguished tree bond has \(U^g_b=1\), and for an arbitrary
positive bond \(b=(x,\mu)\), with \(y=x+e_\mu\),

\[
 U^g_\mu(x)=U(q_x)U_\mu(x)U(q_y)^{-1}.
 \tag{2.5}
\]

Let \(c_\mu\) be the coordinate loop based at zero consisting of \(n\)
positive \(\mu\)-steps, and put

\[
 H_\mu=U(c_\mu).
 \tag{2.6}
\]

**Lemma 2 (explicit axial normal form).**  The gauge (2.4) obeys

\[
 \begin{aligned}
 x_\mu<n-1:
 &&\|U^g_\mu(x)-1\|_{\rm op}
 &\le \Big(\sum_{\nu>\mu}x_\nu\Big)\varepsilon
 \le(d-1)(n-1)\varepsilon,\\
 x_\mu=n-1:
 &&\|U^g_\mu(x)-H_\mu\|_{\rm op}
 &\le\Big(\sum_{\nu>\mu}x_\nu
       +n\sum_{\nu<\mu}x_\nu\Big)\varepsilon\\
 &&&\le(d-1)n(n-1)\varepsilon.
 \end{aligned}
 \tag{2.7}
\]

Moreover,

\[
 \|H_\mu H_\nu H_\mu^{-1}H_\nu^{-1}-1\|_{\rm op}
 \le n^2\varepsilon.
 \tag{2.8}
\]

*Proof.*  If \(x_\mu<n-1\), move the final \(\mu\)-step of
\(q_x(x,x+e_\mu)\) to the left across the
\(\sum_{\nu>\mu}x_\nu\) later coordinate steps.  The resulting path is
exactly \(q_y\).  Equations (2.2) and (2.5) give the first line.

If \(x_\mu=n-1\), the same moves first produce a block of \(n\)
\(\mu\)-steps.  Moving this block left across the earlier coordinate steps
costs \(n\sum_{\nu<\mu}x_\nu\) further swaps and produces the path
\(c_\mu q_y\).  Equations (2.2), (2.5), and (2.6) give the second line.
The displayed common bound follows because

\[
 (d-\mu)(n-1)+n(\mu-1)(n-1)
 \le(d-1)n(n-1).
\]

Finally, changing \(c_\mu c_\nu\) into \(c_\nu c_\mu\) requires exactly
\(n^2\) adjacent swaps.  Thus
\(\|H_\mu H_\nu-H_\nu H_\mu\|_{\rm op}\le n^2\varepsilon\).  Right
multiplication by \(H_\mu^{-1}H_\nu^{-1}\) proves (2.8). \(\square\)

## 3. An explicit almost-commuting SU(2) lemma

Every \(A\in SU(2)\) is uniquely

\[
 A=a_0 1+i\,a\cdot\sigma,
 \qquad a_0^2+|a|^2=1,
 \tag{3.1}
\]

where \(\sigma\) are the Pauli matrices.  In these coordinates,

\[
 \|A-B\|_{\rm op}^2=(a_0-b_0)^2+|a-b|^2.
 \tag{3.2}
\]

**Lemma 3 (almost commuting implies near commuting).**  Suppose
\(A_1,\ldots,A_d\in SU(2)\) and

\[
 \max_{\mu,\nu}
 \|A_\mu A_\nu A_\mu^{-1}A_\nu^{-1}-1\|_{\rm op}
 \le\delta.
 \tag{3.3}
\]

Then there are pairwise commuting \(B_1,\ldots,B_d\in SU(2)\) such that

\[
 \max_\mu\|A_\mu-B_\mu\|_{\rm op}\le\sqrt\delta.
 \tag{3.4}
\]

The constant one is independent of \(d\).

*Proof.*  Write \(A_\mu=a_{0\mu}1+i a_\mu\cdot\sigma\).  Pauli
multiplication and unitary invariance give the exact identity

\[
 \|A_\mu A_\nu A_\mu^{-1}A_\nu^{-1}-1\|_{\rm op}
 =\|A_\mu A_\nu-A_\nu A_\mu\|_{\rm op}
 =2|a_\mu\times a_\nu|.
 \tag{3.5}
\]

Put \(s=\max_\mu|a_\mu|\).  One commuting candidate is obtained by
rounding every \(A_\mu\) to the nearer central element
\(\epsilon_\mu1\), where \(\epsilon_\mu={\rm sign}(a_{0\mu})\) and either
sign is allowed when \(a_{0\mu}=0\).  By (3.2),

\[
 \|A_\mu-\epsilon_\mu1\|_{\rm op}^2
 =2(1-|a_{0\mu}|)\le2|a_\mu|^2,
 \tag{3.6}
\]

so this candidate has error at most \(\sqrt2s\).

If \(s>0\), choose \(k\) with \(|a_k|=s\), put \(u=a_k/s\), and
decompose \(a_\mu=t_\mu u+a_\mu^\perp\).  Equation (3.5) gives

\[
 p_\mu:=|a_\mu^\perp|
 =\frac{|a_k\times a_\mu|}{s}
 \le\frac{\delta}{2s}.
 \tag{3.7}
\]

Project \((a_{0\mu},a_\mu)\in S^3\) to the great circle

\[
 T_u=\{b_0 1+i b\,u\cdot\sigma:b_0^2+b^2=1\}.
\]

All projected matrices commute.  If
\(r_\mu=(a_{0\mu}^2+t_\mu^2)^{1/2}=(1-p_\mu^2)^{1/2}\), the nearest
point is obtained by dividing \((a_{0\mu},t_\mu)\) by \(r_\mu\) (with
any point of \(T_u\) allowed when \(r_\mu=0\)).  Its squared distance is

\[
 2(1-r_\mu)
 =\frac{2p_\mu^2}{1+\sqrt{1-p_\mu^2}}
 \le2p_\mu^2.
 \tag{3.8}
\]

This second commuting candidate has error at most
\(\delta/(\sqrt2s)\).  The smaller of the two candidate errors is at most

\[
 \min\{\sqrt2s,\delta/(\sqrt2s)\}\le\sqrt\delta,
\]

because their product is \(\delta\).  The case \(s=0\) is already covered
by (3.6). \(\square\)

## 4. Proof of Theorem 1

Apply Lemma 3 to the cycle holonomies in Lemma 2.  By (2.8), there are
commuting \(K_1,\ldots,K_d\) such that

\[
 \max_\mu\|H_\mu-K_\mu\|_{\rm op}\le n\sqrt\varepsilon.
 \tag{4.1}
\]

Define the seam configuration

\[
 F_\mu(x)=
 \begin{cases}
 K_\mu,&x_\mu=n-1,\\
 1,&x_\mu<n-1.
 \end{cases}
 \tag{4.2}
\]

Every plaquette of \(F\) is one: plaquettes meeting one seam contain the
same \(K_\mu\) with opposite orientations, and a plaquette meeting two
seams is the commutator of \(K_\mu\) and \(K_\nu\).  Thus \(F\) is flat.

Put \(\rho=n\sqrt\varepsilon\).  If \(\rho\le1\), Lemma 2 and (4.1)
give, on a non-seam bond,

\[
 \|U^g_b-F_b\|_{\rm op}
 \le(d-1)(n-1)\varepsilon
 \le(d-1)\rho,
 \tag{4.3}
\]

and, on a seam bond,

\[
 \|U^g_b-F_b\|_{\rm op}
 \le(d-1)n(n-1)\varepsilon+\rho
 \le(d-1)\rho^2+\rho
 \le d\rho.
 \tag{4.4}
\]

If \(\rho>1\), take the identity gauge and the identity flat
configuration.  Since the operator-norm diameter of SU(2) is two,

\[
 \max_b\|U_b-1\|_{\rm op}\le2\le d\rho
 \qquad(d\ge2).
 \tag{4.5}
\]

Equations (4.3)--(4.5) prove (1.5). \(\square\)

## 5. Sharpness of the square-root exponent

Fix \(d\ge2\) and \(n\ge1\).  For \(0<\alpha\le\pi/2\), take the
constant-link configuration

\[
 U_1(x)=e^{i(\alpha/n)\sigma_3},\qquad
 U_2(x)=e^{i(\alpha/n)\sigma_1},\qquad
 U_\mu(x)=1\quad(\mu\ge3).
 \tag{5.1}
\]

By (3.5), its only nontrivial plaquettes have exact defect

\[
 \varepsilon_\alpha=2\sin^2(\alpha/n).
 \tag{5.2}
\]

The two coordinate holonomies are
\(e^{i\alpha\sigma_3}\) and \(e^{i\alpha\sigma_1}\).  If a gauge
transform of (5.1) is within \(\eta\) linkwise of a flat connection, then
telescoping each length-\(n\) coordinate loop shows that these two
holonomies, after a common conjugation, are within \(n\eta\) of a commuting
pair.  Indeed, flatness makes the based holonomies a representation of
\(\pi_1(\mathbb T^d)=\mathbb Z^d\), so its coordinate holonomies commute.
Common conjugation rotates both Pauli axes and does not change the estimate
below.

For completeness, let \(C,D\) be any commuting pair.  Their Pauli-vector
parts lie on one common line \(\mathbb Ru\).  With \(r=\sin\alpha\), the
vector parts of the two holonomies are \(r e_3\) and \(r e_1\).  Therefore

\[
 \begin{aligned}
 \max\{\|e^{i\alpha\sigma_3}-C\|_{\rm op},
        \|e^{i\alpha\sigma_1}-D\|_{\rm op}\}
 &\ge r\max\{(1-u_3^2)^{1/2},(1-u_1^2)^{1/2}\}\\
 &\ge \frac{\sin\alpha}{\sqrt2},
 \end{aligned}
 \tag{5.3}
\]

because \(u_1^2+u_3^2\le1\).  Consequently

\[
 d_\infty(U,{\rm Flat})
 \ge\frac{\sin\alpha}{\sqrt2\,n}
 =\frac{\sin\alpha}{2n\sin(\alpha/n)}
   \sqrt{\varepsilon_\alpha}.
 \tag{5.4}
\]

The prefactor tends to \(1/2\) as \(\alpha\downarrow0\).  Hence no estimate
\(d_\infty(U,{\rm Flat})\le C(n,d)\varepsilon^b\) with \(b>1/2\) can hold
uniformly as \(\varepsilon\downarrow0\).

## 6. Consequence for note 54

For the fixed terminal torus in note 54, Theorem 1 replaces the compactness
modulus by the explicit choice

\[
 \omega(\varepsilon)\le d n\sqrt\varepsilon.
 \tag{6.1}
\]

Thus the corrected perturbative input there may use the concrete smallness
condition \(C_1(L)d n\sqrt{\varepsilon_0}\le1\).  This note does not claim
an explicit Lipschitz constant for Balaban's nonlinear minimal-configuration
map; obtaining a quantitative fine-background corollary additionally
requires the corresponding published or separately proved fine-plaquette
bound.
