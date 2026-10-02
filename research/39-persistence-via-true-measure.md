# (P) from a marked large-field bound for the true measure

Status: **conditional reduction** (T31). **See §5:** (T1) as first stated is
too strong, because the exterior law is R-modified. The repaired route is
(T1\*) + (T2-R).

- **Proved here.** Proposition 1: (P) of note 25 (4.1) follows from two
  hypotheses.
  - (T1) Label domination: the pre-replacement R'-summands at scale k are
    nonnegative, and their sum is dominated by Balaban's scale-k density.
    That density is equivalent to the true measure on gauge-invariant
    functions of the scale-k block variables.
  - (T2) A marked large-field bound for the true measure: the probability
    that the block images near a fixed region are non-small at levels
    k, k+1, ..., k+t is at most C w_k e^{-at}, with w_k = exp(-c p(g_k)²)
    and a = c p(γ)² - C'.
- **Consequences.**
  - On this route (P) needs neither (PA) nor (SER) nor (UB-ms). Persistence
    **is** a sequence of Balaban large-field events, and their suppression
    is Balaban's own per-scale factor.
  - This bypasses the entropy obstruction of note 38. The per-scale
    integration pays entropy O(1) per level-j cube.
  - It replaces "transfer from R-modified to pre-replacement labels"
    (note 26 §2) by two cleaner statements: a positivity statement about
    labels (T1) and a statement about the true measure (T2).
- **Open.** (T1) and (T2).
  - (T2) is the "marked form" of Balaban's large-field factors that note 25
    §4 already identified as unpublished. It is now formulated for the
    **true measure**, independently of the R-operation's labels.
  - (T1) is a bookkeeping statement about notes 20 and 25.
- **Role of notes 34-37.** They become an alternative: they derive per-level
  suppression from the Wilson action deterministically. That is what one
  needs if (T2) is to be proved from positivity of the action in each level's
  integration, which is how Balaban obtains his factors (CMP 122 II p. 380,
  Theorem 1 of CMP 102b, (71) of CMP 102). So they remain the deterministic
  core of a proof of (T2).

## 1. The event

Fix a placement Λ at scale k. Let E_t(Λ) be the event that for each
j = 0, 1, ..., t some level-(k+j) block-variable plaquette within C L^j of Λ
(in scale-k units) has angle >= ε_{k+j} = g_{k+j} p(g_{k+j}).

Properties:

- E_t(Λ) is gauge invariant.
- It is measurable with respect to the block variables at levels >= k.
- On E_t(Λ), Balaban's small-field characteristic function χ_{k+j} vanishes
  near Λ for every j <= t. So every term of Balaban's history expansion that
  is nonzero on E_t(Λ) has a large-field region at each of these scales
  near Λ.

The persistence event of note 25, t(W) >= t, is exactly E_t(Λ) for the
label's region Λ, evaluated at the label's fiber and exterior. The level-0
part of E_t is the label's own large-field condition.

## 2. Hypotheses

**(T1) Label domination.** For each depth m and each terminal block,

    Σ_{placements} Σ_{labels λ at Λ} ∫ ν(dV_c) p_λ(W, V_c) 1{E_t(Λ)} dW
        <= C_1 Σ_{placements} μ_k(E_t(Λ)),

where μ_k is Balaban's scale-k density, normalized. On gauge-invariant
events of block variables it gives the same probabilities as the true
measure (the reverse Faddeev-Popov equivalence, CMP 122 II §1, discussion before (1.71)).

Note 20 states that the fully resolved pre-localization R'-summands are
positive. (T1) additionally asks that they do not over-count, i.e. that they
form a sub-decomposition of the density at that stage up to a constant C_1.

**(T2) Marked large-field bound.** For the true measure μ and every Λ,

    μ(E_t(Λ)) <= C_2 exp(-c Σ_{j=0}^{t} p(g_{k+j})²) e^{C_3 (t+1)}.

Here the e^{C_3} per level is the entropy of choosing the level-(k+j)
large-field region near Λ among O(1) level-(k+j) cubes.

**Why (T2) is natural.** Insert the indicator 1_{E_t(Λ)} into the
partition function and run Balaban's procedure.

1. At step k+j the indicator forces 1 - χ_{k+j} near Λ.
2. The large-field factor exp(-γ_0 p_0(g_{k+j})²) comes from positivity of
   the Wilson action in that step's integration (CMP 122 II p. 380), and
   the indicator is nonnegative and bounded by 1.
3. Large-field regions are treated by bounds, not by analytic expansion,
   so the indicator, which depends only on large-field-region variables,
   does not interfere with analyticity.
4. The ratio Z_E/Z is controlled by the same convergent expansion that
   controls Z (CMP 122 II Theorem 1, bounds (1.79)-(1.81)).

None of this is printed for an inserted indicator. That is why (T2) is a
hypothesis. Note that this indicator is at fixed Λ and has multi-scale
support, unlike the uniform χ decompositions Balaban uses.

## 3. Proposition 1

**Proposition 1.** (T1) and (T2) imply (P) of note 25 (4.1):

    M_{m,t} <= C w_m L^{4m} e^{-at},   w_m = exp(-c p(g_k)²),
    a = c min_j p(g_{k+j})² - C_3.

*Proof.* By definition M_{m,t} is at most the left side of (T1) with
E_t(Λ). Apply (T1). The number of placements per terminal block is L^{4m}.
Apply (T2) to each placement, and split off the j = 0 factor as w_m. ∎

Because p(g)² grows like (log g^{-1})^{2p_0}, the condition L⁴e^{-a} < 1
holds for small γ.

## 4. Revised map of (P)

There are two routes to (P):

- **(A)** (T1) + (T2). This is the shortest route. It is a statement about
  the true measure plus label bookkeeping.
- **(B)** (PA) [notes 34-37: (D1), (D2) published-input derivations, plus
  (SER)] + (UB-ms) [note 38].

Route B gives an independent deterministic mechanism. It is the natural way
to **prove** (T2), since (UB-ms) applied to the true measure is (T2) with
the per-level cost of note 37 Theorem 3.

The recommended next step is to settle (T1) from notes 20 and 25 and from
CMP 122 I §1. That is a definite, finite check of positivity and counting.

## 5. Correction to (T1), and the repaired route (A')

**(T1) as stated is too strong.** In note 25 the exterior measure ν of a
label at scale k is Balaban's scale-k density, and that density is
R-modified at earlier scales. At every earlier R'-stage the fiber law inside
the replaced region was swapped for a template, keeping only the exterior
marginal (note 20 (1.4)). The law of block variables near earlier replaced
regions therefore differs from the true law. Domination by the true measure
μ cannot be expected label by label.

**Repaired route (A').** Use the label's own replacement instead.

**(T1\*) Fiber-law comparison.** Let N_λ be the number of scale-k
MR-cubes in the label's domain. For every label λ and a.e. V_c,

    sup_W p̂_λ(W | V_c) / q̂_λ(W | V_c) <= exp(C N_λ log g_k^{-2}).

Here q̂_λ = (normalized graph average of q_i/Q_i), from note 20 (3.3)-(3.5).

**Why (T1\*) is plausible.**

1. q_i in (3.4) carries exp(-g_k^{-2} A(ζ_i, U_{k,X_i})), the Wilson action
   localized by the cutoff ζ_i <= 1. The old summand carries the full
   Wilson action.
2. Every Wilson plaquette term 1 - Re tr U_p is >= 0 for G-valued fields,
   so A(full) >= A(ζ_i, ·) pointwise.
3. The W-dependent part of A(full) - A(ζ_i, ·) is supported on the boundary
   layer where ζ_i < 1. If W does not enter there, this part cancels
   between p̂ and the conditional normalization, and only the
   non-Wilson terms remain.
4. The non-Wilson terms are boundary terms, R-terms and normalizations.
   They are bounded by O(1) per MR-cube, plus O(log g_k^{-2}) per cube for
   normalizations (CMP 122 II p. 381).
5. The factor exp(C N_λ log g_k^{-2}) is absorbed by the label's own
   large-field factor exp(-γ_0 p_0(g_k)² N_λ), since p_0(g)² is much larger
   than log g^{-2}.

**(T2-R) Marked bound for the R-modified expansion.** In Balaban's
R-modified history expansion from scale k on, the mass of histories whose
block variables near Λ are non-small at levels k+1, ..., k+t is at most
C e^{-at} times the unmarked mass. Note 26 §1 records that the per-scale
factors exist for exactly these history terms. What is missing is the
marking (an indicator at fixed Λ), and as in §2 this is natural.

**Proposition 2.** (T1\*) and (T2-R) imply (P).

*Proof.* M_{m,t} = Σ ∫ν C_λ p̂_λ(E). By (T1\*),
p̂_λ(E) <= e^{C N_λ log g_k^{-2}} q̂_λ(E). Then
∫ν C_λ q̂_λ(E) is the mass of E for the post-replacement label, which is
part of the R-modified expansion. Apply (T2-R) and the placement count
L^{4m}. Absorb e^{C N_λ log g_k^{-2}} into w_m. ∎

**Status after this correction.**

- (P) ⇐ (T1\*) + (T2-R) (route A'), or (P) ⇐ (PA) + (UB-ms) (route B).
- (T1\*) is a local, single-label statement on O(1) volume, so there is no
  entropy issue. It needs only a check that W does not enter the boundary
  layer of ζ_i in CMP 122 I (1.100), together with Balaban's term bounds.
- Route A (T1 with the true measure) is withdrawn.
