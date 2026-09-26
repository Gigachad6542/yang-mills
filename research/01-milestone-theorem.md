# Milestone theorem: fixed-volume block-observable convergence

Status: **target**.  This file specifies what would count as completion; it is not
a theorem currently proved in the literature or in this repository.

## RG-adapted observable class

Fix a physical observation scale \(\ell>0\) for which \(R/\ell\in\mathbb N\).
For lattice spacings \(a_n=\ell L^{-n}\), let \(Q_n\) denote the (n)-fold
gauge-covariant block map used by the chosen Balaban RG construction.  Its output
is a coarse (SU(2)) connection \(V=Q_nU\) on the \(\ell\)-lattice, modulo the
block gauge convention.

Let \(C_1,\ldots,C_m\) be closed coarse-lattice paths contained in a fixed proper
subset of the torus, and let \(h\) be holomorphic on a complex neighborhood of
\([-2,2]^m\).  Define

\[
 \mathcal O_{n,h}(U)
 =h\!\left(\operatorname{Tr}\operatorname{Hol}_{C_1}(Q_nU),\ldots,
           \operatorname{Tr}\operatorname{Hol}_{C_m}(Q_nU)\right).
\]

For real (SU(2)) configurations this is bounded and gauge invariant.  The use of
the final block field is structural: after the exact block-variable insertion the
source stays at the terminal RG scale instead of producing a new ultraviolet
vertex at every step.

The precise definition of \(Q_n\), including its gauge covariance, path choices,
and compatibility with Balaban's large-field domains, is Proof Obligation P1.

## Target statement M1

Choose finitely many real-valued observables
\(\mathcal O_{n,1},\ldots,\mathcal O_{n,q}\) from the class above and set

\[
 Z_n(z)=\mathbb E_{\mu_{a_n,R}}
 \exp\!\left(\sum_{j=1}^q z_j\mathcal O_{n,j}\right),
 \qquad W_n(z)=\log Z_n(z),
 \qquad z\in\mathbb C^q.
\]

There should exist a polyradius \(\rho=(\rho_1,\ldots,\rho_q)>0\), independent of
(n), and a holomorphic function (W_\infty\) on
\(D_\rho=\{z:|z_j|<\rho_j\}\), such that:

1. **Uniform zero-free source domain.**  (Z_n\) is nonzero on (D_\rho\), and the
   branch (W_n(0)=0) is holomorphic there.
2. **Summable cutoff increments.**  There are \(\delta_n\ge0\) with
   \(\sum_n\delta_n<\infty\) such that
   \[
      \sup_{z\in D_\rho}|W_{n+1}(z)-W_n(z)|\le\delta_n.
   \]
3. **Boundary-condition robustness.**  Replacing the periodic fine-lattice
   boundary condition by any member of a stated admissible class changes
   (W_n\) by a quantity tending uniformly to zero on every smaller polydisc.
4. **Nondegeneracy.**  At least one limiting variance
   \(\partial_i\partial_jW_\infty(0)\) is nonzero.

## Consequence M1-C

Target M1 implies convergence of every fixed joint cumulant, with quantitative
tails and factorial bounds.  This implication is proved independently in
`03-source-cumulant-lemma.md`.  It is not the open part of the project.

## Acceptance criteria

M1 is complete only if:

- the (Q_n) used in the observable is exactly the map controlled by the cited RG
  theorem, rather than an analogous informal average;
- constants are independent of the ultraviolet depth (n);
- vacuum-energy normalizations cancel in the normalized (Z_n(z)/Z_n(0));
- large-field polymers are included;
- convergence, rather than compactness or boundedness, is proved;
- no statement about point-local fields or a mass gap is inferred from M1 alone.
