# Terminal mean shifts and the complete \(R\)-observable gap

Status: **Lemma 1 and the diagnostic probability lemmas below are proved
here.**  The identification of the two fiber laws is taken from Balaban's
published formulas, with the caveats stated in Section 2.  The three
Yang--Mills estimates H6--H8 isolated below are open.  In particular, this
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
\(\mathrm{Reg}\).  Put

\[
 \xi=\nabla f(\Phi_0),\qquad
 \kappa=\sup_{u\in K}\|\nabla^2 f(u)\|_{\rm op},
 \tag{3.1}
\]

and suppose

\[
 \omega:=\sup_{\operatorname{supp}(p+q)}
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

### Corollary 2: terminal oscillation

If

\[
 \Delta_\Lambda=
 \sup_{\mathrm{Reg}\cap\operatorname{supp}(p+q)}
 |\Phi-\Phi_0|,
 \tag{3.6}
\]

then

\[
 |\mathbb E_pF-\mathbb E_qF|
 \le |\xi|\,|M_{p,q}|+\kappa\Delta_\Lambda^2
 +\omega\bigl(p(\mathrm{Reg}^c)+q(\mathrm{Reg}^c)\bigr).
 \tag{3.7}
\]

For the \(R\)-problem, \(\Phi=\Phi_K\) should be a smooth gauge-invariant
coordinate map of the selected **terminal** holonomy data---for example, a
finite vector of character functions.  It need not be one-to-one.  A
gauge-fixed bond chart is also possible only if the gauge-fixing map and its
derivatives are included in the estimates.  If logarithmic coordinates are
used, they are used only on \(\mathrm{Reg}\); bounded tests are controlled
crudely on its complement.  This avoids assuming a global logarithm and keeps
the differentials relevant to H6 covariantly conserved.

The three missing Yang--Mills inputs are now explicit:

> **H6 (terminal oscillation).**  On \(\mathrm{Reg}\), prove, uniformly in
> histories and exterior fields,
> \[
> \Delta_\Lambda
> \le C(|E_\Lambda|+L^d)L^{(1-d)m}.
> \tag{3.8}
> \]
> This must include the first irregular level and propagation through regular
> nontrivial backgrounds.
>
> **H7 (bad-fiber tail).**  Prove a history- and shape-summed bound on
> \(\widehat p_\Lambda(\mathrm{Reg}^c)\) and
> \(\widehat q_\Lambda(\mathrm{Reg}^c)\) strong enough to remain summable after
> the \(L^{dm}\) placement count.
>
> **H8 / Y6\(^{\prime\prime}\) (terminal mean shift).**  With \(M_\Lambda\)
> defined by (3.3) in the terminal chart, prove
> \[
> |M_\Lambda|
> \le C|E_\Lambda|L^{(1-d)m}\eta_m,
> \qquad
> \sum_m\varepsilon_mL^m\eta_m<\infty,
> \tag{3.9}
> \]
> uniformly in histories and exterior fields.

Here \(\varepsilon_m\) denotes the already-summed component suppression, not
a bound on the normalized conditional mean.

Under the additional counting hypothesis that components with \(|E_\Lambda|=s\)
occur with weight at most \(C\varepsilon_mL^{dm}/s\) per terminal block, H8
contributes at most \(C\varepsilon_mL^m\eta_m\).  H6 makes the quadratic term
at most

\[
 C\varepsilon_m sL^{(2-d)m},
 \tag{3.10}
\]

before the remaining shape sum.  It is geometrically summable in \(d=4\) if
the shape weights absorb the factor \(s\).  A conservative sufficient form of
H7 is

\[
 \sum_m\varepsilon_mL^{dm}
 \sup_{\Lambda,V_c,h}
 \bigl[\widehat p_\Lambda(\mathrm{Reg}^c\mid V_c)
      +\widehat q_\Lambda(\mathrm{Reg}^c\mid V_c)\bigr]<\infty.
 \tag{3.11}
\]

Equations (3.8)--(3.11) are a conditional scale reduction, not published
estimates.

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

This does not invalidate (4.1).  It makes (4.1) the linear seed for H6 rather
than a proof of H8.

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

## 6. Why the evident symmetry does not supply H8

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

There is a useful **conditional flat-background exception**.  Suppose a
neighborhood \(N\supset\Lambda\) can be put in a pure-gauge frame, and suppose
that, with this exterior held fixed, both localized fiber laws, the regular
event, and the terminal perturbation \(Y_{\rm loc}\) obey

\[
 S_{h*}\widehat p_\Lambda=\widehat p_\Lambda,\qquad
 S_{h*}\widehat q_\Lambda=\widehat q_\Lambda,\qquad
 Y_{\rm loc}(S_hW)=\operatorname{Ad}_hY_{\rm loc}(W)
 \tag{6.2}
\]

for every constant color rotation \(h\).  For a compact simple group, the
adjoint representation has no invariant vector.  Hence each regular first
moment of \(Y_{\rm loc}\) vanishes.  Equivalently, the linear term of any smooth
gauge-invariant terminal test vanishes, and Lemma 1 leaves only the quadratic
and bad-set terms.

This gives a structurally sound route to H8: verify (6.2) for every localized
history at a flat exterior, then prove a uniform susceptibility estimate for
the change in the terminal mean under exterior curvature.  Schematically, one
would need

\[
 |M_\Lambda(V_c)-M_\Lambda(V_{\rm flat})|
 \le \chi_\Lambda\,
       \operatorname{curv}(V_c|_N)
       +\text{localized tail},
 \tag{6.3}
\]

with the right side satisfying (3.9) after history and placement sums.  Neither
the invariance through every complete-\(R\) localization nor the susceptibility
bound is in the published estimates.  In particular, averaging over exterior
fields cannot be used until correlations between the exterior weight and the
fiber bias are controlled.

## 7. Published inputs and open hypotheses

| ID | Input | Status |
|---|---|---|
| H1 | Fiber variable and fixed exterior data; CMP **122 I**, Eqs. (0.3), (1.73)--(1.76) | published |
| H2 | Axial small-field template; CMP **122 I**, Eqs. (1.100)--(1.101) | published formula; scan transcription still required for verbatim use |
| H3 | True history-term representation; CMP **119**, Eqs. (2.18), (2.23), and CMP **122 I**, Eqs. (1.71)--(1.75) | published representation, not a moment bound |
| H4 | Positivity, fiber-mass normalization, and component suppression | published source-free bounds |
| H5 | Regular-domain analyticity and functional derivatives of the averaging map; CMP **98**, Propositions 3--7 | published; no comparison of the fiber laws |
| H6 | Terminal oscillation (3.8), including the first irregular step and curved backgrounds | open; the trivial-background linear part is proved in note 10 |
| H7 | Summable regular-set-complement probability for the normalized fiber laws | open |
| H8 | Terminal mean-shift estimate (3.9), Y6\(^{\prime\prime}\) | open; core conditional-law input |

The next defensible technical target is H6.  CMP **98** provides the local
analytic machinery, but its published first-derivative estimates do not by
themselves cover the irregular first step or prove the terminal bound.  H7 and
H8 require information about normalized fiber laws that the source-free
\(R\)-bounds intentionally do not retain.  Research note 12 reduces H6 to a
curvature-stable one-step contraction of conserved currents and one localized
rough-step path bound; neither estimate is stated in Proposition 5.

One could redesign the template by an exponential tilt chosen to match the
terminal mean.  That removes the linear defect by construction, but introduces
new localized linear terms and a source-dependent minimizer.  It is a possible
new RG scheme, not a consequence of Balaban's present one.
