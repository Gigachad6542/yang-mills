# Balaban dependency and theorem audit

Status: **primary-source audit complete for the active milestone**.

## Bottom line

Balaban's published four-dimensional result is:

- source-free;
- an ultraviolet stability bound, not cutoff convergence;
- conditional on the entire effective-coupling sequence remaining in a small
  interval;
- based on a large-field \(R\)-operation that preserves the vacuum integral but
  generally changes the density, so it does not directly control observables;
- missing the published SU(2) coupling-flow argument needed to keep a nonzero
  terminal coupling fixed as the ultraviolet cutoff is removed.

It therefore cannot directly support a claim of fixed-volume continuum
convergence of gauge-invariant observables.

## Conventions and the exact one-step transformation

Balaban takes \(G\subset U(N)\), usually compact semisimple, and normalizes the
trace by \(\operatorname{tr}1=1\). The Wilson functional is

\[
 A^\epsilon(U)=\sum_p\epsilon^{d-4}
 \bigl(1-\operatorname{Re}\operatorname{tr}U(\partial p)\bigr)
\]

in CMP **109**, Eq. (0.2), printed p. 252, with initial density
\(\rho_0(U)=\exp\{-g_0^{-2}A(U)-E\}\). Relative to the common convention
\(\beta\sum_p(1-N^{-1}\operatorname{ReTr}U_p)\),
\(\beta=2N/g_{\mathrm{lat}}^2\), Balaban's parameter satisfies
\(g_B^{-2}=2N/g_{\mathrm{lat}}^2\).

The blocking has two pieces:

1. \(U\mapsto\bar U\) is a deterministic nonlinear, gauge-covariant block
   average. CMP **98**, Eqs. (10)--(15), printed pp. 19--20, gives the original
   definition, covariance, and linearization. Euclidean-symmetric versions occur
   in CMP **109**, Eq. (0.4), p. 253, and Eq. (0.12), p. 254.
2. The RG operator integrates over fine fields subject to an exact group-delta
   constraint:
   \[
    (T\rho)(V)=\int dU\,\delta(\bar U V^{-1})\rho(U),
   \]
   CMP **119**, Eq. (0.1), printed p. 243.

Thus \(\bar U\) is the deterministic map inside the delta constraint; it is not a
random block variable. The normalization identity

\[
 \int dV\,(T\rho)(V)=\int dU\,\rho(U)
\]

is explicit in the 1986 ICM account, Eqs. (9)--(10), printed p. 1261. These
formulas close the finite-dimensional terminal-source identity in
`04-terminal-source-identity.md`.

## Three-dimensional theorem

CMP **102**, 255--275, contains:

- Eq. (1), p. 256: \(g_0^2=g^2\epsilon\) in \(d=3\);
- Eq. (5), pp. 256--257: cutoff- and scale-uniform upper/lower density bounds;
- Theorem 1, p. 257: ultraviolet stability for compact semisimple \(G\);
- Theorem 2, p. 272: the inductive bounds from which Theorem 1 follows.

This is a source-free stability theorem, not convergence of partition functions
or correlators. The paper also calls the proof "very sketchy" and says technical
details are omitted (p. 257), which matters for any formalization program.

## Four-dimensional conditionality

CMP **109** constructs a small-field effective exponent

\[
 -g_k^{-2}A^\eta(U_k)+E_k(U_k),
\]

with \(E_k\) decomposed into scale-labelled gauge-invariant analytic polymers;
see Eqs. (0.22)--(0.30), printed pp. 256--259.

- Theorem 1, p. 259, closes the construction assuming \(0<g_k\le\gamma\).
- Theorem 3, p. 264, is the precise analytic/local induction under the same
  assumption.
- Theorem 2, pp. 259--260, states for \(G=SU(2)\) the existence of
  \(g_0(\epsilon,g)\) such that \(g_K=g\) and every \(g_k\) remains small; the
  paper says its perturbative proof will appear separately.

The separate proof did not appear in the series. CMP **122 II**, Theorem 1,
printed p. 355, again assumes \(g_k\in(0,\gamma]\). The paragraph immediately
after it says that the proof of CMP **109**, Theorem 2, "has not been published
yet" and that Theorem 1 therefore remains subject to the assumption.

The density bound in CMP **122 II**, Eq. (0.1), printed pp. 355--356,

\[
 \chi_ke^{-g_k^{-2}A(U_k)-E_-|T_\eta|}
 \le\rho_k\le e^{E_+|T_\eta|},
\]

is conditional and is not an inter-cutoff Cauchy estimate.

The exact coupling recursion is

\[
 \frac1{g_1^2}=\frac1{g_0^2}-\beta_1(g_0)
 \quad\text{(CMP **109**, Eq. (0.18), p. 255)},
\]

and generally

\[
 \frac1{g_{k+1}^2}=\frac1{g_k^2}-\beta_{k+1}(g_k)
 \quad\text{(Eq. (0.20), p. 256; repeated as (2.15), p. 268)}.
\]

Equations (1.20)--(1.22), p. 264, extract \(\beta_{j+1}\) from a
vacuum-polarization Hessian/moment. The paper supplies smoothness/analyticity and
uniform boundedness but no uniform positive lower bound or expansion
\(\beta_j(u)=b_*+O(u^2)\). Printed p. 298 also notes that \(\beta_j\) depends on
all preceding couplings despite the one-variable notation. The irrelevant-
polymer bound (0.29) is not a beta-function remainder estimate. The abstract
memoryless backward- and history-dependent forward-shooting steps, together with
the exact missing hypotheses, are isolated in
`08-coupling-flow-reduction.md`.

## Complete density structure

CMP **119**, Eq. (2.18), p. 257, sums over nested small-/large-field histories.
Its exponent, Eq. (2.23), pp. 258--259, has the form

\[
 -g_k^{-2}A(U_k)+E_k(U_k)+R_k(U_k)
 +B_k(U_k,\mathcal A)-E_k^{\mathrm{vac}}.
\]

- \(E_k\): ordinary small-field, coupling- and vacuum-renormalized polymers,
  Eqs. (2.25)--(2.29);
- \(R_k\): large-field-renormalization terms, Eqs. (2.30)--(2.33);
- \(B_k\): polymers localized near large-field boundaries,
  Eqs. (2.40)--(2.42).

Theorem 1, p. 262, preserves this class under the \(RT\) step, subject to its
coupling and \(R\)-operation hypotheses. Theorem 2, p. 263, gives local action
estimates, and Corollary 3, p. 264, gives conditional ultraviolet stability.
CMP **122 I**, Eq. (0.4), p. 176, constructs the basic large-field rewrite while
preserving the total integral. Its prototype is termwise fiber-normalized, but
the fibers depend on the summand/history. Printed pp. 193--194 explicitly say
that the preparatory steps through Eq. (1.75) preserve \(\rho_k\), whereas the
next operation changes the density and replaces equality by equivalence, meaning
equality only after integration over \(V_k\). Printed p. 200 repeats that the
resulting density may not equal \(\rho_k\) although their integrals agree;
Eqs. (1.99)--(1.100) occur on p. 201. CMP **122 II** supplies localization,
exponentiation, and bounds, and p. 378 introduces a second “equivalent, but not
equal” step when reverse Faddeev--Popov removal is performed only after
component integrations.

Accordingly, the exact physical density \(T^k\rho_0\) and the stabilized density
generated by the complete \(RT\) procedure must not be identified. The latter is
adequate for the partition function. For a nonconstant terminal test one needs a
source/test-dependent \(R\)-construction or a quantitative comparison between the
two measures. This obstruction is formalized in
`09-common-space-and-r-obstruction.md`.  The exact source lift of the
introductory fiber prototype, and the remaining locality/summability obligations
for the complete operation, are in
`10-source-dependent-r-prototype.md`.

## What the papers say about observables

CMP **122 II**, printed p. 356, says that Theorem 1 is a basis for studying
expectation values of loop and averaged-loop variables, but that these problems
require detailed analysis and further publication. No source-dependent density
estimate, loop expectation theorem, or continuum correlator theorem follows in
the paper.

The \(J\) in CMP **109**, Eqs. (1.8)--(1.9), p. 261, is an auxiliary bond field
used in differentiating \(U\); it is not a Schwinger source. This project uses
\(K\) for new sources when following Balaban's notation closely.

## What a genuine source extension touches

Even with a bounded, gauge-invariant source, the proof must extend each layer:

- **CMP 109:** marked \(K\)-analytic polymers, joint covariance in \((U,K)\),
  and mixing of identity/action components where relevant;
- **CMP 116:** a marked Mayer/cluster expansion with a source norm and uniform
  \(C^n n!\) derivative estimates; the published Lemma 3, pp. 20--21, is
  unmarked;
- **CMP 119:** marked \(E\), \(R\), and \(B\) sectors, with insertion supports
  transported through background determining sets;
- **CMP 122:** either a source-dependent \(R_K\) preserving \(Z(K)\) for every
  \(K\), or a separately controlled conditional-expectation map;
- **cutoff comparison:** a common source domain, matched bare data, and a
  terminal-scale Cauchy estimate between \(\epsilon\) and \(\epsilon/L\).

For bounded terminal observables, the elementary zero-free complex disc has
already been proved in `03-source-cumulant-lemma.md`; positivity is not needed for
that step.

## Minimal dependency graph

```text
CMP95 free covariances
  -> CMP96 multiscale/restricted covariances
       +-----------------------------------+
CMP98 nonlinear block averaging           |
  -> CMP99 regular fields/gauge fixing     |
  -> CMP99 background propagators --------+
                                          |
                                          v
CMP102 variational problem / analytic background
       +-> CMP102 three-dimensional stability
       +-> CMP109 four-dimensional small fields
             -> CMP116 cluster localization
             -> CMP119 complete E/R/B density class
             -> CMP122 I basic normalized R step
             -> CMP122 II localization and conditional stability

Missing independent node:
proved SU(2) coupling-flow theorem stated as CMP109, Theorem 2
```

## Exact early-stack routing

- CMP **95**, Propositions 1.1--1.2, pp. 33--36: uniform free-covariance and
  exponential-decay bounds.
- CMP **96**, Proposition 2.6, pp. 247--248, and Corollary 2.8, p. 249: main
  multiscale propagator/minimizer inputs.
- CMP **98**, Propositions 2--7: locality, regular-domain expansions, a
  cutoff-independent bounded functional derivative (Proposition 5, p. 42),
  and analyticity of averaging.  Proposition 5 is not a spatial-decay or
  conserved-current contraction theorem; the H6-local strengthening is
  isolated in research note 12.
- CMP **99**, 75--102, Theorem 2, p. 83: unique regular Landau representative.
- CMP **99**, 389--434, Theorems 3.1--3.4, pp. 397--400; Theorems 3.7--3.10,
  pp. 409--415; Theorem 3.14, pp. 426--427; Theorem 3.15, p. 432: background
  propagators, random walks, localization, and covariance.
- CMP **102**, 277--309, Theorem 1, p. 279, and Proposition 9, p. 309: unique
  minimal critical orbit and analytic/local background field.

## Primary links

- [CMP 95](https://doi.org/10.1007/BF01215753)
- [CMP 96](https://doi.org/10.1007/BF01240221)
- [CMP 98](https://doi.org/10.1007/BF01211042)
- [CMP 99, gauge fixing](https://doi.org/10.1007/BF01466594)
- [CMP 99, background propagators](https://doi.org/10.1007/BF01240355)
- [CMP 102, variational problem](https://doi.org/10.1007/BF01229381)
- [CMP 102, three-dimensional stability](https://doi.org/10.1007/BF01229380)
- [CMP 109](https://doi.org/10.1007/BF01215223)
- [CMP 116](https://doi.org/10.1007/BF01239022)
- [CMP 119](https://doi.org/10.1007/BF01217741)
- [CMP 122 I](https://doi.org/10.1007/BF01257412)
- [CMP 122 II](https://doi.org/10.1007/BF01238433)
- [1986 ICM proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1986.2/ICM1986.2.ocr.pdf)
