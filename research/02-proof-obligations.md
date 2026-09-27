# Proof-obligation ledger

Statuses: **proved here**, **published input**, **published conditional input**,
and **open**.

## Dependency graph

```text
H0 prove the SU(2) coupling-flow claim announced as CMP 109, Theorem 2
 |
 +--> H1 published source-free RT stability theorem (conditional on H0)
          |
          +--> Robs make the measure-changing R step preserve terminal tests
                    |

P1 exact T block-map dictionary                       |
 |                                                     |
 +--> P0b terminal-source identity for exact T --------+
                                                        |
physical common-space defect + history/polymer bound --> P4
                                                        |
P5 bounded-source zero-free disc --> A1 analytic lemma -+--> M1 convergence
                                                                  |
                                                                  +--> P6

Parallel local-source track:
H1 + P1 --> S0 fully marked small/large-field RG --> local-field program
```

## Obligations

| ID | Statement | Status | Evidence needed |
|---|---|---|---|
| H0 | Prove the SU(2) effective-coupling trajectory stated in CMP **109**, Theorem 2, keeping a prescribed terminal coupling while every \(g_k\) remains small. | open; announced proof unpublished | A complete replacement for the missing proof. The scalar shooting step is proved in `08-coupling-flow-reduction.md`; uniform positive beta-increment bounds are not. |
| H1 | Source-free four-dimensional \(RT\) density/stability bounds, assuming \(0<g_k\le\gamma\). | published conditional input | CMP **109**, Theorems 1 and 3; CMP **119**, Corollary 3; CMP **122 II**, Theorem 1. These control the vacuum integral and an auxiliary stabilized density, not the physical terminal law. |
| P0a | A source depending only on the output of an exact block kernel factors through that RG step. | proved here | `04-terminal-source-identity.md`. |
| P0b | Match P0a to Balaban's exact deterministic average inside the group-delta constraint. | proved here from published formulas | CMP **98**, Eqs. (10)--(15); CMP **119**, Eq. (0.1); `04-terminal-source-identity.md`. This is an identity for \(T\), not for the large-field \(R\)-replacement. |
| P1 | Identify the published block variable and its gauge covariance without changing conventions. | published input, audited | CMP **98**, Eqs. (10)--(15); Euclidean-symmetric variants in CMP **109**, Eqs. (0.4), (0.12). |
| Robs | Extend each large-field \(R\)-operation so that it preserves the selected terminal generating functions, or bound its cumulative terminal-test bias by a quantity vanishing with the cutoff. | open; prerequisite for M1 through Balaban's \(RT\) route | CMP **122 I**, Eq. (0.4), p. 176 and the equivalence discussion on pp. 194, 200 show that \(R\) preserves the unweighted integral while changing the density. See `09-common-space-and-r-obstruction.md`. |
| S0 | Extend every small-field and large-field/polymer estimate to microscopic bounded plaquette-character sources, with analytic derivative bounds uniform in ultraviolet depth. | open parallel track | A full marked version of the published estimates. S0 is stronger than Robs, but the \(R\)-part of Robs cannot be omitted from terminal-source M1. |
| P4 | Compare ultraviolet depths \(n+1\) and \(n\) for the physical \(T^n\)-pushforward measures on a common terminal lattice and obtain a summable observable-test bound. | open | Principal convergence estimate. It requires common-space compatibility, marginal matching, complete history control, and a scale gain beating lattice entropy. Abstract reductions are in `07` and `09`. |
| P5 | Establish a cutoff-independent zero-free source polydisc for finitely many uniformly bounded observables. | proved here | Elementary estimate in `01-milestone-theorem.md` and `03-source-cumulant-lemma.md`. |
| A1 | Holomorphic Cauchy control implies convergence and factorial bounds for all fixed cumulants. | proved here | `03-source-cumulant-lemma.md`. |
| P6 | Show at least one limiting variance is positive. | open | A lower bound surviving the cutoff; upper bounds do not imply nondegeneracy. |
| M1b | Prove robustness under a stated change of finite-volume boundary condition. | open extension | Comparison of boundary polymer sectors after M1. |

## Highest-risk interfaces

1. **Observable-changing \(R\)-step.** The published \(R\)-operation preserves
   the partition integral but generally changes the density. Vacuum stability
   therefore cannot be inserted directly into a terminal-expectation proof.
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

Run three explicit tracks. Track A constructs Robs, a terminal-test-preserving
version of the large-field step, or a quantitative comparison between the
physical and stabilized measures. Track B compares adjacent **physical** depths
on their first common lattice, with a complete history pairing and rooted
polymer-difference estimate as specified in `09`. Track C reconstructs or
replaces the unpublished coupling-flow proof. The full marked CMP **116** program
remains the stronger parallel Stage S0, but the \(R\)-observable interface is now
part of M1 itself.
