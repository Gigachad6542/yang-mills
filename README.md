# Constructive 4D Yang--Mills: working repository

This repository is an honest research workspace for the constructive
four-dimensional pure Yang--Mills problem. It does **not** claim a construction
or a mass-gap proof.
Every result is labelled as one of:

- **proved here** -- a complete argument is present in this repository;
- **published input** -- a precise external theorem is cited;
- **published conditional input** -- a cited theorem whose stated hypothesis
  remains open in this project;
- **target** -- a theorem we are trying to establish;
- **conditional reduction** -- a proved implication whose hypotheses remain open;
- **open** -- a proof obligation not supplied here or by the cited inputs.

## Current milestone

For \(G=SU(2)\) on a fixed physical four-torus, prove convergence as the lattice
spacing tends to zero for a finite family of bounded, gauge-invariant observables
of a fixed physical-scale RG block field.  The source-dependent generating
functional must converge on a cutoff-independent complex polydisc, with bounds on
all source derivatives. The exact terminal source factors through Balaban's
group-delta block map \(T\), but not through the large-field \(R\)-replacement,
which preserves the vacuum integral while generally changing the density. An
a source-stable complete-\(R\) extension is therefore part of the Balaban
\(RT\) route to the milestone.

In parallel, a source-stable version of the RG for normalized plaquette
characters is a local-observable stress test. Unlike terminal sources, microscopic
plaquette sources do enter the multiscale polymer analysis. Their raw continuum
limit is not advertised as a renormalized curvature field.

This is deliberately weaker than the Clay problem. It targets a first missing
observable theorem beyond Balaban's conditional, source-free ultraviolet-stability
estimates while avoiding three later problems:

1. removal of the infrared cutoff;
2. construction of point-local renormalized curvature polynomials;
3. a physical-unit mass gap.

## Current theorem status

| Component | Status |
|---|---|
| Exact transport of a terminal source through Balaban's group-delta \(T\)-transformation | proved here from the published formula; does not cover \(R\) |
| Uniform zero-free complex disc for finitely many bounded observables | proved here |
| Generating-functional convergence \(\Rightarrow\) convergence and factorial bounds for fixed cumulants | proved here |
| Summable projective-density difference \(\Rightarrow\) the required generating-functional comparison | proved here |
| Four-dimensional source-free \(RT\) density/vacuum bounds | published, conditional on a small effective-coupling sequence |
| Exact source-dependent lift of the fiber-normalized introductory \(R\) prototype, with a uniform zero-free polydisc | proved here |
| Source-stable localization/exponentiation bounds for the complete large-field \(R\)-operation, or vanishing cumulative \(R\)-bias | open; prerequisite for observable M1 through Balaban's \(RT\) route |
| SU(2) coupling-flow claim used by those bounds | open in this project; announced proof was not published |
| Adjacent-cutoff comparison of physical terminal measures | open; principal M1 estimate |

## Repository map

- `research/00-charter.md` -- scope, conventions, and non-claims.
- `research/01-milestone-theorem.md` -- exact target and acceptance criteria.
- `research/02-proof-obligations.md` -- dependency graph and status ledger.
- `research/03-source-cumulant-lemma.md` -- abstract analytic reduction, proved here.
- `research/04-terminal-source-identity.md` -- exact source transport through an
  abstract block kernel and Balaban's exact \(T\)-map, proved here; its boundary
  at the measure-changing \(R\)-step is explicit.
- `research/05-observable-strategy.md` -- comparison of local, blocked, and flowed
  observable families.
- `research/06-balaban-audit.md` -- theorem-by-theorem dependency audit, including
  the unpublished coupling-flow input and exact block formula.
- `research/07-depth-comparison-reduction.md` -- proved projective-density
  criterion reducing adjacent-cutoff control to cumulant convergence.
- `research/08-coupling-flow-reduction.md` -- proved memoryless backward- and
  history-dependent forward-shooting lemmas, plus the two-term scalar
  asymptotic, isolating the missing RG beta estimates.
- `research/09-common-space-and-r-obstruction.md` -- the exact common-space
  reduction, the observable obstruction at \(R\), history-mixture bounds, and
  polymer-to-projective estimates.
- `research/10-source-dependent-r-prototype.md` -- a proved multi-source
  fiber-normalization theorem, its exact match to the introductory
  \(R\)-prototype, and the remaining complete-\(R\) locality/summability gap.
- `references/primary-sources.md` -- annotated primary-source bibliography.
- `manuscript/main.tex` -- paper-style draft assembled from the research notes.
- `output/pdf/constructive-ym-fixed-volume-milestone.pdf` -- verified nine-page
  build of the current manuscript.

## Immediate rule

No partition-function bound is described as a continuum state, no subsequential
limit as a unique limit, and no decay estimate as a spectral gap unless the dense
observable algebra and physical-unit uniformity hypotheses are stated explicitly.

## Build

The manuscript requires [Tectonic](https://tectonic-typesetting.github.io/). Run

```sh
make manuscript
```

or provide an explicit executable with
`make manuscript TECTONIC=/path/to/tectonic`. The verified output is written to
`output/pdf/constructive-ym-fixed-volume-milestone.pdf`.
