# Correctness audit, 2026-10-09

Requested by Daniel directly (Claude session started for the Project Euclid
downloads; not the lead session). One pass, correctness only. No notes were
edited; every proposed change is in §6 for the lead to apply or reject.

## 0. Scope and method

Read in full and checked line by line (constants recomputed where a number
is quoted):

- manuscript `main.tex` (every proposition and proof);
- 3D route: notes 17, 18, 42, 44, 45, 46, 51, 52, 53, 54, 57, 61 (§§1-4,
  6, 6a, 6b, 6c, 6e), 63, 64, 67;
- 4D route: notes 19, 20, 21, 22, 24, 25, 26 §7, 27, 28, 29, 31, 32, 33,
  35, 36, 37, 38 §2, 39, 41, 47, 48, 49, 50, 58 §2;
- partly: notes 03, 04, 07 (Prop 1'), 09 (Prop 4).
- Source check: CMP 119 printed pp. 255-256 from the page images (the PDFs
  were downloaded today into `sources/papers/`).
- Scripted checks: all `NN §X` and `Theorem/Lemma/Prop NN.k`
  cross-references resolve; every note is in the README map; the lattice
  sums N_1, N_2, N_3, Ñ_2 of note 61 §6e; note 62's W12 gap against
  `t58_matching.out`.

Not audited: notes 01, 05, 06, 08, 10, 23, 30, 34 (Thm 3), 40, 43, 55, 56,
59, 60; notes 11-16 (lead review T9) and 12 (Codex review) were not
re-audited (AGENTS.md rule 2). Balaban readings were not re-checked except
CMP 119 pp. 255-256.

## 1. Verdict

No result labelled "proved here" in the audited notes is false, with one
exception of substance in a *reading* (§2.1) and one wrong numerical
conclusion drawn from a lower bound (§2.3). The other findings are a
status label that hides an unproved source input (§2.2), a false remark in
the manuscript (§2.4), small constant/convention slips, stale summaries,
one missed cross-reference, and missing write-ups.

## 2. Errors

### 2.1 Note 61 §6a item 2 misreads CMP 119 (2.6)-(2.9) (confirmed on page images)

Note 61 l. 269-276 says the inequalities "bound the finer-scale quantity by
the coarser one" and "hold in 3D, with room", and that no inequality in the
reverse direction was found. The printed page (CMP 119 p. 255, n > m) reads

    g_n <= (1 + g_n²β'(n-m))^{1/2} g_m <= (1+β_0)(n-m)^{1/2} g_m,   g_m <= (1+β_0) g_n,   (2.6)

and p. 256 has ε_n <= (1+β_0)(n-m)^{1/2} ε_m (2.8, first line) and
R_m <= (L+1)(n-m)^{β_0} R_n (2.9, second line). The first lines of (2.6)
and (2.8) bound the coarser quantity by the finer one. In 3D,
g_n/g_m = L^{(n-m)/2} >= √2 > 1 + β_0 already at n - m = 1, so they fail;
(2.7) and (2.9) second lines fail once (n-m)^p, (n-m)^r outgrow
(n-m)^{β_0}. This is exactly what the T71 draft
(`wip/round-2026-10-08/t71/65-cmp119-sect3-d3-reading.md` §3.1) says; the
draft is right on this point.

Effect: the README's "(H4): ... T62 read the inductive assumptions of
Sect. 2: supported" (README l. 195-197) and note 61 §6a's verdict are not
supported as written. Whether the d = 3 induction needs these inequalities
with n - m > 1 is the open question for T71.

### 2.2 (T1\*) "holds" depends on CMP 102b (190), whose proof Balaban omits (note 39, README)

Note 39 §5a bounds W's influence on the boundary layer "by the decay of
δℋ/δB (CMP 102b (190); note 36)". §7b then concludes "**(T1\*) therefore
holds**" (l. 322), and the README says (P) "rests on published structure"
(l. 97-105). Notes 54, 61 §6b.1 and 63 treat (190) as an unproved source
step ("proof omitted") everywhere else; note 63 was written to avoid it.
The label should be: (T1\*) holds given CMP 102b (190) [published, proof
omitted] and Balaban's bounds on the non-Wilson terms (CMP 122 II p. 381).

### 2.3 s_L < 1 for L >= 4 is claimed from lower bounds (notes 35, 36, 37)

Note 35 §2 says each tabulated value is the exact norm of *one row*, hence
"a lower bound for s_L" (s_L is the max over rows), with only the listed
rows computed (one row for L = 4, 5) and the torus-size dependence
unverified (§4). The header (l. 25: "This holds for L >= 4"), §3 item 1,
note 36 l. 106 ("s_L^{ab} <= 0.88") and note 37 l. 113 ("true for L >= 4")
use these numbers as upper bounds. A lower bound cannot show s_L < 1. The
"fails for L = 2, 3" half is correct. Impact: route B of (P) only (notes
34-37), which is not on the critical path.

### 2.4 Manuscript: the real-source remark is false in the paper's own setting

`main.tex` l. 329-335: "convergence only on real sources is insufficient;
1 + n^{-1/2} sin(nz) ...". For the paper's Z_n (uniformly bounded
observables) |Z_n(z)| <= e^{Σ B_j|z_j|} on C^q, so by Vitali/Montel
convergence on any real neighbourhood of 0 already gives locally uniform
convergence on C^q, hence cumulant convergence. The example is not a
generating function of bounded variables. (Note 03's list is fine: it is
about general holomorphic F.) Consequence worth stating: for bounded
terminal observables, the polydisc form of M1 is equivalent to
convergence in distribution of the finite vector of observables.

### 2.5 KP weight convention (note 61 §6e Prop 6e.2(ii); note 49 §6)

Note 61 l. 1100: "Σ_{Z∋□} w(Z) e^{½κd(Z)} <= ½ <= ½κ. This is the KP
condition ... a(X) = ½κd(X)". §6e defines d(Z) as the length of a minimal
spanning tree, so d(□) = 0 and a(□) = 0: the stated KP condition fails at
face value. Note 49 l. 146 has the same "<= a(□) = ½κ", which needs
d_k(□) = 1 (its sum also starts at n = 1); the convention is not stated.
Fix: a(X) = ½κd(X) + a_0 with a_0 = 3e·(single-polymer bound); this needs
that bound <= 1/(3e) (note 49: c_1 <= 1/(3e), i.e. α_1 small, instead of
c_1 <= 1). No conclusion changes.

### 2.6 Smaller slips

- Note 22 Thm A (l. 83): "h_k - h_{k'} >= (c/2)(k'-k) - 2ℓb_+" ignores the
  two partial end windows, where single β_j may be negative. The proof
  gives (c/2)(k'-k) - (b_+ + c/2)·4ℓ >= (c/2)(k'-k) - 6ℓb_+, and the
  stated constant can fail (k, k' in the middles of adjacent windows).
- Note 61 l. 478 and l. 1158: "(n_0L^j)³ = n_0³ε_0³ε_k^{-3}"; the block
  count at scale k is (n_0L^k)³. The final formulas are right.
- Note 61 §6b.5 (l. 538): "Ξ(s) is zero-free on |s| < 1/(r_max - 1)":
  Ξ = Π(1 + s(r-1))^{-1/2} has no zeros; 1/(r_max - 1) is its
  singularity (divergence) radius.
- Note 61 Lemma 6b.1 proof: the induction hypothesis should be "distance
  from E_i^{(s)} <= r" (needed for the segment claim), not
  "E_i^{(s+h)} ∈ N_r(𝒞_i)"; the bounds proved give exactly that.
- Note 63 Prop 2 step 1 (l. 177): the list of terms in a_U - a_♭ omits the
  background-curvature term ⟨F_U, [A, A']⟩, |F_U| ~ ω/M²; it is
  <= Cω N(A)N(A'), so the conclusion stands.
- Note 25 Lemma 1 step 2 (l. 55): with the convention U^g_b = g(x)U_b g(y)^{-1}
  the transformation is u = g'^{-1}g, not gg'^{-1}. Harmless.
- Note 31 Lemma 1 step 6: the restricted first-order term carries an extra
  factor ~ (gσ/α)(|X| log|X|)^{1/2}, not absorbed in "2|X| e^{-α²/(32g²σ²)}"
  for large |X|. Constant only.
- Note 18 §3: "H3D-1' ... is implied by H3D-1" holds only for the trivial
  one-piece decomposition (Σ_x|a_x| >= |Σ_x a_x|).
- Note 52 §1: uses |r(p_0)|² <= 4dπ²/M²; the bound is dπ²/M², so the
  d-dimensional constant is 2x loose (still valid).
- README l. 237 and PROGRESS l. 84: "-0.0057(19)"; note 62 and
  `t58_matching.out` give -0.00567 ± 0.00205, i.e. -0.0057(21).

## 3. Stale or inconsistent status statements

- Note 61 §4 (l. 204-207): "M1-3D <= (NA♭) + (A_s) + (H4) ... All three
  remaining inputs are readings". Since T66 the README has four inputs,
  with (L_s) a new estimate, not a reading. The Thm 1 proof sentence
  (l. 113: "All the maps involved are differentiable along the
  interpolation, because the data stay in Balaban's analytic domain") is
  exactly what §6b shows is not automatic; it is not annotated in place.
- Note 42: the header and Theorem 3 state the domain as |s|g p(g) <= α'
  and ||R|| <= 2M(gp/α')²; the T63 reading in the same note found CMP 102's
  cutoff is p², so for CMP 102 these are |s|g p² <= α' and O(g²p⁴) (note 61
  uses p⁴). §5 and l. 27 "M1-3D ⇐ (S1) + (A_s)" are stale.
- Note 53 §5 (l. 254-259): "M1-3D <= (A_s) + (NA♭)" is stale.
- Note 29 Cor 2: "in 3D ... couplings identical across depths (Δ_k = 0)";
  note 61 shows the generated F² terms make Δ ≠ 0 and handles them by (H3).
- Note 50 §4 (l. 229): "(E) sketched" and "vertex Riemann sums stated"
  contradict the header ("(E) open", T67 failed attempt) and note 58.
- Note 48 header: "proved for every quadratic and linear operator
  ingredient" models the step fluctuation through H_k and C^{(M)}. Note 41
  §1 describes Balaban's K_j with penalties at all levels i <= j, and note 41
  §5.6, the README and T75 say the multi-level penalty is open. No note
  shows the two descriptions agree. Its bottom status ("item 4 stated") is
  superseded by note 58.
- Note 41 Prop 1: its hypothesis (O2) ||K_j - K_∞||_δ <= C_O ϑ^j cannot hold
  for the Laplacian part, whose difference is unbounded (as §5's remark
  says). The working route is §5 Thm 2 on induced kernels; Prop 1 should
  say so.

## 4. Missed connection

- Note 67 §3.3(a), l. 31 and l. 527 list Q <= 0 (L·A_min >= A_N) as
  "computation only". It is proved: note 61 Lemma 6c.2 (T76) shows
  |w*B|² <= L|B|² for every fine flux B, and with the exact kernel identity
  d(qA) = w*(CA) (note 18 §8(a), note 19 (2.1)) this is A_N(V) <= L·A_min(V).
  Note 61 §6e.3 also uses "Q <= 0" without citing 6c.2.

## 5. Missing sections and unfinished write-ups

- **T54 is finished but not written up.** `research/scripts/t54_n3_b330.out`,
  `t54_n3_b340.out`, `t54_n3_b350.out` (32⁴, 550 updates, about 15100 s
  each, with W22) and `t54_n2_b330.out` are complete on Daniel's Mac. They
  are git-ignored (`.gitignore` l. 21, `t54_*.out`) and not committed; the
  last commit still says "N = 3 runs at 250/550 updates". Note 56 has no
  N = 3 row and no 2x2 comparison.
- **T71 is unblocked.** CMP 119, 109, 116, 122 II, both CMP 99 papers and
  CMP 102 (variational) are now in `sources/papers/` (Project Euclid,
  downloaded in Chrome). The draft's §3.1 is confirmed (§2.1 above).
- **Manuscript** (`main.tex`, dated September 2026) covers notes 01-13
  only: nothing on the 3D route (17, 18, 53, 61, 63, 64, 67), the master
  reductions (27, 29) or the numerics. The README calls it "assembled from
  the research notes".
- **Ledger** `research/02-proof-obligations.md` has no rows for the 3D
  inputs (NA♭), (A_s), (H4), (L_s); they appear only inside the P4 row.
  The README "Current theorem status" table row for P4-3D predates its own
  3D section (H3D-0 proved, note 61 assembly).
- **Reserved sections** pending open tasks: note 61 §6d (T78, in progress),
  notes 65 and 66 (T71, T72), note 64 §8 (T79), note 50 §2.6 (T73), note 41
  §5a (T75), note 42 §4 (T55), the twisted-sector section of note 35 (T53).

## 6. Proposed edits (for the lead)

| File | Change |
|---|---|
| research/61 §6a item 2, README l. 195-197 | (2.6)-(2.9): first lines of (2.6), (2.8) and second lines of (2.7), (2.9) fail at d = 3 (CMP 119 pp. 255-256); (H4) "supported at the level of the inductive assumptions" withdrawn pending T71 |
| research/39 §7b, README l. 97-105 | (T1\*) holds given CMP 102b (190) (proof omitted) and the O-term bounds |
| research/35 header + §3, 36 l. 106, 37 l. 113 | "s_L < 1 for L >= 4" → "the computed rows (lower bounds for s_L) are below 1 for L >= 4; s_L < 1 is not established" |
| manuscript l. 329-335 | replace by the Vitali remark (§2.4) |
| research/61 l. 1100, 49 l. 146 | a(X) = ½κd(X) + a_0 (§2.5) |
| research/22 l. 83 | constant 2ℓb_+ → 6ℓb_+ (or restrict to window endpoints) |
| research/61 l. 478, 1158 | (n_0L^j)³ → (n_0L^k)³ |
| README l. 237, PROGRESS l. 84 | -0.0057(19) → -0.0057(21) |
| research/67 §3.3(a), l. 31, l. 527; 61 §6e.3 | cite note 61 Lemma 6c.2: Q <= 0 is proved |
| research/61 §4, 42 header/§5, 53 §5, 29 Cor 2, 50 §4, 48 header | mark the stale summaries superseded (§3) |
| research/56 | N = 3 matching row and W22 comparison from the finished T54 runs |

## 7. Checked and correct

Manuscript: all propositions and theorems (the shooting IVT needs the
connected-component argument, which is not written but goes through).
Note 03 Theorems A-D. Note 17 Props 1-3. Note 18 Props 1-4, Thms 1, 1', 2,
5, Cor 3, and the Gaussian numbers ((2/3)(L²-1)/M², -(1-L^{-2})κ²/6). Note 19
(3.3), (3.4), (5.2)-(5.4). Note 20 Prop 1, Thm 2, the §2 counterexample.
Note 21 Lemma 2, Props 1, 3-5. Note 22 Lemma A0, Lemma B, Cor C, Prop D.
Note 24 Thm 1 (c_{4,L} = 12288L², κ_0, Lemma E's σ = (7d+16)Lr). Note 25
Lemmas 1-2, Cor 4. Note 26 Prop 2. Note 27 Thm 1. Note 28 Prop 1, Thm 2.
Note 29 Thm 1. Notes 31, 32 (Lemmas 1-2; Prop 1, Thm 3). Note 33 Lemmas
1-2, Thm 3, Cor 4. Note 36 §3. Note 37 Lemmas 1-2. Note 38 Lemma 1. Note 39
§5a algebra. Note 41 Lemmas 1-4, Thm 2 (Schur inverse re-derived; π²/48).
Note 42 Lemmas 1-2, Thm 3. Note 44 Thms 1, 3, Cor 2 (C = π⁶/16 ≈ 60.1). Note
45 Prop 1 and the potential-version constant (≈ 190). Notes 46, 47, 51, 52.
Note 49 Lemma 1, Prop 2. Note 50 Props 2.1, 2.2, 3. Note 53 in full (Lemma 1,
Thm 2 with Lemma 3, Thm 4's degree count, Thm 5, Prop 6). Note 54
counterexample, Thm 2, Lemma 3. Note 57 in full. Note 58 Lemma A. Note 61
Lemma G, Thm 1, Props 2-3, Lemma 6b.1, §6c (Lemmas 6c.1-6c.2, Thm 6c.3,
Prop 6c.4), §6e Props 6e.1-6e.2 and the quoted numbers. Note 63 Lemma 1,
Lemma 3, Prop 2. Note 64 Thm 64.1 (β_*, c_0(2) = 143.4, ball volume), Lemmas
64.1-64.6, Thm 64.2, Prop 64.3. Note 67 Props 67.1, 67.3, 67.5.
