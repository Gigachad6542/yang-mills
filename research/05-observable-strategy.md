# Observable strategy

Status: **design decision**, based on published structural facts. This note keeps
separate three goals that no single present observable family satisfies at once:
exact half-space locality, established positive-flow renormalization, and a
source that is simple for Balaban's RG.

| Family | Main advantage | Main obstruction | Project role |
|---|---|---|---|
| Normalized plaquette characters | Exactly local, gauge invariant, uniformly bounded, compatible with the Wilson positive-time algebra | The raw limit is dominated by the identity; \(a^{-4}\)-scaled \(\operatorname{tr}F^2\) needs identity subtraction, matching, and contact counterterms | Stage S0 stress test for source-dependent small/large-field RG |
| Terminal block-holonomy characters | Uniformly bounded; the source factors through every exact \(T\)-block map | Balaban's \(R\)-operation changes the density while preserving only its integral; a terminal-test \(R\)-extension is open, and fixed-scale fields are not point-local | Stage M1 cutoff-convergence target |
| Four-dimensional Wilson-flow fields/loops | Positive-flow observables have the best perturbative UV control | Flow diffuses across the time-reflection plane over radius \(\sqrt{8t}\); energy-density bounds grow with the cutoff | Later continuum-oriented theorem, without automatic RP claim |
| Spatial-flow spatial-loop characters | Gauge invariant, bounded, and remain inside a fixed time slice | Break \(O(4)\); no all-orders finiteness theorem comparable to four-dimensional flow | Later OS-compatible smoothing candidate |

## Stage S0 source

For \(j\in\tfrac12\mathbb N_0\),

\[
 \phi_{j,p}(U)=\frac{\chi_j(U_p)}{2j+1},
 \qquad |\phi_{j,p}|\le1.
\]

With finitely many representations and a smooth macroscopic source,

\[
 G_{a,R}(J,z)=\left\langle\exp\left\{
 a^4\sum_p\sum_jJ_j(c_p)\phi_{j,p}
 +\sum_{r=1}^qz_r\phi_{j_r,p_r}
 \right\}\right\rangle.
\]

Since a four-dimensional hypercubic torus of side \(R\) has
\(6(R/a)^4\) unoriented plaquettes,

\[
 |G_{a,R}(J,z)|
 \le\exp\!\left(6R^4\sum_j\lVert J_j\rVert_\infty
                 +\sum_r|z_r|\right).
\]

This makes elementary source analyticity easy. The new result must be a
scale-resolved, source-stable polymer estimate or an actual cutoff comparison,
not another global generating-function upper bound.

## The local-field warning

The fundamental action observable

\[
 q_p=1-\frac12\operatorname{Tr}U_p\in[0,2]
\]

is finite at every cutoff, but the candidate scalar action density

\[
 \mathcal E_a^{\mathrm{bare}}(x)
 =\frac{\beta(a)}{a^4}\sum_{\mu<\nu}
  \left(1-\frac12\operatorname{Tr}U_{\mu\nu}(x)\right)
\]

is not covered by bounded-source arguments. A later local-field theorem must
construct, at minimum,

\[
 \mathcal E_a^R
 =Z_E(a)\bigl(\mathcal E_a^{\mathrm{bare}}-c_I(a)\mathbf1\bigr)
\]

and the counterterms required for products or a spacetime-dependent source.

## Reflection positivity

The Wilson measure is reflection positive for the reflection-compatible lattice
setup. For positive-time sources the useful statement is the kernel inequality

\[
 \sum_{r,s}\overline{c_r}c_s\,G_a[\Theta J_r+J_s]\ge0.
\]

One should not replace it with the false blanket statement that every complex or
inhomogeneous source-deformed measure is reflection positive.

Four-dimensional Wilson flow commutes with reflection as a transformation, but a
flowed insertion at positive Euclidean time generally depends on links on the
negative side. That is why fixed positive flow time does not automatically define
an observable in the OS positive-time algebra.

## Sequencing decision

1. Use plaquette characters to expose every source-dependent estimate in the
   published RG machinery.
2. Construct a terminal-test-preserving \(R\)-step (or a vanishing \(R\)-bias
   estimate), then prove the M1 physical cutoff comparison for block-holonomy
   characters.
3. Investigate bounded flowed-loop characters. Use full flow for continuum UV
   control or spatial flow for half-space locality, stating the corresponding
   compromise explicitly.
4. Only after these steps address point-local curvature polynomials through a
   renormalized \(t\downarrow0\) or block-scale \(\ell\downarrow0\) theorem.
