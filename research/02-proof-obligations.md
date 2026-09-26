# Proof-obligation ledger

Statuses: **proved here**, **published input**, **open**, **blocked pending audit**.

## Dependency graph

```text
P0 exact finite-lattice source identity
  |
  +--> P1 block-map/gauge-covariance dictionary
  |      |
  |      +--> P2 source-compatible small-field RG estimates
  |      +--> P3 source-compatible large-field/polymer estimates
  |               |
  +---------------+--> P4 summable cutoff-increment estimate
                           |
                           +--> P5 zero-free complex source polydisc
                                      |
                                      +--> A1 analytic cumulant lemma
                                                |
                                                +--> M1 cumulant convergence
```

## Obligations

| ID | Statement | Status | Evidence needed |
|---|---|---|---|
| P0 | Insert the terminal block variable and show that a source depending only on it factors through every preceding RG integration exactly. | open | Algebraic derivation using the precise Balaban transformation. |
| P1 | Identify the published block map, gauge fixing, and coarse holonomy observable without changing conventions. | blocked pending audit | Exact equations and theorem/page references from the Balaban series. |
| P2 | Prove holomorphy and unchanged small-field estimates for the terminal bounded source. | open | Uniform complex-source norm estimates. |
| P3 | Show that large-field localization/exponentiation remains summable uniformly on the same source polydisc. | open | Source-aware polymer bounds including boundary polymers. |
| P4 | Compare depths (n+1) and (n) on a common terminal lattice and obtain a summable bound for (W_{n+1}-W_n). | open | This is the principal new UV convergence estimate. Stability alone is insufficient. |
| P5 | Establish a cutoff-independent zero-free polydisc or directly construct (W_n) as a convergent connected-polymer series. | open | Lee--Yang zeros cannot simply be assumed absent for complex sources. |
| A1 | Uniform holomorphic Cauchy control implies convergence and factorial bounds for all fixed cumulants. | proved here | See `03-source-cumulant-lemma.md`. |
| P6 | Show at least one limiting variance is positive. | open | A lower bound surviving the cutoff; upper bounds do not imply nondegeneracy. |

## Highest-risk interfaces

1. **Depth comparison.**  Balaban's stability theorem controls each ultraviolet
   depth but is not automatically a comparison theorem between depths.
2. **Large fields.**  Boundedness of the terminal observable prevents explosive
   source weights for fixed (z), but it does not by itself make the difference of
   two normalized measures small.
3. **Gauge convention.**  Coarse Wilson loops are gauge invariant, but a claimed
   identity involving (Q_nU) must survive the block axial gauge and residual gauge
   transformations used in the actual construction.
4. **Complex zeros.**  Real positivity gives (Z_n(z)>0) for real (z); it says
   nothing comparable for a complex polydisc.

## Next proof attempt

Once P1 is audited, prove P0 as an exact finite-dimensional identity.  Then isolate
the minimal norm in Balaban's terminal effective density for which P4 follows by a
Lipschitz estimate on normalized expectations.  This will show whether the project
requires convergence of the full effective density or only a weaker dual norm
tested by the selected block-observable algebra.
