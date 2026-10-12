# Non-abelian (PA) on the ε_0-small event, from fiber convexity and minimizer regularity

Status:

- **Proved here.**
  - Lemma 1: an exact plaquette-angle inequality for a field written as a
    minimizer times a fluctuation, with C_F = 4. It uses only the
    bi-invariance of the metric on SU(2).
  - Lemma 2: exact telescoping of the minimal effective actions
    (dynamic programming).
  - Theorem 3 (chain lemma): on the event that every image plaquette near
    the persistence region is below a fixed ε_0, the non-abelian (PA) of
    note 26 holds with c_L = c η²/(C_F²(R+1)), where R = ⌈log(ε_0/ε_min)/log ρ_L⌉,
    **assuming** two variational inputs, (D1) and (D2).
- **Conditional reduction.**
  - Non-abelian (PA) on the ε_0-small event ⇐ (D1) uniform fiber strong
    convexity + (D2) minimizer regularity.
  - The resulting rate a ≈ c p(γ)² log ρ_L / log(1/γ) still satisfies
    L⁴e^{-a} < 1 for small γ, because p(γ)² = b_0²(1 + log γ^{-1})^{2p_0}
    with p_0 > 2.
- **Open.**
  - (D1) and (D2) as stated: local, uniform in the level. Both are
    variational statements of Balaban's type (CMP 102b), but they are not
    proved here.
  - The ε_0-large event: some image plaquette near the region exceeds ε_0
    at some level <= t + R.

Unlike note 26 §7, the argument needs **no linearization over the
persistence region**. So the restriction "diameter <= c/κ" mentioned there
disappears. Near-orthogonality of the abelian kernels is replaced by
telescoping (Lemma 2) and a pigeonhole on chains (Theorem 3).

## 1. Setting

Write level j for scale k + j. U_j is the level-j image of the scale-k field
U, so U_0 = U and U_{j+1} = C U_j, where C is Balaban's one-level average
(CMP 109 (0.4)). For a level-j plaquette p, ϑ_j(p) is the angle of U_j(∂p),
that is, its distance to 1 in the bi-invariant metric d(x, y) = |log(x^{-1}y)|
on SU(2). ϑ_j(p) is gauge invariant.

**Minimal effective actions.** Put

    S_0 := A_k (scale-k Wilson action),
    S_j(W) := min{ A_k(U) : U_j = W }.

**Persistence (note 26).** For j = 1, ..., t there is a level-j plaquette
p_j within distance C L^j of Λ (in scale-k units) with ϑ_j(p_j) >= ε_j, where
ε_j := ε_{k+j} = g_{k+j} p(g_{k+j}).

**ε_0-small event E_0.** Every level-j plaquette within distance
C_E L^j log(1/ε_min) of Λ has ϑ_j <= ε_0, for 0 <= j <= t + R (R as below).
Here ε_0 is a fixed small constant at which Balaban's variational theory
applies.

## 2. Two inputs (not proved here)

**(D1) Fiber convexity.** On E_0, for every level j, each level-j field W
can be written in some gauge as W = W^min(CW) e^{iφ_j}. Here W^min(V) is
the minimizer of S_j on the fiber {W : CW = V}, and

    S_j(W) >= S_{j+1}(CW) + c_1 |φ_j|_∞²,

with c_1 > 0 independent of j, k and L.

The point is the 4D scale invariance: a level-j angle θ costs about θ²
fine action at every level, so no factor L^{±j} appears. Balaban's positivity
of the local quadratic form (CMP 102b Thm. 1; CMP 102 (71)), which note 26
§1 cites for the large-field factors, is this statement at one level for
the fine action.

**(D2) Minimizer regularity.** On E_0, for every level-j plaquette p,

    ϑ(W^min(V)(∂p)) <= C_I L^{-2} sup_{p'} e^{-δ dist_{j+1}(p, p')} ϑ_{j+1}(p'),

where the sup runs over level-(j+1) plaquettes and C_I and δ are independent
of j. This is "the minimizer is smooth on the coarse scale, with fine
curvature equal to coarse curvature over L²". Note 33 §1 uses the same
input.

## 3. Lemmas

**Lemma 1 (plaquette angle of a perturbed field).** For any field W^min and
fluctuation φ,

    ϑ(W^min e^{iφ}(∂p)) <= ϑ(W^min(∂p)) + Σ_{b∈∂p} |φ_b| <= ϑ(W^min(∂p)) + 4|φ|_∞.

*Proof.* The metric is bi-invariant. Hence
d(A e^{iφ} B, AB) = d(e^{iφ}B, B) = d(e^{iφ}, 1) = |φ|. Insert the four
factors one at a time and use the triangle inequality. ∎

**Lemma 2 (exact telescoping).** For every scale-k field U and every t,

    A_k(U) >= S_t(U_t) + Σ_{j<t} (S_j(U_j) - S_{j+1}(U_{j+1})),

with equality, and each bracket is >= 0. Under (D1), on E_0,

    A_k(U) >= c_1 Σ_{j<t} |φ_j|_∞².

*Proof.*

1. S_0(U_0) = A_k(U), and the sum telescopes.
2. The minimization defining S_{j+1} can be done in two stages. A field
   with level-(j+1) image V has some level-j image W with CW = V, so
   S_{j+1}(V) = min{S_j(W) : CW = V}. Hence each bracket is >= 0.
3. S_t >= 0. Apply (D1) to each bracket. ∎

## 4. The chain lemma

Put C_F := 4 and s_L := C_I L^{-2}, the sup-to-sup norm of the one-level minimizer
image map. Fix η ∈ (0, 1) and put ρ_L := (1-η)/s_L. Assume ρ_L > 1, that is,
s_L < 1 - η. The abelian computation of note 35 gives s_L ≈ 1.6, 1.1, 0.77,
0.55 for L = 2, 3, 4, 5, so this assumption holds for L >= 4 and fails for
L <= 3 (§5, item 4). [T53 (note 35 §5): these are far-corner rows; for
L >= 3 larger rows exist (n0 = 6: 1.258, 0.881, 0.675 for L = 3, 4, 5), so
with the depth growth L = 4 gives about 0.97-1.01 and s_L < 1 is suggested
only for L >= 5; all are lower bounds (audit, T82).]
Let ε_min := min_{j<=t} ε_j and R := ⌈log(ε_0/ε_min)/log ρ_L⌉.

**Theorem 3.** Assume (D1), (D2) and the event E_0. If U is persistent on
levels 1, ..., t, then

    g_k^{-2} A_k(U) >= (c_1 η²/(C_F²(R+1))) Σ_{j=1}^t ε_j²/g_{k+j}².

This is (PA) of note 26 with c_L = c_1 η²/(C_F²(R+1)).

*Proof.*

1. *Dichotomy at one level.* Let q be a level-j plaquette with
   ϑ_j(q) =: α >= ε_j. By Lemma 1 applied with W = U_j, and then (D2),

       α <= s_L sup_{p'} e^{-δ dist(q,p')} ϑ_{j+1}(p') + C_F |φ_j|_∞.

   So one of the following holds:
   - (G) |φ_j|_∞ >= ηα/C_F >= ηε_j/C_F;
   - (N) some level-(j+1) plaquette p' has
     ϑ_{j+1}(p') >= ((1-η)α/s_L) e^{δ dist(q,p')} >= ρ_L α.
2. *Chains.* Start from the persistence witness p_j. While (N) holds, move
   to the plaquette p' it provides and repeat at the next level, with α
   replaced by the new angle. After r consecutive (N) steps the angle is at
   least ρ_L^r ε_j. On E_0 every angle is <= ε_0, so r <= R. Since
   e^{δ dist} <= ε_0/ε_min, each step moves O(log(1/ε_min)) level units, so
   the chain stays inside the region of E_0.
3. So for each j ∈ {1, ..., t} there is a level σ(j) ∈ [j, j + R] at which
   (G) holds with |φ_{σ(j)}|_∞ >= ηε_j/C_F. The angle only grows along the
   chain, so the threshold ε_j is kept.
4. *Pigeonhole.* Each level i equals σ(j) for at most R + 1 values of j.
   Hence

       |φ_i|_∞² >= max_{σ(j)=i} η²ε_j²/C_F² >= (1/(R+1)) Σ_{σ(j)=i} η²ε_j²/C_F²,

   and summing over i gives
   Σ_i |φ_i|_∞² >= η² Σ_{j=1}^t ε_j² / (C_F²(R+1)).
5. *Action.* By Lemma 2 (with t + R in place of t),
   A_k(U) >= c_1 Σ_i |φ_i|_∞². Multiply by g_k^{-2} and use g_k <= g_{k+j}
   (the coupling grows toward the infrared). ∎

**Rate.** By note 26 Prop. 1, with ε_j²/g_{k+j}² = p(g_{k+j})²,

    a = (1-δ) c_L min_j p(g_{k+j})² - C'
      ≈ (1-δ) (c_1 η²/C_F²) p(γ)² log ρ_L / log(ε_0/(γ p(γ))).

Since p(γ)² = b_0²(1 + log γ^{-1})^{2p_0} with p_0 > 2, a grows like
(log γ^{-1})^{2p_0 - 1}. So L⁴e^{-a} < 1 for small γ. The loss of
log(1/γ) relative to the abelian Prop. 2 of note 26 is the price of not
linearizing. It is harmless.

## 5. Checks and limits

1. *Abelian case.* In the abelian, quadratic theory:
   - (D1) is exact Pythagoras: the fine minimizer on a fiber is an
     orthogonal projection, so S_j(W) = S_{j+1}(CW) + Q_j(φ_j), with Q_j
     uniformly equivalent to the standard form.
   - (D2) is the smoothness of Balaban's linear interpolation kernels
     (CMP 95/96).

   Both reduce to Balaban's uniform bounds for the linear theory: the
   uniform positivity of Q_j on fiber directions, and kernel decay. Theorem
   3 then gives a weaker constant than note 26 Prop. 2 (which has no R and
   needs no such input), but the same linear growth in t.
2. *The ε_0-large event.* If some level-i plaquette near Λ exceeds ε_0 with
   i <= t + R, the chain argument stops at level i. Two facts are available:
   - levels below i - R are still covered by Theorem 3;
   - level i carries a fixed amount of action, ε_0² in level-i units.

   But a single cost ε_0²/g_k² does not dominate t p(γ)² when t is
   comparable to the depth m, since 1/g_k² ~ β_* m. Covering this event
   needs either a localized action count per large level, or Balaban's own
   large-field factor exp(-c ε_0²/g²) at each such level. The second is a
   statement about the density, i.e. the (UB) side of note 26. This is the
   remaining gap in (PA).
3. *Localization.* Lemma 2 bounds the total action A_k(U). (UB) of note 26
   is stated for a region N disjoint from the other large-field regions.
   Matching them needs (D1) in a local form, with the action restricted to
   a neighborhood of the chain. That neighborhood is C L^j log(1/ε_min) at
   level j, which is the region used in E_0.

4. *The size of s_L (note 35).* In the abelian 4D theory (D2) holds exactly,
   and its best sup-norm constant was computed by linear programming.
   - The worst rows are the far-corner children: s_L ≈ 1.54, 1.12, 0.77,
     0.55 for L = 2, 3, 4, 5 at one level. These are lower bounds on the
     maximum over rows, on a 6⁴ coarse torus.
   - At L = 2, s_L grows with the depth: 1.54, 1.63, 1.69 for m = 1, 2, 3,
     with shrinking increments.

   The reason s_L is not O(L^{-2}): coarse flux patterns that oscillate at
   the block scale are suppressed by the averaging kernel, so the minimizer
   that reproduces them must have larger fine fluxes. So the "coarse
   curvature over L²" reading of (D2) is wrong in the sup norm; only s_L < 1
   is available, and only for L >= 4 [T53: suggested only for L >= 5, see
   note 35 §5; not established for any L]. Theorem 3 needs exactly that. With
   L = 2 or 3 the chain argument fails, and an energy (ℓ²) form of (D2)
   would be needed.

## 6. Net effect on (P)

(P) ⇐ (PA) + (UB-ms) (note 26 Prop. 1 as corrected by note 38). With this note:

- (PA) on E_0 ⇐ (D1) + (D2), which are uniform variational properties of
  Balaban's minimizers;
- (PA) off E_0 is handled by note 37 under (SER).

The deterministic part of (P) therefore no longer needs any new idea beyond
Balaban's variational theory, applied uniformly across levels.
