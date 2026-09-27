# Common-space comparison and the large-field \(R\)-operation obstruction

Status: **the measure-theoretic and polymer-summation implications are proved
here**. Their Yang--Mills hypotheses are open. In particular, the published
large-field construction does not supply the observable-preserving
\(R\)-operation required below.

## 1. Two densities that must not be conflated

Let \(T_k\) denote the exact group-delta blocking map. Starting from the Wilson
density \(\rho_0\), the physical coarse density is

\[
 \rho_k^{\mathrm{phys}}=T_{k-1}\cdots T_0\rho_0.
\]

Balaban's four-dimensional stability proof also uses a large-field
\(R\)-operation. Its defining property is preservation of the **unweighted
integral**, not equality of densities. CMP **122 I** says in the introduction
that large-field expressions are replaced so that integrals of densities are
unchanged and records

\[
 \int dV\,(R\rho)(V)=\int dV\,\rho(V)
 \tag{CMP 122 I, (0.4), p. 176}.
\]

The detailed construction first performs transformations that preserve
\(\rho_k\), but then explicitly replaces equality by an equivalence meaning only
equality after integration over \(V_k\) (printed p. 194, around
Eqs. (1.75)--(1.76)). Its summary again says that the resulting density may not
equal \(\rho_k\), although the two have equal integrals (printed p. 200, around
Eqs. (1.99)--(1.100)). Thus the density controlled by the complete \(RT\)
induction is an auxiliary stabilized density, schematically

\[
 \widehat\rho_k=R_kT_{k-1}\cdots R_1T_0\rho_0,
\]

with the same vacuum partition function as the exact blocked density, but not
automatically the same terminal law.

This distinction explains Balaban's statement in CMP **122 II**, p. 356, that
loop and averaged-loop expectations still require detailed analysis and further
publication.

## 2. Exact \(T\)-transport does not solve the \(R\) problem

For an exact block map \(T\) and a terminal test \(F\),

\[
 T_z\rho(V)=e^{zF(V)}T\rho(V)
\]

is the identity proved in 04-terminal-source-identity.md. It removes the need to
mark the integrations inside \(T\). It says nothing about a subsequent
\(R\)-replacement for which only
\(\int R\rho=\int\rho\) is known.

### Proposition 1: mass preservation is insufficient for observables

There is no bound on

\[
 \int f\,R\rho-\int f\,\rho
\]

for nonconstant bounded \(f\) that follows from positivity and
\(\int R\rho=\int\rho\) alone.

### Proof

On the two-point space \(\{0,1\}\) with counting measure, take
\(\rho=(1,1)\) and \(R\rho=(2-\epsilon,\epsilon)\), \(0<\epsilon<1\). Both are
strictly positive and have mass two. For \(f(x)=x\), their normalized
expectations are \(1/2\) and \(\epsilon/2\). The difference can approach
\(1/2\). \(\square\)

Therefore a theorem about the physical terminal observable needs at least one
of the following new inputs:

1. a source- or test-dependent \(R_z\) satisfying

   \[
     \int e^{zF}R_z\rho=\int e^{zF}\rho
   \]

   on a common complex disc, together with the full \(E/R/B\) stability bounds;
2. an \(R\)-operation preserving the pushforward measure under all remaining
   block maps, not merely its total mass; or
3. a quantitative estimate showing that the cumulative observable bias from the
   \(R\)-replacements vanishes as the ultraviolet cutoff is removed.

A source at the terminal scale is still simpler than a microscopic local source:
it factors through every exact \(T\)-step. But it does **not** eliminate the
source/test extension of the large-field \(R\)-step.

## 3. Exact reduction to a one-layer physical defect

The following reduction applies to the physical measures and is independent of
the \(R\)-construction.

Let \(\Omega_{N+1}\), \(\Omega_N\), and \(\Omega_*\) be measurable configuration
spaces. Let \(q_N:\Omega_{N+1}\to\Omega_N\) be the first block map and
\(b_N:\Omega_N\to\Omega_*\) the remaining map to a fixed terminal lattice.
Assume the compatibility

\[
 b_{N+1}=b_N\circ q_N.
\]

For fine-cutoff probability measures \(\mu_N\), put

\[
 \widetilde\mu_N=(q_N)_*\mu_{N+1},\qquad
 \nu_N=(b_N)_*\mu_N.
\]

### Proposition 2: defect propagation is contractive

For every bounded terminal test \(f\),

\[
 \nu_{N+1}(f)-\nu_N(f)
 =\widetilde\mu_N(f\circ b_N)-\mu_N(f\circ b_N),
\]

and hence

\[
 |\nu_{N+1}(f)-\nu_N(f)|
 \le \lVert f\rVert_\infty
 \lVert\widetilde\mu_N-\mu_N\rVert_{\mathrm{TV},*}.
\]

If

\[
 \frac{d\widetilde\mu_N}{d\mu_N}
 =\frac{e^{D_N}}{\mu_N(e^{D_N})},
\]

then

\[
 |\nu_{N+1}(f)-\nu_N(f)|
 \le \lVert f\rVert_\infty
      \bigl(e^{\operatorname{osc}D_N}-1\bigr).
\]

### Proof

Functoriality of pushforward and \(b_{N+1}=b_N\circ q_N\) give the identity. The
first estimate is the definition of the dual total-variation norm. The second
is Proposition 1 of 07-depth-comparison-reduction.md, applied before the
remaining pushforward. \(\square\)

This isolates the ideal P4 target: compare the once-blocked cutoff-\(N+1\)
Wilson measure with the cutoff-\(N\) Wilson measure on their first common
lattice, after matching the vacuum and marginal coupling coordinates. The
remaining exact block transformations cannot amplify the bounded-test error.
The published \(RT\) bounds cannot be inserted into this proposition until the
observable bias of \(R\) is controlled.

## 4. A sum over large-field histories is another nontrivial interface

CMP **119**, Eq. (2.18), represents the complete density as a sum over nested
large-field histories. Polymer bounds for a fixed history do not automatically
bound the logarithm of the summed density.

### Proposition 3: uniform history envelope

Let

\[
 \rho(\omega)=\sum_h a_h(\omega),\qquad
 \widetilde\rho(\omega)=\sum_h a_h(\omega)e^{r_h(\omega)},
\]

with \(a_h\ge0\), and suppose the sums are finite and positive. If

\[
 m\le r_h(\omega)\le M
 \quad\text{for every }h,\omega,
\]

then

\[
 m\le \log\frac{\widetilde\rho(\omega)}{\rho(\omega)}\le M,
 \qquad
 \operatorname{osc}\log\frac{\widetilde\rho}{\rho}\le M-m.
\]

### Proof

The ratio is a convex combination of the numbers \(e^{r_h(\omega)}\), with
weights \(a_h(\omega)/\rho(\omega)\). \(\square\)

The center must be common across histories. Individual oscillation bounds do
not suffice. For example, on \(\Omega=\{0,1\}\), take

\[
 (a_1(0),a_2(0))=(1,\epsilon),\qquad
 (a_1(1),a_2(1))=(\epsilon,1),
\]

and \(r_1=C,r_2=0\). Each \(r_h\) has zero field oscillation, while the
oscillation of the complete log-density ratio approaches \(C\) as
\(\epsilon\downarrow0\). History-dependent vacuum constants therefore cannot be
discarded one history at a time.

A valid P4 estimate must use either a polymer expansion for the complete
\(\log\rho\) after history summation, or a paired-history comparison with one
common centering interval. Unmatched histories require an additional positive
remainder estimate.

## 5. From local polymer differences to a projective bound

Suppose a **complete** log-density defect on a finite graph \(\Lambda\), modulo
one global constant, has the uniformly convergent expansion

\[
 D_N(\omega)=c_N+
 \sum_s\sum_{X\subset\Lambda}\Delta\Phi_{N,s}(X;\omega),
\]

where \(s\) may label \(E,R,B\) sectors. Define the rooted oscillation norm

\[
 \eta_{N,s}=\sup_{x\in\Lambda}
 \sum_{X\ni x}\frac{\operatorname{osc}\Delta\Phi_{N,s}(X)}{|X|}.
\]

### Proposition 4: polymer scalarization

\[
 \boxed{
 \operatorname{osc}D_N\le |\Lambda|\sum_s\eta_{N,s}.}
\]

### Proof

Subadditivity of oscillation gives a sum over \(s,X\). For each sector,

\[
 \sum_X\operatorname{osc}\Delta\Phi(X)
 =\sum_{x\in\Lambda}\sum_{X\ni x}
   \frac{\operatorname{osc}\Delta\Phi(X)}{|X|}
 \le |\Lambda|\eta.
\]

For countably many polymers, subtract each activity's value at a fixed
configuration. Summability of the oscillations gives uniform convergence by the
Weierstrass test. \(\square\)

On a graph of maximum degree \(z\), the number of connected \(m\)-site polymers
containing a fixed site is at most \(A^{m-1}\) with, for example, \(A=z^2\).
Thus

\[
 \operatorname{osc}\Delta\Phi_N(X)
 \le\delta_Ne^{-\kappa|X|},\qquad Ae^{-\kappa}<1,
\]

implies

\[
 \eta_N\le
 \delta_N\frac{e^{-\kappa}}{1-Ae^{-\kappa}}.
\]

Polymer-size decay must beat lattice-animal entropy, and the remaining
ultraviolet-depth factor \(\delta_N\) must be summable.

## 6. Refining lattices, volume factors, and marginal matching

If scale \(r\) has at most \(|\Lambda_0|L^{dr}\) sites and the defect contains
activities at all scales, then

\[
 \operatorname{osc}D_N
 \le |\Lambda_0|\sum_{r=0}^N L^{dr}\eta_{N,r}.
\]

For the useful model bound

\[
 \eta_{N,r}\le C\alpha^{N-r}\beta^r,
\]

summability in \(N\) follows if

\[
 \alpha<1,\qquad L^d\beta<1,
\]

because

\[
 \sum_{N\ge0}\operatorname{osc}D_N
 \le\frac{C|\Lambda_0|}{(1-\alpha)(1-L^d\beta)}.
\]

Thus a microscopic factor \(q^N\) with merely \(q<1\) is not enough: the
\(L^{dN}\) site entropy requires \(L^dq<1\). Equivalently, if
\(a_N=\ell L^{-N}\) on a fixed physical volume and a rooted local defect is
\(O(a_N^{d+\sigma})\), then its global oscillation is
\(O(R^da_N^\sigma)\), which is geometrically summable for \(\sigma>0\).

An adjacent action defect of the form

\[
 D_N=c_N+\delta\lambda_N A+
 \sum_X(\Delta E_N+\Delta R_N+\Delta B_N)(X)
\]

obeys

\[
 \operatorname{osc}D_N\le |\Lambda|
 \bigl(C_A|\delta\lambda_N|+
       \eta_N^E+\eta_N^R+\eta_N^B\bigr).
\]

The global constant \(c_N\) disappears, but the marginal action mismatch does
not. Matching the coupling coordinate is therefore essential. Also, Balaban's
\(B\)-terms are attached to boundaries of field-history regions, not necessarily
to the physical torus boundary; without a Peierls or averaged estimate they must
be counted volumetrically.

At fixed terminal scale, \(|\Lambda|\asymp(R/\ell)^d\). These estimates are
sufficient for the fixed-\(R,\ell\) milestone, but are not uniform in volume. A
thermodynamic-limit theorem would need a local covariance/interpolation norm and
uniform clustering, not global oscillation.

## 7. Revised minimal route to M1

The exact logical chain is now:

1. **H0:** construct the small-coupling trajectory with a fixed terminal
   renormalization condition.
2. **Robs:** extend the large-field \(R\)-operation to preserve the selected
   terminal generating functions, or prove a vanishing cumulative test bias.
3. **P4a:** put adjacent physical cutoffs on a genuinely common lattice and
   verify compatibility of the iterated deterministic averages.
4. **P4b:** match vacuum and marginal coordinates and compare complete
   large-field histories, including unmatched sectors.
5. **P4c:** prove a rooted difference bound whose scale gain beats the refining
   lattice entropy.
6. Apply Propositions 2--4, the projective criterion in 07, and the analytic
   lemmas in 03.

Published source-free \(RT\) stability is indispensable input to this program,
but it closes none of Robs, P4a, P4b, or P4c by itself.

