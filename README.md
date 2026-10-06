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

## Where the 4D programme stands (lead summary, updated 2026-10-03)

Each item below is proved here, or reduced here to a precisely stated open
estimate. The research notes give the details.

- **Exact structure (proved):**
  - terminal sources pass exactly through T (notes 04, 14);
  - the zero-free source disc and cumulant control (03, 07);
  - in 3D, nondegeneracy (17) and the conditional depth comparison (18).
- **Master reduction (note 27):** M1-4D convergence <= (H0) coupling flow
  with shooting + (T) terminal memory decay + (B) a summable R-bias series
  with memory decay.
- **(H0), coupling flow (notes 22, 41):** reduced to:
  - (C) geometric convergence of the free one-loop increments. This follows
    from convergence of Balaban's free step operators: proved for the
    averaging kernels and weights (41) and for the marginal quadratic form,
    rate O(log M/M) proved, about M^-2 measured (47). Assembled in 48:
    all quadratic and linear ingredients converge geometrically; the vertex
    Riemann sums are reduced by a general alias-sum lemma (58) to a
    bookkeeping form (V), checked for the leading gluon vertices;
  - (S) the one-loop sum rule. With (C) and Schur additivity, an O(1) edge
    bound for composites (sketched) forces beta_inf^0 = 2b_0 log L (note 50).
    No finite scheme constant is needed;
  - (D) memory decay.
- **(B), the R-bias:**
  - equal fiber mass for R' (20) and curved-background contraction (24),
    both proved;
  - H7 absorbed into the persistence bound (P) (25).
  - **(P)**, shortest route (39): (T1*), a per-label fiber-law comparison,
    holds: it reduces exactly to a boundary-layer bound, and that bound holds
    because R_k >= (log g_k^-2)^r with r >= 2 (CMP 119 p. 245). Plus (T2-R),
    Balaban's domain factors CMP 122 II (1.79)-(1.89) via a rooted
    Kotecky-Preiss lemma (49). Its KP hypothesis is checked against Balaban's
    activity bound CMP 122 II (1.97)-(1.99) (49 §6). Persistence costs a factor only once per
    domain lifetime K <= n_0 + R_k, so the rate is a_eff ~ p_0(gamma)^2/R(gamma).
    It diverges because 2p_0 > (d+1)r, which Balaban's own induction requires
    (49 §5). So (P) rests on published structure. An independent action-based route is in
    notes 34-38 ((PA), (D1), (D2), (SER), (UB-ms)).
  - **Generalized averaged H8** is a covariance (32). Its decay (H-dec)
    follows from local extensive tangent bounds (LS) plus large fields (LF)
    (33).
- **Single-step theorems (the remaining core).** Note 29 reduces all memory
  decay ((D), (T-b), (B-b) in 4D; H3D-1 in 3D) to (S1) transport
  contraction, (S2) O(g²) generation, and (S3) β-dependence. Note 40 checks
  the scheme in an exact Migdal-Kadanoff RG. Status:
  - **(S1)** is *not* a published input: CMP 109 p. 259 disclaims RG
    contraction. It fails in Balaban's plain sup norms (35). It holds in the
    energy norm. For the abelian linearization the transport part is
    **proved**: ||grad F_min|| <= C M^-1 ||F_min||, with C <= 60 (about 4
    sharp), so first differences of images gain L^-1 per step (44).
    Dimension-6 data gain L^-3/2 (proved, note 44 Thm 3). Non-abelian
    transfer on the small-field event (45): the same rates up to C_1(L) eps_0,
    given (NA), a Cauchy-plus-Schur consequence of CMP 99 Thm 3.4. (Note 54:
    on the torus (NA) must be taken relative to the nearest flat background,
    (NA♭); at flat backgrounds the transport constant is exactly abelian.)
  - **(S2)** follows for a whole step from (A_s), Balaban's single-step
    bounds for complex fluctuation coupling, by an exact even deformation
    and a Schwarz lemma (42). In 3D, (A_s) reduces to CMP 102's
    sixth-order remainder bound.
  - **(S3)** has the order structure confirmed in the MK model (40).
  - **Glue (51):** Balaban's sup-norm activities have quadratic parts bounded
    in the form norm by C E_0, with higher orders O(eps_0) smaller. So
    (S1)-(S3) hold together in a mixed norm, given (A_s), (NA) and Balaban's
    fifth-order expansion.
- **Numerics (note 56):** in 4D SU(2), matching the terminal averaged plaquette at
  depths N = 1, 2 also fixes the terminal 1x2 loop: the difference is 0.000(2),
  against 0.015 between N = 0 and 1. The beta step falls toward the one-loop 0.2575
  (0.36 -> 0.30). This is evidence for (H0)/M1-4D, not a proof.
- **Nondegeneracy (P6-4D)** <= (V^R) + (B-small) (28). Three of the four
  source checks for (V^R) are now cited.

## Shortest remaining route: three dimensions

Status as of 2026-10-06, for SU(2) on a fixed 3D torus. M1-3D asks for
convergence and nondegeneracy of fixed terminal block observables as the
cutoff is removed.

**Proved here**

- Nondegeneracy P6-3D, from CMP 102 (note 17).
- The depth-comparison theorems: H3D-0 + H3D-1 => P4-3D => M1-3D convergence
  (note 18 Theorem 1).
- H3D-0, at every fixed depth (note 53). One step of Balaban's average has a
  push-forward density bounded above and below. The proof:
  - each coarse bond has a private link;
  - the conditional Jacobian is >= c_L > 0, by operator concavity of the
    SU(2) log-Hessian;
  - the map is injective a.e., by a degree count.

  This also holds for the symmetric 4D average CMP 109 (0.4).
- Energy-norm transport (single-step (S1), transport part):
  - abelian linearization (note 44);
  - every flat SU(2) background, including nontrivial holonomy (note 54);
  - with the quantitative near-flat lemma (note 57, Codex).
- H3D-1' at the linearized level, σ >= 2 (note 52).
- The interacting assembly, as a conditional theorem (note 61). In
  physical-coupling units, a bootstrap for two flows gives H3D-1 with rate
  (N + 1) max(θ', 1/L)^N from:
  - (H1) transport;
  - (H2) generation;
  - (H3) 3D marginal structure;
  - (H4) large fields;
  - (H5) terminal conversion.

  (H3) follows from (A_s) (Prop. 2), and (H5) is proved (Prop. 3).

**Remaining inputs, all readings of Balaban's papers**

So

    M1-3D <= (NA♭) + (A_s) + (H4):

- (NA♭): CMP 99 Theorem 3.4 around a flat background (Cauchy plus Schur;
  note 54). Read in T64: supported, provided n_0 > O(1)M (Balaban's
  localization cubes must not wrap the torus) and d n_0 sqrt(eps_0) <= alpha_1/2.
  Caveat: the decay bound CMP 102b (190) for the minimizer derivative, used in
  the Schur step, is stated by Balaban without proof ("we do not perform these
  calculations here").
  Note 63 avoids this: an energy-norm perturbation lemma for constrained
  minimizers (proved) gives (NA♭) from flat coercivity, CMP 102b's sup bounds
  and a small multiplier term.
- (A_s): CMP 102's single-step bounds for complex fluctuation coupling,
  reduced to its sixth-order remainder bound (note 42). Read in T63: no use of
  reality or positivity of g_0; the domain is |s| g_0 p(g_0)^2 <= alpha'.
- (H4): CMP 119's exact convergent expansions at d = 3 (read in T62, partially: supported). There the
  large-field factors are arbitrary powers of ε, and no R-operation is
  needed, by Balaban's own statement in the CMP 119 introduction. Add note
  49's rooted KP lemma (note 61 §6). Codex task T62.

None of the three is a new estimate, and all three have now been read against
the sources: (NA♭) and (A_s) are supported with stated conditions, and (H4) is
supported at the level of CMP 119's inductive assumptions. The remaining
uncertainty is in the parts of the sources not checked line by line: CMP 119
Sect. 3 and CMP 122 at d = 3, CMP 102b (182)-(190), and the cited
sub-papers. M1-3D therefore stays a conditional reduction, not a theorem.

**Numerical evidence**

- Terminal Balaban-averaged observables converge geometrically in the
  depth (note 55). The fitted form X_∞ + aL^{-N} + bL^{-2N} is what note 61
  predicts.
- The rate does not depend on L or on the terminal volume.
- Two bare actions that differ by an irrelevant term give converging
  terminal observables (note 59).
- In 4D, matching the terminal plaquette across depths fixes the terminal
  1×2 loop (note 56).
- In 4D, the Wilson/Symanzik gap at matched terminal P is -0.0075(18) at N = 1
  and -0.0057(19) at N = 2. Decay is not established at these depths (note 62).

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
- `research/13-averaged-bias.md` -- Averaged \(R\)-bias as a connected correlation
- `research/14-three-dimensional-m1.md` -- Three dimensions: exact \(T\)-transport and the absence of \(R\)-bias
- `research/15-h6-symmetric-average.md` -- The symmetric CMP 109 average: rough and trivial-background H6 bounds
- `research/16-normalized-tail.md` -- Normalization, bad-event tails, and H7\(_\Sigma\)
- `research/17-three-dimensional-nondegeneracy.md` -- Three-dimensional M1 reduction and terminal nondegeneracy
- `research/18-three-dimensional-depth-comparison.md` -- The three-dimensional adjacent-depth comparison (P4-3D)
- `research/19-gaussian-power-counting.md` -- Four-dimensional Gaussian power counting for a rooted even defect
- `research/20-equal-mass-per-label.md` -- Equal mass per label: the \(R'\)-proof and the complete-\(R\) stopping point
- `research/21-beta-derivative-4d.md` -- The β-derivative bound H4D-3 in four dimensions
- `research/22-coupling-flow-free-field-reduction.md` -- Reducing the coupling-flow theorem H0 to a free-field statement
- `research/23-one-loop-window.md` -- One-loop window sums: exact scalar calibration and the SU(2) stopping point
- `research/24-curved-contraction.md` -- Curved-background contraction for the CMP 109 average: note 12's (3.3) proved
- `research/25-h7-absorbed.md` -- H7 absorbed: rough-then-contract and large-field persistence
- `research/26-persistence-bound.md` -- The persistence bound (P): source reading and the exact missing step
- `research/27-4d-master-reduction.md` -- Corrected 4D master reduction: comparison at fixed terminal coupling
- `research/28-4d-nondegeneracy-reduction.md` -- P6-4D: nondegeneracy from superpolynomial large-field suppression
- `research/29-contraction-from-single-step.md` -- Memory decay from single-step Lipschitz bounds
- `research/30-su2-2d-sup-check.md` -- Exact 2D SU(2) check of the sup-oscillation depth comparison
- `research/31-s2-model-lemma.md` -- (S2) at the level of one fluctuation integral: the O(g²) mechanism, proved
- `research/32-h8-by-integration-by-parts.md` -- Generalized averaged H8 as a decorrelation estimate (integration by parts)
- `research/33-hdec-from-local-tangent-bounds.md` -- Rooted decorrelation (H-dec) from local single-step tangent bounds
- `research/34-nonabelian-persistence-action.md` -- Non-abelian (PA) on the ε_0-small event, from fiber convexity and minimizer regularity
- `research/35-minimizer-regularity-abelian.md` -- Minimizer regularity (D2) in the abelian 4D theory: exact sup-norm constants
- `research/36-d1-d2-from-balaban-variational.md` -- (D1) and (D2) of note 34 from Balaban's variational theory (CMP 102b, CMP 99)
- `research/37-pa-large-levels.md` -- (PA) on all events: large levels cost a fixed action each
- `research/38-ub-entropy-obstruction.md` -- (UB): what CMP 122 II gives, a lemma, and why a single-scale (UB) cannot give (P)
- `research/39-persistence-via-true-measure.md` -- (P) from a marked large-field bound for the true measure
- `research/40-mk-single-step-check.md` -- Note 29's single-step hypotheses in the 4D SU(2) Migdal-Kadanoff RG
- `research/41-free-increments-convergence.md` -- (C) of note 22: geometric convergence of the free increments from operator convergence
- `research/42-s2-by-even-deformation.md` -- (S2) for a whole RG step by an even complex deformation of the fluctuation coupling
- `research/43-energy-norm-transport.md` -- Transport in the energy norm: the gain sup norms miss
- `research/44-abelian-energy-s1-theorem.md` -- (S1) for first differences, abelian, energy norm: a theorem
- `research/45-nonabelian-energy-s1-transfer.md` -- Non-abelian transfer of note 44 (energy-norm transport) from Balaban's bounds
- `research/46-quadratic-form-norm.md` -- The norm in which (S1) holds: quadratic forms relative to the marginal energy
- `research/52-h3d1-linearized.md` -- H3D-1' at the linearized level, from note 44
- `research/53-average-pushforward-density.md` -- H3D-0(b): the push-forward density of Balaban's average is bounded above and below
- `research/54-flat-backgrounds-and-na.md` -- (NA) on the torus: flat backgrounds with holonomy, a counterexample and the corrected statement
- `research/55-mc-terminal-convergence.md` -- Monte Carlo test of M1-3D: terminal block observables converge across depths
- `research/56-mc-4d-universality.md` -- Monte Carlo test in 4D: universality of Balaban-averaged terminal observables
- `research/57-near-flat-quantitative.md` -- (Codex, T52) quantitative near-flat lemma: dist(U, Flat) <= d n sqrt(eps), sharp exponent
- `research/58-vertex-alias-sums.md` -- Vertex Riemann sums for (C): a general alias-sum convergence lemma
- `research/59-mc-action-universality.md` -- Monte Carlo: the terminal observables forget an irrelevant term in the bare action (3D)
- `research/61-3d-assembly-conditional.md` -- The 3D assembly: H3D-1 from single-step bounds, written out (conditional)
- `research/63-na-energy-perturbation.md` -- (NA♭) in the energy norm without CMP 102b (190): a constrained-minimizer perturbation lemma
- `research/62-mc-4d-action-memory.md` -- Monte Carlo, 4D: Wilson vs Symanzik at matched terminal P (inconclusive at N <= 2)
- `research/60-literature-check-2026-10.md` -- Literature check, October 2026: M1-3D/M1-4D still open in print
- `research/51-mixed-norm-compatibility.md` -- Mixed-norm compatibility: Balaban's sup-norm activities in the form norm
- `research/50-sum-rule-from-multiplicativity.md` -- (S) of note 22: only bounded edges are needed
- `research/49-t2r-rooted-lemma.md` -- (T2-R) from Balaban's domain factors: a rooted polymer lemma and a correction
- `research/48-free-increments-assembly.md` -- (C) of note 22 assembled: free increments converge geometrically
- `research/47-marginal-form-convergence.md` -- Depth convergence of the marginal form: the block-flux covariance converges geometrically
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
