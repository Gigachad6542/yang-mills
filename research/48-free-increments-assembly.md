# (C) of note 22 assembled: free increments converge geometrically

[Superseded (audit 2026-10-09, T82): this note models the step fluctuation through H_k and C^{(M)};
Balaban's K_j carries averaging penalties at all levels i <= j (note 41 §1),
the multi-level penalty is open (note 41 §5.6, T75), and the equivalence of
the two descriptions is not shown here. The claim below holds for the model
of this note.]

Status: **proved for every quadratic and linear operator ingredient**
(T42); the cubic and quartic vertex Riemann sums are **stated**. Data:
`research/scripts/t42_minimizer_symbol_convergence.py` (output `.out`).

## The ingredients of β_k^0

The free (g = 0) one-loop increment β_k^0 (note 22; CMP 109 (5.37)) is the p²
coefficient of the background Hessian of ½ log det of the step-k
fluctuation operator at the trivial background. In Balaban's scheme:

- the step-k fluctuation B lives on the scale-k block lattice. It enters
  the fine field through the minimizer map H_k (CMP 102b Prop. 9). At the
  trivial background H_k is the abelian minimizer map T of note 44, tensored
  with the identity on su(2);
- its Gaussian covariance is the inverse of the induced quadratic form,
  whose symbol is built from the block-flux covariance C^{(M)} (note 47) and
  the averaging weights;
- the vertices V', V'' are the first and second background derivatives of
  the fine-lattice Wilson action and gauge-fixing terms evaluated on H_k B.
  They are fine-lattice sums, over each block, of local polynomials in the
  fine field.

After rescaling to the block lattice, Π_k(K) is a loop integral over
block-lattice momenta of products of these symbols. β_k^0 is a fixed
second moment of it (note 41 §1).

## Convergence of each ingredient as k -> ∞ (M = L^k)

1. **Covariance** C^{(M)}(K) and its inverse on the exact subspace:
   O((1 + log M)/M), proved (note 47); measured about M^{-2}.
2. **Minimizer map**, as the induced child symbol
   B^{(m)}_{ℓ'}(K) = (cross alias sum) · C^{(M)}(K)^{-1}. The cross alias sum
   has the same product-of-δ weight structure as C^{(M)}, with one factor
   ŵ_{M/L} instead of ŵ_M. So the proof of note 47 Theorem 1 applies to it
   verbatim, and the product converges at the same rate. Measured, L = 2:

   | m -> m+1 | sup_{K,ℓ'} |B^{(m)} - B^{(m+1)}| | ratio |
   |---|---|---|
   | 1 -> 2 | 3.27e-1 | — |
   | 2 -> 3 | 9.25e-2 | 3.53 |
   | 3 -> 4 | 2.74e-2 | 3.38 |

3. **Averaging weights** a_k: rate L^{-2k} (note 41).
4. **Vertices (reduced, note 58: Lemma A proved; the structural form (V) is checked
   for the leading gluon vertices).** V', V'' evaluated on H_k B are
   sums over the L^{4k} fine sites of a block of local polynomials (degree
   2-4) in the fine field H_k B. In rescaled units, with H_k B smooth at the
   block scale (note 44: gradients O(M^{-1}) in energy), these are Riemann
   sums of continuum integrals with error O(1/M). The SU(2) structure
   constants enter only as fixed tensors.
5. **Loop integral.** The symbols are uniformly bounded, and the coarse
   propagator is uniformly bounded below on the exact subspace (note 47 §3).
   So the loop integral and its second K-moment converge with the slowest
   rate among items 1-4. The constant-field zero modes are excluded by the
   exact-subspace restriction and gauge fixing, as in CMP 109 §5.

**Conclusion.** |β_k^0 - β_∞^0| <= C (1 + log L^k) L^{-k}. This is (C) of
note 22, with ϑ = L^{-1+ε}, for any ε > 0. Together with (S) and note 22
Prop. D it gives (U), and then (W).

## Status of H0 after this note

    H0 <= (B), regularity [published]
        + (C) [items 1-3 and 5 proved; item 4, the vertex Riemann sums, stated
               (since note 58: reduced to (V) and checked for the gluon,
               ghost and gauge-fixing vertices)]
        + (S) finite one-loop scheme matching [universal part published]
        + (D) memory decay [single-step reduction: notes 29, 42, 44-46].

The remaining genuinely open inputs to H0 are (S)'s finite matching and
(D)'s single-step bounds (A_s), (NA) and (S3).
