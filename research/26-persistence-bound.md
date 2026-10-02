# The persistence bound (P): source reading and the exact missing step

Status: **failed attempt** (T17) for the full statement; the abelian case of the missing lemma (PA) is **proved** (§7) and checked numerically (§6). (P) of note 25, (4.1), is not derivable
from the published bounds as stated. This note records:

- what Balaban's large-field factors give (a source reading);
- why the result does not apply to (P) directly;
- a reduction of (P) to two precisely stated lemmas, (PA) and (UB). The
  first is a deterministic action bound; the second is an action-weighted
  upper bound;
- a heuristic computation showing that the expected rate satisfies
  L⁴e^{-a} < 1 for small γ.

## 1. What the sources give

CMP 122 II §1, at the end of the proof of Theorem 1 (pp. 380-381):

- For every large-field region at step j, the characteristic functions
  χ_j(P_j), χ'_j(Q_j), χ^{(j)c}(R_j) produce factors from the positivity of
  the local quadratic form of the Wilson action (Theorem 1 of CMP 102b; (71)
  of CMP 102).
- Covering P_j ∪ Q_j ∪ R_j by MR_j-cubes, each component Z^{(j)}_i yields
  a factor of the form exp(-γ_0 (d'_j(Z^{(j)}_i) + 1) p_0(g_j)²). The
  printed formula is partly garbled in the OCR; the dependence on d'_j and
  p_0(g_j) is legible.
- Against this, each large-field domain contributes a growth factor
  exp(O(1) M^{dR_d+1} d'_j(Z_j)), plus O(log g_j^{-2}) per unit volume from
  normalizations.
- The preparatory steps of the R-operation (CMP 122 I §1) add factors such
  as exp(-A_1 p_0(g_j)²).

These are **per-scale, per-region** factors in the history expansion of the
**R-modified** densities ρ_k. A history in which a region is large at
scales j, j+1, ..., j+t has large-field regions at each of those scales and
receives the product of the t+1 factors. In that sense the "marked" bound
exists for R-modified history terms.

## 2. Why this does not give (P) directly

In note 25, (P) concerns the **true pre-replacement** conditional fiber law
p̂ of an R'-label at scale k, and the persistence t(W): the number of
coarser levels on which the **images** U_{k+1}(W), ..., U_{k+t}(W) of the
fiber configuration stay non-small-field near the region. Two features
prevent a direct reading:

1. Persistence is a property of the scale-k configuration evaluated through
   later block maps. At the R'-stage of scale k, the later integrations have
   not been performed, so Balaban's later-scale characteristic functions
   are not yet part of the label. The suppression of persistent images must
   come from the scale-k density itself.
2. The published upper bound on the scale-k density, CMP 122 II (0.1),
   ρ_k <= exp(E_+|T_η|), carries no action. The action-dependent factors
   appear only inside the inductive proof (the positivity bounds in §1 of
   CMP 122 II) and are not stated as a bound one can use.

## 3. Reduction of (P) to two lemmas

**(PA) Persistent-curvature action lemma (deterministic; open).** Let U be a
scale-k lattice gauge field on a neighborhood of a region Λ. Suppose that
for each level j = 1, ..., t, some level-j image plaquette p_j within
distance C L^j of Λ has ϑ(U_{k+j}(∂p_j)) >= ε_{k+j}. Then the scale-k Wilson
action on the union of the corresponding level-j neighborhoods satisfies

    g_k^{-2} A_k(U | ∪_j N_j) >= c_L Σ_{j=1}^t ε_{k+j}² / g_{k+j}².

**(UB) Action-weighted upper bound (open, implicit in CMP 122 II §1).** The
pre-replacement summand of an R'-label at scale k is bounded by
exp(-(1-δ) g_k^{-2} A_k(U|N) + C|N|) on any region N disjoint from the
other large-field regions of its history, with constants uniform in k.

**Proposition 1 (proved, conditional).** (PA) and (UB) imply (P) with
a = (1-δ) c_L min_j p(g_j)² - C', since ε_j = g_j p(g_j) (Balaban's
small-field threshold) gives ε_j²/g_j² = p(g_j)². Hence L⁴e^{-a} < 1 once
(1-δ) c_L p(γ)² > 4 log L + C', which holds for small γ.

*Proof.* On the persistence-t event, (PA) gives the action bound. (UB)
turns it into the mass bound w_m e^{-at} relative to the persistence-0
mass. The L^{4m} placement count is unchanged. ∎

## 4. Why (PA) should hold: scale invariance

In 4D the Yang-Mills action is scale invariant. Consider a smooth abelian
field whose flux through a disk of radius r is at least ε at every scale
r ∈ [R_0, L^t R_0]. Its field strength must be about ε/r² at radius r, and
the action is ∫ F² d⁴x ~ ∫ (ε²/r⁴) r³ dr = ε² t log L. So the action grows
**linearly in the number of persisting scales**. Each level costs about ε²
(times log L), and with ε_j²/g_j² = p(g_j)² this gives e^{-a} per level with
a ~ c p(γ)² log L. (PA) is the lattice, non-abelian and
Balaban-average version of this statement. A proof would combine:

- Balaban's variational theory (CMP 102b), which says that the minimal
  scale-k action with prescribed level-j averages is comparable to the
  level-j action;
- a disjoint-shell decomposition, giving additivity over levels.

## 5. Verdict and next step

T17 ends as a **failed attempt**. (P) does not follow from the published
statements, because the per-scale large-field factors are proved for
R-modified history terms and the published density upper bound has no
action. (P) does follow from (PA) + (UB) (Prop. 1).

- (UB) is a matter of extracting a statement already used inside CMP 122 II
  §1.
- (PA) is a new but elementary-looking deterministic lemma, with the
  scale-invariance heuristic of §4 behind it. A concrete first check is the
  abelian linearized version: the minimal ½|dA|² subject to nested
  block-flux constraints ⟨w_j, dA⟩ >= ε, j = 1..t, equals
  ½ε² 1ᵀG^{-1}1 with G the Gram matrix of the block-flux functionals
  (note 19's kernels). (PA) in that case is linear growth of 1ᵀG^{-1}1 in t.

## 6. Abelian check of (PA) (computation)

`research/scripts/t17_persistence_gram.py` (output `.out`) computes the
Gram matrix G_ij = ⟨w_i, P w_j⟩ of nested 4D block-flux functionals (note 19
kernels, common corner, orientation (0,1)) by FFT on (Z/n)^4.

| L, n | level variances G_jj | max nested correlation | 1ᵀG^{-1}1 for t = 1, 2, 3, 4 |
|---|---|---|---|
| 2, 48 | 0.235, 0.172, 0.155, 0.144 | 0.083 | 4.26, 9.44, 15.04, 21.21 |
| 3, 54 | 0.189, 0.154, 0.105 | 0.050 | 5.30, 11.79, 22.26 |

Nested levels are almost uncorrelated, and the variances decrease to the
scale-invariant continuum value of about 0.105 (note 19, Var(X) -> 0.1047;
the last level at each n is affected by the torus size). So 1ᵀG^{-1}1 grows
**linearly** in t, at about 1/G_jj per level. In the abelian, linearized
case, holding the block flux >= ε on t nested levels costs action at least
½ε² Σ_j 1/G_jj ≈ ½ε² t/0.105, which is (PA) with c_L > 0. The non-abelian,
Balaban-average version and (UB) remain open.

## 7. Abelian (PA): proof

**Proposition 2 (proved).** Take an abelian lattice field A on the scale-k
lattice with B = dA. For levels j = 1, ..., t, let w_j be the level-j
block-flux functional of note 19 (2.1)/(3.6): the M_j-box average times the
M_j×M_j square, M_j = L^j, at arbitrary placements and orientations. If
|⟨w_j, B⟩| >= ε_j for every j, then

    ½|B|² >= ½ (Σ_j ε_j)² (L² - 1) / (t (L² + 1)).

In particular ½|B|² >= ½ ε² t (L²-1)/(L²+1) when every ε_j = ε, which is
linear in t.

*Proof.*

1. *Sizes.* The kernel is w_j = M_j^{-4} T_{M_j} ⊗ T_{M_j} ⊗ 1_{M_j} ⊗ 1_{M_j},
   with T_M = 1_M * 1_M. So
   - ||w_j||_1 = M_j^{-4}(M_j²)² M_j² = M_j²;
   - ||w_j||_∞ = M_j^{-4} · M_j · M_j = M_j^{-2};
   - ||w_j||_2² = M_j^{-8}((2M_j³+M_j)/3)² M_j² <= 1 (decreasing from 1 at
     M = 1 to 4/9).
2. *Near-orthogonality.* For i < j, |⟨w_i, w_j⟩| <= ||w_i||_1 ||w_j||_∞ = L^{-2(j-i)}.
3. *Sum.* With s_j = sign⟨w_j, B⟩,
   ||Σ_j s_j w_j||² <= Σ_j ||w_j||² + 2Σ_{i<j} L^{-2(j-i)} <= t(1 + 2/(L²-1)).
4. *Cauchy-Schwarz.* Σ_j ε_j <= Σ_j |⟨w_j,B⟩| = ⟨Σ s_j w_j, B⟩ <= ||Σ s_j w_j|| |B|.
   Square and use step 3. ∎

The FFT Gram values of §6 (about 5 to 9 per level, against the proved
(L²-1)/(L²+1) = 0.6 for L = 2) show that the bound is conservative but has
the right linear form.

**Non-abelian gap.** For SU(2) with Balaban's average, the level-j image
angle is ⟨w_j, F⟩ + O(curvature²) only where the fine field is small in a
gauge, while axial-gauge link sizes grow like R·κ over regions of size R
(note 24 Lemma B). A fine plaquette of angle >= ε_0 already costs g_k^{-2}cε_0²
by itself. Otherwise all fine plaquettes are small, but linearization over a
region of size L^t still needs L^t·κ small. The non-abelian (PA) is
therefore proved here only on the sub-event where the persistence region has
diameter <= c/κ, and (UB) is still needed. Both remain open in general.
