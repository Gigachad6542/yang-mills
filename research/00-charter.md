# Research charter

## Objective

The long-range objective is a constructive \(SU(2)\) Yang--Mills theory on
\(\mathbb R^4\) satisfying the Osterwalder--Schrader axioms, the short-distance
identification required by Jaffe--Witten, and a positive physical mass gap.

The active objective is narrower:

> Extend fixed-volume ultraviolet control from the vacuum functional to a
> determining family of bounded gauge-invariant observables, with complex-source
> estimates strong enough to control every fixed cumulant.

## Regulator and normalization

Let \(a>0\) and let \(\mathbb T^4_R\) be a four-torus of fixed physical side
length \(R\), approximated by the periodic lattice
\(\Lambda_{a,R}=a\mathbb Z^4/R\mathbb Z^4\).  An oriented edge \(e\) carries
\(U_e\in SU(2)\), with \(U_{\bar e}=U_e^{-1}\).  The Wilson measure is

\[
  d\mu_{a,R}(U)=Z_{a,R}^{-1}
  \exp\!\left[-\beta(a)\sum_p
    \left(1-\tfrac12\operatorname{ReTr}U_p\right)\right]
  \prod_{e\in E^+_{a,R}}dU_e,
  \qquad \beta(a)=\frac4{g_0(a)^2}.
\]

The bare trajectory must eventually be defined by a nonperturbative
renormalization condition.  Until that is supplied, the two-loop relation is an
asymptotic input rather than a definition of a continuum theory:

\[
 a\Lambda_L=(b_0g_0^2)^{-51/121}
 e^{-1/(2b_0g_0^2)}(1+O(g_0^2)),
 \quad b_0=\frac{11}{24\pi^2}.
\]

## Evidence policy

1. Primary papers take precedence over reviews and web summaries.
2. A citation to a paper is not a citation to every informal consequence of it;
   theorem numbers and hypotheses will be recorded whenever obtainable.
3. Perturbative finiteness, formal RG flow, numerical continuum extrapolation, and
   constructive convergence are treated as distinct claims.
4. Fixed positive flow time is explicitly labelled nonlocal on the underlying
   four-dimensional theory.
5. Computer-assisted estimates may certify a finite inequality, but simulations
   are not proof of a continuum limit.
6. Balaban's four-dimensional estimates are used only with every stated
   hypothesis, including control of the effective coupling sequence; an
   announced but unpublished coupling-flow argument is not treated as a theorem.
7. A large-field \(R\)-operation that preserves the vacuum integral is not
   treated as preserving normalized observable expectations. The physical
   \(T^n\)-pushforward and the auxiliary \(RT\)-stabilized density remain distinct
   until a terminal-test comparison is proved.

## Non-claims of the active milestone

The active milestone does not claim point locality, full OS reconstruction,
infinite volume, \(O(4)\) restoration, nontrivial scattering, confinement, or a
mass gap.  Its output is intended to be a controlled finite-volume continuum
cylinder algebra on which those later questions can be formulated without
pretending that partition-function stability already supplies correlation
functions.
