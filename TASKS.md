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

### T85 [fix] — open, posted 2026-10-12 by the lead: the three readings behind note 68 Thm 68.5 ((H4a) at d = 3)
Scope: a new §7 of `research/68-large-field-gas-d3.md` only.
Note 68 proved (G2) and reduced (G1) to three statements that CMP 122 II does not print at R = identity: (H-form) the R = id density has the form (1.104) with R' = 0, Y_i = all components of Z_k, and a factor e^{A'_k} independent of the large-field configuration; (H-C) the summed coupling bound, uniform in the Y_i (II proves (1.99) with the Y_i fixed); (1.79) for the unprocessed T_k (stated "for all large field regions", pp. 383-384, derived for T'_k). From the page images of CMP 122 II pp. 355-392 (pp. 355-375 not yet read) and CMP 122 I where cited, say for each whether it holds at d = 3 with R = identity, with page and equation numbers, or what is missing. Also the thickness of Z~ versus the footprint S(Y) (note 68 §6 "Not checked").
Done when: each of the three is confirmed, corrected, or shown to need a new argument (named). Commit `[T85][fix]`.

### T83 [proof] — open, posted 2026-10-10 by the lead: the inputs (P) and (L) of note 61 Theorem 6d.1
Scope: `research/61-3d-assembly-conditional.md`, a new §6d.6 only, plus `research/scripts/t83_*.py`.
T78 reduced kernel locality (R2) to (P) a local primitive Λ_0 on the fibre Z = ker div ∩ ker w (range r_P M, norm C_P M, M = L^j), (L) a local closed lift b of closed coarse fluxes (w b = 1, range r_L M, norm C_L M^{-1/2}), and (H) for interior s. (P) is false on all closed fluxes (linking; §6d.2), so its proof must use wz = 0.
(1) Prove (P): box Poincaré lemma (cone operator) on boxes of side ~M, glued through the Čech-de Rham tower; show the last (Čech H²) step is solvable locally because the coarse fluxes of z vanish; give C_P, r_P independent of M. (2) Prove (L) by a Whitney-type lift R^{(2)} commuting with d, with (wR^{(2)})^{-1} local on closed fluxes uniformly in M; check numerically (Fourier model of t78_kernel_decay.py) for L = 2, 3, j <= 4.
Done when: (P) and (L) proved with explicit constants (then Theorem 6d.1 is unconditional at s = 0, 1), or a `failed-attempt` naming the step.

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
Lead, 2026-10-09: after T80 (note 67) the route of Prop. 64.3 via (EQ) is closed, but Theorem 64.2 for all axes is still what (I-LF)(b′) for SU(2) needs (note 67 §5).

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
