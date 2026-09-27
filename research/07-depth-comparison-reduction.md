# Adjacent-depth comparison via projective density control

Status: **proved here as an abstract reduction**. The required Yang--Mills
estimate on the effective densities remains open.

The terminal-source identity means that no source vertex is needed inside the
exact group-delta block maps \(T\). It does **not** remove the source/test problem
for Balaban's large-field \(R\)-operation, which preserves the vacuum integral
while generally changing the density. Subject to that separate Robs obligation,
M1 reduces to comparing two positive **physical** terminal measures on the same
fixed coarse configuration space. This note gives a sufficient norm for that
comparison; `09-common-space-and-r-obstruction.md` records the missing
physical-versus-stabilized bridge.

## Setup

Let \(\nu_n\) and \(\nu_{n+1}\) be probability measures on the same compact
space \(\Omega\), with \(\nu_{n+1}\ll\nu_n\), and suppose

\[
 \frac{d\nu_{n+1}}{d\nu_n}(V)
 =\frac{e^{D_n(V)}}{\nu_n(e^{D_n})}
\]

for a bounded real function \(D_n\). Define its oscillation

\[
 \operatorname{osc}D_n
 =\sup_{V\in\Omega}D_n(V)-\inf_{V\in\Omega}D_n(V)
 =:\varepsilon_n.
\]

This is the natural quantity for normalized densities: adding a vacuum-energy
constant to \(D_n\) does not change its oscillation.

## Proposition 1: bounded-test comparison

For every bounded measurable \(f\),

\[
 \left|\nu_{n+1}(f)-\nu_n(f)\right|
 \le \lVert f\rVert_\infty\bigl(e^{\varepsilon_n}-1\bigr).
\]

### Proof

Subtract \(\inf D_n\), which leaves the normalized Radon--Nikodym derivative
unchanged. Then \(1\le e^{D_n}\le e^{\varepsilon_n}\), and therefore

\[
 e^{-\varepsilon_n}
 \le \frac{e^{D_n}}{\nu_n(e^{D_n})}
 \le e^{\varepsilon_n}.
\]

Writing the difference of expectations against \(\nu_n\) and using
\(\max\{1-e^{-\varepsilon_n},e^{\varepsilon_n}-1\}
=e^{\varepsilon_n}-1\) proves the claim. \(\square\)

## Proposition 1': an \(L^1\) projective criterion

Under the same Radon--Nikodym hypothesis, let \(c\in\mathbb R\) and set

\[
 \delta_n(c)=\nu_n\!\left(\left|e^{D_n-c}-1\right|\right).
\]

If \(\delta_n(c)<1\), then every bounded measurable \(f\) satisfies

\[
 |\nu_{n+1}(f)-\nu_n(f)|
 \le \lVert f\rVert_\infty
      \frac{2\delta_n(c)}{1-\delta_n(c)}.
\]

The estimate may be optimized over \(c\). It is weaker than uniform oscillation
control because it tolerates a large defect on a set of small \(\nu_n\)-mass.

### Proof

Put \(X=e^{D_n-c}\) and \(m=\nu_n(X)\). Then
\(m\ge1-\delta_n(c)>0\), and the normalized Radon--Nikodym derivative is
\(X/m\). Moreover,

\[
 \nu_n\!\left(\left|\frac Xm-1\right|\right)
 \le \frac{\nu_n(|X-1|)+|1-m|}{m}
 \le \frac{2\delta_n(c)}{1-\delta_n(c)}.
\]

Integrating \(f\) against this density difference proves the claim.
\(\square\)

## Proposition 2: generating functions and cumulants

Let \(|F_j|\le B_j\) and

\[
 Z_n(z)=\nu_n\!\left(e^{\sum_jz_jF_j}\right),
 \qquad
 S_\rho=\sum_jB_j\rho_j.
\]

Then

\[
 \sup_{z\in D_\rho}|Z_{n+1}(z)-Z_n(z)|
 \le e^{S_\rho}\bigl(e^{\varepsilon_n}-1\bigr).
\]

If \(S_\rho<\log2\), the normalized logarithms are holomorphic on the same
polydisc and

\[
 \lVert\operatorname{Log}Z_{n+1}-\operatorname{Log}Z_n\rVert_{D_\rho}
 \le
 \frac{e^{S_\rho}}{2-e^{S_\rho}}
 \bigl(e^{\varepsilon_n}-1\bigr).
\]

Consequently, if \(\sum_n\varepsilon_n<\infty\), every fixed joint cumulant is
Cauchy, with the tail estimate

\[
 \left|\kappa_\alpha(Z_\infty)-\kappa_\alpha(Z_N)\right|
 \le
 \alpha!\rho^{-\alpha}
 \frac{e^{S_\rho}}{2-e^{S_\rho}}
 \sum_{n\ge N}\bigl(e^{\varepsilon_n}-1\bigr).
\]

### Proof

The exponential test function has norm at most \(e^{S_\rho}\), so Proposition 1
gives the first estimate. The uniform zero-free disc and Lipschitz estimate for
the logarithm are Theorem C of `03-source-cumulant-lemma.md`. Summability of
\(\varepsilon_n\) implies summability of \(e^{\varepsilon_n}-1\): the sequence
is bounded and \(e^x-1\le e^M x\) for \(0\le x\le M\). Cauchy's derivative
estimate then gives the cumulant tail. \(\square\)

The same argument with Proposition 1' replaces
\(e^{\varepsilon_n}-1\) by
\(2\delta_n(c_n)/(1-\delta_n(c_n))\). Summability of those quantities is enough
for all conclusions of Proposition 2.

## Effective-action form

If the physical terminal measures have strictly positive densities
\(\rho_n\) and \(\rho_{n+1}\) with respect to the same coarse Haar measure, take

\[
 D_n=\log\rho_{n+1}-\log\rho_n.
\]

The sufficient M1 estimate is therefore

\[
 \sum_n\operatorname{osc}
 \bigl(\log\rho_{n+1}-\log\rho_n\bigr)<\infty.
\]

This is a projective estimate: all field-independent vacuum energies disappear.
It is substantially stronger than the source-test requirement: summability of
the oscillations gives summable increments in full dual total variation. Its
advantage is instead invariance under one global vacuum-energy constant. The
\(L^1\) criterion above is a weaker fallback when the uniform log ratio is badly
behaved on rare configurations.

## Concrete next target

Put the cutoff-\(a_n\) and cutoff-\(a_{n+1}\) **physical** theories on a common
terminal \(\ell\)-lattice and use the same gauge convention. Impose one physical
terminal renormalization condition, or prove that equality of Balaban's
history-dependent \(g_K\) implies it with a summable marginal mismatch. Then
establish an observable-preserving replacement for the CMP **119/122** \(RT\)
density. A strong sufficient estimate is a geometric or otherwise summable bound

\[
 \operatorname{osc}
 \bigl(\log\rho_{n+1}^{(\ell)}-\log\rho_n^{(\ell)}\bigr)
 \le C\vartheta^n,
 \qquad 0<\vartheta<1,
\]

conditional first on the small-coupling sequence. Published stability bounds on
each auxiliary density separately do not imply this difference estimate. Since
CMP **119**, Eq. (2.18), is a sum over large-field histories, the comparison must
also control the history sum with a common centering; termwise oscillations modulo
history-dependent constants are insufficient. A rooted polymer criterion and a
sharp counterexample are proved in the common-space note. If global oscillation
is unavailable, the immediate alternative is a summable source-test estimate or
the \(L^1\) criterion of Proposition 1'.

## Boundary of the reduction

The propositions do not produce \(D_n\), prove mutual absolute continuity,
identify the auxiliary \(RT\) density with the physical \(T^n\)-pushforward, or
bound any CMP **119** polymer difference. Those are remaining Yang--Mills steps.
They do show that one **global** additive constant is irrelevant and turn a
summable physical effective-action comparison into quantitative cumulant
convergence. Constants depending on a large-field history are not globally
irrelevant before the history sum.
