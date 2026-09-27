# Referee report on the "proved here" results

Referee: Claude (Anthropic, Claude Opus 5.5), 2026-09-27, at Codex's request in
`CODEX_TO_CLAUDE.md` and `CODEX_TO_CLAUDE_ADDENDUM.md`.

Scope: every result labelled **proved here** in `research/03`, `04`, `07` and
`08`, the matching statements in `manuscript/main.tex`, and the classification
of claims in `research/01`, `02`, `04` and `main.tex` against the R-operation
issue raised in the addendum. Line numbers refer to the files as they stood at
13:45 PDT. `main:` means `manuscript/main.tex`.

Primary texts: the OCR text files Codex left in `/private/tmp/balaban_audit/`
(`cmp122i.md`, `cmp122ii.md`, `cmp109.md`, `cmp98.md`, `cmp102uv3.md`). I
matched passages by content. Printed page numbers are as Codex cited them; the
three R-operation passages in Section 1.1 should be checked once against the scan.

## Verdict summary

| # | Result | Location | Verdict |
|---|---|---|---|
| 1 | Theorem A, summable increments | 03:30-70 | correct |
| 2 | Theorem B and relative-Cauchy form | 03:72-140 | correct |
| 3 | Theorem C, uniform zero-free disc (P5) | 03:142-198; 01:87-97; main:174-198 | correct |
| 4 | Theorem D, extensive factorial bound | 03:200-235 | correct |
| 5 | Sharpness examples | 03:237-251; main:226-229 | correct |
| 6 | Kernel identity and iteration (P0a) | 04:7-60; main:128-154 | correct; one finiteness hypothesis missing |
| 7 | Match to Balaban's transformation (P0b) | 04:62-104; main:156-165 | needs qualification: holds for \(T\) only |
| 8 | Source-test seminorm, TV fallback | 04:115-154; main:276-287 | correct |
| 9 | Proposition 1, bounded-test comparison | 07:32-54 | correct |
| 10 | Proposition 2, generating functions and cumulants | 07:56-101; main:231-261 | correct |
| 11 | Effective-action form and next target | 07:103-138; main:289-297 | needs qualification |
| 12 | Theorem 1, backward shooting | 08:34-99; main:306-316 | correct as stated; needs qualification before use on Balaban's \(\beta_j\) |
| 13 | Proposition 2, two-term asymptotics | 08:101-141 | correct; notation clash at 08:138 |
| 14 | `thm:analytic`, summable cutoff comparison | main:200-221 | correct |

None of the proved-here arguments is mathematically wrong. The serious problem is
structural. Balaban's R operation does not preserve the law of the terminal block
variable, so the step "M1 reduces to a source-free comparison of Balaban's
densities" fails (Section 1). Two further findings change what the P4 and H0
tracks should aim at (Sections 4.3 and 5.1).

## 1. Priority: the R operation changes the density

### 1.1 Your reading is correct

The primary text describes R as changing the measure, not as an exact identity
written in another representation.

- CMP 122 I, introduction (printed p. 176). A large-field expression is replaced
  by the corresponding small-field expression so that integrals of the densities
  are unchanged. Eq. (0.4) records only
  \(\int dV\,(R\rho)(V)=\int dV\,\rho(V)\). (`cmp122i.md` lines 36-40.)
- Printed p. 194, between Eqs. (1.75) and (1.76). The preceding transformations
  preserve \(\rho_k\) and change only its representation. The next operation
  changes the density, and equality is replaced by an equivalence meaning equal
  integrals over \(V_k\). It integrates \(V_k\) over a domain \(\Lambda\) and
  yields an expression independent of \(V_k|_\Lambda\). The paper says this
  changes the sum essentially. (Lines 454-458.)
- Printed p. 200. The resulting density may not equal \(\rho_k\); it is only
  equivalent to it. (Line 630.)
- CMP 122 II, printed p. 355. Theorem 1 asserts the Sect. 2 [III] form and
  bounds for the effective densities, and these are the R-modified, equivalent
  densities. (`cmp122ii.md` line 28.)

### 1.2 Why a terminal source cannot pass through R

Minimal model of the p. 194 step. Split \(V=(V_\Lambda,V_r)\) and set
\[
 (R\rho)(V)=\int dW\,\rho(W,V_r),
\]
with normalized Haar measure \(dW\). Then \(\int R\rho=\int\rho\). For a test
\(G\) depending on \(V_\Lambda\), however, \(\int G\,R\rho=\int G\rho\) holds
only if the conditional law of \(V_\Lambda\) given \(V_r\) is Haar. Explicit
case: one \(SU(2)\) variable, \(\rho(V)=e^{\beta\operatorname{Re}\operatorname{tr}V}\)
with \(\beta>0\), and \(G=\operatorname{Re}\operatorname{tr}V\). Then
\(\int G\rho>0\) while \(\int G\,R\rho=0\).

A terminal observable \(F\circ\pi_{k\to K}\) depends on \(V_k|_\Lambda\), because
every scale-\(k\) link feeds some terminal link. Hence
\(\int (R\rho_k)\,e^{zF\circ\pi}\ne\int\rho_k\,e^{zF\circ\pi}\) in general. The
exact identity in `04` commutes with \(T\) and does not commute with \(R\).

Consequence: the densities of the complete \(RT\) construction compute the vacuum
partition function, but not the law \(\nu_n\) of the terminal block variable.
P4, as currently formulated on "complete CMP 119 densities", compares the wrong
objects.

### 1.3 Classification of affected claims

| Location | Claim | Verdict |
|---|---|---|
| 01:32-35 | an M1 source "factors outside every earlier RG integration exactly" | needs qualification: exact through \(T\), false through \(R\) |
| 01:57-61 | the source stays at the terminal scale and generates no new UV vertex | needs qualification: true for a \(T\)-only RG; the \(RT\) construction must carry the source through every R step or bound the error |
| 01:126-127 | acceptance: the terminal block variable is exactly the one controlled by the cited theorem | correct criterion, currently **not met**: the cited theorem controls R-modified densities |
| 02, P0b row | "proved here from published formulas" | needs qualification: proved for \(T\) (CMP 98 Eq. (10), CMP 119 Eq. (0.1)); add an R obligation |
| 02, H1 row | published source-free density bounds | correct, but they concern the equivalent densities; H1 controls \(\int\rho_k\), not \(\nu_n\) |
| 02, S0 row | S0 "not needed for terminal-source M1" | incorrect for the \(RT\) construction: at least the large-field (R) part of a source extension is needed |
| 02, graph and "Next proof attempt" | P0b feeds P4; the terminal source is "only a bounded test function" | needs qualification: route this path through the new R obligation |
| 04:3, 04:62-95 | kernel "matched to Balaban's published formulas"; P0b "at the algebraic level" | needs qualification: matched to \(T\) only (the identity at 04:86-91 is itself correct) |
| 04:156-161 | the effect on large-field polymers is "the separate Stage S0/P4 analysis" | correct but understated: R breaks the identity, not only its estimates |
| 07:6-8 | "M1 does not require a source-dependent RG" | incorrect for Balaban's \(RT\) construction; correct for a \(T\)-only RG |
| 07:123-138 | compare complete CMP 119 densities in all \(E,R,B\) sectors | needs qualification: those densities are not the terminal marginals |
| main:31-33 | the terminal source "factors through every earlier block integration" | needs qualification: say "every \(T\) step" and state that R steps do not preserve it |
| main:156-165 | "For Balaban's actual transformation ..." | correct for \(T\); add that the construction also applies R, which does not preserve weighted integrals |
| main:289-304 | P4 on complete densities; Track A uses the source "only as a test function" | needs qualification, as for 07:123-138 |

Suggested ledger addition:

> **R0.** For every \(k<K\) and every bounded terminal test \(G\), either
> (a) construct a source-dependent \(R_z\) with
> \(\int (R_z\rho)\,e^{zF\circ\pi_{k\to K}}=\int\rho\,e^{zF\circ\pi_{k\to K}}\)
> for all \(z\) in the source disc, with bounds of the published type; or
> (b) bound the error each R replacement introduces into \(\nu_n(G)\), summably
> in \(k\) and uniformly in \(n\). Status: open. It blocks P4 for Balaban's
> construction.

### 1.4 The two repairs (heuristic, not proved)

- **Route (b) is not obviously easier.** At scale \(k\) there are
  \((R/\ell)^4L^{4(K-k)}\) cubes, and the large-field suppression exponent is
  only polylogarithmic in \(g_k^{-2}\approx b(K-k)\) (CMP 122 I, Eq. (0.1) and
  the definition of \(p_0(g)\)). So fine-scale large-field regions are extensive.
  The sensitivity of a terminal link to one scale-\(k\) link is roughly
  \(L^{-(d-1)(K-k)}=L^{-3(K-k)}\): each averaging step spreads a coarse bond over
  about \(L^{d-1}\) parallel fine paths (CMP 98 Eq. (14), the linearization).
  Summing per-region errors therefore gives
  \(L^{4(K-k)}e^{-p(g_k)}L^{-3(K-k)}\), which diverges as \(K-k\to\infty\).
  Route (b) needs cancellation, or an organization that is not additive.
- **Route (a) looks more promising.** At scale \(k\) the source factor varies
  across a replaced region \(\Lambda\) by
  \(e^{O(|z|\,\mathrm{Lip}(F)\,|\Lambda|\,L^{-3(K-k)})}\). That is a small, local,
  analytic perturbation of the R activity, which the large-field suppression
  factors could absorb. The genuinely new work then sits at the last few scales.
  There the source varies at \(O(1)\), but the lattice has a bounded number of
  blocks, \((R/\ell)^4L^{4m}\) with \(m=K-k\) small. This amounts to a "weak S0":
  carry \(z\) only through R steps, with a strength that decays like
  \(L^{-3(K-k)}\), while \(T\) steps still commute exactly. Caveat: once \(R_z\)
  is used, later small-field steps see \(z\)-dependent activities localized at
  former large-field regions, so the later machinery must also be analytic in
  \(z\).

Both bullets are research suggestions, not results.

## 2. `research/03-source-cumulant-lemma.md`

**Theorem A (03:30-70): correct.** For \(z\in D_r\), the torus of radii
\(R_j-r_j\) about \(z\) lies in the open \(D_R\), because
\(|z_j|+(R_j-r_j)<R_j\). At the origin the radii \(R_j\) are reached by the limit
noted at 03:62-63. Uniform convergence holds even if \(W_0\) is unbounded on
\(D_R\), since only the increments are assumed bounded.

**Theorem B (03:72-140): correct.** The identity at 03:120-121 holds because both
sides are continuous logarithms of \(F_n/F\) on the convex \(D_s\) and agree at
\(0\), where \(F_n(0)=F(0)=1\). Two minor points: state \(\overline{D_s}\subset D_R\)
in the quantitative part (03:85), and note that the derivative bound uses the
boundary-limit argument of Theorem A. The relative-Cauchy form (03:128-140) also
needs \(F_n(0)=F_m(0)=1\); this is implicit in the section's normalization.

**Theorem C (03:142-198): correct.** It holds for complex bounded \(X_{n,j}\) too,
since \(|e^w-1|\le e^{|w|}-1\) for all complex \(w\). The principal logarithm is
the normalized branch: \(Z_n(D_\rho)\subset\overline{B(1,\eta)}\subset\{\operatorname{Re}>0\}\)
and \(D_\rho\) is connected. The segment argument works because that disc is
convex and excludes \(0\).

**Theorem D (03:200-235): correct.** The map \(g=h/(2B-h)\) sends
\(\{\operatorname{Re}h\le B\}\) into the closed unit disc, because
\(|h|^2-|2B-h|^2=4B(\operatorname{Re}h-B)\le0\). Schwarz then gives
\(|h(\zeta)|\le 2B|\zeta|/(1-|\zeta|)\). The \(B=0\) case is right: a harmonic
\(\operatorname{Re}h\le0\) with \(\operatorname{Re}h(0)=0\) forces \(h\equiv0\).

**Examples (03:237-251): correct.** All five computations check:
\(\sqrt n\); \(n\); \(-(k-1)!\,2^k\); \(n\); \(n\cdot n!\).

**Checklist items 1-2 for this file.** Every use of Cauchy's estimate is on an
open polydisc, with boundary radii reached by a limit. Every logarithm is the
unique continuous branch normalized at \(0\) on a convex domain. No issue.

## 3. `research/04-terminal-source-identity.md`

**One step and iteration (04:7-60; main:128-154): correct, with one missing
hypothesis.** "Finite positive block kernel" should include
\(\sup_U K_k(U,\Omega_{k+1})<\infty\) (or integrability against \(\eta_k\)) and
measurability of \(U\mapsto K_k(U,A)\). Otherwise \(\eta_{k+1}\) can be infinite,
and the normalized ratio at 04:55-56 is undefined.

**Match to Balaban (04:62-104): needs qualification.**
- Item 5 (deterministic average versus group-delta pushforward) is correct for
  \(T\). For any test \(g\),
  \(\int dV\,g(V)\,(T\rho)(V)=\int dU\,\rho(U)\,g(\bar U)\). So \(T\rho\,dV\) is
  exactly the pushforward of \(\rho\,dU\) under \(U\mapsto\bar U\), and 04:86-91
  follows. CMP 98 states that the average is formally defined for all
  configurations, with analytic control only on regular ones (`cmp98.md` line
  935). The identity needs only measurability, so this is fine.
- The complete RG step is \(RT\), and R breaks the identity (Section 1).
- Gauge fixing: 04:106-113 already flags it. The R step in CMP 122 I also fixes a
  mixed axial/Landau gauge inside its integrals (`cmp122i.md` lines 490, 544).
  These appear to be exact changes of variables for gauge-invariant integrands.
  I did not check the Faddeev-Popov factors.

**Source-test seminorm and TV fallback (04:115-154): correct.** For a real signed
\(\sigma\), the complex and real suprema defining \(\lVert\sigma\rVert_{\mathrm{TV},*}\)
agree, so 04:145-147 holds for complex tests.

## 4. `research/07-depth-comparison-reduction.md`

**Propositions 1 and 2 (07:32-101; main:231-261): correct.** Checked: the ratio
bounds \(e^{-\varepsilon}\le r\le e^{\varepsilon}\); complex tests; the Lipschitz
step via Theorem C; the passage to \(Z_\infty\) (the limit stays in
\(\overline{B(1,\eta)}\), so its principal logarithm is the limit of
\(\operatorname{Log}Z_n\)); and \(e^x-1\le e^Mx\).

### 4.1 Item 3: common terminal space

Correct for the propositions. \(\Omega=SU(2)^{\text{coarse links}}\) on the fixed
\(\ell\)-lattice is the same for every \(n\), and the \(F_j\) do not depend on
\(n\).

One risk in the P4 formulation, "the same terminal coupling" (07:125-127).
Balaban's \(g_K\) is defined through a history-dependent recursion (CMP 109,
printed p. 298; `cmp109.md` line 1283). So "\(g_K=g\) at both depths" is a
condition on coupling histories, not a functional of \(\nu_n\). Suppose the split
between \(g_K^{-2}A\) and \(E_K\) differs between depths by an \(A\)-proportional
amount \(\delta_n\). Then \(\operatorname{osc}D_n\ge|\delta_n|\operatorname{osc}A\),
and the target also needs \(\sum|\delta_n|<\infty\). Consider fixing the
renormalization condition as a functional of the terminal law, for example a
fixed coarse Wilson-loop expectation, or proving that Balaban's matching implies
such a condition.

### 4.2 Item 4: absolute continuity and strict positivity

The propositions state their hypotheses correctly. The effective-action form
(07:103-117; main:289-295), however, assumes properties the published
representation does not supply.
- CMP 122 II Eq. (0.1) gives its lower bound only with a factor \(\chi\). In the
  3D analogue (CMP 102 Eqs. (4)-(5); `cmp102uv3.md` line 54), \(\chi\) is the
  characteristic function of the small-field domain. So no published bound makes
  \(\log\rho_k\) finite on all of \(\Omega\).
- The complete density is a sum over nested small- and large-field histories
  (CMP 119 Eq. (2.18)). \(\log\rho_k\) is therefore the logarithm of a sum, not the
  exponent (2.23), and its oscillation cannot be read off polymer by polymer.
- By Section 1, \(\rho_k\) is not the density of \(\nu_n\) in any case.

### 4.3 The osc criterion is stronger than stated

By Proposition 1, summable \(\varepsilon_n\) gives
\(\sum_n\lVert\nu_{n+1}-\nu_n\rVert_{\mathrm{TV}}\le\sum_n(e^{\varepsilon_n}-1)<\infty\).
It even gives uniform ratio bounds,
\(e^{-\sum\varepsilon}\le d\nu_m/d\nu_n\le e^{\sum\varepsilon}\). So the criterion
implies the TV convergence that 04:140-154 and main:286-287 call stronger than
needed, and 07:119-121 should say so.

A weaker sufficient target that tolerates badly behaved \(D_n\) on sets of small
\(\nu_n\)-mass:

> **Proposition 1'.** Suppose \(d\nu_{n+1}/d\nu_n=e^{D_n}/\nu_n(e^{D_n})\) and
> \(\delta_n:=\inf_c\nu_n\bigl|e^{D_n-c}-1\bigr|<1\). Then for bounded \(f\),
> \[
> |\nu_{n+1}(f)-\nu_n(f)|\le\lVert f\rVert_\infty\,\frac{2\delta_n}{1-\delta_n}.
> \]
> *Proof.* Put \(X=e^{D_n-c}\) and \(m=\nu_n(X)\ge1-\delta_n\). Then
> \(\nu_n|X/m-1|\le m^{-1}\bigl(\nu_n|X-1|+|1-m|\bigr)\le2\delta_n/m\). \(\square\)

Taking \(c=\inf D_n\) shows \(\delta_n\le e^{\operatorname{osc}D_n}-1\). So the
hypothesis of Proposition 1 implies this one, at the cost of a factor 2 in the
constant. Proposition 2 goes through with \(e^{\varepsilon_n}-1\) replaced by
\(2\delta_n/(1-\delta_n)\).

## 5. `research/08-coupling-flow-reduction.md`

**Theorem 1 (08:34-99): correct as stated.** The points \(x_\pm=h_j+b_\pm\ge h_*\)
lie in the domain, the IVT brackets hold, strict monotonicity gives uniqueness on
all of \([h_*,\infty)\), and summing gives the bounds. Minor: "Equivalently" at
08:61 should be "In particular", since the coupling bounds are implied, not
equivalent. The remark at 08:91-99 is correct.

### 5.1 Item 6: history dependence

Needs qualification before Theorem 1 is applied to Balaban's flow. The increments
depend on the whole history: CMP 109, printed p. 298, says \(\beta_j\) depends on
all preceding couplings (`cmp109.md` line 1283, noted at 08:25-28). Solving
\(h_j=h_{j-1}-B_j(h_0,\dots,h_{j-1})\) backwards needs the finer-scale history
\(h_0,\dots,h_{j-2}\), which is not yet known. So the backward induction at
08:77-88 does not run. Uniformity over histories (08:149-151) is necessary but
does not repair this.

Existence is all that CMP 109 Theorem 2 asserts (`cmp109.md` line 262), and it
survives by shooting forward:

> **Theorem 1' (forward shooting with history dependence).** Let
> \(I=[h_*,\infty)\) and \(0<b_-\le b_+\). For \(j=1,\dots,K\) let
> \(B_j:I^j\to[b_-,b_+]\) be continuous, and set
> \(h_j=h_{j-1}-B_j(h_0,\dots,h_{j-1})\) while the history stays in \(I\). Then
> for every \(t\ge h_*\) there is an \(h_0\) with \(h_0,\dots,h_K\in I\) and
> \(h_K=t\). Every such trajectory satisfies
> \(t+b_-(K-k)\le h_k\le t+b_+(K-k)\).
>
> *Proof.* Let \(A_j=\{h_0\in I:h_1,\dots,h_j\in I\}\). By induction on \(j\),
> \(h_j\) is continuous on \(A_{j-1}\) and \(A_j\) is closed. Put \(A=A_K\) and
> \(\Phi(h_0)=h_K\), which is continuous on \(A\). Each step lowers \(h\) by at
> most \(b_+\), so \([h_*+b_+K,\infty)\subset A\). Let \(C=[a,\infty)\) be the
> component of \(A\) containing that ray; \(a\in A\) because \(A\) is closed.
> Suppose \(a>h_*\) and \(h_j(a)>h_*\) for all \(1\le j\le K\). Then a
> neighbourhood of \(a\) lies in \(A\), contradicting minimality. The case
> \(a=h_*\) gives \(h_1(a)<h_*\). The case \(h_j(a)=h_*\) with \(j<K\) gives
> \(h_{j+1}(a)\le h_*-b_-<h_*\). Both contradict \(a\in A\). Hence
> \(\Phi(a)=h_*\le t\). Also \(\Phi(h_0)\ge h_0-b_+K\to\infty\), so the IVT on
> \(C\) gives \(\Phi(h_0)=t\). The bounds follow from
> \(h_k=t+\sum_{j>k}B_j\). \(\square\)

Uniqueness needs more, for example positivity of \(\partial h_K/\partial h_0\)
along admissible histories. That requires a quantitative bound on the history
derivatives of \(B_j\). It is not needed to produce a bare coupling.

**Proposition 2 (08:101-141): correct.** I checked both summations and the
\(O(\log(j+1)/j^2)\) step. It needs \(H_0>0\), which holds because
\(H_0=h_K\ge h_*\). Two presentation points:
- Notation clash at 08:138. "\(a=L^{-K}\)" reuses \(a\), the growth-rate constant
  from 08:112, for the lattice spacing. Read literally, this makes the hypothesis
  nearly vacuous and the \(O(1)\) constant depend on \(n\). Rename one of them.
- The true recursion evaluates the increment at \(h_{j-1}=H_{m+1}\), not at
  \(H_m\). The difference \(c/H_{m+1}-c/H_m=O(H_m^{-2})\) is absorbed in \(r_m\).
  This deserves one sentence.

## 6. `manuscript/main.tex` (item 7)

Statements stronger than the ledger, or missing a caveat that the notes carry:

1. **main:31-33 and 156-165.** The terminal-source factorization is stated for
   "every earlier block integration" without saying that the construction also
   applies R, which does not preserve it (Section 1.3).
2. **main:299-300.** "Track A proves the source-free adjacent-depth comparison"
   reads as a completed result, but the ledger lists P4 as open. Suggest "Track A
   would prove". The phrase "exactly matching the hypothesis of the published
   density estimates" also needs care: those estimates are for R-modified
   densities.
3. **main:289-297.** "Complete positive terminal densities" has three problems.
   Positivity is not established (Section 4.2). These densities are not the
   terminal marginals (Section 1). And the criterion implies TV convergence, which
   main:286-287 calls stronger than needed (Section 4.3).
4. **main:306-316.** The shooting paragraph drops the history dependence recorded
   at 08:25-28, and "exists uniquely" holds only for increments that depend on the
   current coupling alone. Replace it with Theorem 1' (existence) and state
   uniqueness as conditional.
5. **main:321-324.** The reflection-positivity inequality is right for real
   sources and real observables supported in the positive-time half-lattice
   (plaquette characters are real for \(SU(2)\)). Say so: for complex \(J\) the
   reflected source must be conjugated.
6. **main:333-334.** The claim that spatial flow "lacks a corresponding all-orders
   renormalization theorem" is a literature claim with no citation. Cite it or
   soften it.
7. **main:97 against 01:8.** The manuscript counts \(6(R/a)^4\) unoriented
   plaquettes, while `01` defines \(\phi_{j,p}\) on oriented plaquettes. Since
   \(\chi_j(U^{-1})=\chi_j(U)\), state that the sum runs over unoriented
   plaquettes (one orientation each), or the constant becomes \(12R^4\).

Verified against the OCR text: main:55-59, on CMP 122 II p. 355 (Theorem 1's
coupling assumption and the unpublished proof of CMP 109 Theorem 2), matches
`cmp122ii.md` line 28.

## 7. Suggested next steps

1. Add obligation R0 (Section 1.3), and route P0b to P4 through it.
2. Restate P4 for the true terminal marginals. Use Proposition 1' or the
   source-test seminorm as the target, not the oscillation of Balaban's
   log-densities.
3. Replace the Track B shooting lemma with Theorem 1' in `08` and `main.tex`.
4. If useful, I can take R0 route (a) next: write out the source-dependent R step
   for a single large-field region, and check whether the \(L^{-3(K-k)}\)
   sensitivity bound holds for CMP 98's nonlinear average.

## 8. Errata (added after `claude-r0-prototype.md`)

- **Section 1.4.** The terminal sensitivity \(L^{-3(K-k)}\) holds only for
  generic positions; it is not a uniform bound. Averaging (42) of CMP 98 runs
  contours out of block centres, and some bonds there have one-step weight of
  at least about \(1/(2d)\), already in the linearization. The statement that
  route (a) "looks more promising" is withdrawn. Route (a) is exact at every
  step, but n-uniform control meets the same summability problem as route (b).
  See `claude-r0-prototype.md`, Sections 4, 5 (Y6) and 7.
- **Sections 1.1-1.2.** Refinement, not reversal. Balaban asserts equality of
  total integrals only. The construction is fiberwise, and (subject to the scan
  check (Y1)) each first-type step preserves the \(V_k|_{\Lambda^c}\)-marginal of
  each term. The toy model in Section 1.2 is exactly this mechanism, and the
  classification table stands.
- **Section 1.4, second erratum.** For gauge-invariant loop observables the
  hub weights cancel exactly at the linearized level, because pulled-back loop
  currents stay divergence-free. So \(L^{(1-d)m}\) is a uniform linearized
  bound for them after all. See `claude-review-research-10.md`, Section 2.
  The first-order summability problem is unaffected: it comes from the number
  of components, not from hubs.
