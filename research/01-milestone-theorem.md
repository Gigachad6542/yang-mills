# Milestone theorem: source-stable RG and block-observable convergence

Status: **target**. This file specifies what would count as completion; it does
not state a theorem currently proved in the literature or in this repository.

## Parallel stage S0: local-source stress test

For (j\in\tfrac12\mathbb N_0) and an oriented plaquette (p), put

\[
 \phi_{j,p}(U)=\frac{1}{2j+1}\chi_j(U_p),
 \qquad |\phi_{j,p}(U)|\le 1.
\]

For a finite representation set \(\mathcal J\), smooth macroscopic sources
\(J_j\), and finitely many marked plaquettes, define

\[
 G_{a,R}(J,z)=\mathbb E_{\mu_{a,R}}\exp\!\left\{
 a^4\sum_p\sum_{j\in\mathcal J}J_j(c_p)\phi_{j,p}
 +\sum_{r=1}^qz_r\phi_{j_r,p_r}\right\}.
\]

Stage S0 asks for the full small-field/large-field Balaban representation with
these sources, analytic source-dependent polymer activities, and scale-uniform
derivative bounds in the same localization norms as the vacuum construction.
This is a test of whether sources survive the published RG machinery. It does
**not** assert cutoff convergence. Raw plaquette characters tend toward their
identity contribution and are not, without subtraction and matching, the
renormalized local field \(\operatorname{tr}F^2\).

The full microscopic-source theorem S0 is not a prerequisite for M1. A
microscopic plaquette source is present at the ultraviolet scale and marks every
block integration. An M1 source depends only on the terminal block variable and
factors outside every earlier exact \(T\)-integration. It does **not** factor
through Balaban's large-field \(R\)-replacement, which preserves the unweighted
integral but generally changes the density. The smaller, terminal-test
\(R\)-extension called Robs in `09-common-space-and-r-obstruction.md` is therefore
a prerequisite for using the published \(RT\) bounds in M1.

## Stage M1: fixed-scale block observables

Fix a physical observation scale \(\ell>0\) with \(R/\ell\in\mathbb N\). For
lattice spacings \(a_n=\ell L^{-n}\), let \(U\mapsto\bar U^{(n)}\) denote the
\(n\)-fold deterministic gauge-covariant average in
Balaban's construction. Its terminal variable is a coarse \(SU(2)\) connection
\(V=\bar U^{(n)}\) on the \(\ell\)-lattice, subject to the construction's gauge
convention. The exact group-delta transformation and source identity are recorded
in `04-terminal-source-identity.md`.

Let \(C_1,\ldots,C_m\) be closed coarse-lattice paths and let \(h\) be a bounded
continuous function on \([-2,2]^m\) (holomorphic on a complex neighborhood when
field-complexification estimates require it). Define

\[
 \mathcal O_{n,h}(U)
 =h\!\left(\operatorname{TrHol}_{C_1}(\bar U^{(n)}),\ldots,
           \operatorname{TrHol}_{C_m}(\bar U^{(n)})\right).
\]

Balaban's exact \(T\)-transformation inserts the deterministic average through a
group-delta constraint. A source depending only on the terminal variable factors
through that constraint exactly, so it creates no new vertex inside the exact
block integrations. The published four-dimensional induction, however, controls
an \(RT\)-stabilized density. CMP **122 I** explicitly defines \(R\) by equality
of total integrals while allowing the density to change. Consequently the
physical terminal generating function is not identified with the integral of
the published stabilized density. One must extend \(R\) to the terminal test or
bound its cumulative observable bias; see
`09-common-space-and-r-obstruction.md`.

Choose finitely many real-valued observables
\(\mathcal O_{n,1},\ldots,\mathcal O_{n,q}\), uniformly bounded by constants
\(B_1,\ldots,B_q\), and set

\[
 Z_n(z)=\mathbb E_{\mu_{a_n,R}}
 \exp\!\left(\sum_{j=1}^q z_j\mathcal O_{n,j}\right),
 \qquad z\in\mathbb C^q.
\]

### Target M1

There should be a polydisc \(D_\rho\), independent of \(n\), and a holomorphic
\(Z_\infty\) such that

1. **Summable cutoff comparison.** There are \(\delta_n\ge0\),
   \(\sum_n\delta_n<\infty\), for which
   \[
      \sup_{z\in D_\rho}|Z_{n+1}(z)-Z_n(z)|\le\delta_n.
   \]
2. **Large-field completeness.** The comparison includes every large-field and
   boundary polymer; it is not only a small-field expansion.
3. **Observable-preserving large-field step.** Every \(R\)-replacement preserves
   the selected terminal generating functions, or its cumulative test error is
   proved to vanish uniformly on the source polydisc.
4. **Nondegeneracy.** At least one limiting variance is strictly positive.

Uniform boundedness already gives an elementary cutoff-independent zero-free
subdisc:

\[
 |Z_n(z)-1|
 \le \exp\!\left(\sum_jB_j|z_j|\right)-1<1
 \quad\text{if}\quad
 \sum_jB_j|z_j|<\log2.
\]

Thus zero-freeness is **proved here**, not a separate RG conjecture. On that
subdisc \(W_n=\log Z_n\) is holomorphic, and the summable comparison yields
convergence of all fixed joint cumulants by `03-source-cumulant-lemma.md`.

### Extension M1b: boundary robustness

After M1, compare periodic boundary conditions with an explicitly stated
admissible class. Uniform convergence of the corresponding normalized generating
functions on smaller source polydiscs is useful for infrared work but is not part
of the minimal fixed-torus theorem.

## Reflection-positivity boundary

Reflection positivity is a property of the Wilson measure paired with its
positive-time observable algebra. The correct generating-functional statement is

\[
 \sum_{r,s}\overline{c_r}c_s\,
 G_a[\Theta J_r+J_s]\ge0.
\]

No claim is made that a general complex source-deformed measure is itself
reflection positive. Four-dimensional positive-flow observables also need not lie
in the positive-time algebra because the flow crosses the reflection plane.

## Acceptance criteria

M1 is complete only if:

- the terminal block variable is exactly the one controlled by the cited RG
  theorem, rather than an informal average;
- the measure being compared is the physical \(T^n\)-pushforward of the Wilson
  measure, or its difference from the auxiliary \(RT\) density is controlled in
  the required terminal-test norm;
- constants are independent of ultraviolet depth \(n\);
- vacuum-energy normalizations cancel in the normalized generating function;
- large-field polymers are included;
- convergence, rather than compactness or boundedness, is proved;
- no statement about point-local fields, infinite volume, or a mass gap is
  inferred from M1 alone.
