# Task board

Owner: the lead (Claude; lead returned by Daniel on 2026-09-29, 14:31 PDT). The rules are in `AGENTS.md`. Take the
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


- T3 [proof/counterexample] — claimed by `averaged_h8`, 2026-09-29: H8 in averaged form. The pointwise
  (fixed-exterior) H8_Sigma is probably false. The averaged bias is a
  covariance, and gauge invariance plus power counting suggest it gains
  exactly the missing factor L^{-m}. Target note:
  `research/13-averaged-bias.md`.
- T4 [computation] — claimed by `three_dimensional_m1`, 2026-09-29: M1 in three dimensions. Check whether Balaban's 3D
  large-field suppression makes the R-bias sum converge with crude bounds.
  CMP 122 I, p. 176 says that for d < 4 the bound is an arbitrarily large
  power of epsilon. Target note: `research/14-three-dimensional-m1.md`.
- T5 [proof/counterexample] — completed by Codex, 2026-09-29:
  determine exactly when Balaban's unnormalized large-field/component bounds
  imply the normalized bad-event probabilities required by H7_Sigma. Prove a
  sharp normalization lemma and either match its hypotheses to the published
  construction or give a finite-dimensional counterexample isolating the
  missing lower bound. Target note: `research/16-normalized-tail.md`.

## Lead (Claude): in progress

- T6 [proof]: M1 in 3D and nondegeneracy (P6-3D) from the two-sided bounds
  (5) of CMP 102. Target note: `research/17-three-dimensional-nondegeneracy.md`.
- T7 [proof/failed-attempt]: the 3D adjacent-depth comparison (P4-3D), the
  one real open estimate for M1 in 3D. Target note:
  `research/18-three-dimensional-depth-comparison.md`.
- T8 [computation/proof]: the Gaussian abelian model. Prove the covariance of
  a terminal loop with a local gauge-invariant even defect scales like
  L^{-4m} in 4D, while the fixed-exterior shift does not. This supports T3.
  Target note: `research/19-gaussian-power-counting.md`.
- T9 [review]: lead review of T1 and T2, for correctness only.

## Proposals
(Workers: at most 5 lines each.)
