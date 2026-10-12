# Task board archive (history only)

Archived by the lead on 2026-10-09. This is the task board as it stood then,
kept verbatim for history. Open tasks were copied to `TASKS.md`, which is the
only live board: take no tasks from this file.

# Task board

Owner: the lead (Claude, session "Yang Mills research loop setup", appointed by Daniel on 2026-10-07). The rules are in `AGENTS.md`. Take the
lowest-numbered unclaimed task assigned to you.

## Infrastructure

### T0b [infra] — completed by Codex, 2026-09-29: record the lead handoff
Scope: `AGENTS.md`, `TASKS.md`, `PROGRESS.md`.
Daniel transferred repository leadership from Claude to Codex after Claude
exhausted the available usage. The unfinished lead tasks below are reassigned
without changing their mathematical scope.

## Assigned to Codex

### T1 [fix] — completed by Codex, 2026-09-29: apply the five open corrections from the last review
Scope: `research/11-transverse-bias-reduction.md`,
`research/12-covariant-terminal-sensitivity.md`, `research/02-proof-obligations.md`,
`README.md`, `manuscript/main.tex`.
The source is `collaboration/claude-h6-placement-review.md`. You had read it
at 00:17 on 2026-09-28 when your usage limit stopped you. Apply these
without asking for another review:
1. Restate Lemma 3 of note 12 as Lemma 3' (convex combination of spectral
   logarithms, central transporter on the right). It then covers CMP 98
   (42) and CMP 109 (0.4). State that CMP 109 (0.12) is covered only on the
   small-diameter domain of M.
2. In Lemma 4 of note 12, replace Q_1 with Q_m in (5.3) and (5.4). State
   the Hilbert-Schmidt/operator-norm factor sqrt(2), and require the path
   hypotheses at every t in [0,1].
3. In note 11 (3.9), use 1/Z-normalized absolute fiber masses. Use the
   total-variation form of Lemma 1 for signed terms. Replace components
   sequentially within a scale.
4. Make the shape-sum hypothesis in (3.11) explicitly a second moment,
   sum_s A_s pi_s (s+L^d)^2 <= C eps_m.
5. Add the outside-curvature term C Delta_Lambda beta_Lambda to the first
   line of (6.3) in note 11. Replace the note 11 sentence claiming that note
   12 "reduces H6_Sigma to a strong uniform contraction route".

Done when: all five are in, the manuscript builds, there is one commit
`[T1][fix] ...`, and one line is added to `PROGRESS.md`.

### T2 [proof] — completed by Codex, 2026-09-29: rough first step and trivial-background H6 for the averages the 4D proof actually uses
Scope: a new note, `research/15-h6-symmetric-average.md`.
Balaban's 4D block map uses CMP 109 Eq. (0.4) (symmetric contour average),
not CMP 98 (42). Prove, with explicit constants:
- (a) the rough one-step bound (Lemma 3') for (0.4), with n_c(S) replaced
  by the total contour weight meeting S;
- (b) the divergence-free current lemma (note 10, Lemma 2) for the
  linearization of (0.4), including the sup and l^1 bounds and the
  l^2 bound ||P tau||_2^2 <= L^{2-d} ||tau||_2^2 at the trivial background;
- (c) the first-layer path bound (5.3) for (0.4) at the trivial exterior.

Read the scan text for (0.4) in `sources/tmp-audit-snapshot-2026-09-28/cmp109.md`.
If the OCR is garbled, say which symbols you reconstructed.
Done when: (a)-(c) are proved, or each is replaced by a `failed-attempt`
naming the exact obstruction, and there is one commit.

## Active research (Codex: finish these before taking new work)

Lead note for T4, 2026-09-29: Balaban's 3D construction has **no R
operation at all**. CMP 102, printed p. 256, defines the densities by
Eq. (2), \(\rho_{k+1}=T\rho_k\). The bounds (5) of Theorem 1 are stated for
exactly these densities. OCR: `sources/tmp-audit-snapshot-2026-09-28/cmp102uv3.md`,
around line 40; clean scan: `sources/papers/Balaban1985-CMP102-UV-stability-3D.pdf`.
So in 3D the terminal source passes through every step exactly, and there is
no R-bias to bound. Please make this the main finding of note 14. Keep the
crude R-bias count only as a remark ("even an R-type replacement would be
harmless in 3D"). Do not widen T4 beyond this.


- T3 [proof/counterexample] — completed by Codex, 2026-09-29: H8 in averaged form. The pointwise
  (fixed-exterior) H8_Sigma is probably false. The averaged bias is a
  covariance, and gauge invariance plus power counting suggest it gains
  exactly the missing factor L^{-m}. Target note:
  `research/13-averaged-bias.md`.
- T4 [computation] — completed by Codex, 2026-09-29: M1 in three dimensions. Check whether Balaban's 3D
  large-field suppression makes the R-bias sum converge with crude bounds.
  CMP 122 I, p. 176 says that for d < 4 the bound is an arbitrarily large
  power of epsilon. Target note: `research/14-three-dimensional-m1.md`.
- T5 [proof/counterexample] — completed by Codex, 2026-09-29:
  determine exactly when Balaban's unnormalized large-field/component bounds
  imply the normalized bad-event probabilities required by H7_Sigma. Prove a
  sharp normalization lemma and either match its hypotheses to the published
  construction or give a finite-dimensional counterexample isolating the
  missing lower bound. Target note: `research/16-normalized-tail.md`.

## Assigned to Codex (new, 2026-09-30)

### T6 [proof] — completed by Codex, 2026-10-01: M1 in 3D and nondegeneracy (P6-3D)
Scope: a new note, `research/17-three-dimensional-nondegeneracy.md`, plus
one row each in `research/02-proof-obligations.md` and `README.md`.
Use CMP 102 Theorem 1: the bounds (5) for the exact densities
\(\rho_{k+1}=T\rho_k\). Label it a published input whose proof the paper
calls "very sketchy". Prove:
- (a) a precise statement of M1-3D for SU(2): Balaban normalization
  g_0^2 = g^2 eps, terminal spacing eps_0 (or a fixed coarser l reached by
  further exact T steps), closed coarse loops. List which ledger items
  vanish in 3D and why (no R, so Robs/H6-H8 vanish; superrenormalizable,
  so H0 vanishes), and which remain (P4, P6).
- (b) the normalized terminal law nu_n on the fixed terminal lattice has
  a Haar density <= C everywhere and >= c > 0 on the terminal small-field
  set S, uniformly in n. Handle the minimal configuration U_K(U), the bound
  on A(U_K(U)) on S, and normalization.
- (c) inf_n Var_{nu_n}(F) > 0 for every continuous F that is nonconstant on
  S. Every subsequential limit is nondegenerate, and any two limits are
  mutually absolutely continuous on S-type sets.
- (d) if you use a coarser scale l, check that the bounds survive the
  extra exact pushforward.

Name any extra property of U_K you need as a hypothesis. Done when:
(a)-(d) are proved or replaced by a precise `failed-attempt`, with one
commit and one PROGRESS line.

## Assigned to Codex (new, 2026-10-02)

### T10 [fix] — completed by Codex, 2026-10-02: apply the T9 review edits
Scope: `research/11-transverse-bias-reduction.md`, `research/13-averaged-bias.md`,
`research/14-three-dimensional-m1.md`, `research/16-normalized-tail.md`,
`research/17-three-dimensional-nondegeneracy.md`, plus `README.md` and
`research/02-proof-obligations.md` if a status changes.
Apply items 1-8 of "Required edits" in `collaboration/lead-review-T1-T6.md`
without asking for another review. For item 7/F2, check CMP 102 Eq. (3),
printed p. 256, on the local page image of
`sources/papers/Balaban1985-CMP102-UV-stability-3D.pdf`. If its lower side is
the action-free bound, rest Prop. 2 of note 17 on it. Otherwise, say what it
actually reads. Do not change any proposition beyond what the review asks.
Done when: all items are in, there is one `[T10][fix]` commit, and one
PROGRESS line.

### T11 [proof] — completed by Codex, 2026-10-02: equal fiber mass per label in the actual 4D R-operation
Scope: a new note, `research/20-equal-mass-per-label.md`.
Notes 13 and 16 need P_λ(Ω) = R_λ(Ω) for **each** history label λ. CMP 122 I
p. 176 (0.3)-(0.4) gives this for the introductory R. On p. 177, Balaban says
the actual procedure uses denominators equal to "integrals of some parts of
these densities". Read CMP 122 I section 1 (from the page images; pp. 193-194
show that the integrating operation preserves each term's integral) and
determine one of the following:
- (a) a proof that the actual localized renormalization preserves each
  label's fiber mass;
- (b) an explicit finite example of the actual rule (partial denominators)
  where a label's mass changes, with a bound on the ratio P_λ/P'_λ if one
  follows from the published construction;
- (c) a failed-attempt naming the exact missing formula.
Done when: one of (a)-(c) is committed as `[T11][...]` with one PROGRESS line.

### T8 [computation/proof] — completed by Codex, 2026-10-02: Gaussian abelian 4D power counting (reassigned from the lead, 2026-10-02)
Scope: a new note, `research/19-gaussian-power-counting.md`, plus scripts in
`research/scripts/t8_*.py`. Take it after T10 and T11.
Model: 4D noncompact U(1), fine torus (Z/n)^4, n = n0*L^N, action
(beta/2)|dA|^2 with beta = 1/g^2 (dimensionless in 4D), and Balaban's linear block average Q
(research/10 (7.1)-(7.2)). The lead's 3D version is the template: the
aliasing formula and the brute-force checks in `research/scripts/t7_*.py`
(coming with T7). Compute exactly:
- (a) the covariance of a terminal plaquette flux, or a small terminal loop, with a
  local even gauge-invariant defect inserted at depth m below the terminal
  scale, once the exact block propagation is included. Show whether it decays like
  L^{-4m} (or say which power appears);
- (b) the same defect's effect at a fixed exterior field (the "fixed-exterior
  shift" of research/13), showing that it does not decay;
- (c) brute-force real-space checks on small tori against the Fourier formula,
  to machine precision. Use an eigendecomposition, not `pinv`; `pinv`'s default
  tolerance gave 1e-5 errors in 3D.
State the exact formula, the table, and the fitted exponent. Prove the exponent
if you can; otherwise label it a computation.
Done when: committed as `[T8][computation]` with one PROGRESS line.

### T13 [computation] — completed by Codex, 2026-10-02: exact sigma-model window calibration; SU(2) vertex computation stopped
Scope: a new note, `research/23-one-loop-window.md`, plus scripts
`research/scripts/t13_*.py`. Take it after T11 and T8.
Context: research/22 reduces Balaban's coupling-flow theorem H0 to (D) and
(U): the free (g=0) one-loop coupling shift over n block steps is
2 b_0 n log L + O(1), with bounded edges. Compute, by exact lattice momentum
sums (no Monte Carlo), the transverse p^2 coefficient of the one-loop vacuum
polarization of SU(2) gauge fluctuations, with the background-field method
(gluon and ghost loops), in a simplified block scheme: the fluctuation field
is constrained to have zero linear block average at the coarse end (the T7
kernel `research/scripts/t7_*.py` is Balaban's linear average), with any fixed
lattice gauge. Report beta^0_[i,i+n] for n = 1..6 and L = 2, 3. Check the
slope 2 b_0 log L, with b_0 = 11*2/(48 pi^2), and the boundedness of the edge
constant. If the full scheme is too large, do the scalar-field analogue
first (O(N) sigma model in d=2, coefficient (N-2)/(2 pi)) as a calibration,
and state exactly how far you got.
Done when: committed as `[T13][computation]` (or `[failed-attempt]`) with one
PROGRESS line.

### T17 [proof/failed-attempt]: marked large-field persistence bound (P) — reassigned to Claude (lead), 2026-10-02 (Codex out of credits, per Daniel)
Scope: a new note, `research/26-persistence-bound.md`. Take it after T13.
Context: research/25 reduces H7 and the quadratic R-bias terms to the bound
(P), (4.1) there. Let M_{m,t} be the unnormalized mass, per terminal block,
of R'-labels at depth m whose true-configuration image stays large-field
for t further levels. Then (P) is M_{m,t} <= C w_m L^{4m} e^{-a t} with
L^4 e^{-a} < 1. Using CMP 122 I-II (large-field factors exp(-c p(g_k)^2) per
region and scale, the history expansion) and CMP 119 (localization), prove
(P) from the published bounds, or state exactly which "marked" version of
those bounds is missing. Use page images where the OCR is garbled.
Done when: committed as `[T17][proof]` or `[T17][failed-attempt]` with one
PROGRESS line.

### T19 [computation/failed-attempt]: SU(2) one-loop window (finish T13's stopping point) — reassigned to Claude (lead), 2026-10-02
Scope: extend `research/23-one-loop-window.md` (a new section) and
`research/scripts/t19_*.py`. Take it after T17.
Implement the background derivatives of the lattice Wilson Hessian, the ghost
operator and the block constraint that T13 lists as missing (2.2)-(2.4), at
trivial background and second order in a slowly varying background. Compute
the transverse p^2 coefficient of the constrained one-loop window for SU(2),
L = 3, n = 1..3 or as far as feasible. Use symmetry and the alias structure
to reduce the 729^4 sum (for example momentum-shell sampling with error bars,
or a smaller L). Target: increments approaching 2 b_0 log L, with b_0 =
11*2/(48 pi^2), and a converging edge. These would be the (C)+(S) evidence
for note 22 Prop D in the actual gauge theory.
Done when: committed as `[T19][computation]` or `[T19][failed-attempt]` with
one PROGRESS line.

## Assigned to Codex (new, 2026-10-06)

Codex is back online. Take these in order (lowest number first), one at a time,
under the rules of `AGENTS.md`. Each one is self-contained.

### T52 [proof] — completed by Codex, 2026-10-06: quantitative near-flat lemma (note 54, Lemma 3)
Reviewed by the lead, 2026-10-06: correct. I checked the commutator identity (3.5), both commuting candidates of Lemma 3
(min <= sqrt(delta)), the swap counts of Lemma 2, the seam-bond bound (d-1)rho^2 + rho <= d rho, and the sharpness example.
Scope: a new note, `research/57-near-flat-quantitative.md`. Also note 54, but
only to add a one-line pointer.
Note 54 Lemma 3 shows by compactness that an SU(2) lattice configuration on
the torus (Z/n)^d with max_p |U(dp) - 1| <= ε is within ω(ε) -> 0 of a flat
configuration, after a gauge transformation. No rate is given.
Prove an explicit bound ω(ε) <= C(d) n^a ε^b, with stated a and b; b = 1/2 is
expected. The route is a complete axial (maximal-tree) gauge, which makes
the non-tree links products of plaquettes, followed by a lemma that almost
commuting SU(2) elements are close to commuting ones. That lemma must have
an explicit constant, and note 54 §3's example (commutator of order α²,
distance of order α) shows that b = 1/2 is sharp.
Done when: the bound is proved with all constants explicit, or there is a
`failed-attempt` naming the exact step that fails. Commit `[T52][proof]`
plus one PROGRESS line.

### T53 [computation] — reassigned from Codex to a subagent, 2026-10-08: sup-norm constant s_L in twisted sectors (note 36 caveat)
Scope: `research/scripts/t27_minimizer_regularity.py` (add a twist option),
its output, and a short section in `research/35-minimizer-regularity-abelian.md`.
Note 36 (holonomy caveat) claims that the exact-flux sup-norm constant s_L of
note 35 is unchanged, up to O(e^{-δ n_0}), in the twisted Bloch sectors
created by a flat background with holonomy (note 54 §1). Test this. Add a
quasi-periodic twist e^{iθ} to the fine Fourier grid, so that coarse momenta
become K ∈ (2π/n_0)(Z^4 + θ/(2π)). Rerun the LP of note 35 for L = 2, 3, 4,
m = 1, at θ = π/4 and π/2. Report s_L(θ) next to s_L(0).
Done when: the table is in note 35 and states whether the claim of note 36
holds. Commit `[T53][computation]` plus one PROGRESS line.

### T54 [computation] — reassigned from Codex to the lead, 2026-10-08 (runs in progress): 4D universality test, third depth and a third observable (note 56)
Scope: `research/scripts/t51_mc_universality_4d.py` (add a 2x2 loop
observable if needed), new output files, and a new section in
`research/56-mc-4d-universality.md`.
Note 56 matched the terminal plaquette at depths N = 1, 2 (8^4, 16^4). There
the terminal 1x2 loop agreed (difference 0.000(2)), and the beta step was
0.30 against the one-loop 0.2575.
1. Add the terminal 2x2 loop and repeat the N = 1, 2 matching for it.
2. Run N = 3 (32^4) at 3 beta values bracketing the matching point P = 0.64.
   Extrapolating the beta step suggests beta_3 is about 3.37-3.40. Use
   `t51_matching.py` (extend DATA).
3. Report the beta steps beta_3 - beta_2 and the W12 differences.

Expect about 4-5 h per beta at 32^4 in numpy, single core: the 16^4 points took about 1000 s, and 32^4 is 16 times larger. Run the three
beta values in parallel. Use 150 thermalization updates
and at least 200 measurements, as in note 56.
Optional extension (note 62): also run the tree-level Symanzik action at N = 3 with `t58_mc_action_universality.py`
(masked staples, about 11 h per beta at 32^4), to decide the 4D memory test.
Done when: the N = 3 matching row and the 2x2 comparison are in note 56.
Commit `[T54][computation]` plus one PROGRESS line.
Lead, 2026-10-08: the three N = 3 runs (32^4, betas 3.30, 3.40, 3.50, seeds
54330, 54340, 54350) were started at 23:16 UTC in the cloud container
(about 5.6 h each, one core each; output `research/scripts/t54_n3_beta*.out`).
The 2x2 loop and the write-up follow when they finish.
Update: container restarts kill background processes, so the runs now use
the checkpointed driver `t54_mc_checkpointed.py` (adds the 2x2 loop) and the
N = 0, 1, 2 points are re-run with it for W22 (`t54_chain.sh`). **On every lead
wake, run `sh research/scripts/t54_supervise.sh`**; it resumes any killed run
from its checkpoint and reports which are done.

### T55 [fix] — claimed by Codex, 2026-10-07 (no deliverable; Codex out of usage); reassigned to a subagent, 2026-10-08: (A_s) source check of CMP 109 §§3-5 (note 42 §4)
Scope: `research/42-s2-by-even-deformation.md` §4 only.
Note 42 §4 (T49) checked CMP 116 Part II §1 and CMP 109 §2. Read CMP 109
§§3-5 (`sources/ocr/cmp109.md`, fluctuation-field action, Ward identities,
beta-function extraction). List every place where the coupling g_k enters an
estimate, and say for each whether the estimate uses only |g_k| p(g_k) (or
|g_k| |B|) or something more: the sign, reality or positivity of g_k, or of
g_k^{-2} A. Under the deformation g_k -> s g_k with |s g_k| p(g_k) <= α', the
generated marginal coefficient becomes complex. Say whether any step of §§3-5
uses that coefficient being real.
Done when: note 42 §4 has the list, with page and equation numbers, and a
one-line verdict: "no use of reality found", or the exact place where it is
used. Commit `[T55][fix]` plus one PROGRESS line.

## Assigned to Codex (new, 2026-10-06, second batch): close the 3D chain

**Priority order for Codex: T55, then T53, T54.** (T62-T64 were done by Claude on 2026-10-06.) This
overrides the lowest-number rule for these tasks. Note 61 reduces M1-3D to
three readings of Balaban's papers, which are below.

### T62 [fix]: (H4) — CMP 119 Sect. 2 at d = 3 (note 61 §6) — completed by Claude (partial reading), 2026-10-06; see note 61 §6a
Scope: `research/61-3d-assembly-conditional.md` §6 only.
CMP 119's introduction (printed pp. 244-245) says that for d < 4 the
large-field factors are arbitrary powers of ε and control the large-field
regions "for all steps", so no R-operation is needed. Read CMP 119 Sect. 2
(`sources/ocr/cmp119.md`), the inductive description of the effective
densities. For each inductive assumption, say whether it holds verbatim at
d = 3 with R = identity, or what changes: powers of L^j, ε-exponents,
entropy factors. Then state precisely the large-field activity bound that
results. It should have the form |activity(X)| <= C ε_j^q e^{-κ d(X)},
with q arbitrary.
Done when: §6 has the list, with page and equation numbers, and a one-line
verdict ((H4) supported, or the exact obstruction). Commit `[T62][fix]` plus
one PROGRESS line.

### T63 [fix]: (A_s) for CMP 102 — the complex-coupling remainder bound (note 42 §4) — completed by Claude, 2026-10-06; see note 42 §4 reading report
Scope: `research/42-s2-by-even-deformation.md` §4 ("Sharper source fact for
3D") only.
Read CMP 102 pp. 261-264 (`sources/ocr/cmp102uv3.md`). Check that the
sixth-order expansion of v(g_0A) - g_0^{-2}V(g_0A), its remainder
O(g_0^7 p^{18}), the cumulant expansion to sixth order, and the
random-walk localization bounds (23)-(25) hold verbatim when g_0 is
replaced by a complex s g_0 with |s g_0| p(g_0)^{18/7} <= α'. That is, check
that no step uses reality or positivity of g_0. List each estimate with its
equation number and the property it uses.
Done when: a list and a one-line verdict are in note 42 §4. Commit
`[T63][fix]` plus one PROGRESS line.

### T64 [fix]: (NA♭) — CMP 99 Theorem 3.4 around a flat background (note 54 §4) — completed by Claude, 2026-10-06; see note 54 §4 reading report
Scope: `research/54-flat-backgrounds-and-na.md` §4 only.
(NA♭) claims analyticity of the background-field operators at
configurations U'U♭, with U♭ flat (possibly with nontrivial holonomy) and
U' small. Read CMP 99 Theorem 3.4 and its hypotheses, conditions (3.37) and
around (`sources/ocr/cmp99prop.md`, `cmp99regular.md`). Check that:
- (a) a flat background with arbitrary holonomy satisfies the regularity
  hypotheses;
- (b) the analyticity domain is a sup-norm ball of radius independent of
  the depth;
- (c) the derivative bounds come with the scale factor (L^k η)^{-1} per
  derivative, which is what the Schur step of note 45 needs.
Done when: the three checks, with equation numbers, and a verdict are in
note 54 §4. Commit `[T64][fix]` plus one PROGRESS line.

## Round 2026-10-07 (lead: "Yang Mills research loop setup")

Goal of the round: turn M1-3D from a conditional reduction into a theorem
whose only inputs are published statements read line by line, and close the
two sketched items of H0 ((E) and two-scale (O1)).

**2026-10-08: Codex is out of usage. Daniel gave the lead full control of the
repository, and every open Codex task is reassigned to subagents dispatched
by the lead** (Sonnet workers in worktrees, each deliverable checked by
independent adversarial verifiers and then by the lead). The Balaban PDFs are
now fetched in the cloud container (`sh sources/fetch_papers.sh`, not
committed; absolute path `/home/user/yang-mills/sources/papers/`), so the
page-image readings T71-T72 no longer need the Mac. CMP 99 "background
propagators" still fails to download; its OCR is in `sources/ocr/`.
The Sonnet workers on T73, T75, T78 and T79 stopped on 2026-10-07 at the
Sonnet session limit before committing; their partial scripts were salvaged
and the tasks are re-dispatched.

### T66 [proof] — failed-attempt by Sonnet, 2026-10-07; reviewed by the lead: correct (Gaussian table reproduced by `t66_gauss_disc.py`; one overstatement in §6b.4 item 3 softened): localized s-analyticity and (H4b) (note 61)
Scope: `research/61-3d-assembly-conditional.md`, a new §6b only.
The proof of note 61 Theorem 1 differentiates the two flows along
μ_s = e^{sD_N} μ_0 / Ξ(s) (note 18 §2). Note 18 Prop. 3 shows the global
zero-free strip in s has width π/osc D_N, which shrinks with the volume, so
Cauchy estimates in s cannot be taken globally. Prove that D_N (note 18 §8,
F2: the one-step defect) is a sum Σ_X d_X of local terms with Balaban-type
decay, so that every polymer activity of the s-deformed CMP 102 expansion is
analytic in a disc |s| <= s_0 with s_0 independent of N. Deduce, with
constants: (a) the input sizes δ_0 <= C_0, Δ_0 <= C_0 ε_N of (H5) for
complex |s| <= s_0; (b) the influence bound (H4b) for large-field activities.
If D_N is not local in this sense, write a `failed-attempt` naming the term.
Done when: §6b has the lemma with proof (or the failed attempt).

### T67 [proof] — failed-attempt by Sonnet, 2026-10-07; reviewed by the lead: correct after one wording fix: the edge bound (E) (note 50 Lemma 2)
Scope: `research/50-sum-rule-from-multiplicativity.md` §2 only.
Replace the sketch of Lemma 2, β_∞^0(L) = 2b_0 log L + O(1) uniformly in L,
by a proof. Write the propagator of the limit step as G_0 + (UV edge) +
(IR edge), with the IR edge the W^T C^{-1} W term (notes 47-48), and prove
the stated power-law bounds on both edges. Then show that the edge
contributions to the p² coefficient are O(1) uniformly in L, and that the
window contribution is 2b_0 log L + O(1). The vertex algebra may be quoted
from a standard background-field reference, stated in the form used. Also
prove the bound for the n-step composites uniformly in n, which is what
Prop. 3 assumes.
Done when: Lemma 2 is proved with an explicit O(1) dependence, or a
`failed-attempt` names the integral that is not uniformly bounded.

### T68 [proof] — completed by Sonnet, 2026-10-07; reviewed by the lead: correct, for the single-level alias model (lower penalty levels, general-α gauge fixing and the constrained ghost are open, as the note says): two-scale (O1) (note 41, item 3)
Scope: `research/41-free-increments-convergence.md`, a new section.
Note 41 states, without proof, that the Laplacian, gauge-fixing and ghost
operators on the fine lattice of step j converge at rate L^{-j} on the range
where G_j smooths. Work with the induced coarse-lattice kernels (no common
continuum space needed). Prove a two-scale (O1): a bound on the induced
kernel of G_j (K_j - K_∞) in the exponentially weighted norm of note 41,
with rate C L^{-j}, for the free abelian (Gaussian) step with Balaban's
linear average. Use the alias-sum lemmas of notes 47 and 58. Say whether the
argument extends verbatim to the gauge-fixing and ghost operators.
Done when: the bound is proved with explicit rate, or a `failed-attempt`.

### T69 [proof] — completed by Sonnet, 2026-10-07; reviewed by the lead: correct, conditional on the OCR readings R1-R4 and the §6.8 exclusions (unconstrained Schur terms, b^(2), wrap-around): structural form (V) for ghost and gauge-fixing vertices (note 58)
Scope: `research/58-vertex-alias-sums.md`, a new section.
Note 58 checks (V) for the leading gluon vertices (s = -3, -4) and lists
the ghost and gauge-fixing vertices as open (line ~195). Write those
vertices in Balaban's gauge-fixed background-field scheme (CMP 99, CMP 109;
`sources/ocr/`), expand them in the background to second order, and check
(V) with explicit growth exponents s < 1, so that Lemma A / A2 applies.
The covariant-average terms are out of scope.
Done when: (V) is verified for both families with stated s, or a
`failed-attempt` names the vertex whose growth exponent is >= 1.

### T73 [proof] — assigned to Sonnet (re-dispatched 2026-10-08 after the session-limit stop; partial scripts `t73_*.py` salvaged): (E) for the scalar loop in note 48's model (note 50 §2.5)
Scope: `research/50-sum-rule-from-multiplicativity.md`, a new §2.6, plus
`research/scripts/t73_*.py`.
T67 showed that (E) cannot be proved termwise from the fine-lattice G_0. Do
the scalar (orbital) case only. (1) Write the propagator of the free step in
note 48's model: the fluctuation B on the scale-k block lattice, entering
through the minimizer map H_k (child symbol, note 48 item 2), with
covariance from C^{(M)} (note 47); take the limit k -> ∞ at fixed block
ratio L. (2) Write the p² coefficient of the scalar bubble plus seagull with
it, by Lemma A2 (note 58), treating alias 0 jointly with its correction
(note 50 Prop. 2.2). (3) Bound the bulk, IR-shell and UV-shell
contributions uniformly in L, and show the bulk gives c log L + O(1) with the
scalar constant c identified. Check the result numerically for L = 2, 3, 4,
(6) if feasible.
Done when: the scalar (E) is proved with explicit O(1), or a `failed-attempt`
names the shell integral that is not uniformly bounded.

### T74 [proof] — failed-attempt by Sonnet, 2026-10-07; reviewed by the lead: correct (absolute bound Theorem 64.1 proved; the Z-local relative form (R) is open, see T77): the large-field lower bound (I-LF)(b) (note 61 §6b)
Scope: a new note, `research/64-large-field-lower-bound.md`, plus
`research/scripts/t74_*.py` if a constant is checked numerically.
T66 found that the s-analyticity of note 61 §6b needs, on each large-field
region Z of the coarse configuration V, a lower bound uniform in N:

    D_N(V) >= -C_- β_N A_Z(V) - e_ent |Z| log β_N   (locally on Z),

where D_N = log(Tρ^{(N+1)}/ρ^{(N)}) (note 18), 3D SU(2), Wilson action,
β_{N+1} = L β_N, and T is Balaban's average (CMP 98 (42)). CMP 102's lower
bound (47) covers only the small-field set. Prove the bound directly: build an
explicit fine extension U_ext(V) of V (for example by note 53's private-link
structure, spreading each coarse holonomy over the L² fine plaquettes), bound
β_{N+1} A(U_ext) by C β_N A(V) plus a per-block constant, and lower-bound the
Haar volume of a neighbourhood of U_ext in the fibre with note 53's Jacobian
bound c_L. State C_-, e_ent explicitly. Say whether the bound is local (each
term depends on V near Z only).
Done when: proved with explicit constants, or a `failed-attempt` naming the
step (e.g. the extension's action for large holonomies) that fails.

### T75 [proof] — assigned to Sonnet (re-dispatched 2026-10-08; partial script `t75_multilevel_green.py` salvaged): two-scale (O1) with all penalty levels (note 41 §5)
Scope: `research/41-free-increments-convergence.md`, a new §5a, plus
`research/scripts/t75_*.py`.
T68 proved the two-scale (O1) for K_M = Λ_M + a w w^† (top-level average
only). Balaban's free step operator at level j carries the penalties of all
levels i <= j (note 41 §1, CMP 99 recursion before (3.26), weights a_i), so
K = Λ + Σ_i a_i Q_i^† Q_i, a finite-rank-per-K perturbation at each level
but with rank growing with the number of levels. Extend Theorem 2: either by
iterating the Schur/Sherman-Morrison step level by level with bounds uniform
in the number of levels, or by showing that levels i < j - k_0 contribute
O(L^{-2(j-i)}) and can be absorbed. Keep the alias-sum convergence rate.
Check numerically (eigh) for L = 2, d = 2 and 4, j <= 4.
Done when: Theorem 2 holds for the full multi-level operator with explicit
rate, or a `failed-attempt` names the term that is not uniform in j.

### T76 [proof] — completed by Sonnet, 2026-10-07; reviewed by the lead: correct for the quadratic (Schur) sector, abelian skeleton; SU(2) flat-background version conditional on note 54 §2; R1-R5 of §6c.6 open: (I-S) along the real s-orbit by convexity (note 61 §6b)
Scope: `research/61-3d-assembly-conditional.md`, a new §6c, plus
`research/scripts/t76_*.py` if a constant is checked.
Note 61 §6b's Lemma 6b.1 assumes (I-S): the step maps are analytic and obey
Lemma G's difference inequalities on a neighbourhood of the real orbit
{E_j^{(s)} : s ∈ [0, 1]}. T66 noted that the one-step defect T1 is an O(1)
*relative* change of the quadratic form at high momentum, outside CMP 102's
class (41) and outside note 63's small-perturbation lemma. But the
interpolated density e^{sD_N}ρ_0 = ρ_0^{1-s}(Tρ_1)^s is a geometric mean of
two genuine Balaban densities, so its quadratic form is a convex combination
of two coercive forms. Prove that the s-interpolated data lie, uniformly in
s ∈ [0,1] and N, in the form-norm class of notes 46, 51 and 63 (coercivity,
mixed-norm bounds, flat-background transport (H1)), with constants no worse
than the max over the two endpoints. Then state exactly which part of (I-S)
remains (the higher-order analytic part along the orbit, which is the
published (A_s)/(H2) input). Check the coercivity claim on the abelian
Gaussian model (note 18 §8, `t7_gauss3d.py`).
Done when: proved with explicit constants, or a `failed-attempt` naming the
step where convexity does not suffice.

### T77 [proof] — failed-attempt by Sonnet, 2026-10-07; reviewed by the lead: correct (exact transport identity Thm 64.2 for last-axis bonds; (R) given (EQ); (EQ) and axes 1-2 open): the Z-local relative bound (R) (note 64 §6)
Scope: `research/64-large-field-lower-bound.md`, new §7, plus `research/scripts/t77_*.py`.
T74 proved the absolute lower bound (Theorem 64.1) but not the relative form
(R): D_N(V) - D_N(V^Z) >= -C_- β_N A_Z(V) - e_ent |Z| log β_N. It fails
because the 1/β-ball entropy is extensive and does not match the vacuum
constant c_N. Carry out note 64 §6: with a collar Z⁺ ⊃ Z, prove the matched
pair (lower bound on Tρ(V) with Gaussian-width balls, radius κβ^{-1/2},
outside Z⁺; upper bound on Tρ(V^Z) with the same per-bond factors outside
Z⁺), so that the extensive parts cancel with g_-/g_+ = e^{O(1)} per bond.
Use the fibre Hessian of A_{N+1} at the constrained minimizer (CMP 102b
Thm 1; note 63 Lemma 3 for flat coercivity; note 57 near-flat lemma). The
bonds outside Z⁺ may be restricted to the small-field set if that is what
the s-weights of note 61 Lemma 6b.2 actually need; say so explicitly.
Done when: (R) is proved with explicit constants (or for the restricted
case that Lemma 6b.2 needs), or a `failed-attempt` names the step.

### T78 [proof] — assigned to Sonnet (re-dispatched 2026-10-08; nothing salvaged): kernel locality of the interpolated forms (note 61 §6c.6, R2)
Scope: `research/61-3d-assembly-conditional.md`, new §6d, plus `research/scripts/t78_*.py`.
T76 proved S <= W_j <= Π_j^{(s)} <= W_{j+1} in the quadratic sector but noted
(R2) that a Loewner sandwich does not give locality: the real-space kernel of
Π_j^{(s)} (and of its minimizer map B_s(Φ), (6c.1)) must decay exponentially,
uniformly in s ∈ [0,1], j, N, for the polymer/mixed norm of note 51 to apply.
Prove this by a Combes-Thomas argument: conjugate the composite fibre problem
(6c.1) by e^{μ·x}, show the conjugated form stays coercive on the fibre for
|μ| <= μ_0 (with μ_0 independent of s, j, N, using S <= S + sΔ <= (1+ρ)S
and the finite range of w), and deduce |kernel(x,y)| <= C e^{-μ_0|x-y|} in
coarse units. Note whether the decay rate is in units of the level N-j lattice
(it must be, for the mixed norm). Check numerically on the abelian model
(`t76_convexity.py` setup) for L = 2, 3.
Done when: exponential decay is proved with explicit μ_0, C, or a
`failed-attempt` names the step (e.g. the constraint space under conjugation).

### T79 [proof] — assigned to Sonnet (re-dispatched 2026-10-08; partial script `t79_center_obstruction.py` salvaged): exact fibre transport for all three bond axes (note 64 §7.5)
Scope: `research/64-large-field-lower-bound.md`, new §8, plus `research/scripts/t79_*.py`.
T77 built a Haar-preserving map 𝒯_R on fine configurations with
q(𝒯_R U) = R·q(U) exactly for coarse bonds in the last axis of Balaban's
contour order (CMP 95 (1.7), CMP 98 (42)), giving the exact identity
Tρ(V)/Tρ(V^Z) = E_{fibre over V^Z}[e^{-β_{N+1}ΔA}] (Thm 64.2). For axes 1, 2
the contours Y_{c,x} sharing a crossing link have different in-block paths,
and the script shows q errors of order 1e-2. Find an exact transport for all
axes: e.g. act on the private link only (note 53 Lemma 1) after a fibre
change of variables, compose a gauge transformation inside the block with a
crossing-link rotation, or otherwise exploit Φ_{RY}(RX) = RΦ_Y(X). Prove
q∘𝒯 = R·q and Haar preservation (or compute the Jacobian), and extend Lemma
64.5's plaquette classification to the new map. Check q exactness to 1e-14
in the script for all three axes, L = 2, 3. If no exact map exists, give the
obstruction and the best approximate map with an explicit Jacobian bound.
Done when: Theorem 64.2 holds for all axes, or a `failed-attempt` with the
obstruction.

### T80 [proof] — assigned to Sonnet, 2026-10-08: the equipartition bound (EQ') for the fibre Gibbs measure (note 64 §7.4-7.5)
Scope: a new note `research/67-fibre-equipartition.md`, plus
`research/scripts/t80_*.py`. (T79 edits note 64 §8 in parallel; do not edit note 64.)
T77 reduced the Z-local bound (R), hence (I-LF)(b) of note 61 §6b, to (EQ'):
E_{μ_{V'}}[β_{N+1} A_q] <= C_A for every fine plaquette q near Z, uniformly in
N, in β_{N+1} >= β_*(L), and in the coarse configuration V' (μ_{V'} is the
Wilson Gibbs measure on the fibre q(U) = V' of Balaban's average). Its
log-convexity route (Lemma 64.6) stalls at a lower bound for the fibre
partition function with a rough outside. Try an integration-by-parts
(Ward-identity) route instead: parametrize the fibre by U_rest with the
private links b(U_rest) determined (note 53 Lemma 1, Theorems 2, 4), take a
left-invariant vector field on one free link ℓ, and integrate by parts against
the fibre density. For the Wilson action this gives
E[β² |∇_ℓ A|²] = E[β Δ_ℓ A] + (terms from ∇_ℓ b and ∇_ℓ log J), and
Δ_ℓ(1 - ½ tr U_p) is a bounded multiple of ½ tr U_p. Bound the extra terms by
note 53's Jacobian bounds and Lemma 64.2. Then pass from the gradient bound
(which controls sin² of the plaquette angle) to A_q itself, handling angles
near π separately (for example by a large-deviation bound at that plaquette).
Gauge zero modes (note 64 §7.5) must be handled: work with gauge-invariant
quantities only.
Done when: (EQ') is proved with explicit C_A, or a `failed-attempt` names the
step (and says whether the boundary terms or the near-π angles are the
obstruction).

### T71 [fix] — reassigned from Codex to a subagent, 2026-10-08: CMP 119 Sect. 3 at d = 3, from page images (note 61 §6a)
Scope (changed 2026-10-08, to avoid edit conflicts): a new note
`research/65-cmp119-sect3-d3-reading.md`; the lead adds the pointer in note 61 §6a.
T62 read CMP 119 Sect. 2 at d = 3 from the OCR and stopped at Sect. 3 (the
(k+1)-st step), whose OCR is unreadable. Read Sect. 3 from the page images
in `sources/papers/`. For each estimate, with equation number, say whether
it holds at d = 3 with R = identity, or what changes (powers of L, ε
exponents, entropy). Then state the resulting localized large-field
activity bound in the form |activity(X)| <= C ε_j^q e^{-κ d(X)}.
Done when: note 65 has the list and a one-line verdict. Commit `[T71][fix]`.

### T72 [fix] — reassigned from Codex to a subagent, 2026-10-08: CMP 122 II (1.79)-(1.99) at d = 3 with R = identity (notes 49, 61)
Scope (changed 2026-10-08): a new note `research/66-cmp122ii-d3-reading.md`;
the lead adds the pointers in notes 49 §6 and 61 §6a.
From the page images, check that Balaban's domain factors (1.79)-(1.89) and
the final activity bound (1.97)-(1.99) hold at d = 3 when the R-operation is
the identity, so that note 49's rooted KP lemma gives (H4a). List each
inequality used, with its d-dependence. Also (added after T66): say whether
the exponentiated expansion (1.92)-(1.99) at d = 3 localizes CMP 102's
sixth-order remainder (22)-(24), which is what note 61 §6b.4 item 1 needs.
Done when: note 66 has the list and a one-line verdict. Commit `[T72][fix]`.

## Lead (Claude): in progress

- T7 [proof/computation] — completed by Claude, 2026-10-02: P4-3D as conditional
  theorems, plus the 4D split-route transfer (Thm. 5), the Dimock literature
  check, and the exact 3D Gaussian check. Result:
  `research/18-three-dimensional-depth-comparison.md`. P4-3D itself is still open.
- T8: reassigned to Codex on 2026-10-02 (see "Assigned to Codex").
- T9 [review] — completed by Claude, 2026-10-02: lead review of T1-T6,
  correctness only. Result: `collaboration/lead-review-T1-T6.md`.

- T12 [proof] — completed by Claude, 2026-10-02 (`research/21-beta-derivative-4d.md`): H4D-3 in 4D. Prove or refute a
  uniform bound on ∂_β of normalized terminal expectations along the
  asymptotic-freedom trajectory. The tools are research/18 Thm. 5, exact
  T-transport (note 14), and Balaban's CMP 109/116 effective-coupling bounds.
  Also identify exactly where the R-operation breaks transport of
  ∂_β = -Cov(·, A_N). Target note: `research/21-beta-derivative-4d.md`.
- T14 [proof] — completed by Claude, 2026-10-02 (`research/22-coupling-flow-free-field-reduction.md`):
  H0 reduced to windowed free-field positivity (U) plus memory decay (D).
- T10 [fix] by Codex: reviewed by the lead, 2026-10-02. Correct; one `qquad`
  typo fixed by the lead.
- T15 [proof/computation] — completed by Claude, 2026-10-02 (`research/24-curved-contraction.md`):
  note 12 (3.3) proved for the CMP 109 average, and H6_Σ reduced to H7_Σ plus component counting.
- T11 [proof] by Codex: reviewed by the lead, 2026-10-02. Correct. Prop. 1 and the
  counterexample were checked. Theorem 2 rests on Codex's page-image reading of CMP 122 I
  (1.100) (the OCR is garbled), and the stated limits (final signed labels, the reverse FP
  step) are right. The equal-mass hypothesis of notes 13/16 now holds at the R'-stage.
- T16 [proof] — completed by Claude, 2026-10-02 (`research/25-h7-absorbed.md`):
  relative-gauge and rough-then-contract lemmas; H7 absorbed into large-field persistence (P)
  plus a generalized H8.
- T8 [computation] by Codex: reviewed by the lead, 2026-10-02. Correct; the table
  reproduces exactly, and the Wick/Parseval identities were checked. Its fixed-exterior
  correction (M^{-2}, not O(1)) is right and important.
- T18 [proof] — completed by Claude, 2026-10-02 (`research/27-4d-master-reduction.md`):
  corrected 4D master reduction at fixed terminal coupling. M1-4D <= (H0) + (T) + (B).
- T13 [computation] by Codex: reviewed by the lead, 2026-10-02. Correct. The O(3)
  increments converge to (N-2)log L/(2 pi) and the edge converges geometrically, so (C)+(S)
  hold in the scalar analogue. The SU(2) stop is honestly stated; it continues as T19.
- T20 [proof] — completed by Claude, 2026-10-02 (`research/28-4d-nondegeneracy-reduction.md`):
  P6-4D from a terminal small-field variance bound plus an R-bias bound carrying the large-field factor.
- T21 [proof] — completed by Claude, 2026-10-02 (`research/29-contraction-from-single-step.md`):
  memory decay (D, T-b, B-b, and H3D-1 in 3D) reduced to single-step Lipschitz bounds (S1)-(S3)
  by a weighted forward/backward bootstrap.
- T22 [computation] — completed by Claude, 2026-10-02 (`research/30-su2-2d-sup-check.md`):
  exact 2D SU(2) check that the sup-oscillation depth comparison holds with rate L^{-2N}.
- T17 [failed-attempt/computation] — completed by Claude, 2026-10-02 (`research/26-persistence-bound.md`):
  (P) is not derivable from the published bounds as stated. It is reduced to the persistent-curvature
  action lemma (PA) plus an action-weighted upper bound (UB); (PA) is verified in the abelian case.
- T19 [failed-attempt] — closed by Claude, 2026-10-02 (`research/23-one-loop-window.md` §7): three routes
  assessed and each stops at a named step; the universal part of (S) is published, and the SU(2) scheme edge
  needs second background derivatives of Balaban's composite average (multi-session). Off the critical path.
- T23 [proof] — completed by Claude, 2026-10-02 (`research/31-s2-model-lemma.md`): the O(g^2)
  mechanism of (S2) proved for one fluctuation integral (Taylor/Cauchy, plus Stein for the tilted mean);
  what remains for full (S2) is localization, background analyticity and large fields.
- T24 [proof] — completed by Claude, 2026-10-02 (`research/32-h8-by-integration-by-parts.md`): each
  first-order R-bias term equals -m_lambda Cov(G o U^ref, h_lambda) by integration by parts on the exterior
  (local right inverse of the linearized block map); generalized averaged H8 reduces to rooted decorrelation (H-dec).
- T25 [proof] — completed by Claude, 2026-10-02 (`research/33-hdec-from-local-tangent-bounds.md`): (H-dec)
  with factor L^{-4m}·poly(m) from local extensive tangent bounds (LS) + large fields (LF); Ad-invariance excludes
  dimension-2 parts (Lemma 1); zero-charge redistributions are divergences (Lemma 2); corrects note 32 Cor 5 (still summable).
- T26 [proof, conditional reduction] — completed by Claude, 2026-10-02 (`research/34-nonabelian-persistence-action.md`):
  non-abelian (PA) on the eps_0-small event from fiber convexity (D1) + minimizer regularity (D2), via exact
  telescoping of minimal actions and a chain/pigeonhole lemma; rate a ~ p(gamma)^2/log(1/gamma). Open: (D1), (D2), eps_0-large event.
- T27 [computation] — completed by Claude, 2026-10-02 (`research/35-minimizer-regularity-abelian.md`): exact
  sup-norm constant s_L of the abelian 4D minimizer image map (LP over the Bianchi annihilator): s_L = 1.54, 1.12, 0.77, 0.55
  for L = 2..5 (m = 1), mild growth in m. So (D2) holds only as s_L < 1 (L >= 4), not as O(L^-2); note 34 Thm 3 is
  generalized (eta-split) and note 33 §1 reading corrected. The n0 = 8 torus check was not completed (2 h limit); torus dependence unverified.
- T28 [computation + source reading] — completed by Claude, 2026-10-02 (`research/36-d1-d2-from-balaban-variational.md`):
  (D2) for SU(2) on E_0 follows from CMP 102b Prop 9 (analytic minimizer, linear term H_0) by linearization at the flat
  configuration, with s^NA <= s^ab(1+C eps_0)+C eps_0; (D1) from Thm 1 uniqueness plus the second variation. Localization and
  remainder uniformity are sketched. Abelian (D1) constant computed: c_1 = 1/(2 Lambda) ~ 0.6, uniform in the level.
- T29 [proof, conditional reduction] — completed by Claude, 2026-10-02 (`research/37-pa-large-levels.md`): abelian
  annular bound (a large level forces Morrey-weighted annular action >= delta) and summation lemma (each large level costs a
  fixed action); non-abelian (PA) on all events <= (D1), (D2) + lattice small-energy regularity (SER). (P) <= (UB) + (SER) + notes 34-36.
- T30 [failed-attempt] — completed by Claude, 2026-10-02 (`research/38-ub-entropy-obstruction.md`): CMP 122 II keeps a positive
  Wilson term on the label's own large-field domain (single-scale (UB) holds there); Lemma 1: irrelevant polymer differences are
  <= delta_E * action (via Ad-invariance). But a single-scale (UB) cannot give (P), because of entropy exp(c L^{4t}); note 26 Prop 1 is
  corrected to (P) <= (PA) + (UB-ms), with a multi-scale bound whose source is Balaban's per-scale factors (transfer to pre-replacement labels is open).
- T31 [conditional reduction] — completed by Claude, 2026-10-02 (`research/39-persistence-via-true-measure.md`): (P) <= (T1)
  label domination (pre-replacement R'-summands positive and dominated by the scale-k density) + (T2) marked large-field bound for
  the true measure. Needs no (PA), (SER) or (UB-ms). Corrected in §5: (T1) is too strong (the exterior law is R-modified); repaired
  route (P) <= (T1*) fiber-law comparison p_hat/q_hat <= exp(C N log g^-2) + (T2-R). Next step: check that W does not enter the zeta boundary layer in CMP 122 I (1.100).

- T32 [computation] — completed by Claude, 2026-10-02 (`research/40-mk-single-step-check.md`): 4D SU(2) Migdal-Kadanoff
  single-step Jacobian: theta -> 1/16 = L^-4, e = O(g^4) at heat-kernel shape, b*c = O(g^4) (b, c separately coordinate dependent),
  e ~ 3.4 w linear in irrelevant size. Note 29's hypotheses are consistent with asymptotic freedom; note 29 §3 remark added.

- T33 [proof, conditional] — completed by Claude, 2026-10-02 (`research/41-free-increments-convergence.md`): (C) of note 22
  (geometric convergence of the free increments beta_j^0) from (O1) uniform weighted propagator bounds [published at U = 1] and (O2)
  geometric operator convergence, via the resolvent identity. (O2) is done for the averaging kernels (note 19 (2.1)) and the weights a_j;
  the discretization part needs a two-scale (O1).

- T34 [proof, conditional] — completed by Claude, 2026-10-02 (`research/42-s2-by-even-deformation.md`): (S2) for a full
  RG step. Deforming the fluctuation coupling g -> sg gives an exactly even step in s that is pure transport at s = 0; with the even
  Schwarz lemma, D_E F = transport + O(g^2 p(g)^2), under (A_s): Balaban's single-step bounds uniform for complex |sg| <= alpha'/p(g).
  M1-3D <= (S1) + (A_s) for CMP 102.

- T35 [fix] — completed by Claude, 2026-10-03: source reading of CMP 109 p. 259 shows that Balaban's irrelevance bound (0.29) is
  explicitly not a per-step RG contraction. So (S1) of note 29 is a new theorem, not a published input. README and note 29 corrected.
  (S1) is now the main unproved single-step statement on both the 3D and 4D routes, together with (A_s) of note 42.

- T36 [computation] — completed by Claude, 2026-10-03 (`research/43-energy-norm-transport.md`): in the energy (l2) norm on
  exact coarse fluxes, transport conserves energy (L^4 mean^2 -> 1) and neighbouring-child differences (dimension 5) gain 2.3/L per step;
  sup norms miss this gain (note 35). Corrected: cross-face pairs gain only ~L^-0.6 for L <= 5 (worst row ~1 at L = 5). Pre-asymptotic face effects.

- T37 [proof] — completed by Claude, 2026-10-03 (`research/44-abelian-energy-s1-theorem.md`): abelian 4D, Balaban linear block
  flux: ||grad F_min||_2 <= C M^-1 ||F_min||_2 for all exact coarse data, with C <= 60 (proved, via the co-closed factorization
  J_rho(p_l) = A_rho(p_l) c_rho(K) and the alias-0 energy fraction) and sharp C -> ~4 (computed). Corollary: one-step image differences
  are O(L^-1) of the energy, across faces too. This is the transport part of (S1) in the energy norm, abelian linearization.

- T38 [fix/source reading] — completed by Claude, 2026-10-03: CMP 119 p. 245 defines R_0 as the smallest power of L with
  R_0 >= (log g_0^-2)^r, r >= 2, and R_k likewise. So condition (5.1) of note 39 holds and (T1*) holds; (P) now needs only the
  marker bookkeeping of (T2-R) (note 39 §6, §7b).

- T39 [proof, conditional] — completed by Claude, 2026-10-03 (`research/45-nonabelian-energy-s1-transfer.md`): SU(2) on E_0:
  ||grad H(B)|| <= (C_ab + C_1(L) eps_0) M^-1 ||H(B)||, from note 44 (flat part) plus (NA), the background-perturbation bound in
  energy norm. (NA) follows from CMP 99 Thm 3.4 (analyticity in the background) by Cauchy and Schur; C_1(L) is not tracked.
  Transport part of (S1) in the energy norm for SU(2), given (NA).

- T40 [proof] — completed by Claude, 2026-10-03 (`research/46-quadratic-form-norm.md`): the norm for (S1) is the form norm
  relative to the minimal energy. Gauge invariance makes the leading part of delta E a quadratic form; transport is Q -> Q o T;
  dimension-6 forms contract by (C/L)^2 and dimension-8 forms by C_3^2 L^-3 per step, and marginal forms by <= 1 (from note 44).

- T41 [proof] — completed by Claude, 2026-10-03 (`research/47-marginal-form-convergence.md`): the block-flux covariance
  C^(M)(K) (the marginal minimal-energy form) converges to a continuum symbol with ||C^(M) - C^inf|| <= C(1+log M)/M uniformly in K
  (alias weights 1/sin^2 - 1/x^2 <= 1, Fejer/Parseval, projector and phase errors); measured rate ~M^-2 (ratios 3.0, 3.5 per doubling).
  This is the marginal-form part of (O2) in note 41; the one-loop vertex part remains.

- T42 [proof, partly stated] — completed by Claude, 2026-10-03 (`research/48-free-increments-assembly.md`): (C) of note 22
  assembled. Covariance, minimizer-map symbol (cross alias sum x C^-1; measured ratios 3.53, 3.38 per level) and weights all converge
  geometrically by the note 47 argument; the vertex Riemann sums are stated. |beta_k^0 - beta_inf^0| <= C (1+log L^k) L^-k.

- T43 [proof + correction] — completed by Claude, 2026-10-03 (`research/49-t2r-rooted-lemma.md`): rooted Kotecky-Preiss lemma;
  (T2-R) from CMP 122 II (1.79)-(1.89). Correction to note 39 §6: carried domains get no new factor for K <= n_0 + R_j steps (1.83),
  so a_eff ~ p_0^2/R ~ (log)^{2p_0 - r}; needs 2p_0 > r (source check) and the KP form of Balaban's expansion.

- T44 [proof + sketch] — completed by Claude, 2026-10-03 (`research/50-sum-rule-from-multiplicativity.md`): (S) of note 22.
  Exact multiplicativity of the limit step (box formula + Lemma B + note 48) gives beta_inf^0(L) = c log L; an O(1) edge bound (E)
  (power-law propagator corrections at both edges; sketched) forces c = 2b_0. The scheme constant from T19 is no longer needed.

- T45 [proof] — completed by Claude, 2026-10-03 (`research/51-mixed-norm-compatibility.md`): Balaban's sup-norm analytic
  activities have quadratic parts bounded in the form norm by C E_0 alpha^-2 (Cauchy + Ad-invariance + axial gauge), and higher orders
  are O(eps_0) smaller. With note 46 transport and note 42 generation this makes note 29's single-step hypotheses consistent in a mixed norm.

- T46 [proof] — completed by Claude, 2026-10-03 (`research/52-h3d1-linearized.md`): H3D-1' (note 18) proved at the linearized
  (abelian Gaussian, 3D) level with sigma >= 2, from the d-dimensional note 44 Theorem 1 and note 51 Lemma 4. Hence
  M1-3D <= (A_s) [CMP 102 remainder bound] + (NA) [3D] + H3D-0(b) [fixed-N, qualitative], plus notes 17, 18, 44-46, 51-52.

- T47 [proof] — completed by Claude, 2026-10-03 (`research/53-average-pushforward-density.md`, script `t47_average_jacobian.py`):
  H3D-0(b) proved. One private link per coarse bond (exact), conditional Jacobian >= c_L > 0 (operator concavity of
  P_h + |h|cot|h|(I - P_h)), a.e. injectivity (degree count, checked 150/150 by Newton). So M1-3D <= (A_s) + (NA).

- T48 [counterexample + proof] — completed by Claude, 2026-10-03 (`research/54-flat-backgrounds-and-na.md`): note 45's (NA)
  fails on the torus (flat backgrounds with holonomy). Proved: note 44's transport bound holds exactly at every flat SU(2)
  background (twisted Bloch sectors); small-field backgrounds are o(1)-close to flat ones (compactness). Corrected (NA♭).

- T49 [fix] — completed by Claude, 2026-10-03 (note 42 §4): (A_s) source check, 4D. CMP 116 Part II §1 uses g_k only via
  analyticity domains in g_k B, the substitution B' = g_k CB - hD(g_k CB), and the 1/g_k^2 prefactor cancelled at second order;
  the Gaussian is g-independent. CMP 109 p. 266 states a variant of chi_k that makes E^(j), beta_j analytic in the couplings,
  but with radius ~ gamma_k, not alpha'/p(g_k). CMP 109 sections 3-5 not checked.

- T50 [computation] — completed by Claude, 2026-10-03 (`research/55-mc-terminal-convergence.md`): Monte Carlo, SU(2), d = 3,
  n0 = 4, L = 2, beta_N = beta0 2^N, N <= 3. Terminal averaged observables converge geometrically (ratio about 2.6 per step at beta0 = 4;
  onset at finest beta >= 8 for beta0 = 2). N = 4 (64^3) added: increments 0.0054 (P), 0.0069 (W12), still geometric.

- T51 [computation] — completed by Claude, 2026-10-04 (`research/56-mc-4d-universality.md`): 4D SU(2) Monte Carlo with
  Balaban's iterated average. At matched terminal P, W12 differs by 0.015 between N = 0 and 1, and by 0.000(2) between
  N = 1 and 2. The beta step falls 0.36 -> 0.30 toward the one-loop 0.2575.

- T56 [fix] — completed by Claude, 2026-10-06 (note 49 §6): the KP form of Balaban's final expansion is checked against CMP 122 II
  (1.97)-(1.99). After the Mayer expansion, the activities are bounded by c_1 e^{-(1+beta) kappa d_k}; with domain counting this gives KP for
  a = kappa d/2 when kappa is large. This was the last listed source item for (P).

- T57 [proof] — completed by Claude, 2026-10-06 (`research/58-vertex-alias-sums.md`): Lemma A, convergence of alias sums with
  Dirichlet-product weights and symbols of growth (1+|q|)^s, s < 1, at rate (1+log M) M^{s_+-1}. Proposition B: the vertex Riemann sums
  (note 48 item 4) follow from the structural form (V), which is checked for the leading gluon vertices (s = -3, -4). Lemma A2 (§2a)
  covers the two-alias extension for background aliases and the P-derivatives. Still open: the ghost and covariant-average terms.

- T58 [computation] — completed by Claude, 2026-10-06 (`research/59-mc-action-universality.md`): 3D SU(2), Wilson vs tree-level
  Symanzik at beta_N = 4·2^N. The terminal differences shrink from 0.083 to 0.009 (P) and from 0.115 to 0.017 (W12) over N = 0..3, at
  about the rate L^-N, and the limits agree within the extrapolation uncertainty.

- T59 [proof] — completed by Claude, 2026-10-06 (note 53 §6): H3D-0(b) also holds for Balaban's symmetric 4D average CMP 109 (0.4).
  The central crossing link is private, the weights are positive and sum to 1 - L^{1-d}, and Theorems 2, 4, 5 hold verbatim. This supplies
  the H3D-0 input of note 18 Theorem 5 (4D).

- T60 [fix] — completed by Claude, 2026-10-06 (`research/60-literature-check-2026-10.md`): literature check. No accepted publication
  proves M1-3D/M1-4D or Balaban's coupling-flow theorem. Related: Chatterjee 2024 (Gaussian Higgs scaling limit) and Cao-Chatterjee (state
  space). Unrefereed 4D existence claims are listed as unverified and not used.

- T61 [proof, conditional] — completed by Claude, 2026-10-06 (`research/61-3d-assembly-conditional.md`): the interacting H3D-1
  is written out. Lemma G (proved) is a summable-coupling bootstrap with physical-coupling bookkeeping. Theorem 1: (H1) transport (NA♭),
  (H2) generation (A_s), (H3) 3D marginal structure, (H4) large fields and (H5) terminal conversion imply H3D-1 with rate
  (N+1) max(theta', 1/L)^N, hence M1-3D. This explains the sigma = 1 component seen in the Monte Carlo.

- T58b [computation] — completed by Claude, 2026-10-06 (`research/62-mc-4d-action-memory.md`): 4D Wilson vs Symanzik at matched
  terminal P. The W12 gap is -0.0075(18) at N = 1 and -0.0057(19) at N = 2. Inconclusive: decay not established; N = 3 needed.

- T65 [proof] — completed by Claude, 2026-10-06 (`research/63-na-energy-perturbation.md`): Lemma 1 (proved) — constrained quadratic
  minimizers move by O(delta) in energy norm when forms and constraints move by delta. Prop. 2: (NA♭) in energy form from (I1) flat
  coercivity, (I2) CMP 102b sup bounds and (I3) a small multiplier term, avoiding the unproved CMP 102b (190) and Schur's test.

## Completed in lean mode (from 2026-10-09)

### T80 [counterexample] — **completed 2026-10-09** (Sonnet worker, lead-reviewed); rescoped (see the lead's note at the end of this entry); assigned to Sonnet, 2026-10-08: the equipartition bound (EQ') for the fibre Gibbs measure (note 64 §7.4-7.5)
Scope: a new note `research/67-fibre-equipartition.md`, plus
`research/scripts/t80_*.py`. (T79 edits note 64 §8 in parallel; do not edit note 64.)
T77 reduced the Z-local bound (R), hence (I-LF)(b) of note 61 §6b, to (EQ'):
E_{μ_{V'}}[β_{N+1} A_q] <= C_A for every fine plaquette q near Z, uniformly in
N, in β_{N+1} >= β_*(L), and in the coarse configuration V' (μ_{V'} is the
Wilson Gibbs measure on the fibre q(U) = V' of Balaban's average). Its
log-convexity route (Lemma 64.6) stalls at a lower bound for the fibre
partition function with a rough outside. Try an integration-by-parts
(Ward-identity) route instead: parametrize the fibre by U_rest with the
private links b(U_rest) determined (note 53 Lemma 1, Theorems 2, 4), take a
left-invariant vector field on one free link ℓ, and integrate by parts against
the fibre density. For the Wilson action this gives
E[β² |∇_ℓ A|²] = E[β Δ_ℓ A] + (terms from ∇_ℓ b and ∇_ℓ log J), and
Δ_ℓ(1 - ½ tr U_p) is a bounded multiple of ½ tr U_p. Bound the extra terms by
note 53's Jacobian bounds and Lemma 64.2. Then pass from the gradient bound
(which controls sin² of the plaquette angle) to A_q itself, handling angles
near π separately (for example by a large-deviation bound at that plaquette).
Gauge zero modes (note 64 §7.5) must be handled: work with gauge-invariant
quantities only.
Done when: (EQ') is proved with explicit C_A, or a `failed-attempt` names the
step (and says whether the boundary terms or the near-π angles are the
obstruction).
Partial work: `wip/round-2026-10-08/t80/` (scripts only).
Lead, 2026-10-09 (rescope): the salvaged `t80_abelian_fibre.py` shows that (EQ') as stated is false (abelian Gaussian fibre: E[βA_q] = βθ_cl²/2 + O(1), unbounded in β when V' has coarse flux near q), and that G_η of Prop. 64.3 at the classical minimizer exceeds the slack (1-η)L² - 1 by factors 10²-10⁴. New scope: write these up (counterexample), then decide (R) itself in the abelian Gaussian model, where D_N = β_N(A_N - L A_min) + const exactly: is Q - P_ZᵀQP_Z + C A_Z ⪰ 0 for a finite C, and which Z-local form of (R) holds.
Verdict (lead review): accepted, with one sentence of note 67 §3.4 corrected by the lead. Note 67: (EQ') and (EQ) are false as stated (exact Gaussian fibre, Prop. 67.1); Prop. 64.3's G_η route misses the slack by 10²-10⁴; (R) with a Z-local right-hand side is false in the abelian Gaussian model (Prop. 67.3: the column of the Schur complement A_min at c is not finite-range; explicit V with A_Z(V) = 0 and D = -0.234θ²β_N at L = 2, checked by brute force); the corrected form with an exponentially decaying tail holds there (Prop. 67.5; C_near = 2.84, C_T(2) = 8.8 at L = 2). Q = A_N - L A_min <= 0 numerically, with Theorem 64.1's L² - 1 sharp at L = 2. Follow-up: T81.

### T81 [proof] — **completed 2026-10-09** (Sonnet worker, lead-reviewed); posted 2026-10-09 by the lead: Lemma 6b.2 of note 61 under the corrected large-field bound (I-LF)(b′) (note 67 §5)
Scope: `research/61-3d-assembly-conditional.md`, a new §6e only (do not rewrite §6b).
T80 showed that (I-LF)(b) in its relative reading (R) is false in the abelian
Gaussian model and that what holds there is (I-LF)(b′):
D_N(V) - D_N(V^Z) >= -C_- β_N A_Z(V) - C_T β_N Σ_{c∈Z} Σ_{x∌Z} e^{-m d(x,c)} A_x(V^Z) - e_ent|Z| log β_N
(note 67 Prop. 67.5, §5). Redo Lemma 6b.2 (note 61 lines 449-470 and what follows) with (I-LF)(b′) as the hypothesis:
(1) the σ = -τ bound with the tail; (2) the tail in a small-field exterior (β_N A_x <= p²/2: tail <= ½C_T N_m p² per bond);
(3) large-field regions at distance < r_0 merged into one polymer, and the polymer factorization with the new connectivity radius;
(4) the resulting s_0^{LF} with explicit dependence on C_T, N_m, m, c_1. Say whether the KP summation of note 49 §6 still closes with the larger radius.
Done when: Lemma 6b.2′ is proved from (I-LF)(a), (I-LF)(b′) and Lemma 6b.1, or a `failed-attempt` names the step (e.g. the merged polymers' entropy against p²).
Verdict (lead review): accepted. Note 61 §6e: the σ = -τ step of Lemma 6b.2 uses the relative reading; Lemma 6b.2′ is proved from (I-LF)(a), (I-LF)(b′) in union form, Lemma 6b.1, (LF-E) and (LF-act), with s_0^{LF′} = min{c_1/(2(1-c_1)), 1/(2(C_- + 4C_T N_m))} (about 10⁻³ in the model); no merging beyond radius 2; KP closes for any fixed radius; the per-polymer route fails at a gauge-dependent cross term. Lead additions: the exterior factor E_σ(V^Z) needs a gauge in which V^Z is small-field on N(Z) (not done; same gap as the original lemma); the worker's union-form check committed as t81_union_check.py.

### T54 [computation] — **completed 2026-10-10** (lead; runs finished 2026-10-09 19:54 on Daniel's Mac); reassigned from Codex to the lead, 2026-10-08: 4D universality test, third depth and a third observable (note 56)
Scope: `research/scripts/t51_mc_universality_4d.py` (add a 2x2 loop
observable if needed), new output files, and a new section in
`research/56-mc-4d-universality.md`.
Note 56 matched the terminal plaquette at depths N = 1, 2 (8^4, 16^4). There
the terminal 1x2 loop agreed (difference 0.000(2)), and the beta step was
0.30 against the one-loop 0.2575.
1. Add the terminal 2x2 loop and repeat the N = 1, 2 matching for it.
2. Run N = 3 (32^4) at 3 beta values bracketing the matching point P = 0.64.
   Extrapolating the beta step suggests beta_3 is about 3.37-3.40. Use
   `t51_matching.py` (extend DATA).
3. Report the beta steps beta_3 - beta_2 and the W12 differences.

Expect about 4-5 h per beta at 32^4 in numpy, single core: the 16^4 points took about 1000 s, and 32^4 is 16 times larger. Run the three
beta values in parallel. Use 150 thermalization updates
and at least 200 measurements, as in note 56.
Optional extension (note 62): also run the tree-level Symanzik action at N = 3 with `t58_mc_action_universality.py`
(masked staples, about 11 h per beta at 32^4), to decide the 4D memory test.
Done when: the N = 3 matching row and the 2x2 comparison are in note 56.
Commit `[T54][computation]` plus one PROGRESS line.
Lead, 2026-10-08: the three N = 3 runs (32^4, betas 3.30, 3.40, 3.50, seeds
54330, 54340, 54350) were started at 23:16 UTC in the cloud container
(about 5.6 h each, one core each; output `research/scripts/t54_n3_beta*.out`).
The 2x2 loop and the write-up follow when they finish.
Update: container restarts kill background processes, so the runs now use
the checkpointed driver `t54_mc_checkpointed.py` (adds the 2x2 loop) and the
N = 0, 1, 2 points are re-run with it for W22 (`t54_chain.sh`). **On every lead
wake, run `sh research/scripts/t54_supervise.sh`**; it resumes any killed run
from its checkpoint and reports which are done.

**Status 2026-10-09 (handoff).** Finished, with the checkpointed driver
(adds W22), outputs committed as `research/scripts/t54_n{N}_b{beta}.out`:
N = 0 at beta 2.40, 2.50, 2.60; N = 1 at 2.60, 2.70, 2.80, 2.90; N = 2 at
2.85, 3.00. Still to run: N = 2 at 3.15, 3.30 (about 26 min each) and the
three N = 3 points (32^4, about 6.3 h each at about 44 s per update). The
N = 3 checkpoints of the old container (50 of 550 updates) do not transfer:
in a new container `sh research/scripts/t54_supervise.sh` starts them from
scratch. Run it on every lead wake: container restarts kill background
processes, and the supervisor resumes from the checkpoints. Then fit the
matching with `t51_matching.py` (extend DATA with the W22 column) and write
the note 56 section.
Result: note 56 section "Third depth (N = 3, 32⁴) and the 2×2 loop (T54)"; `t54_matching.py`/`.out`. The optional Symanzik N = 3 run (note 62) was not done.

### T78 [failed-attempt] — **completed 2026-10-10** (Sonnet worker, two session-limit stops, lead-reviewed); moved ahead of T79 by the lead (T79's consumer, the (EQ) route, was closed by T80); earlier: assigned to Sonnet (re-dispatched 2026-10-08; nothing salvaged): kernel locality of the interpolated forms (note 61 §6c.6, R2)
Scope: `research/61-3d-assembly-conditional.md`, new §6d, plus `research/scripts/t78_*.py`.
T76 proved S <= W_j <= Π_j^{(s)} <= W_{j+1} in the quadratic sector but noted
(R2) that a Loewner sandwich does not give locality: the real-space kernel of
Π_j^{(s)} (and of its minimizer map B_s(Φ), (6c.1)) must decay exponentially,
uniformly in s ∈ [0,1], j, N, for the polymer/mixed norm of note 51 to apply.
Prove this by a Combes-Thomas argument: conjugate the composite fibre problem
(6c.1) by e^{μ·x}, show the conjugated form stays coercive on the fibre for
|μ| <= μ_0 (with μ_0 independent of s, j, N, using S <= S + sΔ <= (1+ρ)S
and the finite range of w), and deduce |kernel(x,y)| <= C e^{-μ_0|x-y|} in
coarse units. Note whether the decay rate is in units of the level N-j lattice
(it must be, for the mixed norm). Check numerically on the abelian model
(`t76_convexity.py` setup) for L = 2, 3.
Done when: exponential decay is proved with explicit μ_0, C, or a
`failed-attempt` names the step (e.g. the constraint space under conjugation).
Verdict (lead review): accepted as a conditional reduction (failed-attempt for the unconditional statement). Note 61 §6d Theorem 6d.1: Combes-Thomas for the composite fibre, by cutting off potentials and repairing the constraint with a local lift; decay rate μ_0 per coarse unit uniform in s, j, N, given (P), (L), (H). Normalization: Π_j^{(s)} = L^j min{...} (brute force). Numerics: rate >= 1.25 per coarse unit for L = 2, 3, j <= 3, s ∈ {0, ½, 1}; the zero-extended flux form has a |x|^{-3} tail. Lead correction: (P) is false on all closed fluxes (linking argument) and is restated on the fibre Z; the suggested route to (L) via a coarse primitive fails for the same reason. Follow-up: T83.

### T71 [fix] — **completed 2026-10-10** (lead-reviewed); worker: the Claude session "Project Euclid paper downloads" (worker; started by Daniel, accepted by the lead); earlier claimed for a Sonnet worker, 2026-10-09; reassigned from Codex to a subagent, 2026-10-08: CMP 119 Sect. 3 at d = 3, from page images (note 61 §6a)
Scope (changed 2026-10-08, to avoid edit conflicts): a new note
`research/65-cmp119-sect3-d3-reading.md`; the lead adds the pointer in note 61 §6a.
T62 read CMP 119 Sect. 2 at d = 3 from the OCR and stopped at Sect. 3 (the
(k+1)-st step), whose OCR is unreadable. Read Sect. 3 from the page images
in `sources/papers/`. For each estimate, with equation number, say whether
it holds at d = 3 with R = identity, or what changes (powers of L, ε
exponents, entropy). Then state the resulting localized large-field
activity bound in the form |activity(X)| <= C ε_j^q e^{-κ d(X)}.
Done when: note 65 has the list and a one-line verdict. Commit `[T71][fix]`.
Partial work: `wip/round-2026-10-08/t71/` holds an essentially complete draft of note 65 and its script (unverified; see the README there). Start from it.
Lead, 2026-10-10: unblocked; Daniel downloaded all Project Euclid PDFs in his browser. Lead, 2026-10-09: **blocked on the page images.** On Daniel's Mac, Project Euclid answers `fetch_papers.sh` with a bot-check page after three downloads; CMP 119, 109, 116, 122 II, both CMP 99 and CMP 102 (variational) are missing from `sources/papers/`. The lead does not bypass the check; Daniel can download them in a browser (links in `fetch_papers.sh`), or the lead retries later. The worker brief is ready.
Verdict (lead review): accepted. Note 65 verified against the page images (eight checks; two corrected in detail: p_0 >= 5r is in the text after (1.1); CMP 119 has the global Corollary 3 bound involving T_k but no localized one). Sect. 3 survives at d = 3 with R = identity after four changes; no large-field activity bound in CMP 119; Prop. 65.4 relabelled a target. The lead applied note 65 §6 items 1-6 and 8 to note 61 §6a, note 49 and the README; item 7 (which uses of (T2-R) in notes 39/25 remain at d = 3) is recorded in note 49 only. The wip draft was removed.

### T82 [fix] — **completed 2026-10-10** (worker: session "Project Euclid paper downloads", branch t82-claude; lead-reviewed); posted 2026-10-10 by the lead: apply the approved items of the 2026-10-09 correctness audit
Source: `collaboration/claude-audit-2026-10-09.md` (Daniel-requested audit by the session "Project Euclid paper downloads"; the lead approved the items below). Scope: exactly the files named in the audit's §6 table, except as noted. For each item, re-check the claim against the text before editing (one line in the commit body per item: applied / not applied and why).
Approved: §2.2 (note 39 §7b, README l. 97-105: (T1*) holds *given* CMP 102b (190), proof omitted); §2.3 (notes 35 header and §3, 36 l. 106, 37 l. 113: the computed rows are lower bounds for s_L; s_L < 1 for L >= 4 is not established); §2.4 (manuscript l. 329-335: replace the real-source remark by the Vitali argument, after checking that the paper's observables are uniformly bounded); §2.5 (note 61 §6e Prop. 6e.2(ii), note 49 §6: a(X) = ½κd(X) + a_0 and the single-polymer bound <= 1/(3e)); every item of §2.6 except the PROGRESS/README error bar (already fixed); §3 (mark the stale summaries superseded, with a pointer to the current statement); §4 (note 67 §3.3(a), header, status, and note 61 §6e.3: Q <= 0 is proved by the argument of note 61 Lemma 6c.2 plus the kernel identity d(qA) = w*(CA); check that this identity holds for the average used in note 67's model, else say "proved given the identity; numerically confirmed").
Not in T82: §2.1 (note 61 §6a; the lead applies it with T71's note 65 §6), §5 (manuscript update and ledger rows: separate tasks), note 56 (done in T54).
Note 61 is also edited by T78 (new §6d): touch only the lines the audit names.
Done when: every approved item is applied or rejected with a reason. Commit `[T82][fix]` plus one PROGRESS line.
Verdict (lead review): accepted. All approved items applied, except two audit items the worker showed were wrong (note 22 Thm A constant: a partial window costs < ℓb_+, so 2ℓb_+ stands — checked by the lead; note 25 gauge order: correct under the convention of step 3, now stated). KP weight a(X) = ½κd(X) + 1 (c_1 <= 1/(2e)) checked. Q <= 0 now proved (note 61 Lemma 6c.2 + kernel identity, t82_kernel_check67.py re-run). Manuscript remark replaced by the Vitali-Montel argument; PDF rebuilt.

### T72 [fix] — **completed 2026-10-11** (Sonnet worker, one session-limit stop; lead-reviewed); reassigned from Codex to a subagent, 2026-10-08: CMP 122 II (1.79)-(1.99) at d = 3 with R = identity (notes 49, 61)
Scope (changed 2026-10-08): a new note `research/66-cmp122ii-d3-reading.md`;
the lead adds the pointers in notes 49 §6 and 61 §6a.
From the page images, check that Balaban's domain factors (1.79)-(1.89) and
the final activity bound (1.97)-(1.99) hold at d = 3 when the R-operation is
the identity, so that note 49's rooted KP lemma gives (H4a). List each
inequality used, with its d-dependence. Also (added after T66): say whether
the exponentiated expansion (1.92)-(1.99) at d = 3 localizes CMP 102's
sixth-order remainder (22)-(24), which is what note 61 §6b.4 item 1 needs.
Done when: note 66 has the list and a one-line verdict. Commit `[T72][fix]`.
Partial work: `wip/round-2026-10-08/t72/` (script only). Read note 65 first (T71): it reduces the needed bound to inputs (W) and (E) of CMP 122 II (its §5).
Verdict (lead review): accepted (pp. 385 and 387 checked by the lead against the images: (1.83) has R^{d+1}, (1.82) needs R^{d+2}, (1.89) is linear in p_0, the improved -κ_1 d_k(X) bound is one sentence). Note 66: (1.79)-(1.89) survive at d = 3 with R = identity after three changes (conditional reduction); (1.90)-(1.99) are the R-operation's expansion, vacuous at d = 3, with scale-independent α^{1/3}; they do not localize CMP 102's sixth-order remainder (the localized fluctuation expansion is CMP 119 (3.39)-(3.47)); the failing (2.6)-(2.9) forms are used only in the R-specific preparatory step. Lead applied note 66 §5 to notes 49, 61, 65 and the README. Follow-up: T84 (gaps G1, G2).

### T55 [fix] — **completed 2026-10-11** (lead-reviewed); worker: the session "Project Euclid paper downloads" (worker); claimed by Codex, 2026-10-07 (no deliverable; Codex out of usage); reassigned to a subagent, 2026-10-08: (A_s) source check of CMP 109 §§3-5 (note 42 §4)
Scope: `research/42-s2-by-even-deformation.md` §4 only.
Note 42 §4 (T49) checked CMP 116 Part II §1 and CMP 109 §2. Read CMP 109
§§3-5 (`sources/ocr/cmp109.md`, fluctuation-field action, Ward identities,
beta-function extraction). List every place where the coupling g_k enters an
estimate, and say for each whether the estimate uses only |g_k| p(g_k) (or
|g_k| |B|) or something more: the sign, reality or positivity of g_k, or of
g_k^{-2} A. Under the deformation g_k -> s g_k with |s g_k| p(g_k) <= α', the
generated marginal coefficient becomes complex. Say whether any step of §§3-5
uses that coefficient being real.
Done when: note 42 §4 has the list, with page and equation numbers, and a
one-line verdict: "no use of reality found", or the exact place where it is
used. Commit `[T55][fix]` plus one PROGRESS line.
Verdict (lead review): accepted (p. 295 checked by the lead on the image: the only reality statements are after (5.29), (5.30)). Note 42 §4: in CMP 109 §§3-5, g_k enters only through P^{(k)} (3.1) and B' (3.2); every estimate uses only the size of B'; the counterterm cancellation (4.38)-(4.45) and the β extraction (5.1)-(5.44) are identities plus size bounds; no use of reality found.

### T84 [proof] — **completed 2026-10-12** (Sonnet worker, one session-limit stop; lead-reviewed); posted 2026-10-11 by the lead: the gaps (G1), (G2) of (H4a) at d = 3 (note 66 §4 Q1)
Scope: a new note `research/68-large-field-gas-d3.md`, plus `research/scripts/t84_*.py`.
Note 66 found that at d = 3 with R = identity CMP 122 II gives each persisting large-field domain Y the weight T_k(Y)1 <= exp(-2p_0(g_k) - κ_k(Y)) ((1.89), inductive bookkeeping (1.80)-(1.88), which survives with three changes), but (G1) CMP 122 II writes no polymer representation of the large-field-domain gas at R = identity (only the R-operation output (1.103)-(1.104)), and (G2) the decay -κ_1 d_k(X) added to (1.89) for arbitrary regions is asserted on p. 387, not proved.
(1) Write the large-field-domain gas at R = identity as a polymer system: domains Y with weights from (1.89), interacting through the small-field expansion (CMP 119 (3.44)-(3.47), note 65) and through hard-core/overlap constraints, and state the KP condition of note 49 §6 (weight a(X) = ½κd(X) + 1) that it needs. (2) Prove (G2) from (1.80) at R = identity: κ_k(Y) >= κ_1 d_k(Y) for every domain (the creation budget γ_0 A_1² p_0²(d' + 1) of (1.85) against the R^{d+1} losses), with the exponent conditions of note 66 §3. (3) Conclude the bound |activity| <= C_q g_k^q e^{-κ d(X)} that note 61 Lemma 6b.2 / §6e assume, or name the step that fails.
Done when: (H4a) at d = 3 is proved from CMP 122 II's printed inputs (1.79)-(1.89), CMP 119 Sect. 3 and note 49, or a `failed-attempt` names the step.
Verdict (lead review): accepted (Prop. 68.1 induction and Thm 68.4 KP steps checked; script re-run, identical). Note 68: (G2) proved at R = id (surplus κ - Φ carried exactly; κ_k >= Φ + λD + c_*P²; only 2p_0 > (d+2)r); (G1) reduced to (H-form), (H-C), (1.79) for unprocessed T_k; Thm 68.5 gives |w(Γ)| <= C_q g_k^q e^{-κd_k} for large-field polymers, KP with a = ½κd + 1. Follow-up: T85 (the three readings).

### T53 [computation] — **completed 2026-10-12** (lead-reviewed); worker: the session "Project Euclid paper downloads" (worker); reassigned from Codex to a subagent, 2026-10-08: sup-norm constant s_L in twisted sectors (note 36 caveat)
Scope: `research/scripts/t27_minimizer_regularity.py` (add a twist option),
its output, and a short section in `research/35-minimizer-regularity-abelian.md`.
Note 36 (holonomy caveat) claims that the exact-flux sup-norm constant s_L of
note 35 is unchanged, up to O(e^{-δ n_0}), in the twisted Bloch sectors
created by a flat background with holonomy (note 54 §1). Test this. Add a
quasi-periodic twist e^{iθ} to the fine Fourier grid, so that coarse momenta
become K ∈ (2π/n_0)(Z^4 + θ/(2π)). Rerun the LP of note 35 for L = 2, 3, 4,
m = 1, at θ = π/4 and π/2. Report s_L(θ) next to s_L(0).
Done when: the table is in note 35 and states whether the claim of note 36
holds. Commit `[T53][computation]` plus one PROGRESS line.
Verdict (lead review): accepted (twistcheck re-run: all identities to 1e-15; the L = 4, n0 = 6, θ = 0 row re-run: 0.8807). Note 35 §5: diagonal twists lower the largest rows, one-direction twists raise them by < 0.1% at n0 = 6, gaps shrink from n0 = 4 to 6 (note 36's claim holds up to a small wrap-around amount; rate not confirmed). Side finding: for L >= 3 the far-corner rows are not the largest; s_L < 1 is suggested only for L >= 5. Lead added [T53] markers in notes 34 and 36.

## Proposals
(Workers: at most 5 lines each.)
- Lead, 2026-10-02: the lead's notes 21-30 have had only self-checks, which caught three errors
  (fixed: note 18 Thm 5 hypothesis, note 25 Lemma 1 constant, note 27 (T-a) rate). AGENTS.md
  gives no reviewer for lead work. Daniel may want one independent correctness pass, by Codex
  as a one-time task, on notes 24 (Thm 1), 25 (Lemmas 1-2), 27 (Thm 1) and 29 (Thm 1).
- Lead, 2026-10-02 (update): since then, self-checks caught more errors (note 26 Prop 1 entropy gap,
  note 33 §1 L^-4 reading, note 34 (D2) constant, note 39 (T1)); all are fixed in place. If Codex gets
  one review task, the highest-value targets are now note 39 (§5a, §6: the (P) route), note 42 (Lemma 1,
  Thm 3: the (S2) route), note 33 (Thm 3) and note 37 (Lemmas 1-2).
- Lead, 2026-10-03: (S1) is now the central open single-step theorem (CMP 109 p. 259 disclaims it). Proposal: define a mixed
  norm (energy norm for transport and contraction, Balaban's sup norms for analytic remainders) and prove (S1) for the abelian
  linearization first, using note 43's kernel data as the target constants.
