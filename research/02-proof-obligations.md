# Proof-obligation ledger

(Rows H0, R2, R3 and P4 updated 2026-10-03 by the lead; see README for the summary.)

Statuses: **proved here**, **published input**, **published conditional input**,
and **open**.

## Dependency graph

```text
H0 --> H1 --+
             +--> Robs -----------------------------------+
R0a --------+                                             |
R1 + R2 + R3 (quantitative-bias route) -------------------+
                                                            +--> P4 --+
P0a --+                                                    |         |
       +--> P0b -------------------------------------------+         +--> M1
P1 ----+                                                    |         |
common-space defect + complete history/polymer bound -------+         |
P5 --> A1 ------------------------------------------------------------+
P6 nondegeneracy ------------------------------------------------------+

Parallel local-source track:
H1 + P1 --> S0 fully marked small/large-field RG --> local-field program
```

Here H0 is the coupling-flow proof, H1 the conditional source-free (RT)
stability input, R0a the exact source lift of the introductory fiber prototype,
R1--R3 the alternative quantitative-bias route to the complete observable
interface, P0a the abstract block-kernel identity, and P1 the exact
\(T\)-dictionary.  R1--R3 do not replace the remaining history/localization
bookkeeping in Robs.

## Obligations

| ID | Statement | Status | Evidence needed |
|---|---|---|---|
| H0 | Prove the SU(2) effective-coupling trajectory stated in CMP **109**, Theorem 2, keeping a prescribed terminal coupling while every \(g_k\) remains small. | open; reduced (2026-10-03) | Scalar shooting `08`; `22` reduces H0 to (C) + (S) + (D). (C): every quadratic and linear ingredient proved (`41`, `47`, `48`); the vertex Riemann sums are stated. (S): only an O(1) edge bound for composites is needed (`50`, sketched). (D): memory decay, reduced to single-step bounds (`29`). Transport (S1) is proved in the energy/form norm for the abelian linearization (`44`, `46`) and transferred to SU(2) given (NA) (`45`). Generation (S2) follows from (A_s) (`42`). Open: (A_s), (NA) constants, (S3) in the form norm. |
| H1 | Source-free four-dimensional \(RT\) density/stability bounds, assuming \(0<g_k\le\gamma\). | published conditional input | CMP **109**, Theorems 1 and 3; CMP **119**, Corollary 3; CMP **122 II**, Theorem 1. These control the vacuum integral and an auxiliary stabilized density, not the physical terminal law. |
| P0a | A source depending only on the output of an exact block kernel factors through that RG step. | proved here | `04-terminal-source-identity.md`. |
| P0b | Match P0a to Balaban's exact deterministic average inside the group-delta constraint. | proved here from published formulas | CMP **98**, Eqs. (10)--(15); CMP **119**, Eq. (0.1); `04-terminal-source-identity.md`. This is an identity for \(T\), not for the large-field \(R\)-replacement. |
| P1 | Identify the published block variable and its gauge covariance without changing conventions. | published input, audited | CMP **98**, Eqs. (10)--(15); Euclidean-symmetric variants in CMP **109**, Eqs. (0.4), (0.12). |
| R0a | Lift the introductory fiber-normalized \(R\)-prototype to finitely many terminal sources and prove a cutoff-independent zero-free source domain. | proved here | CMP **122 I**, Eq. (0.3), p. 176 is exactly a restricted-variable fiber replacement. `10-source-dependent-r-prototype.md` proves the multi-source lift, distortion bounds, and sequential analytic-family identity. |
| R1 / H6\(_\Sigma\) | Prove a summable, history- and placement-weighted bound on the **squared** terminal sensitivity of all \(R\)-components, including the first irregular step and regular curved backgrounds. | reduced to H7\(_\Sigma\) plus component counting (note 24: curved contraction (3.3) proved; first-layer path bound at any exterior); previously open; abstract reductions, the trivial-background linear part, and a convex-log rough one-step bound proved here | `10`, Lemma 2 proves the flat divergence-free linear-current bound, including the symmetric averages at first order. `12`, Lemmas 1--4 give conservation, uniform-contraction implications, and a rough one-step estimate covering the CMP **98** prototype and the four-dimensional convex-log average of CMP **109**, Eq. (0.4). The nonlinear group mean in Eq. (0.12) is covered only on its small-diameter domain after a separate Lipschitz estimate. A uniform per-component bound is only a strong sufficient route and may fail on curved hub chains; the placement-summed norm is primary. CMP **98**, Proposition 5 gives only a cutoff-independent bounded derivative. |
| R2 / H7\(_\Sigma\) | Prove a summable history- and placement-weighted tail bound for the complement of the regular terminal chart under both normalized fiber laws. | absorbed (note 25) into generalized H8 plus (P). **(P): reduced to published structure** (`39`, `49`): (T1\*) holds since R_k >= (log g_k^-2)^r with r >= 2 (CMP 119 p. 245); (T2-R) follows from Balaban's domain factors CMP 122 II (1.79)-(1.89) via a rooted KP lemma, with rate a_eff ~ p_0^2/R, which diverges because 2p_0 > (d+1)r. Remaining: the KP form of Balaban's final expansion (his convergence proof). | An action-based alternative is in `34`-`38`. |
| R3 / H8\(_\Sigma\) | Prove a summable history- and placement-weighted bound on the regular masked **terminal** mean shifts. | reduced: generalized averaged H8 is a covariance (`32`); its decay (H-dec) follows from extensive single-step tangent bounds (LS) plus large fields (LF) (`33`). (LS) transport part: `44`-`46`; generation: `42`. Open: (LF), the large-field analogue of H8, and (LS) in full. | `11`, Lemma 1 and Y6\(^{\prime\prime}\) (history). |
| Robs | Identify and propagate R0a through every localized denominator, history, localization/exponentiation step, and the final reverse Faddeev--Popov equivalence, with source bounds uniform in ultraviolet depth; alternatively combine R1--R3 with the complete history sum to bound the cumulative physical terminal-test bias by a vanishing quantity. | open; prerequisite for M1 through Balaban's \(RT\) route | CMP **122 I**, pp. 177, 193--194, 200--201 and CMP **122 II**, p. 378. Nonzero source denominators are elementary; locality, terminal-law comparison, and summability are not. See `09`--`11`. |
| S0 | Extend every small-field and large-field/polymer estimate to microscopic bounded plaquette-character sources, with analytic derivative bounds uniform in ultraviolet depth. | open parallel track | A full marked version of the published estimates. S0 is stronger than Robs, but the \(R\)-part of Robs cannot be omitted from terminal-source M1. |
| P4 | Compare ultraviolet depths \(n+1\) and \(n\) for the physical \(T^n\)-pushforward measures on a common terminal lattice and obtain a summable observable-test bound. | open | Principal convergence estimate. It requires common-space compatibility, marginal matching, complete history control, and a scale gain beating lattice entropy. Abstract reductions are in `07` and `09`; the master reduction is `27` (superseding note 18 Thm. 5): M1-4D <= (H0) + (T) memory decay + (B) R-bias. Memory decay is reduced to single-step bounds (`29`); see H0 and R1-R3. |
| P5 | Establish a cutoff-independent zero-free source polydisc for finitely many uniformly bounded observables. | proved here | Elementary estimate in `01-milestone-theorem.md` and `03-source-cumulant-lemma.md`. |
| A1 | Holomorphic Cauchy control implies convergence and factorial bounds for all fixed cumulants. | proved here | `03-source-cumulant-lemma.md`. |
| P6 | Show at least one limiting variance is positive. | conditional reduction (note 28): from a terminal small-field variance bound (V^R) and an R-bias bound carrying the large-field factor (B-small); open | A lower bound surviving the cutoff; upper bounds do not imply nondegeneracy. |
| P6-3D | For the exact three-dimensional terminal laws, prove a cutoff-uniform positive variance for every continuous real test nonconstant on the fixed small-field set. | proved here from published input | CMP **102**, Eq. (3)'s action-free terminal bound, with the paper's explicit sketchiness and lower-bound caveats; `17-three-dimensional-nondegeneracy.md`. The minimal-background regularity explains the sharper Eq. (5) but is not an extra P6-3D input. This does not change the open four-dimensional P6 row. |
| M1b | Prove robustness under a stated change of finite-volume boundary condition. | open extension | Comparison of boundary polymer sectors after M1. |

## Highest-risk interfaces

1. **Observable-changing \(R\)-step.** The introductory \(R\)-prototype is
   fiber-normalized and now has an exact abstract source lift, but the published
   complete construction changes the density and provides no source-stable
   locality/summability theorem.  Its true and template normalized fiber laws
   are not known to have common support.  The corrected bias route requires a
   placement-summed squared terminal-sensitivity bound, a summable regular-set
   tail, and a placement-summed terminal mean shift; a projected fine-field
   mean does not suffice.
2. **Depth comparison.** Balaban's stability theorem controls each ultraviolet
   depth but is not automatically a comparison theorem between physical depths.
3. **Coupling flow.** Even the source-free four-dimensional bound assumes the
   small-coupling trajectory whose announced SU(2) proof was not published.
4. **Large fields and histories.** Bounded terminal observables prevent explosive
   source weights on a small source disc, but do not make two normalized measures
   close. Sectorwise oscillation estimates also fail if history-dependent
   constants are not centered uniformly before the history sum.
5. **Gauge convention.** Coarse Wilson loops are gauge invariant, but a claimed
   identity involving a block field must survive the construction's block axial
   gauge and residual gauge transformations.
6. **Meaningful scaling.** Raw plaquette characters are ideal RG diagnostics but
   do not by themselves define a renormalized \(\operatorname{tr}F^2\) field.
7. **Nondegeneracy.** Even genuine convergence could be to a deterministic or
   otherwise trivial fixed-scale observable; a variance lower bound is separate.

## Next proof attempt

Run three explicit tracks. Track A upgrades the proved prototype lift R0a to
Robs by retaining the analytic source family through the localized complete
large-field step, or follows the quantitative-bias route R1--R3.  The first
technical target on that route is R1/H6\(_\Sigma\); R2/H7\(_\Sigma\) and
R3/H8\(_\Sigma\) require new information about normalized fiber laws. Track B compares adjacent **physical** depths
on their first common lattice, with a complete history pairing and rooted
polymer-difference estimate as specified in `09`. Track C reconstructs or
replaces the unpublished coupling-flow proof. The full marked CMP **116** program
remains the stronger parallel Stage S0, but the \(R\)-observable interface is now
part of M1 itself.
