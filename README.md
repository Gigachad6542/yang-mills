# Constructive 4D Yang--Mills: working repository

This repository is an honest research workspace for the constructive
four-dimensional pure Yang--Mills problem. It does **not** claim a construction
or a mass-gap proof.
Every result is labelled as one of:

- **proved here** -- a complete argument is present in this repository;
- **published input** -- a precise external theorem is cited;
- **target** -- a theorem we are trying to establish;
- **conditional reduction** -- a proved implication whose hypotheses remain open.

## Current milestone

For \(G=SU(2)\) on a fixed physical four-torus, prove convergence as the lattice
spacing tends to zero for a finite family of bounded, gauge-invariant observables
of a fixed physical-scale RG block field.  The source-dependent generating
functional must converge on a cutoff-independent complex polydisc, with bounds on
all source derivatives.

Before that comparison theorem, establish a source-stable version of each exact
Balaban RG step for normalized plaquette characters. This local source family is
the cleanest diagnostic for the small-field/large-field machinery, but its raw
continuum limit is not advertised as a renormalized curvature field.

This is deliberately weaker than the Clay problem.  It targets the first missing
observable theorem beyond Balaban's ultraviolet-stability estimates while avoiding
three later problems:

1. removal of the infrared cutoff;
2. construction of point-local renormalized curvature polynomials;
3. a physical-unit mass gap.

## Repository map

- `research/00-charter.md` -- scope, conventions, and non-claims.
- `research/01-milestone-theorem.md` -- exact target and acceptance criteria.
- `research/02-proof-obligations.md` -- dependency graph and status ledger.
- `research/03-source-cumulant-lemma.md` -- abstract analytic reduction, proved here.
- `research/04-terminal-source-identity.md` -- exact source transport through an
  abstract block kernel, proved here; matching to Balaban remains open.
- `research/05-observable-strategy.md` -- comparison of local, blocked, and flowed
  observable families.
- `references/primary-sources.md` -- annotated primary-source bibliography.
- `manuscript/main.tex` -- paper-style draft assembled from the research notes.

## Immediate rule

No partition-function bound is described as a continuum state, no subsequential
limit as a unique limit, and no decay estimate as a spectral gap unless the dense
observable algebra and physical-unit uniformity hypotheses are stated explicitly.
