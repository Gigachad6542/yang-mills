# Proof-obligation ledger

Statuses: **proved here**, **published input**, **published conditional input**,
and **open**.

## Dependency graph

```text
H0 prove the SU(2) coupling-flow claim announced as CMP 109, Theorem 2
 |
 +--> H1 published source-free 4D stability theorem (conditional on H0)
          |
          +--> P4 adjacent-depth comparison of terminal densities

P1 exact Balaban block-map dictionary
 |
 +--> P0b identify the abstract terminal-source identity in that kernel
          |
          +---------------------> P4
                                    |
P0a abstract source identity -------+
P5 bounded-source zero-free disc ---> A1 analytic cumulant lemma
                                           |
P4 ----------------------------------------+--> M1 cumulant convergence
                                                    |
                                                    +--> P6 nondegeneracy

Parallel local-source track:
H1 + P1 --> S0 marked small/large-field RG --> renormalized local-field program
```

## Obligations

| ID | Statement | Status | Evidence needed |
|---|---|---|---|
| H0 | Prove the SU(2) effective-coupling trajectory stated in CMP **109**, Theorem 2, keeping a prescribed terminal coupling while every \(g_k\) remains small. | open; announced proof unpublished | A complete replacement for the missing proof. The scalar shooting step is proved in `08-coupling-flow-reduction.md`; uniform positive beta-increment bounds are not. |
| H1 | Source-free four-dimensional density/stability bounds, assuming \(0<g_k\le\gamma\). | published conditional input | CMP **109**, Theorems 1 and 3; CMP **119**, Corollary 3; CMP **122 II**, Theorem 1. |
| P0a | A source depending only on the output of an exact block kernel factors through that RG step. | proved here | `04-terminal-source-identity.md`. |
| P0b | Match P0a to Balaban's exact deterministic average inside the group-delta constraint. | proved here from published formulas | CMP **98**, Eqs. (10)--(15); CMP **119**, Eq. (0.1); `04-terminal-source-identity.md`. |
| P1 | Identify the published block variable and its gauge covariance without changing conventions. | published input, audited | CMP **98**, Eqs. (10)--(15); Euclidean-symmetric variants in CMP **109**, Eqs. (0.4), (0.12). |
| S0 | Extend every small-field and large-field/polymer estimate to microscopic bounded plaquette-character sources, with analytic derivative bounds uniform in ultraviolet depth. | open parallel track | Marked versions of the published estimates; not needed for terminal-source M1. |
| P4 | Compare ultraviolet depths \(n+1\) and \(n\) on a common terminal lattice and obtain a summable bound for their normalized source-free terminal densities in the observable-test norm. | open | Principal new convergence estimate; stability alone is insufficient. A sufficient projective-density criterion is proved in `07-depth-comparison-reduction.md`. |
| P5 | Establish a cutoff-independent zero-free source polydisc for finitely many uniformly bounded observables. | proved here | Elementary estimate in `01-milestone-theorem.md` and `03-source-cumulant-lemma.md`. |
| A1 | Holomorphic Cauchy control implies convergence and factorial bounds for all fixed cumulants. | proved here | `03-source-cumulant-lemma.md`. |
| P6 | Show at least one limiting variance is positive. | open | A lower bound surviving the cutoff; upper bounds do not imply nondegeneracy. |
| M1b | Prove robustness under a stated change of finite-volume boundary condition. | open extension | Comparison of boundary polymer sectors after M1. |

## Highest-risk interfaces

1. **Depth comparison.** Balaban's stability theorem controls each ultraviolet
   depth but is not automatically a comparison theorem between depths.
2. **Coupling flow.** Even the source-free four-dimensional bound assumes the
   small-coupling trajectory whose announced SU(2) proof was not published.
3. **Large fields.** Bounded terminal observables prevent explosive source
   weights on a small source disc, but do not make two normalized measures close.
4. **Gauge convention.** Coarse Wilson loops are gauge invariant, but a claimed
   identity involving a block field must survive the construction's block axial
   gauge and residual gauge transformations.
5. **Meaningful scaling.** Raw plaquette characters are ideal RG diagnostics but
   do not by themselves define a renormalized \(\operatorname{tr}F^2\) field.
6. **Nondegeneracy.** Even genuine convergence could be to a deterministic or
   otherwise trivial fixed-scale observable; a variance lower bound is separate.

## Next proof attempt

Run two explicit main tracks. Track A compares the **source-free** terminal
densities at adjacent ultraviolet depths under the conditional hypothesis
\(0<g_k\le\gamma\); the terminal source is then only a bounded test function.
Track B reconstructs or replaces the unpublished coupling-flow proof. Track A can
make genuine conditional progress without pretending Track B is closed. The
marked CMP **116** and source-dependent \(R\)-operation work belongs to parallel
Stage S0 for microscopic insertions, not to M1.
