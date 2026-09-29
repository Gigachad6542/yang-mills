# Terminal mean shifts and the complete \(R\)-observable gap

Status: **Lemma 1 and the diagnostic probability lemmas below are proved
here.**  The identification of the two fiber laws is taken from Balaban's
published formulas, with the caveats stated in Section 2.  The three
Yang--Mills estimates H6\(_\Sigma\)--H8\(_\Sigma\) isolated below are open.  In particular, this
note does not prove that the complete \(R\)-operation preserves, or
asymptotically preserves, terminal observables.

This note supersedes the earlier fine-field condition Y6'.  That condition was
not sufficient: nonlinear block averaging creates Baker--Campbell--Hausdorff
terms whose fine-coordinate Hessian is still first order in the terminal
sensitivity.  The clean reduction must be made in a **terminal** chart.

## 1. The observable defect on one fiber

Fix one history, one exterior field \(V_c\), and one \(R\)-component
\(\Lambda\) at scale \(k=K-m\).  Normalize the true and template fiber
weights to probability laws

\[
 \widehat p_\Lambda(dW\mid V_c),\qquad
 \widehat q_\Lambda(dW\mid V_c).
\]

For a bounded terminal test \(F\), the source-blind replacement changes its
conditional expectation by

\[
 B_\Lambda(F)
 =\mathbb E_{\widehat q_\Lambda}F
  -\mathbb E_{\widehat p_\Lambda}F.
 \tag{1.1}
\]

Equivalently, the exact source correction of research note 10 satisfies

\[
 \partial_z\log D_\Lambda(0)
 =\mathbb E_{\widehat p_\Lambda}F
  -\mathbb E_{\widehat q_\Lambda}F.
 \tag{1.2}
\]

Fiber-mass suppression does not bound (1.1): normalization cancels that small
mass.  What is needed is either direct control of the conditional terminal
laws or a structural cancellation in the particular terminal tests.

## 2. What the published fiber formulas do and do not provide

The true fiber weight is the restriction of one history term in the density
of CMP **119**, Eqs. (2.18), (2.23), to
\(W=V_k|_\Lambda\), with \(V_c=V_k|_{\Lambda^c}\) fixed.  CMP **122 I**,
Eqs. (1.71)--(1.76), integrates these variables after imposing the
history-dependent characteristic functions.  The extra function
\(\chi_{k,\Lambda}\) in Eq. (1.75) restricts the field outside the integration
region; it is not a small-field cutoff on every component of \(W\).

The template in CMP **122 I**, Eqs. (1.100)--(1.101), is instead an axial-gauge
small-field weight of the schematic form

\[
 \widehat q_\Lambda(dW\mid V_c)\ \propto\
 e^{-g_k^{-2}A(\zeta,U_{k,X}(W,V_c))}
 \delta_G(W)\,
 \mathbf 1\{ |\log W(b)|<M_0\varepsilon_k:\ b\in\Lambda\}\,dW,
 \tag{2.1}
\]

averaged over the prescribed coordinate graphs.  Formula (2.1) is schematic:
the journal scan must be used before quoting its normalization or indices
verbatim.

Thus the template is supported in a small axial chart, whereas the published
representation of the true fiber law does not impose the same support
restriction on \(W\).  The positive Wilson integrand strongly indicates true
fiber mass outside the template support, but the present argument needs only
the weaker, fully justified conclusion:

> The published bounds do not establish
> \(\widehat p_\Lambda\ll\widehat q_\Lambda\), mutual absolute continuity, or
> a finite log-likelihood ratio on the full fiber.

Consequently, entropy, likelihood-ratio interpolation, and integration by
parts across the two actual laws are not presently licensed.  Hard
characteristic functions would also create boundary terms in a formal
integration-by-parts argument.

## 3. The correct abstract reduction

### Lemma 1: terminal-chart linearization with a bad-set remainder

Let \(p,q\) be probability measures on a fiber \(\Omega\), let
\(\Phi:\Omega\to\mathbb R^N\) and \(F:\Omega\to\mathbb R\) be measurable,
and let \(\mathrm{Reg}\subset\Omega\) be measurable.  Assume that
\(\Phi(\mathrm{Reg})\) lies in a convex set \(K\), that \(\Phi_0\in K\), and
that there is an \(f\in C^2(K)\) for which \(F=f\circ\Phi\) on
\(\mathrm{Reg}\).  Assume
\(|\Phi-\Phi_0|\mathbf1_{\rm Reg}\) is integrable under both laws.  Put

\[
 \xi=\nabla f(\Phi_0),\qquad
 \kappa=\sup_{u\in K}\|\nabla^2 f(u)\|_{\rm op},
 \tag{3.1}
\]

and suppose

\[
 \omega:=\mathop{\rm ess\,sup}_{p+q}
       |F-f(\Phi_0)|<\infty.
 \tag{3.2}
\]

Define the regular, centered mean shift

\[
 M_{p,q}:=
 \mathbb E_p[(\Phi-\Phi_0)\mathbf1_{\rm Reg}]
 -\mathbb E_q[(\Phi-\Phi_0)\mathbf1_{\rm Reg}].
 \tag{3.3}
\]

Then

\[
 \mathbb E_pF-\mathbb E_qF=\langle\xi,M_{p,q}\rangle+r
 \tag{3.4}
\]

with

\[
 \begin{aligned}
 |r|\le{}&\frac\kappa2\left(
  \mathbb E_p[|\Phi-\Phi_0|^2\mathbf1_{\rm Reg}]
 +\mathbb E_q[|\Phi-\Phi_0|^2\mathbf1_{\rm Reg}]
 \right)\\
 &+\omega\bigl(p(\mathrm{Reg}^c)+q(\mathrm{Reg}^c)\bigr).
 \end{aligned}
 \tag{3.5}
\]

#### Proof

On \(\mathrm{Reg}\), Taylor's theorem along the segment from \(\Phi_0\) to
\(\Phi\) gives

\[
 |f(\Phi)-f(\Phi_0)-\langle\xi,\Phi-\Phi_0\rangle|
 \le\frac\kappa2|\Phi-\Phi_0|^2.
\]

On \(\mathrm{Reg}^c\), use (3.2).  Integrate the two decompositions and
subtract. \(\square\)

The same argument has the following total-variation form, needed when a
localized history expansion produces signed terms.  Let \(p,q\) be finite
signed measures with \(p(\Omega)=q(\Omega)=1\), and interpret \(p[g]\) and
\(q[g]\) as signed integrals.  In (3.2), take the essential supremum with
respect to \(|p|+|q|\).  If the displayed moments are finite, then

\[
 \begin{aligned}
 \left|p[F]-q[F]-\langle\xi,M_{p,q}\rangle\right|
 \le{}&\frac\kappa2\left(
  |p|[|\Phi-\Phi_0|^2\mathbf1_{\rm Reg}]
 +|q|[|\Phi-\Phi_0|^2\mathbf1_{\rm Reg}]
 \right)\\
 &+\omega\left(|p|(\mathrm{Reg}^c)+|q|(\mathrm{Reg}^c)\right),
 \end{aligned}
 \tag{3.5$'$}
\]

where \(M_{p,q}=p[(\Phi-\Phi_0)\mathbf1_{\rm Reg}]
-q[(\Phi-\Phi_0)\mathbf1_{\rm Reg}]\).  Indeed, apply the pointwise Taylor
remainder bounds to the Jordan total variations.  No positivity is used
after the common constant cancels because \(p(\Omega)=q(\Omega)\).

### Corollary 2: terminal oscillation

If

\[
 \Delta_\Lambda=
 \mathop{\rm ess\,sup}_{p+q}
 \bigl(|\Phi-\Phi_0|\mathbf1_{\rm Reg}\bigr),
 \tag{3.6}
\]

then

\[
 |\mathbb E_pF-\mathbb E_qF|
 \le |\xi|\,|M_{p,q}|+\kappa\Delta_\Lambda^2
 +\omega\bigl(p(\mathrm{Reg}^c)+q(\mathrm{Reg}^c)\bigr).
 \tag{3.7}
\]

The split depends on \(\Phi_0\) if \(p(\mathrm{Reg})\ne q(\mathrm{Reg})\).
When \(q(\mathrm{Reg})>0\), a useful choice is
\(\Phi_0=\mathbb E_q[\Phi\mid\mathrm{Reg}]\), provided this barycenter lies in
\(K\).  Then

\[
 M_{p,q}=p(\mathrm{Reg})
 \left(\mathbb E_p[\Phi\mid\mathrm{Reg}]
      -\mathbb E_q[\Phi\mid\mathrm{Reg}]\right),
 \tag{3.8}
\]

so the linear term is a pure conditional-mean mismatch.  Uniform control of
\(\Delta_\Lambda\), \(\omega\), and the derivatives of \(f\) is still required
when this center depends on the history and exterior field.

For the \(R\)-problem, \(\Phi=\Phi_K\) should be a smooth gauge-invariant
coordinate map of the selected **terminal** holonomy data---for example, a
finite vector of character functions.  It need not be one-to-one.  A
gauge-fixed bond chart is also possible only if the gauge-fixing map and its
derivatives are included in the estimates.  If logarithmic coordinates are
used, they are used only on \(\mathrm{Reg}\); bounded tests are controlled
crudely on its complement.  This avoids assuming a global logarithm and keeps
the differentials relevant to H6\(_\Sigma\) covariantly conserved.

The norm actually consumed by the complete history sum is placement-summed.
At each scale, fix a deterministic order of the components and replace them
**one at a time**.  The label \(\lambda\in\mathscr C_m\) records the history,
placement, and position in this order.  Just before replacement \(\lambda\),
let \(P_\lambda(V_c)\nu_\lambda(dV_c)\) be the exterior marginal of that
partially modified history term, including its true fiber mass.  The preceding
replacements are therefore already present in \(P_\lambda\); this sequential
choice makes the difference of expectations an exact telescope without
unrecorded mixed-component differences.

Let \(Z>0\) be the common total mass, which every fiber-normalized
\(R\)-replacement preserves, and choose a finite nonnegative measure

\[
 \varpi_\lambda(dV_c)
 \ge Z^{-1}\bigl|P_\lambda(V_c)\nu_\lambda(dV_c)\bigr|.
 \tag{3.9a}
\]

Thus \(\varpi_\lambda\) is a \(Z^{-1}\)-normalized absolute majorant, not an
unnormalized exterior-integrated mass.  It may strictly dominate a signed
localized activity.  For positive conditional fiber laws use Lemma 1; for
normalized signed fiber terms use (3.5\(^{\prime}\)) and replace every
conditional probability below by the corresponding total-variation mass.
Regard \(\Delta_\lambda\), \(M_\lambda\), and the two conditional bad-event
masses as measurable functions of \(V_c\), defined
\(\varpi_\lambda\)-almost everywhere.  Here \(\Delta_\lambda(V_c)\) and the
other essential suprema are taken with respect to the two conditional laws at
that fixed exterior field.  Define

\[
 \begin{aligned}
 \mathcal Q_m&=\sum_{\lambda\in\mathscr C_m}
   \int \Delta_\lambda(V_c)^2\,\varpi_\lambda(dV_c),\\
 \mathcal B_m&=\sum_{\lambda\in\mathscr C_m}
   \int\!\bigl[|p_\lambda|(\mathrm{Reg}^c\mid V_c)
              +|q_\lambda|(\mathrm{Reg}^c\mid V_c)\bigr]
              \,\varpi_\lambda(dV_c),\\
 \mathcal A_m&=\sum_{\lambda\in\mathscr C_m}
   \int |M_\lambda(V_c)|\,\varpi_\lambda(dV_c).
 \end{aligned}
 \tag{3.9}
\]

The three missing inputs in their minimal sufficient form are

\[
 \boxed{
 \sum_m\mathcal Q_m<\infty\quad\text{(H6\(_\Sigma\))},\qquad
 \sum_m\mathcal B_m<\infty\quad\text{(H7\(_\Sigma\))},\qquad
 \sum_m\mathcal A_m<\infty\quad\text{(H8\(_\Sigma\))}.}
 \tag{3.10}
\]

The tail of each series must be the vanishing error in the physical-versus-
stabilized-measure telescope.  These majorants cannot be taken from a final
auxiliary density after all replacements: they belong to the partially
modified density at the corresponding scale.  Constructing them from the
published source-free activity bounds is itself part of the open history
bookkeeping.

A stronger termwise package is sufficient but is not the primary target.
Let \(A_s\) be the number of size-\(s\) connected shapes anchored at a fixed
block, and let \(\pi_{m,s}\) dominate the normalized weight of any one such
shape at any one anchor.  Put
\(\varepsilon_{m,s}=sA_s\pi_{m,s}\).  Then the total normalized majorant mass
of size-\(s\) placements is at most
\(C\varepsilon_{m,s}L^{dm}/s=C A_s\pi_{m,s}L^{dm}\) per terminal block.
Assume the explicit second-moment condition

\[
 \sum_{s\ge1}A_s\pi_{m,s}(s+L^d)^2
 =\sum_{s\ge1}\varepsilon_{m,s}\frac{(s+L^d)^2}{s}
 \le C\varepsilon_m.
 \tag{3.11}
\]

For fixed \(L\), this is equivalent up to constants to the earlier shorthand
\(\sum_s(s+1)\varepsilon_{m,s}\lesssim\varepsilon_m\); writing (3.11) in
this form makes the required second moment of component size explicit.

Suppose also, uniformly in the exterior data on the support of the majorant,

\[
 \Delta_\lambda\le C(s+L^d)L^{(1-d)m},\qquad
 |M_\lambda|\le CsL^{(1-d)m}\eta_m.
 \tag{3.12}
\]

Then the first-order contribution is at most
\(C\varepsilon_mL^m\eta_m\), while the size-\(s\) quadratic contribution is

\[
 C\varepsilon_{m,s}\frac{(s+L^d)^2}{s}L^{(2-d)m}
 \le C_L\varepsilon_{m,s}(s+1)L^{(2-d)m}.
 \tag{3.13}
\]

The second inequality uses \(s\ge1\) and keeps the hub term that a bare
\(sL^{(2-d)m}\) estimate misses.  Summing (3.13) over \(s\) uses (3.11), so it
is geometrically summable in \(d=4\).  A conservative sufficient tail
condition is

\[
 \sum_m\varepsilon_mL^{dm}
 \mathop{\rm ess\,sup}_{\lambda,V_c}
 \bigl[|p_\lambda|(\mathrm{Reg}^c\mid V_c)
      +|q_\lambda|(\mathrm{Reg}^c\mid V_c)\bigr]<\infty.
 \tag{3.14}
\]

The placement hypothesis and normalized majorants in this termwise package are
not theorems of CMP **122 II**.  Its activity and combinatorial estimates make
such a Peierls-type bound plausible, but passing to normalized local weights is
an additional argument.  Equations (3.9)--(3.14) are conditional reductions,
not published estimates.

## 4. Why a fine first moment is insufficient

At the trivial-field linearization, research note 10 proves that pulling a
closed-loop current back through \(m\) linear averaging steps gives

\[
 \|\tau^{(m)}\|_\infty\le L^{(1-d)m}\|\tau\|_\infty.
 \tag{4.1}
\]

This is a first-derivative statement.  It does not imply that the remainder of
a Taylor expansion in the fine axial coordinates is of order
\(L^{2(1-d)m}\).  Already at one nonlinear averaging step,

\[
 \log(e^Xe^Y)=X+Y+\tfrac12[X,Y]+O(|X|^3+|Y|^3),
 \tag{4.2}
\]

up to the convention for anti-Hermitian versus Hermitian coordinates.  Pairing
the commutator term with the current one level above produces a Hessian with
the **one-insertion** scale of that current.  For a nonabelian group it is
generically nonzero.  Thus second moments and commutator anisotropies of the
two fine laws enter at the same sensitivity order as their first moments.

Consequently, the former condition Y6', which controlled only
\(\mathbb E_{\widehat p}A-\mathbb E_{\widehat q}A\), does not control (1.1).
Nor does projecting that difference repair the problem.  In a complete axial
gauge the tree conditions remove every nonzero root-fixed gradient tangent to
the slice, so the proposed \(\Pi^\perp\) is simply the identity there.  A
gauge-independent fine-field seminorm can be defined by pairing with
divergence-free currents, but it still sees only the linear term and not the
BCH remainder.

This does not invalidate (4.1).  It makes (4.1) a linear seed for
H6\(_\Sigma\), not a proof of H8\(_\Sigma\).

## 5. Diagnostic comparison lemmas

These lemmas show exactly what extra estimates would make standard
probability routes work.  Section 2 explains why their hypotheses are not
known for the actual fiber pair.

### Proposition 3: entropy--subgaussian bound

If \(X-\mathbb E_qX\) is \(\sigma^2\)-subgaussian under \(q\) and
\(p\ll q\), then

\[
 |\mathbb E_pX-\mathbb E_qX|
 \le\sqrt{2\sigma^2D(p\Vert q)}.
 \tag{5.1}
\]

This follows from the entropy variational inequality and optimization in the
Laplace parameter.  Shifted Gaussians attain equality.  Hence an
\(O(L^{-m})\) mean gain requires a genuinely new entropy bound of order
\(L^{-2m}\), after the susceptibility scale is included.

### Proposition 4: tilt interpolation

If \(dp=e^U\,dq/q(e^U)\) and
\(dp_t=e^{tU}\,dq/q(e^{tU})\), then

\[
 \mathbb E_pX-\mathbb E_qX
 =\int_0^1\operatorname{Cov}_{p_t}(X,U)\,dt.
 \tag{5.2}
\]

If all \(p_t\) obey a Poincar\'e inequality with constant \(C_t\) and \(X\)
is a unit coordinate, then

\[
 |\mathbb E_pX-\mathbb E_qX|
 \le\int_0^1 C_t
       (\mathbb E_{p_t}|\nabla U|^2)^{1/2}dt.
 \tag{5.3}
\]

Thus functional inequalities transfer the burden to a small score; they do
not create the geometric factor.  Hard support mismatch makes \(U\) infinite
and invalidates this interpolation.

For completeness, if \(\operatorname{osc}U\le a\), then

\[
 \|p-q\|_{\rm TV}\le\tanh(a/4),\qquad
 |\mathbb E_pf-\mathbb E_qf|
 \le\operatorname{osc}(f)\tanh(a/4),
 \tag{5.4}
\]

where \(\|p-q\|_{\rm TV}=\sup_A|p(A)-q(A)|\).  This still requires
\(\operatorname{osc}U=O(L^{-m})\).

### Proposition 5: Stein identity

If \(q\) has a Stein kernel \(\tau\),

\[
 \mathbb E_q[(A-\mathbb E_qA)\varphi(A)]
 =\mathbb E_q[\tau(A)\nabla\varphi(A)],
\]

then the tilt of Proposition 4 obeys

\[
 \mathbb E_pA-\mathbb E_qA=\mathbb E_p[\tau\nabla U].
 \tag{5.5}
\]

This is an exact burden transfer to a score and a susceptibility.  Boundary
flux must be added for hard cutoffs.

## 6. Why the evident symmetry does not supply H8\(_\Sigma\)

An abstract oddness lemma remains useful.  Let \(S\) preserve a reference
measure, let \(X\circ S=-X\), and write a density as
\(e^{E+O}\), with \(E\circ S=E\) and \(O\circ S=-O\).  Pairing each point
with its image gives

\[
 \mathbb E_\mu X=\mathbb E_{\bar\mu}[X\tanh O],
 \qquad d\bar\mu\propto e^E\cosh(O)d\lambda.
 \tag{6.1}
\]

Exact invariance would kill the odd mean, and an odd defect of size
\(O(L^{-m})\) would suffice.  The actual fixed-conditioning problem lacks this
involution.  For a generic exterior field \(V_c\), the standard Wilson-measure
symmetries that also fix \(V_c\) reduce to the center and gauge
transformations supported in \(\Lambda\):

- a global conjugation fixing generic noncommuting exterior holonomies is
  central;
- for \(SU(2)\), charge conjugation is inner;
- a generic exterior field breaks nontrivial lattice isometries;
- interior gauge transformations change a linearized fine field by gradient
  directions, already annihilated by a closed-loop current.

None flips the terminal observable while leaving the conditioning data fixed.
A symmetry moving \(V_c\) relates different conditional laws and gives no
termwise cancellation.  Approximate fluctuation reversal is also unavailable
for the unrestricted true large-field fiber law.

There is a useful **conditional flat-background mechanism**, but it needs more
than flatness.  For one fixed history assume:

1. the two fiber weights are strictly local to a neighborhood
   \(N\supset\Lambda\), up to a separately bounded polymer tail;
2. \(V_c|_N\) is pure gauge and has been put in the flat frame;
3. every factor in both weights, the axial slice, the history label, and
   \(\mathrm{Reg}\) is invariant under constant color conjugation;
4. the local perturbation \(Y_{\rm loc}\) and every link used to define it have
   support in \(N\), with no uncontrolled boundary-crossing bond.

Under these hypotheses,

\[
 S_{h*}\widehat p_\Lambda=\widehat p_\Lambda,\qquad
 S_{h*}\widehat q_\Lambda=\widehat q_\Lambda,\qquad
 Y_{\rm loc}(S_hW)=\operatorname{Ad}_hY_{\rm loc}(W)
 \tag{6.2}
\]

for every constant color rotation \(h\).  For a compact simple group, the
adjoint representation has no invariant vector.  Hence the regular mean of
every \(\operatorname{Ad}\)-equivariant Lie-algebra polynomial with one free
color index vanishes under each law.

This does **not** imply \(M_\Lambda(V_{\rm flat})=0\) for an invariant terminal
coordinate.  Later nonlinear averages contain BCH commutators.  Adjoint
invariance forces a two-point tensor to have color form
\(C_{bb'}\delta^{ac}\), so color-antisymmetric commutator terms vanish in mean;
color-traced symmetric quadratic terms survive, but contain two terminal
sensitivities.  Terms coupled to a curved field outside \(N\) are not removed
by the local color average.

A sound flat-background route to H8\(_\Sigma\) therefore needs **both** estimates

\[
 \begin{aligned}
 |M_\Lambda(V_{\rm flat})|
 &\le C\Delta_\Lambda^2
       +C\Delta_\Lambda\beta_\Lambda
       +\text{localized tail},\\
 |M_\Lambda(V_c)-M_\Lambda(V_{\rm flat})|
 &\le \chi_\Lambda\operatorname{curv}(V_c|_N)
       +\text{localized tail},
 \end{aligned}
 \tag{6.3}
\]

with their weighted sums satisfying H8\(_\Sigma\).  The first line requires an
equivariant expansion through all later averaging steps, not merely the crude
fine-coordinate Hessian in Lemma 1; here \(\beta_\Lambda\) bounds, in local
lattice units, the curvature outside \(N\) met by those later averaging steps.
The second line is a uniform susceptibility
bound.  Strict locality also fails literally for polymer activities with
unbounded support, so their exponential tails must be included.  The standard
Wilson factors, Ad-invariant norm cutoffs, and axial condition
\(h1h^{-1}=1\) are compatible with (6.2), but invariance of every detailed
history factor still requires a scan-level check.  None of these complete-
\(R\) statements is published.  Averaging over exterior fields cannot be used
until correlations between the exterior weight and fiber bias are controlled.

## 7. Published inputs and open hypotheses

| ID | Input | Status |
|---|---|---|
| H1 | Fiber variable and fixed exterior data; CMP **122 I**, Eqs. (0.3), (1.73)--(1.76) | published |
| H2 | Axial small-field template; CMP **122 I**, Eqs. (1.100)--(1.101) | published formula; scan transcription still required for verbatim use |
| H3 | True history-term representation; CMP **119**, Eqs. (2.18), (2.23), and CMP **122 I**, Eqs. (1.71)--(1.75) | published representation, not a moment bound |
| H4 | Positivity, fiber-mass normalization, and component suppression | published source-free bounds |
| H5 | Regular-domain analyticity and functional derivatives of the averaging map; CMP **98**, Propositions 3--7 | published; no comparison of the fiber laws |
| H6\(_\Sigma\) | Placement-summed squared terminal oscillation in (3.10), including the first irregular step and curved backgrounds | open; the trivial-background linear part is proved in note 10 |
| H7\(_\Sigma\) | Placement-summed regular-set-complement probability in (3.10) | open |
| H8\(_\Sigma\) | Placement-summed terminal mean shift in (3.10), the corrected Y6\(^{\prime\prime}\) | open; core conditional-law input |

The next defensible technical target is H6\(_\Sigma\).  CMP **98** provides the local
analytic machinery, but its published first-derivative estimates do not by
themselves cover the irregular first step or prove the placement-summed bound.
H7\(_\Sigma\) and H8\(_\Sigma\) require information about normalized fiber laws that the source-free
\(R\)-bounds intentionally do not retain.  Research note 12 records a strong
uniform sufficient route to H6\(_\Sigma\), which may fail at curved hubs, and
keeps the placement-summed H6\(_\Sigma\) as the primary target; neither estimate
is stated in Proposition 5.

One could redesign the template by an exponential tilt chosen to match the
terminal mean.  That removes the linear defect by construction, but introduces
new localized linear terms and a source-dependent minimizer.  It is a possible
new RG scheme, not a consequence of Balaban's present one.
