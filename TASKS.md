# Task board

Owner: the lead (see `AGENTS.md`). Completed tasks and the full history are in
`TASKS-archive.md` (history only: take no tasks from it). This file lists only
open tasks, in priority order. Take the first unclaimed task assigned to you.

## How the loop runs (lean mode, from 2026-10-09)

Daniel asked on 2026-10-09 to cut token usage. The rules:

- One Sonnet worker at a time (two at most), dispatched by the lead with the
  Agent tool in its own worktree, with a short brief: the exact statements,
  equation numbers and files it needs, so it does not read whole notes.
- No automatic verifier agents. The lead reviews each deliverable once. Only
  when the lead doubts a specific claim does it send a small targeted check
  (one claim, one page or one computation).
- Workers commit early and often: the account session limit can stop them at
  any moment. The lead squashes when it integrates.
- Page images only for the pages needed (`pdftoppm -r 150 -f P -l P -png`).
- The lead wakes when a worker finishes, with a 1-2 hour fallback, and hands
  off to a fresh session (with a handoff file) when its conversation gets long.
- Setup in a new container: `git config core.hooksPath tools/hooks`;
  `FETCH_SLEEP=30 sh sources/fetch_papers.sh` for the Balaban PDFs (not
  committed); `sh research/scripts/t54_supervise.sh` to (re)start T54.

## Open tasks (priority order)

### T71 [fix] — claimed by Sonnet worker (lead dispatch), 2026-10-09; reassigned from Codex to a subagent, 2026-10-08: CMP 119 Sect. 3 at d = 3, from page images (note 61 §6a)
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
Partial work: `wip/round-2026-10-08/t72/` (script only). Read the T71 draft first: it reduces the needed bound to inputs (W) and (E) of CMP 122 II (its §5).

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
Partial work: `wip/round-2026-10-08/t80/` (scripts only).

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
Partial work: `wip/round-2026-10-08/t79/` (scripts only).

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
Partial work: `wip/round-2026-10-08/t73/` (scripts and outputs; no note text).

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
Partial work: `wip/round-2026-10-08/t75/` (script only).

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
