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
which preserves the vacuum integral while generally changing the density. A
source-stable complete-\(R\) extension is therefore part of the Balaban
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
| Four-dimensional source-free \(RT\) density/vacuum bounds | published conditional input; assumes a small effective-coupling sequence |
| Exact source-dependent lift of the fiber-normalized introductory \(R\) prototype, with a uniform zero-free polydisc | proved here |
| Curved-background contraction for Balaban's symmetric average (note 12 (3.3)) | proved here (note 24); reduces H6\(_\Sigma\) to H7\(_\Sigma\) plus component counting |
| Terminal-chart decomposition of one \(R\)-fiber observable bias into a mean shift, a quadratic regular remainder, and a bad-set tail | proved here as an abstract lemma; the required placement-summed Yang--Mills estimates H6\(_\Sigma\)--H8\(_\Sigma\) are open |
| Source-stable localization/exponentiation bounds for the complete large-field \(R\)-operation, or vanishing cumulative \(R\)-bias | open; prerequisite for observable M1 through Balaban's \(RT\) route |
| SU(2) coupling-flow claim used by those bounds | open; reduced (note 22) to a free-field one-loop universality statement (U) plus memory decay (D), using Balaban's published smoothness of the beta-functions |
| Adjacent-cutoff comparison of physical terminal measures | open; principal M1 estimate |
| Three-dimensional exact-\(T\) pilot: terminal nondegeneracy P6-3D | proved here directly from CMP **102**, Eq. (3)'s published action-free terminal bound, subject to the paper's explicit sketchiness and lower-bound caveats; M1-3D still awaits P4-3D |
| Three-dimensional adjacent-depth comparison P4-3D | conditional reduction (note 18): follows from terminal tangent decay H3D-1, or from coupling differentiability plus irrelevant-defect decay; open. The exact Gaussian model gives rate L^{-2N} |
| Four-dimensional P4 split | conditional reduction (note 18, Thm. 5), but its summable-matching hypothesis is expected to fail (§9a): the one-step coupling mismatch is O(1), so the 4D comparison must be made at fixed terminal effective coupling with an exact marginal cancellation; open |
| Corrected 4D master reduction | conditional reduction (note 27): M1-4D convergence <= coupling flow with shooting + terminal memory decay + summable R-bias series with memory decay |
| 4D β-derivative bound H4D-3 | conditional reduction (note 21): follows from two-loop-order, memory-decaying β-function derivatives, step-wise coupling analyticity of the effective action, and an R-bias bound analytic in β; the cutoff-uniform flow-sensitivity lemma is proved |

## Where the 4D programme stands (lead summary, 2026-10-02)

Each item below is proved here, or reduced here to a precisely stated open
estimate. The research notes give the details.

- **Exact structure (proved):** terminal sources pass exactly through T
  (notes 04, 14); the zero-free source disc and cumulant control (03, 07);
  in 3D, nondegeneracy (17) and the conditional depth comparison (18).
- **Master reduction (note 27):** M1-4D convergence <= (H0) coupling flow
  with shooting + (T) terminal memory decay + (B) a summable R-bias series
  with memory decay. (The earlier split in note 18 Thm 5 is superseded; see
  18 §9a.)
- **(H0), Balaban's unpublished coupling-flow theorem (note 22):** reduced to
  (C) geometric convergence of the free one-loop increments, (S) the
  classical one-loop sum rule, and (D) memory decay. The Codex task T13
  computes the one-loop window numerically.
- **(B), the R-bias:**
  - equal fiber mass for the actual R' (20, proved from CMP 122 I);
  - curved-background contraction (24, proved), so H6 reduces to H7;
  - H7 absorbed via rough-then-contract (25) into the persistence bound (P);
    (P) <= (PA) + (UB) (26), with abelian (PA) proved (26) and non-abelian (PA) on the
    eps_0-small event reduced to Balaban-type fiber convexity and minimizer regularity (34),
    plus a generalized, exterior-averaged H8.
  - The Gaussian model confirms the averaged H8 mechanism (19).
  - Generalized averaged H8 is a covariance between a terminal test and a local
    gauge-invariant function, by integration by parts (32). Its decay (H-dec)
    follows from local, extensive single-step tangent bounds (LS) plus large
    fields (LF). The rate L^{-4m} is charge conservation plus volume
    normalization, up to a power of m that the large-field weight absorbs (33).
- **The one remaining kind of theorem.** The memory-decay statements (D),
  (T-b) and (B-b) in 4D, and H3D-1 in 3D, all assert one thing: Balaban's
  flow contracts the influence of fine-scale defects in irrelevant
  directions. Note 29 reduces that contraction to three single-step
  Lipschitz properties of one Balaban RG step: transport of irrelevant data
  by L^{-alpha}, and O(g^2) dependence of newly generated terms and of the
  beta-function on the input. Those, together with generalized averaged H8,
  (P) and (S), would give M1-4D convergence. Nondegeneracy in 4D (P6) is
  reduced (note 28) to a terminal small-field variance bound plus the quantitative
  R-bias bound; large-field effects are superpolynomially small in the terminal coupling.

## Shortest remaining route: three dimensions

For SU(2) in 3D, the chain to M1-3D (convergence and nondegeneracy of fixed
terminal observables) is:

- nondegeneracy P6-3D: proved from CMP 102 (note 17);
- P4-3D <= terminal memory decay H3D-1 (note 18 Thm. 1);
- H3D-1 <= (S1) + (S2) of note 29. There is no R-operation in 3D, the
  couplings g_k² = g² L^k ε are explicit and identical across depths, so no
  shooting is needed, and g_k -> 0 at fine scales;
- (S1), the transport of existing irrelevant terms with factor L^{-α}, is the
  structure behind CMP 109 (0.29) and Balaban's fifth-order local
  expansion, i.e. a source-level statement.

So **M1-3D reduces to (S2)**: the newly generated irrelevant terms of one
CMP 102 RG step depend Lipschitz-continuously on the input irrelevant data,
with constant O(g_k²) in Balaban's norms. Together with CMP 102's own
"very sketchy" proof, this is the remaining gap for the 3D continuum limit
of terminal observables. That would be a new theorem: the 3D Yang-Mills
measure on a torus, at the level of fixed-scale block observables.

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
- `research/11-transverse-bias-reduction.md` -- the corrected terminal-chart
  bias lemma, the failure of the earlier fine-field first-moment criterion,
  and the open placement-summed terminal-sensitivity, tail, and mean-shift
  estimates.
- `research/12-covariant-terminal-sensitivity.md` -- proved abstract
  conserved-current and iteration lemmas, a convex-log rough one-step estimate
  covering CMP **109**, Eq. (0.4), and the distinction between a strong uniform
  contraction and the actual placement-summed H6\(_\Sigma\) target; the
  nonlinear Eq. (0.12) remains conditional on its small-diameter domain and a
  Lipschitz estimate for the group mean.
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
