# Annotated primary sources

This list records what each source is being used for.  Inclusion is not an
endorsement of claims beyond the cited result.

## Problem and reconstruction target

1. A. Jaffe and E. Witten, *Quantum Yang--Mills Theory*.
   [Official problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
   Used for the local curvature-polynomial field requirement, asymptotically-free
   short-distance behavior, axiomatic target, and definition of the gap.
2. K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions II*,
   Communications in Mathematical Physics **42** (1975), 281--305.
   [DOI](https://doi.org/10.1007/BF01608978).
   Used for the corrected reconstruction hypotheses, including the strengthened
   regularity condition.
3. K. Osterwalder and E. Seiler, *Gauge Field Theories on a Lattice*, Annals of
   Physics **110** (1978), 440--471.
   [DOI](https://doi.org/10.1016/0003-4916(78)90039-8).
   Used for lattice physical/reflection positivity, transfer-matrix positivity,
   and the strong-coupling construction.  It is not cited as a continuum theorem.

## Balaban gauge-field RG package

The following papers form a dependency chain rather than interchangeable citations.

1. T. Bałaban, *Propagators and Renormalization Transformations for Lattice Gauge
   Theories I*, CMP **95** (1984), 17--40.
   [DOI](https://doi.org/10.1007/BF01215753).
2. T. Bałaban, *Propagators and Renormalization Transformations for Lattice Gauge
   Theories II*, CMP **96** (1984), 223--250.
   [DOI](https://doi.org/10.1007/BF01240221).
3. T. Bałaban, *Averaging Operations for Lattice Gauge Theories*, CMP **98**
   (1985), 17--51. [DOI](https://doi.org/10.1007/BF01211042).
   Eqs. (10)--(15), printed pp. 19--20, define and linearize the deterministic
   gauge-covariant block average used in the active observable definition.
4. T. Bałaban, *Spaces of Regular Gauge Field Configurations on a Lattice and
   Gauge Fixing Conditions*, CMP **99** (1985), 75--102.
   [DOI](https://doi.org/10.1007/BF01466594).
5. T. Bałaban, *Propagators for Lattice Gauge Theories in a Background Field*,
   CMP **99** (1985), 389--434.
   [DOI](https://doi.org/10.1007/BF01240355).
6. T. Bałaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge
   Field Theories*, CMP **102** (1985), 255--275.
   [DOI](https://doi.org/10.1007/BF01229380).
7. T. Bałaban, *The Variational Problem and Background Fields in Renormalization
   Group Method for Lattice Gauge Theories*, CMP **102** (1985), 277--309.
   [DOI](https://doi.org/10.1007/BF01229381).
8. T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I:
   Generation of Effective Actions in a Small Field Approximation and a Coupling
   Constant Renormalization in Four Dimensions*, CMP **109** (1987), 249--301.
   [DOI](https://doi.org/10.1007/BF01215223).
9. T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories II:
   Cluster Expansions*, CMP **116** (1988), 1--22.
   [DOI](https://doi.org/10.1007/BF01239022).
10. T. Bałaban, *Convergent Renormalization Expansions for Lattice Gauge
    Theories*, CMP **119** (1988), 243--285.
    [DOI](https://doi.org/10.1007/BF01217741).
11. T. Bałaban, *Large Field Renormalization I: The Basic Step of the R
    Operation*, CMP **122** (1989), 175--202.
    [DOI](https://doi.org/10.1007/BF01257412).
12. T. Bałaban, *Large Field Renormalization II: Localization, Exponentiation,
    and Bounds for the R Operation*, CMP **122** (1989), 355--392.
    [DOI](https://doi.org/10.1007/BF01238433).

**Dependency warning.** The four-dimensional package must not be cited as an
unconditional completed construction. On printed p. 355 of *Large Field
Renormalization II*, Theorem 1 assumes that the sequence of effective coupling
constants remains in \((0,\gamma]\). The following paragraph states that the
proof of the SU(2) coupling-constant behavior announced as Theorem 2 of the 1987
paper had not been published. Exact equations and page references are recorded in
`research/06-balaban-audit.md`.

What the published estimates provide, under their stated hypotheses, is
source-free ultraviolet stability of normalized RG densities/partition functions.
The active project must not silently strengthen this to convergence of normalized
measures or observables.

## Finite-IR-cutoff construction and flowed observables

1. J. Magnen, V. Rivasseau, and R. Sénéor, *Construction of \(YM_4\) with an
   Infrared Cutoff*, CMP **155** (1993), 325--383.
   [DOI](https://doi.org/10.1007/BF02097397).
   Used both for its constructive proposal and for its explicit statement of what
   remains unproved: IR removal, full OS axioms, topology, and a fully detailed
   convergence proof.
2. M. Lüscher, *Properties and Uses of the Wilson Flow in Lattice QCD*, JHEP 08
   (2010) 071. [arXiv:1006.4518](https://arxiv.org/abs/1006.4518).
3. M. Lüscher and P. Weisz, *Perturbative Analysis of the Gradient Flow in
   Non-Abelian Gauge Theories*, JHEP 02 (2011) 051.
   [arXiv:1101.0963](https://arxiv.org/abs/1101.0963).
4. A. Ramos and S. Sint, *Symanzik Improvement of the Gradient Flow in Lattice
   Gauge Theories*, European Physical Journal C **76** (2016) 15.
   [DOI](https://doi.org/10.1140/epjc/s10052-015-3831-9).
   Used for the explicit four-dimensional nonlocality scale of positive-flow
   observables and the local (4+1)-dimensional reformulation.

## Modern expositions used only as routing aids

1. J. Dimock, *The Renormalization Group According to Balaban I: Small Fields*,
   [arXiv:1108.1335](https://arxiv.org/abs/1108.1335).
2. J. Dimock, *The Renormalization Group According to Balaban II: Large Fields*,
   [arXiv:1212.5562](https://arxiv.org/abs/1212.5562).
3. J. Dimock, *The Renormalization Group According to Balaban III: Convergence*,
   Annales Henri Poincaré **15** (2014), 2133--2175.
   [DOI](https://doi.org/10.1007/s00023-013-0303-3).

These expositions concern scalar \(\phi^4_3\), not four-dimensional Yang--Mills;
they may clarify proof architecture but cannot replace a gauge-field theorem.

## Explicit exclusions

Unrefereed manuscripts announcing a complete Yang--Mills solution are not used as
inputs.  Any future claim of that kind must first be reconciled with the official
problem requirements and independently verified theorem by theorem.
