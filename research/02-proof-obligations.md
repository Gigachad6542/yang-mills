# Proof-obligation ledger

Statuses: **proved here**, **published input**, **open**, **blocked pending audit**.

## Dependency graph

```text
P1 Balaban block-kernel dictionary
 |
 +--> P0b identify the abstract terminal-source identity in that kernel
 |
 +--> S0 source-compatible small-field and large-field RG bounds
          |
          +--> P4 comparison of adjacent ultraviolet depths
                    |
P0a abstract source identity ----+
P5 bounded-source zero-free disc +--> A1 analytic cumulant lemma
                                         |
                                         +--> M1 cumulant convergence
                                                  |
                                                  +--> P6 nondegeneracy
```

## Obligations

| ID | Statement | Status | Evidence needed |
|---|---|---|---|
| P0a | A source depending only on the output of an exact block kernel factors through that RG step. | proved here | `04-terminal-source-identity.md`. |
| P0b | Match P0a to Balaban's actual constrained averaging, gauge fixing, and normalizations. | blocked pending audit | Exact equations and theorem/page references. |
| P1 | Identify the published block variable, gauge covariance, path choices, and large-field domains without changing conventions. | blocked pending audit | Exact dictionary from the Balaban series. |
| S0 | Extend every small-field and large-field/polymer estimate to bounded plaquette-character sources, with analytic derivative bounds uniform in ultraviolet depth. | open | Source-aware versions of the published estimates. |
| P4 | Compare ultraviolet depths \(n+1\) and \(n\) on a common terminal lattice and obtain a summable bound for \(Z_{n+1}-Z_n\). | open | Principal new convergence estimate; stability alone is insufficient. |
| P5 | Establish a cutoff-independent zero-free source polydisc for finitely many uniformly bounded observables. | proved here | Elementary estimate in `01-milestone-theorem.md` and `03-source-cumulant-lemma.md`. |
| A1 | Holomorphic Cauchy control implies convergence and factorial bounds for all fixed cumulants. | proved here | `03-source-cumulant-lemma.md`. |
| P6 | Show at least one limiting variance is positive. | open | A lower bound surviving the cutoff; upper bounds do not imply nondegeneracy. |
| M1b | Prove robustness under a stated change of finite-volume boundary condition. | open extension | Comparison of boundary polymer sectors after M1. |

## Highest-risk interfaces

1. **Depth comparison.** Balaban's stability theorem controls each ultraviolet
   depth but is not automatically a comparison theorem between depths.
2. **Large fields.** Bounded terminal observables prevent explosive source
   weights on a small source disc, but do not make two normalized measures close.
3. **Gauge convention.** Coarse Wilson loops are gauge invariant, but a claimed
   identity involving a block field must survive the construction's block axial
   gauge and residual gauge transformations.
4. **Meaningful scaling.** Raw plaquette characters are ideal RG diagnostics but
   do not by themselves define a renormalized \(\operatorname{tr}F^2\) field.
5. **Nondegeneracy.** Even genuine convergence could be to a deterministic or
   otherwise trivial fixed-scale observable; a variance lower bound is separate.

## Next proof attempt

After the P1 audit, write the exact one-step source-dependent density and verify
P0b line by line. Then identify the weakest norm on terminal effective densities
for which normalized expectations are Lipschitz. This decides whether P4 needs
convergence of the full effective density or only convergence in the dual of the
selected bounded block-observable algebra.
