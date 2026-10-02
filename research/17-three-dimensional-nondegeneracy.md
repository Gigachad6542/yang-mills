# Three-dimensional M1 reduction and terminal nondegeneracy

Status: **The normalized-density and nondegeneracy propositions below are
proved here from Balaban's published three-dimensional stability bound and
the stated minimal-background regularity input.**  The latter is part of the
small-field background construction used in the published proof.  Balaban
explicitly describes that proof as "very sketchy" and says that many technical
details are omitted.  The result therefore remains a deduction from a
published input, not an independent completion of those omitted details.

This note discharges P6 for the three-dimensional exact-
\(T\) pilot.  It does not prove the adjacent-depth estimate P4-3D and hence
does not by itself prove M1-3D.

## 1. Fixed terminal lattice and the published input

Fix \(G=SU(2)\), a finite physical three-torus, a block factor \(L\), and a
terminal spacing \(\varepsilon _0\).  For \(n\ge1\), take

\[
 \varepsilon_n=\varepsilon _0L^{-n},\qquad K_n=n,
 \qquad g_{0,n}^{2}=g^2\varepsilon_n .
 \tag{1.1}
\]

Balaban's three-dimensional density starts from

\[
 \rho^{(n)}_0(U)=
 \exp\!\left[-g_{0,n}^{-2}A(U)-E_n\right]
 \tag{1.2}
\]

and is propagated by the exact block transformation

\[
 \rho^{(n)}_{k+1}=T\rho^{(n)}_k .
 \tag{1.3}
\]

After \(K_n\) steps, \(L^{K_n}\varepsilon_n=\varepsilon _0\) and

\[
 g_{K_n}^{2}=g^2\varepsilon _0=:g_*^2 .
 \tag{1.4}
\]

Thus every terminal density lives on the same finite configuration space

\[
 X=SU(2)^{\mathcal B_*},
 \tag{1.5}
\]

where one orientation of each bond of the \(\varepsilon _0\)-lattice is used.
Let \(\lambda\) be normalized product Haar measure on \(X\), and let
\(N_*=|T_1^{(K_n)}|\).  Both \(X\) and \(N_*\) are independent of \(n\).

For \(\eta_n=L^{-K_n}\), CMP **102**, Eq. (5), printed p. 256, gives

\[
 \mathbf 1_S(V)
 \exp\!\left[-g_*^{-2}A^{\eta_n}(U_{K_n}(V))-C_0N_*\right]
 \le \rho^{(n)}_{K_n}(V)
 \le \exp(C_0N_*).
 \tag{1.6}
\]

Here

\[
 A^\eta(U)=\sum_{p\subset T_\eta}
 \eta^{-1}\bigl[1-\operatorname{Re}\operatorname{tr}U(\partial p)\bigr],
 \tag{1.7}
\]

\(U_{K_n}(V)\) is the action-minimizing fine configuration with the
prescribed iterated averages (the variational definition is CMP **102**,
Eq. (42), printed p. 266), and

\[
 S=\left\{V\in X:
   \lVert V(\partial p)-1\rVert<\varepsilon _1
   \text{ for every terminal plaquette }p\right\}.
 \tag{1.8}
\]

This is the set selected by Balaban's \(\chi\) in Eq. (4).  It is a nonempty
open subset of \(X\), so

\[
 s_*:=\lambda(S)>0.
 \tag{1.9}
\]

The constant \(C_0\) may depend on \(g\), \(\varepsilon _0\), the torus,
and \(L\), but not on \(n\).  Theorem 1, printed p. 257, states (1.6) for
the exact densities (1.3).  Its following paragraph explicitly says that the
proof is very sketchy and omits many technical details.  We use (1.6) with
that qualification.

The terminal observables in the three-dimensional M1 pilot are bounded
continuous functions of finitely many closed coarse holonomies, for example

\[
 F(V)=h\!\left(
  \operatorname{TrHol}_{C_1}(V),\ldots,
  \operatorname{TrHol}_{C_m}(V)\right).
 \tag{1.10}
\]

They are gauge invariant and the exact identity in research note 14 transports
their sources through every step of (1.3).

## 2. The minimal-background action on \(S\)

The action in the lower bound (1.6) cannot simply be discarded: a uniform
bound on \(A^{\eta_n}(U_{K_n}(V))\) is the bridge from source-free stability
to a positive terminal density.  We record that bridge explicitly.

### Minimal-background regularity input

On the all-small-field sector, the background used in the lower-bound
induction obeys

\[
 \lVert U_{K_n}(V)(\partial p)-1\rVert
 \le D\,g_-p(g_-)\eta_n^2,
 \qquad V\in S,\quad p\subset T_{\eta_n},
 \tag{2.1}
\]

with \(D\) independent of \(n\) and \(V\).  This is the precise extra
property of \(U_{K_n}\) used below.  It is the global all-small-field
specialization of the regularity condition in CMP **102**, p. 267, preceding
Eq. (44), and of the multiscale condition (68), printed p. 273.  The companion
variational paper, CMP **102**, 277--309, Theorem 1, constructs the minimizing
orbit for small coarse plaquettes and places it in this regular class.  If one
does not accept that published background-regularity construction, then
(2.1), or equivalently the uniform action bound (2.2) below, must be retained
as an explicit hypothesis.

Here \(g_-=g_{K_n-1}=g_*/\sqrt L\), and \(p(g)\) is Balaban's fixed
logarithmic large-field threshold.  Only the fact that
\(g_-p(g_-)\) is independent of \(n\) is used here.

### Proposition 1: uniform action of the minimizing background

There is \(A_*<\infty\), independent of \(n\) and \(V\in S\), such that

\[
 A^{\eta_n}(U_{K_n}(V))\le A_*.
 \tag{2.2}
\]

More precisely,

\[
 g_*^{-2}A^{\eta_n}(U_{K_n}(V))
 \le C_{\rm geom}D^2L^{-1}p(g_-)^2N_*.
 \tag{2.3}
\]

#### Proof

For \(W\in SU(2)\), with either the normalized Hilbert--Schmidt norm or any
fixed equivalent matrix norm,

\[
 1-\operatorname{Re}\operatorname{tr}W
 \le C_{SU(2)}\lVert W-1\rVert^2.
 \tag{2.4}
\]

There are at most \(C_{\rm plaq}N_*\eta_n^{-3}\) fine plaquettes.  Combining
(1.7), (2.1), and (2.4) gives

\[
\begin{aligned}
 A^{\eta_n}(U_{K_n}(V))
 &\le C_{SU(2)}\eta_n^{-1}
       C_{\rm plaq}N_*\eta_n^{-3}
       D^2g_-^2p(g_-)^2\eta_n^4\\
 &=C_{\rm geom}D^2g_*^2L^{-1}p(g_-)^2N_*.
\end{aligned}
 \tag{2.5}
\]

All powers of \(\eta_n\) cancel.  This proves (2.2)--(2.3). \(\square\)

CMP **102**, Eq. (3), printed p. 256, also states the resulting action-free
terminal estimate directly, with an exponent proportional to the fixed
physical volume \(|T_{\varepsilon_n}|\).  Proposition 1 explains why the
sharper flow bound (1.6) has the same consequence and makes clear which
property of the minimal configuration is being used.

## 3. Normalization and two-sided terminal density bounds

Define

\[
 Z_n=\int_X\rho^{(n)}_{K_n}(V)\,d\lambda(V),
 \qquad
 d\nu_n=f_n\,d\lambda,
 \qquad
 f_n=\frac{\rho^{(n)}_{K_n}}{Z_n}.
 \tag{3.1}
\]

The exact normalization identity is CMP **102**, Eq. (6), printed p. 257:

\[
 Z_n=\int T^{K_n}\rho^{(n)}_0=\int\rho^{(n)}_0.
 \tag{3.2}
\]

It proves mass preservation, but the quantitative normalization bounds below
also use the pointwise estimates in (1.6).

### Proposition 2: uniform normalized terminal law

There are constants \(0<c<C<\infty\), independent of \(n\), such that

\[
 f_n(V)\le C\quad\text{for every }V\in X,
 \qquad
 f_n(V)\ge c\quad\text{for every }V\in S.
 \tag{3.3}
\]

#### Proof

Put

\[
 B_*=C_{\rm geom}D^2L^{-1}p(g_-)^2N_*,\qquad
 a=e^{-B_*-C_0N_*},\qquad b=e^{C_0N_*}.
 \tag{3.4}
\]

Equations (1.6) and (2.3) imply

\[
 a\mathbf 1_S\le\rho^{(n)}_{K_n}\le b.
 \tag{3.5}
\]

Since \(\lambda\) is normalized and \(\lambda(S)=s_*>0\),

\[
 as_*\le Z_n\le b.
 \tag{3.6}
\]

Division by \(Z_n\) now gives (3.3), with the explicit choices

\[
 c=\frac ab,
 \qquad
 C=\frac{b}{as_*}.
 \tag{3.7}
\]

The vacuum-energy constant in (1.2) therefore cancels exactly as it should;
no independent lower bound on an unnormalized partition function was assumed.
\(\square\)

## 4. Positive variance and subsequential limits

### Proposition 3: P6-3D

Let \(F:X\to\mathbb R\) be continuous and nonconstant on \(S\).  Then

\[
 \inf_n\operatorname{Var}_{\nu_n}(F)>0.
 \tag{4.1}
\]

Every weak subsequential limit \(\nu\) of \((\nu_n)\) is nondegenerate in
the same sense.  Moreover, if \(\nu\) and \(\nu'\) are two weak subsequential
limits, then their restrictions to \(S\) are mutually absolutely continuous.
Quantitatively, for every Borel set \(A\subset S\),

\[
 \frac cC\,\nu'(A)\le\nu(A)\le\frac Cc\,\nu'(A).
 \tag{4.2}
\]

#### Proof

Because Haar measure has full support and \(S\) is open,

\[
 \sigma_S^2(F):=\inf_{t\in\mathbb R}
   \int_S|F(V)-t|^2\,d\lambda(V)>0.
 \tag{4.3}
\]

Indeed, equality would make \(F\) constant \(\lambda\)-almost everywhere on
\(S\); continuity and full support would then make it constant everywhere on
\(S\).  Proposition 2 gives

\[
\begin{aligned}
 \operatorname{Var}_{\nu_n}(F)
 &=\inf_{t\in\mathbb R}\int_X|F-t|^2\,d\nu_n\\
 &\ge c\inf_{t\in\mathbb R}\int_S|F-t|^2\,d\lambda
 =c\sigma_S^2(F)>0,
\end{aligned}
 \tag{4.4}
\]

uniformly in \(n\).

The space \(X\) is compact, so subsequential limits exist.  If
\(\nu_{n_j}\Rightarrow\nu\), then for every nonnegative continuous test
\(\varphi\), Proposition 2 gives

\[
 \int_X\varphi\,d\nu\le C\int_X\varphi\,d\lambda.
 \tag{4.5}
\]

For every such \(\varphi\) supported compactly inside \(S\), it also gives

\[
 \int_X\varphi\,d\nu\ge c\int_X\varphi\,d\lambda.
 \tag{4.6}
\]

Regular approximation on the open set \(S\) therefore yields the measure
inequalities

\[
 c\lambda|_S\le\nu|_S\le C\lambda|_S.
 \tag{4.7}
\]

The same holds for \(\nu'\).  Thus both restrictions are equivalent to
\(\lambda|_S\), and (4.2) follows.  Finally, since \(F\) and \(F^2\) are
continuous on compact \(X\), variance is continuous under weak convergence;
(4.4) passes to every subsequential limit. \(\square\)

For a concrete M1 observable, one may take the trace of a terminal plaquette
holonomy.  It is continuous, gauge invariant, and nonconstant on the open set
\(S\).  Proposition 3 is therefore stronger than the requirement that at
least one limiting variance be positive.

## 5. What this does and does not prove about M1-3D

The three-dimensional obligation ledger is now:

| Interface | Three-dimensional status |
|---|---|
| H0, effective-coupling shooting | absent: superrenormalizability gives the explicit dimensional flow \(g_k^2=g^2L^k\varepsilon_n\); there is no four-dimensional marginal beta-function trajectory to construct |
| H1, conditional four-dimensional \(RT\) stability | replaced by the published three-dimensional exact-\(T\) bound (1.6), with the paper's explicit sketchiness caveat |
| Robs and H6\(_\Sigma\)--H8\(_\Sigma\) | absent: \(\rho_{k+1}=T\rho_k\) exactly and no observable-changing \(R\)-operation occurs |
| P6-3D | proved in Proposition 3 from the published stability/background inputs |
| P4-3D | open: compare adjacent ultraviolet depths on this common terminal lattice |

Consequently, for any finite family of closed-loop terminal observables, the
three-dimensional analogue of M1 reduces to P4-3D.  If the summable
adjacent-depth comparison is proved, exact source transport gives convergence
of the terminal generating functions, the elementary bounded-observable
argument gives their common zero-free source disc, and Proposition 3 supplies
nondegeneracy.  No conclusion here supplies the missing P4-3D estimate.

## 6. Optional further blocking to a coarser scale

The proof above stops directly at \(\varepsilon _0\); it does not need any
additional block step.  This choice matters.  Exactness and mass preservation
alone do not preserve pointwise Haar-density bounds under an arbitrary
deterministic pushforward.

Here is the exact criterion.  Let \(q:X\to Y\) be a fixed finite composition
of additional block maps, let \(\lambda_Y\) be product Haar measure on the
coarser connection space, and suppose

\[
 q_*\lambda\le H\lambda_Y,
 \qquad
 q_*(\mathbf 1_S\lambda)\ge h\mathbf 1_{S_Y}\lambda_Y
 \tag{6.1}
\]

for some \(H<\infty\), \(h>0\), and nonempty open \(S_Y\).  Pushing (3.3)
forward then gives

\[
 ch\mathbf 1_{S_Y}\lambda_Y
 \le q_*\nu_n\le CH\lambda_Y.
 \tag{6.2}
\]

Thus all arguments in Sections 3--4 survive at the coarser scale.  The first
condition in (6.1) is a bounded-density condition for \(q_*\lambda\); the
second is a uniform positive small-field fiber mass.  Neither follows merely
from \(\int T\rho=\int\rho\).  A constant deterministic map already shows why
mass preservation alone is insufficient.

The cleaner alternative is to choose the desired coarser spacing \(\ell\) as
Balaban's stopping scale from the outset and apply Theorem 1 there, provided
\(g\sqrt\ell\) remains in its allowed regime.  This note uses
\(\varepsilon _0\), so it makes no unproved claim that additional exact
\(T\)-steps preserve product-Haar pointwise bounds.

## 7. Conclusion

For the exact three-dimensional terminal laws, Balaban's small-field lower
bound is strong enough to survive normalization.  The minimizing background
has uniformly bounded action because its fine curvature is \(O(\eta_n^2)\),
and the three-dimensional plaquette count cancels that scale exactly.  The
resulting terminal densities are uniformly bounded above everywhere and below
on one fixed open set.  This proves P6-3D, makes every subsequential limit
nondegenerate, and makes all subsequential limits locally equivalent on the
small-field set.  The sole remaining M1-3D interface is the adjacent-depth
comparison P4-3D.

## Primary sources

- T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge
  Field Theories*, CMP **102** (1985), 255--275: Eqs. (1)--(6), printed
  pp. 256--257; the variational definition (42) and background regularity
  preceding Eq. (44), printed pp. 266--267; Eqs. (68)--(71), printed p. 273.
- T. Balaban, *The Variational Problem and Background Fields in
  Renormalization Group Method for Lattice Gauge Theories*, CMP **102**
  (1985), 277--309: the action in Eq. (5) and Theorem 1, printed pp. 278--279,
  for existence, uniqueness up to gauge, and regularity of the minimizing
  background.
