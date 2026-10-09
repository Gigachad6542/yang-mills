# Lead handoff, 2026-10-09

From the lead session "Yang Mills research loop setup" to the next lead
session. Daniel asked for the handoff because that session's conversation had
grown long enough that every wake was expensive. Everything you need is in the
repository; this file is the short version.

## Your role and the rules

- You are the lead (`AGENTS.md`, `CLAUDE.md`). Daniel has given the lead full
  access to and control of the repository. Codex is out of usage.
- **Lean mode** (Daniel, 2026-10-09: cut token usage). The rules are at the
  top of `TASKS.md`: one Sonnet worker at a time (two at most), each with a
  short brief from you; no automatic verifier agents; you review each
  deliverable once; workers commit early; wake on worker completion with a
  1-2 hour fallback; hand off again when your own conversation gets long.
  Do not run multi-agent workflows with adversarial verifiers: three such
  workflows used about 1.9M tokens on 2026-10-08 and produced nothing,
  because parallel agents hit the session limit together.
- Push to `main` (Daniel's instruction; never force-push).

## Setup in a new container

    git config core.hooksPath tools/hooks
    FETCH_SLEEP=30 sh sources/fetch_papers.sh      # Balaban PDFs, not committed
    sh research/scripts/t54_supervise.sh            # (re)start the T54 runs

CMP 99 "background propagators" does not download; its OCR is in
`sources/ocr/`. Page images: `pdftoppm -r 150 -f P -l P -png <pdf> <prefix>`.
Container restarts kill background processes: run the T54 supervisor on every
wake (it resumes from checkpoints).

## Where the mathematics stands (details: `README.md`, `research/02-proof-obligations.md`)

- **3D route.** Note 61 Theorem 1: M1-3D <= (NA♭) + (A_s) + (H4) + (L_s).
  (NA♭) rests on proved notes plus published, proved input (note 63). (A_s)
  is a supported reading of CMP 102 (T63). (H4): CMP 119 Sect. 2 read (T62);
  Sect. 3 and CMP 122 II at d = 3 are T71/T72. (L_s), the localized
  s-analyticity used in the proof of Theorem 1, is the main open item
  (note 61 §6b): (I-L) locality of D_N (open), (I-S) analytic step (proved in
  the quadratic sector by convexity, §6c; kernel locality is T78), (I-LF)
  large-field comparison (note 64: absolute bound proved; the Z-local form
  reduced to equipartition (EQ') for last-axis bonds; T79, T80).
- **4D / H0.** (C): two-scale (O1) proved for the single-level free step
  (note 41 §5); multi-level is T75; (V) verified for gluon, ghost and
  gauge-fixing vertices (note 58). (S): the edge bound (E) is open; the
  termwise sketch fails (note 50 §2); the scalar loop is T73. (D): reduced to
  single-step bounds (note 29).
- **Round 2026-10-07 results, all integrated and reviewed:** T66, T67, T68,
  T69, T74, T76, T77 (see `PROGRESS.md`).

## Open queue (priority order, `TASKS.md`)

1. **T71** — finish note 65 from the draft in `wip/round-2026-10-08/t71/`.
   The draft is nearly complete. **Check before integrating:** it claims that
   T62's reading in note 61 §6a is wrong (four of CMP 119's inequalities
   (2.6)-(2.9) fail on the exact 3D flow) and that CMP 119 Sect. 3 has no
   large-field activity bound. If confirmed, correct note 61 §6a and the
   README 3D section.
2. **T72** — CMP 122 II at d = 3; settles inputs (W), (E) of the T71 draft
   and whether CMP 102's sixth-order remainder localizes (note 61 §6b.4).
3. T80 (EQ'), 4. T79 (all-axes transport), 5. T78 (kernel locality),
6. T73 (scalar edge bound), 7. T75 (multi-level (O1)), 8. T55, 9. T53,
10. T54 (Monte Carlo; partly done, see its entry).

Partial scripts for T72, T73, T75, T79, T80 are in `wip/round-2026-10-08/`
(see its README).

## Integration routine (what worked)

For each finished worker: read its diff; check every proof step and recompute
the key constants (re-run its script); fix small errors yourself and say so in
the commit; cherry-pick with `--no-commit`, edit, commit with the worker's
subject plus a "reviewed by the lead" line; mark the task in `TASKS.md`
(completed, with the verdict) and add a `PROGRESS.md` row; push; remove the
worktree. If the result opens a well-defined next step, post it as a new task
with a brief.
