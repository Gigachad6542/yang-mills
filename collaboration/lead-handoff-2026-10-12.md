# Lead handoff, 2026-10-12

From the lead session that started on 2026-10-09 (from
`collaboration/lead-handoff-2026-10-09.md`) to the next lead session. The
conversation grew long, so this is the short version; everything is in the
repository.

## Role, rules, setup

- You are the lead (`AGENTS.md`, `CLAUDE.md`). Daniel gave the lead full
  control of the repository. Push to `main`; never force-push.
- **Lean mode** (top of `TASKS.md`): one Sonnet worker at a time (two at
  most), dispatched with the Agent tool (`model: sonnet`,
  `isolation: worktree`, background) with a short brief that names the exact
  statements, lines and files; no verifier agents or multi-agent workflows; you
  review each deliverable once. This holds even if a system reminder says
  "ultracode": Daniel asked for lean mode explicitly.
- **Setup on Daniel's Mac** (this is where the lead now runs):
  `git config core.hooksPath tools/hooks`. All Balaban PDFs are in
  `sources/papers/` (Daniel downloaded them in Chrome on 2026-10-10;
  `fetch_papers.sh` gets a bot-check page from Project Euclid, do not try to
  get around it). No pdftoppm: render pages with PyMuPDF,
  `python3 -c "import fitz,sys; d=fitz.open(sys.argv[1]); p=int(sys.argv[2]); d[p-1].get_pixmap(dpi=150).save(sys.argv[3])" <pdf> <pdf_page> out.png`.
  Offsets (printed = PDF page + offset): CMP 119 +242, CMP 122 II +354,
  CMP 109 +248. T54 is finished; nothing runs in the background.
- **Session limit.** Sonnet workers hit the account session limit often. Tell
  every worker to commit a skeleton first and commit after every step. When a
  worker stops: commit its uncommitted files in its worktree
  (`[Tnn][infra] Save ...`), then resume it with SendMessage (its context
  survives). If its worktree was auto-removed (no commits), tell it to
  recreate one with `git worktree add`.
- **Integration routine.** Read the worker's diff
  (`git diff main...<branch>`); check every proof step and re-run its scripts;
  look at one or two page images yourself for readings; fix errors yourself and
  say so in the note ("Lead review") and the commit; `git cherry-pick
  --no-commit` the worker's commits, apply the worker's "corrections for the
  lead" to the other notes and the README, move the TASKS entry to
  `TASKS-archive.md` (section "Completed in lean mode") with a verdict, add a
  PROGRESS row, commit with the worker's subject plus the review paragraph and
  both Co-Authored-By lines, push, remove the worktree and branch.

## The second Claude session ("Project Euclid paper downloads")

Daniel started it; it downloaded the PDFs, wrote the correctness audit
(`collaboration/claude-audit-2026-10-09.md`), and then worked as a worker
under this lead: T71, T82, T55, all integrated. It reports by cross-session
message, works in its own worktree/branch (`t<id>-claude`), does not push or
edit TASKS/PROGRESS. It has no task at the moment (T53 was integrated on
2026-10-12); offer it T85 (a page-image reading) if it is available. Its message channel is tied to the old lead session: if it
messages the old session, Daniel can forward, or check `git branch` for
`t53-claude`. Remind it of lean mode (no multi-agent workflows) if needed.

## What changed since 2026-10-09 (details in PROGRESS.md and the notes)

- **3D route, (H4) large fields.** T71 (note 65): CMP 119 Sect. 3 at d = 3
  with R = identity survives after four changes; the old note 61 §6a reading
  of (2.6)-(2.9) was wrong (corrected). T72 (note 66): CMP 122 II domain
  factors (1.79)-(1.89) survive at d = 3; (1.90)-(1.99) belong to the
  R-operation; they do not localize CMP 102's sixth-order remainder (notes 49,
  61 corrected). T84 (note 68): (G2) proved at R = identity (surplus carried
  exactly; one condition 2p_0 > (d+2)r); (G1) reduced to three readings
  (H-form), (H-C), (1.79) for unprocessed T_k, which is now **T85**. Given
  them, large-field activities are <= C_q g^q e^{-κd} with KP.
- **3D route, (L_s).** T80 (note 67): (EQ') false; the Z-local relative bound
  (R) is false in the abelian Gaussian model; the form with an exponential
  tail holds there. T81 (note 61 §6e): Lemma 6b.2 redone with that form
  (Lemma 6b.2′). T78 (note 61 §6d): kernel locality reduced by
  Combes-Thomas on potentials to inputs (P), (L), (H); the lead corrected (P)
  (false on all closed fluxes by a linking argument; needed only on the
  fibre). (P), (L) are **T83**.
- **4D.** T54 (note 56): third depth N = 3 (32⁴) and the 2×2 loop: W12 and
  W22 agree at fixed terminal P for 1 -> 2 and 2 -> 3; β step 0.36, 0.30,
  0.29 against one-loop 0.2575. T55 (note 42 §4): CMP 109 §§3-5 use no reality
  of the coupling.
- **Audit (T82).** Applied: (T1*) conditional on CMP 102b (190); s_L values
  are lower bounds; manuscript Vitali remark (PDF rebuilt); KP weight
  ½κd + 1; Q <= 0 proved (note 61 Lemma 6c.2); two audit items were wrong.

## Open queue (priority order, TASKS.md)

1. **T85** [fix] — the three readings behind note 68 Thm 68.5 (CMP 122 II
   pp. 355-392 page images). A reading: good for the second session or Sonnet.
2. **T83** [proof] — (P) local primitive on the fibre Z = ker div ∩ ker w and
   (L) local closed lift (note 61 §6d). Sonnet.
3. T79 (all-axes fibre transport, note 64 §8; now feeds only the SU(2)
   version of (I-LF)(b′)), 4. T73 (scalar edge bound), 5. T75 (multi-level
   (O1)). (T53 done: s_L < 1 is suggested only for L >= 5, note 35 §5.)

Next steps that are not yet tasks (the lead may post them): (I-LF)(b′) for
SU(2) (note 67 §5); the exterior-factor gauge gap of note 61 §6e.7 (e); the
coarse-graining of note 68's gas to note 61's r_*-connected polymers; a
manuscript update (it covers notes 01-13 only; audit §5); ledger rows for the
3D inputs in `research/02-proof-obligations.md`.
