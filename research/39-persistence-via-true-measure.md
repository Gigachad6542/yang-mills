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

### 5a. An exact reduction of (T1\*) (proved)

Write the old summand as p = q · e^{-g_k^{-2} D(W) - O(W)} times factors
independent of W, where:

- D := A(full) - A(ζ_i, ·) >= 0 is the Wilson action weighted by 1 - ζ_i;
- O collects the non-Wilson terms.

Then:

    p̂/q̂ (W) = e^{-g_k^{-2} D(W) - O(W)} / E_q̂[e^{-g_k^{-2} D - O}]
             <= exp( 2 sup_W |O| + g_k^{-2} (sup_W D - inf_W D) ).

Hence (T1\*) holds as soon as

    sup_W |O(W)| + g_k^{-2} osc_W D(W) <= C N_λ log g_k^{-2}.   (5.1)

*Source check (CMP 122 I (1.100)-(1.101)).*

- ζ_i rises from 0 to 1 in a neighborhood of ∂X_i^{-2}.
- The fiber variables sit in Λ_i ⊂ X_i, with |V'(b) - 1| <= M_0 ε_k there.
- W enters D only through the minimal configuration U_{k,X_i}(V'V_{Λ_i})
  in the boundary layer. By the decay of δℋ/δB (CMP 102b (190); note 36),
  that dependence is about e^{-δ dist(Λ_i, ∂X_i)} M_0 ε_k.

So g_k^{-2} osc_W D is roughly g_k^{-2} e^{-δ dist} M_0 ε_k × (layer
volume) × (layer field size), with ε_k/g_k² = p(g_k)/g_k. Condition (5.1)
therefore needs dist(Λ_i, ∂X_i) >~ δ^{-1} log(1/g_k). With Balaban's fixed
M, R it is not automatic. Balaban treats the corresponding terms in
CMP 122 II (1.14)-(1.37) and states that they are small. Whether that
treatment yields (5.1) is the remaining check. It is a finite question about
the sizes in CMP 122 II §1.

*Source status of the distance.* The components X_i carry layers of
MR_k-cubes, and ζ_i is localized at depth about 8MR_k from the fiber
support (CMP 122 II p. 364: "the distance is larger than 8MR_k, hence ... the
additional exponential factor exp(-δ8MR_k)"). Balaban says this factor
"suppresses all powers of log g_k^{-2}, and all powers of M" (CMP 122 II
p. 360). Condition (5.1) needs more: e^{-8δMR_k} p(g_k)/g_k = O(1), that is,
R_k >= (8δM)^{-1} log(p(g_k)/g_k). Whether Balaban's R_k grows that fast
(like log g_k^{-1}) or only like a power of log log g_k^{-1} could not be
settled from the OCR text here. The definition of R_k (CMP 119 §1 or
CMP 116) is the one remaining source fact for (T1\*). If R_k grows more
slowly, the R'-template would have to be built on a slightly larger region
(R_k ~ log g_k^{-1}). The entropy cost of that is O(log g_k^{-1}) per
label, which the label's large-field factor exp(-γ_0 p_0(g_k)²) still
absorbs.

## 6. (T2-R) from CMP 122 II (1.73)-(1.81)

CMP 122 II p. 380 states: "All the expressions in the definition (1.71), for
the configuration U, are real, and the exponential density in the integral
is positive." From this, (1.73)-(1.75) give, for any function F of the
integration variables,

    |T_k(X, (U, J)) F| <= e^{3 sup|σ|} sup|F| · T_k(X, (U, 0)) 1,   (6.1)

where σ is the small first-order term. Then (1.79)-(1.81) bound
T_k(X, (U, 0))1 by the product of the per-scale large-field factors
exp(-γ_0 p_0(g_j)² ...) with entropy factors exp O(1)(MR_j)^{-d}|Z_j| (all
volumes at the scale of the step).

**Marking.** Write 1_{E_t(Λ)} = Π_{j=0}^{t} 1_{E^{(j)}}, where E^{(j)} is the
event that a level-(k+j) plaquette near Λ is non-small. The indicator
1_{E^{(j)}} is a function of the integration variables of the scale-(k+j)
operation, and sup 1_{E^{(j)}} = 1, so it can be inserted as F in (6.1).
On E^{(j)} every term with small-field χ near Λ at that scale vanishes.
Hence each marked step carries at least one large-field factor near Λ, with
entropy O(1) level-(k+j) cubes. That is (T2-R), with
a = γ_0 min_j p_0(g_{k+j})² - O(1).

**Status.** The per-step inequality (6.1) and the factors (1.79)-(1.81)
are published. The marking itself is not printed. Two things are needed
and not written out:

- carrying the fixed-Λ markers through the localization and exponentiation
  that follow each step;
- the ratio to the unmarked normalization Z.

Both are the same bookkeeping Balaban does for unmarked large-field
regions. So (T2-R) is "published mechanism, unprinted bookkeeping".

*Correction (note 49).* "Each marked step carries at least one large-field
factor" is too strong. Inside an unprocessed large-field domain, levels
pass with no new factor for up to K <= n_0 + R_j steps (CMP 122 II (1.83)).
The correct rate is a_eff ~ c p_0(γ)²/(R(γ) + n_0 + 1). This still diverges
as γ -> 0 if 2p_0 > r. Note 49 gives the rooted polymer lemma and the
corrected Proposition.

## 7. Net status of (P)

(P) ⇐ (T1\*) + (T2-R).

- (T2-R): CMP 122 II (6.1) and (1.79)-(1.81) with markers. Bookkeeping
  only.
- (T1\*): reduced exactly (§5a) to the oscillation bound (5.1). That needs
  R_k >~ log(1/g_k), or a template built on a slightly larger region. One
  source fact (the growth of R_k) is unresolved.

The deterministic notes 34-37 are therefore **not** on the critical path
for (P). They give an independent, action-based mechanism and remain useful
for proving (T2-R) in other RG schemes.

### 7a. The growth of R_k (partial resolution)

Dimock's exposition of Balaban's large-field method (Dimock-Balaban RG II,
arXiv:1212.5562, eqs. (147)-(148)) defines the separation parameters as

    r_k = (-log λ_k)^r,   r a positive integer,

and requires the large-field regions Λ_j, Ω_j to be separated by
5[r_j] L^{-(k-j)} M.

If Balaban's R_k for Yang-Mills has the same form, R_k = (log g_k^{-2})^r,
then condition (5.1), R_k >= (8δM)^{-1} log(p(g_k)/g_k):

- holds automatically for small g_k if r >= 2;
- holds for r = 1 when 16δM > 1 (Balaban's M is a large constant).

This form is also consistent with Balaban's remark that exp(-½δMR_k)
"suppresses all powers of log g_k^{-2}" (CMP 122 II p. 360). The exact
definition of R_k in the CMP 109-122 series was not located in the OCR text
of this repository. So (T1\*) is **conditional on R_k having this form**,
which the parallel construction in Dimock's exposition supports.

### 7b. The growth of R_k: resolved

CMP 119, printed p. 245 (OCR `sources/ocr/cmp119.md`, line 46): "R_0 is the
smallest power of L such that R_0 >= (log g_0^{-2})^r, r >= 2". The k-th
step uses R_k defined the same way from g_k. That is why exp(-½δMR_k)
"suppresses all powers of log g_k^{-2}" (CMP 122 II p. 360).

With R_k >= (log g_k^{-2})^r and r >= 2,

    e^{-8δMR_k} p(g_k)/g_k <= exp(-8δM (log g_k^{-2})² + log g_k^{-1} + p_0 log log g_k^{-1}) -> 0,

so condition (5.1) holds for all small g_k. **(T1\*) therefore holds**,
given the exact reduction of §5a, Balaban's bounds on the non-Wilson terms
(CMP 122 II p. 381), and the decay of δℋ/δB used in §5a, which is
CMP 102b (190), a bound whose proof Balaban omits (notes 54 §4, 61 §6b.1,
63). [Audit 2026-10-09, T82: this dependence was not stated here.] The parallel construction in Dimock's exposition (§7a) is consistent
with this. Status of (P): (P) <= (T2-R), whose only gap is the unprinted
marker bookkeeping of §6.
