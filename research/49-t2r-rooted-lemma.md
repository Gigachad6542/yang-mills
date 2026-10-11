# (T2-R) from Balaban's domain factors: a rooted polymer lemma and a correction

Status:

- **Proved here.**
  - Lemma 1: a rooted Kotecký-Preiss bound for the probability that the
    polymer family contains polymers meeting prescribed sets.
  - Proposition 2: (T2-R) of note 39 follows from Lemma 1 and Balaban's
    domain factors CMP 122 II (1.79)-(1.89), with the rate a_eff below.
- **Correction to note 39 §6.** Persistence does **not** cost one
  large-field factor per level. Inside an unprocessed large-field domain,
  levels pass without new factors for up to K <= n_0 + R_j steps
  (CMP 122 II (1.83)). The correct rate is a_eff = c p_0(γ)²/(R(γ) + n_0 + 1),
  where R(γ) ~ (log γ^{-2})^r (CMP 119 p. 245). Since p_0(γ)² ~ (log γ^{-1})^{2p_0},
  a_eff -> ∞ as γ -> 0 provided 2p_0 > r.
- **Source check needed** [resolved, §5 and T71]. Balaban takes r >= 2
  (CMP 119 p. 245) and p_0 >= 5r (CMP 119 p. 246, text after (1.1)), so
  p_0 >= 10. The inequality 2p_0 > r holds for this choice.

## 1. The structure being used (CMP 122 II §1)

At scale k + t, the R-modified density has the representation (1.104).
There is a small-field action outside the large-field region, plus large
field domains Y_i carrying operations T_k(Y_i) and boundary terms. The
history of a domain Z is recorded by the accumulated exponent κ_j(Z), with
the fundamental bound T_k(X)1 <= exp(-2(1+β_0)^{-1} p_0(g_k) - κ d_k(X))
((1.89) and the remark after it). By (1.85):

- each **new** large-field region Z^{(j+1)} created at step j+1 adds
  γ_0 A p_0²(g_{j+1})(d'_{j+1}(Z^{(j+1)}) + 1) + 2p_0(g_{j+1}) to κ;
- a domain carried along by Z = S(Z_0), with **no new large fields**,
  satisfies κ_{j+1}(Z) = κ_j(Z_0) - O(1) M^d R^d d'_{j+1}(Z) (1.83). It gets
  no new factor;
- a domain is carried for at most K steps, until S^K(Z) satisfies
  conditions (i)-(ii) (size <= 100MR and no new large fields for N = R_j
  steps). By (1.81), K <= n_0 + R_j. Then the R-operation processes it.

## 2. Lemma 1 (rooted Kotecký-Preiss bound)

Let a polymer gas have activities w(γ) (possibly complex), compatibility
being disjointness, and suppose the KP condition holds:
Σ_{γ' ≁ γ} |w(γ')| e^{a(γ')} <= a(γ). Let S_1, ..., S_n be sets, and let E
be the event "for each i some polymer of the family meets S_i". Then

    |Z_E|/Z <= Σ_{(γ_1,...,γ_q)} Π_l |w(γ_l)| e^{a(γ_l)},

where the sum runs over families of distinct polymers that together meet
every S_i, and q <= n.

*Proof.* Expand Z_E: choose for each S_i one polymer of the family meeting
it. A family is counted at least once. The distinct chosen polymers
γ_1, ..., γ_q are pairwise compatible, and the rest of the family is a
compatible family avoiding them. So
|Z_E| <= Σ Π|w(γ_l)| · Z(compatible with all γ_l). Finally,
Z(compatible with γ_1..γ_q)/Z <= Π_l e^{a(γ_l)}. This is the standard
consequence of the KP condition via the cluster expansion of
log Z - log Z_{\{γ_l\}^c}. ∎

## 3. Proposition 2 ((T2-R) with the corrected rate)

Let E_t(Λ) be the persistence event of note 39 §1 (block variables near Λ
non-small at levels k, ..., k+t). Assume Balaban's final representation
satisfies the KP condition with a(Y) = ½ κ d(Y) + 1 (§6; his convergent cluster
expansion, CMP 122 II §1-2). Then

    μ^R(E_t(Λ)) <= C exp(-a_eff (t+1)),   a_eff = (1/2) min_j γ_0 A p_0(g_{k+j})² / (n_0 + R_{k+j} + 1) - C'.

*Proof.*

1. *Where the event lives.* On E_t(Λ), at each level k+j the block
   variables near Λ are non-small. Either they lie in a newly created
   large-field region at step k+j, because the χ_{k+j} conditions fail
   there, or they lie inside an unprocessed domain carried from an earlier
   step.
2. *Counting new regions.* A carried domain stays unprocessed for at most
   n_0 + R_j steps (§1). After it is processed, non-smallness at a later
   level near Λ requires a new region. Hence among the t + 1 levels there
   are at least (t+1)/(n_0 + R + 1) creation steps near Λ.
3. *Activity bound.* The domains Y in the final representation that contain
   these creation regions carry, by (1.85), a factor
   exp(-γ_0 A p_0² (d' + 1)) for each creation, times entropy factors
   exp(O(1) M^d R^d d') absorbed for small γ (CMP 122 II (1.80)-(1.81)).
4. *Lemma 1.* Apply it with S_i = the level-(k+j_i) neighbourhoods of Λ at
   the creation steps. The KP weights e^{a(Y)} cost at most half of the
   exponent, times a factor e per polymer (absorbed into C). The geometric sum over domain shapes is controlled by the
   remaining e^{-½κ d(Y)}. ∎

## 4. Consequence for (P)

By note 39 §5 (Prop. 2) and §7b, (P) <= (T1\*) + (T2-R). Now:

- (T1\*) holds (note 39 §7b);
- (T2-R) holds with a_eff ~ c (log γ^{-1})^{2p_0}/(log γ^{-2})^r, by
  Proposition 2, given the KP condition of Balaban's final expansion.

Note 25 (4.1) needs L⁴e^{-a} < 1 with a = a_eff. This holds for small γ if
and only if 2p_0 > r, the source check listed above.

So (P) is reduced to two source facts: the KP form of Balaban's
convergence (his cluster expansion), and the inequality 2p_0 > r. Neither
is a new estimate.

## 5. Source check 2p_0 > r: resolved

- CMP 119, introduction (printed p. 244 [corrected from p. 243, T71]): the large-field threshold is
  |U(∂p) - 1| <= g_0 p_0(g_0), with "p_0(g_0) = A_0 (log g_0^{-2})^{p_0} with a
  positive integer p_0".
- CMP 119 p. 245: R_0 >= (log g_0^{-2})^r, r >= 2.
- Balaban's own induction needs the large-field factor
  γ_0 A p_0(g_j)² (d' + 1) to dominate the domain entropy
  O(1) M^d R_j^{d+1} d' (CMP 122 II (1.81)-(1.82); "this condition is
  satisfied for p_0 large, and g_1 sufficiently small"). With the forms above
  this requires 2p_0 > (d+1) r for small g. In particular 2p_0 > r.
- [T71, note 65 §6 item 6.] Balaban's actual choice is stated on CMP 119
  p. 246, text after (1.1): "in the first step we take ε_0 = g_0 p_0(g_0),
  p_0(g_0) = A_0(log g_0^{-2})^{p_0}, p_0 ≧ 5r" (the first of two choices,
  "the same as in [16]"); with r >= 2, p_0 >= 10. CMP 119 gives no reason for
  5r; the requirement 2p_0 > (d+1) r above is this note's inference from
  CMP 122 II (1.81)-(1.82), and p_0 >= 5r satisfies it for d = 3 and d = 4.
  At d = 3 it reads p_0 > 2r. Note also: at d = 3 with R = identity the
  persistence bounds (T2-R) of this note (d = 4, with the R-operation) are
  replaced by the single-scale question of note 65 §5 (Lemma 65.2, Prop. 65.4,
  target).

So a_eff ~ (log γ^{-2})^{2p_0 - r} -> ∞, and L⁴ e^{-a_eff} < 1 for small γ.
The remaining assumption of Proposition 2 is the KP form of Balaban's final
cluster expansion. That is how his convergence is proved (Mayer expansion
of the exponential, CMP 122 II after (1.89)), not a new estimate. (P) is
thereby reduced to published structure.

## 6. Source check: the KP form of Balaban's final expansion (T56)

CMP 122 II, after (1.89) (printed pp. 388-390).

- "The next step is a construction of an exponentiated cluster expansion
  for the expression in the curly bracket in (1.72). The first operation is
  the Mayer expansion of the exponential, the same as in (7.1) [I]."
- The activities obey (1.92)-(1.97). The final bound (1.97) has the form

      |activity(X')| <= c_1 exp(-(1 + β) κ d_k(X')),

  with c_1 = exp(-p_0(g_k)) when X' meets no large-field region Y_h, and
  c_1 = α_1^{1/3} otherwise. Balaban states: "The estimate (1.97) is
  sufficient for convergence of the exponentiated cluster expansion".
- He then gets {...} = exp Σ_X R'^{(k)}(X) ((1.98)), "given by the
  convergent series (7.13) [I]", with |R'^{(k)}(X)| <= O(1) c_1
  exp(-(1 + β/2) κ d_k(X)) ((1.99)).

*KP condition.* The localization domains are connected unions of cubes. So
the number containing a given cube, with d_k(X) = n, is at most e^{c_d n}
(n = 0 for a single cube, if d_k is the length of a minimal connecting
tree). Hence, with a(X) = ½ κ d_k(X) + 1,

    Σ_{X ∋ □} |activity(X)| e^{a(X)} <= e c_1 Σ_{n>=0} e^{c_d n - (½ + β) κ n} <= 2e c_1,

which is <= 1 <= a(□) once κ >= 4 c_d and c_1 <= 1/(2e); for a polymer of
|X| cubes the incompatible sum is <= |X| <= ½κ d_k(X) + 1 (d_k(X) >= |X| - 1,
κ >= 2). The condition c_1 <= 1/(2e) holds for c_1 = exp(-p_0(g_k)), and for
c_1 = α_1^{1/3} it asks α_1 <= (2e)^{-3}; Balaban takes α_1 small. So his
expansion satisfies the KP condition with a(X) = ½ κ d(X) + 1; the extra
constant costs a factor e per polymer in Lemma 1 and Proposition 2, which
only changes C. [Audit 2026-10-09, T82: the earlier "<= a(□) = ½κ ... c_1 <= 1"
needed d_k(□) >= 1 and dropped the n = 0 term.]

*Status.* The last open source item for (P) is now a reading of CMP 122 II,
(1.97)-(1.99), plus a standard counting step. Assembling the per-step
exponentiated expansions into the multi-scale final density (CMP 122 III,
(2.18)) is the structure note 39 §6 already uses. It is not re-derived here.
