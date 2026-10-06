# Literature check, October 2026: is the continuum limit of 3D/4D pure Yang-Mills known?

Status: **fix** (T60). This is a literature-status record, with no
mathematical claim. It checks whether the targets of this repository
(M1-3D, M1-4D) have been settled in print since note 18's literature
survey.

## Findings (web and arXiv search, 2026-10-06)

- **Chatterjee, "A scaling limit of SU(2) lattice Yang-Mills-Higgs theory"**
  (arXiv:2401.10507). In any d >= 2, along tuned couplings, the
  stereographic projection of the gauge field converges to a **massive
  Gaussian** field. The paper states that it is the first scaling limit of a
  non-abelian lattice gauge theory in d > 2, and that a non-Gaussian limit
  remains open. It needs the Higgs field and does not cover pure
  Yang-Mills.
- **Cao-Chatterjee, "A state space for 3D Euclidean Yang-Mills theories"**
  (arXiv:2111.12813, CMP). It constructs a space of distributional gauge
  orbits, with regularized Wilson loops via the Yang-Mills heat flow, for
  theories that "behave like the GFF" in a stated sense. This is a
  framework conditional on that behaviour, not a construction of the
  measure.
- **Chandra-Chevyrev-Hairer-Shen** (Inventiones 2024): stochastic
  quantization of 3D Yang-Mills-Higgs, with local-in-time solutions. It does
  not construct the invariant measure.
- **Brennecke** (arXiv:2511.07297, J. Stat. Phys.): the leading-order term of
  the lattice U(N) free energy (the Maxwell constant K_d). It is not about
  continuum limits of observables.
- **Unrefereed claims.** arXiv:2506.00284 claims existence and a mass gap
  for SU(3) in 4D via a "convergent joint polymer expansion". A Zenodo
  record (17966583) claims subsequential OS limits. Neither has been
  verified. Both are listed only for completeness and are not used here.
  Claims of this kind need independent expert verification.
- 2D universality and PDE constructions (arXiv:2602.08591, 2607.22236) are
  2D only.

## Consequence for this repository

As far as this search shows, no accepted publication proves:

- convergence of fixed terminal block observables as the cutoff is removed
  for 3D or 4D pure Yang-Mills (M1-3D, M1-4D);
- Balaban's unpublished coupling-flow theorem (CMP 109 Theorem 2), the core
  of H0.

The status labels in the README and in note 02 therefore stand: M1-3D and
M1-4D are open, and the reductions here are conditional.

## Sources

- https://arxiv.org/abs/2401.10507
- https://arxiv.org/abs/2111.12813
- https://arxiv.org/abs/2511.07297
- https://arxiv.org/pdf/2506.00284
- https://zenodo.org/records/17966583
- https://arxiv.org/pdf/2602.08591
- https://arxiv.org/pdf/2607.22236
- https://arxiv.org/html/2608.27976 (3D U(1), numerical: a different continuum limit using a monopole fugacity)
