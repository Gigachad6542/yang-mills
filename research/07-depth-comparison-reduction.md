# Adjacent-depth comparison via projective density control

Status: **proved here as an abstract reduction**. The required Yang--Mills
estimate on the effective densities remains open.

The terminal-source identity means that M1 does not require a source-dependent
RG. It requires comparison of two positive, source-free terminal measures on the
same fixed coarse configuration space. This note gives a concrete sufficient norm
for that comparison.

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

## Effective-action form

If \(\rho_n\) and \(\rho_{n+1}\) are strictly positive densities with respect to
the same coarse Haar measure, take

\[
 D_n=\log\rho_{n+1}-\log\rho_n.
\]

The sufficient M1 estimate is therefore

\[
 \sum_n\operatorname{osc}
 \bigl(\log\rho_{n+1}-\log\rho_n\bigr)<\infty.
\]

This is a projective estimate: all field-independent vacuum energies disappear.
It is stronger than convergence only in the source-test seminorm but weaker and
more RG-natural than fixing absolute normalizations of the full effective action.

## Concrete next target

Put the cutoff-\(a_n\) and cutoff-\(a_{n+1}\) theories on a common terminal
\(\ell\)-lattice, use the same terminal coupling and gauge convention, and write
their complete CMP **119** densities including all \(E\), \(R\), and \(B\)
sectors. The next new estimate is a geometric or otherwise summable bound

\[
 \operatorname{osc}
 \bigl(\log\rho_{n+1}^{(\ell)}-log\rho_n^{(\ell)}\bigr)
 \le C\vartheta^n,
 \qquad 0<\vartheta<1,
\]

conditional first on the small-coupling sequence. Published stability bounds on
each density separately do not imply this difference estimate.

## Boundary of the reduction

The propositions do not produce \(D_n\), prove mutual absolute continuity, or
bound any CMP **119** polymer difference. Those are the remaining Yang--Mills
steps. They do show exactly which additive constants are irrelevant and turn a
summable effective-action comparison into quantitative cumulant convergence.
