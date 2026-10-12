# Large-field gas at d = 3, R = identity: the decay in (1.89) and the polymer representation (T84)

**One-line verdict.** (G2) is proved here at R = id (conditional reduction on the
printed geometry of II pp. 380-387 and the note 66 reading): for every λ,
T_k(Y)1 <= exp(−λ|Y|_M − c_*p_0²(g_k)) once x_K is large, under the single
strict exponent condition 2p_0 > (d+2)r (5r at d = 3; p_0 >= 5r gives margin
5r). (G1) is a conditional reduction: the gas, its compatibility
(disjoint supports containing the S-neighbourhoods of the large-field
domains), and the KP condition with a(Γ) = ½κd_k(Γ)+1 are written and checked,
giving |activity| <= C_q g_k^q e^{−κ d_k} for polymers containing a large-field
domain, resting on three readings not printed in II: (H-form), (H-C) and
(1.79) for the unprocessed T_k.

Status labels: **proved here (conditional)**: Prop. 68.1, Cor. 68.2, Lemma 68.3a,
Thm 68.4, Thm 68.5. **Published input**: the page-image statements (P1)-(P6) of
CMP 122 II pp. 376-392. **Conditional reduction / open**: (R-id), (H-form),
(H-loc), (H-C); (1.79) at R = id.

Script: `research/scripts/t84_surplus_checks.py` (+ `.out`).

## 0. The task, in the notation of this note

At d = 3 with R = identity, note 66 found that CMP 122 II gives each persisting
large-field domain Y the weight T_k(Y)1 <= exp(-2p_0(g_k) - κ_k(Y)) ((1.89)),
with two gaps:

- (G1) CMP 122 II writes no polymer representation of the large-field-domain
  gas at R = identity (only the R-operation's output (1.103)-(1.104));
- (G2) the extra decay -κ_1 d_k(X) in (1.89) for arbitrary regions is
  asserted on p. 387, not proved.

Plan: §2 proves (G2) from the induction (1.80)-(1.88) read at R = identity;
§3-§4 write the gas and check KP; §5 gives the form note 61 needs and names
what is assumed (no step was found to fail); §6 lists script results,
corrections for the lead, and what was not checked.

**Notation.** The integer exponent of CMP 119 (1.1) is p_0 (so p_0 >= 5r,
CMP 119 p. 246); the function of II is P_j := p_0(g_j) = x_j^{p_0}, with
x_j := log g_j^{-2} (A_0 pulled out, as in note 66 §0; keeping A_0 only
rescales constants). 3D flow (CMP 109 p. 259): g_j² = g² L^{j-K}, so
x_j = x_K + (K-j) ln L decreases in j, K = K_end is the unit lattice, and
P_j decreases in j. R_j is the smallest power of L with R_j >= x_j^r.
Cubes: "M-cube" and "MR_j-cube" are the cubes of the scale-j lattice used in
II; V_n(W) := |W| M^{-d} (in scale-n lattice units) is the number of M-cubes
of a union W of cubes; d'_n(W) is the linear size in MR_n-cubes (II p. 380),
d_k(Y) the linear size in M-cubes ((1.67): M^{-1} times the length of a
shortest tree in Y meeting all M-cubes of Y).

## 1. Inputs and readings used

**Published inputs from CMP 122 II (page images, printed pp. 380-387 and
376-379, 390-392, reread for this note).**

- (P1) The definition of κ_j(Z) by (1.83) (no new large field, Z = S(Z_0)) and
  by (1.85) (merge or creation), p. 385-386, with one constant c_E for
  "O(1)M^dR_n^{d+1}d'_n" throughout (p. 380; the passage (1.83) => (1.80) at
  j+1 uses the same constant), and the identification of exp(-κ_j(Z) -
  2p_0(g_{j(Z)})) with the factor of (1.79) connected with the component Z
  (p. 384). Creation weight: p. 381 gives the fundamental factor
  exp(-½γ_0A_1²p_0²(g_j)(d'_j(Z_j^(i))+1) - 2p_0(g_j)); (1.85) prints γ_0A_1²
  (no ½). I use c_0 := ½γ_0A_1² (the value p. 381 supports, and the one
  (1.82) is derived with: ¼γ_0 14^{-d}A_1² = c_0/(2·14^d)). Only c_0 > 0
  matters below.
- (P2) (1.76), (1.84): the covering of a new component by S(old components)
  and (new regions)^{~2}; the graph G on these domains is connected; the
  tree-graph induction of p. 386-387.
- (P3) Geometry p. 384-385: S(Z) = Z'^{~10} (cover by LMR_{j+1}-cubes, then ten
  layers), S(A ∪ B) = S(A) ∪ S(B), S monotone; L_{n-j} < 63; for n > j,
  d'_n(S^{n-j}(Z)) <= 3(126)^d 2^{-(n-j)} d'_j(Z) as long as the cover
  Z^{(n-j)} has linear size > 0, and <= 64^d otherwise ((1.81), first two
  lines). I use only the consequence
  **(Gm-S)** d'_n(S^{n-j}(Z)) <= C_S (d'_j(Z)+1) for all n > j, C_S := 3(126)^d.
- (P4) p. 384: for a domain W of MR_n-cubes, the number of cubes is at most
  3·2^{d-1} times the linear size when that is > 0 (one cube otherwise):
  **(Gm-V)** #cubes(W) <= 3·2^{d-1}(d'_n(W)+1).
- (P5) p. 385: for a connected domain Z contained in the union of the
  (Q^{(i)})^{~2}, d'_m(Z) + 1 <= 2(14)^d Σ_i (d'_m(Q^{(i)}) + 1), via
  d'_m(Q^{~3}) <= 7^d(3·2^{d-1}d'_m(Q) + 2^d) <= 2(14)^d(d'_m(Q) + ½). For a
  single new region Q and a connected domain Z ⊂ Q^{~2}:
  **(Gm-C)** d'_m(Z) + 1 <= 2(14)^d (d'_m(Q) + 1).
- (P6) p. 386-387: for connected domains X, Y that intersect or touch, and a
  connected domain Z ⊂ X ∪ Y,
  **(Gm-M)** (a) d'_m(Z) <= d'_m(X) + d'_m(Y) + 2d, and (b) for n > m,
  d'_n(S^{n-m}(Z)) <= d'_n(S^{n-m}(X)) + d'_n(S^{n-m}(Y)); and the index
  inequality (1.86): 2p_0(g_{j(X)}) + 2p_0(g_{j(Y)}) - 2p_0(g_{j(Z)}) >=
  2(1+β_0)^{-1}p_0(g_{j+1}), where j(Z) is one of j(X), j(Y).

**Readings at d = 3, R = identity (conditional reduction, from note 66 §3).**

- (R-id) No R-operation: no preparatory steps, no first-class components, no
  second case after (1.83), no extra steps in (1.88). The domains are never
  processed, so the budget of (1.80) runs to the unit lattice:
  Φ_j(Z) := Σ_{n=j+1}^{K} c_E M^d R_n^{d+1} d'_n(S^{n-j}(Z)),
  and (1.79) holds for T_k of an unprocessed region (II asserts it "for all
  large field regions", p. 383-384, but derives it for the R-modified T'_k;
  note 66 Q1).
- (F1) R_n <= R_j for n > j (x_n < x_j; trivial).
- (F2) K - j < R_j for every j (note 66 (C1), x_K >= 1, L >= 3).
- (F3) R_{j+1} ∈ {R_j, R_j/L} (note 66 (C2), x_K above a threshold, about 2.6-4.5
  for L = 3..13, r = 2, 3), which is what makes the S-geometry of p. 384 work.
- β_0 = 0 on the 3D flow (P_m >= P_n for m <= n), so the gain in (1.86) is
  2P_{j+1}.

## 2. (G2): the surplus is carried exactly, so the decay is proved

### 2.1 The reformulation

For a component (or sub-domain of the tree induction) Z at scale j put

    s_j(Z) := κ_j(Z) − Φ_j(Z)        (the surplus over the remaining entropy budget),
    D_j(Z) := max_{j<=n<=K} V_n(S^{n-j}(Z)).

II proves s_j >= 0 ((1.80), at R = id with K replaced by K_end - j, note 66).
D_j(Z) is the largest M-cube volume that the unprocessed domain will reach.

**Three exact facts.** (A "family" is a connected sub-collection of the domains
of (1.84): old domains S(Z_j^(n)) and new domains (Z_{j+1}^(i))^{~2}; U(F)
is its union; κ_{j+1} is defined by (1.85) for a family F and a connected
domain Z ⊂ U(F), with Z = U(F) for the proper sub-families of the tree
induction, Z = the component at top level, and Z = S(Z_0) for a single old
domain. All of Φ, D, s below are evaluated at Z.)

(a) *No new large field.* If Z = S(Z_0) then s_{j+1}(Z) = s_j(Z_0), exactly.
Indeed the n = j+1 term of Φ_j(Z_0) is c_EM^dR_{j+1}^{d+1}d'_{j+1}(Z), the
loss in (1.83), and the terms n >= j+2 are Φ_{j+1}(Z) because
S^{n-j}(Z_0) = S^{n-j-1}(Z). So κ_{j+1}(Z) − Φ_{j+1}(Z) = κ_j(Z_0) − Φ_j(Z_0).
Also D_j(Z_0) = max(V_j(Z_0), D_{j+1}(Z)) >= D_{j+1}(Z).

(b) *Merge.* In the tree step (1.86)-(1.87) (Z ⊂ X ∪ Y connected, endpoint X,
rest Y),

    s(Z) >= s(X) + s(Y) + 2P_{j+1} − 2d c_E M^d R_{j+1}^{d+1},

using (1.86), (Gm-M)(a), and Φ_{j+1}(Z) <= Φ_{j+1}(X) + Φ_{j+1}(Y) from
(Gm-M)(b) (applied term by term, n >= j+2). Moreover

    D_{j+1}(Z) <= D_{j+1}(X) + D_{j+1}(Y),

because Z ⊂ X ∪ Y, so S^m(Z) ⊂ S^m(X) ∪ S^m(Y) (P3: S monotone and
union-compatible), and V_n is monotone and subadditive.

(c) *Creation* (single new region Q, connected domain Z ⊂ Q^{~2}; here j+1 =: m):

    s_m(Z) >= (d'_m(Z)+1)[ (c_0/(2·14^d)) P_m² − (c_E M^d + C_Φ) R_m^{d+2} ].

Proof. κ_m(Z) = c_0P_m²(d'_m(Q)+1) + 2P_m − c_EM^dR_m^{d+1}d'_m(Z) − 2P_m
(j(Z) = m), and d'_m(Q)+1 >= (d'_m(Z)+1)/(2·14^d) by (Gm-C). The budget
satisfies Φ_m(Z) <= C_ΦR_m^{d+2}(d'_m(Z)+1), C_Φ := c_EM^dC_S, because by (Gm-S)
and (F1) each of the K−m < R_m (F2) terms is at most c_EM^dR_m^{d+1}C_S(d'_m(Z)+1).
Finally c_EM^dR_m^{d+1}d'_m(Z) <= c_EM^dR_m^{d+2}(d'_m(Z)+1). ∎

Also, by (Gm-V), (Gm-S) and (F1),

    D_m(Z) <= C_V R_m^d (d'_m(Z)+1),   C_V := 3·2^{d-1}(C_S + 1)

(the term n = m: V_m(Z) = R_m^d #cubes(Z); the terms n > m:
V_n(S^{n-m}Z) = R_n^d #cubes(S^{n-m}Z) <= R_n^d 3·2^{d-1}(C_S(d'_m(Z)+1)+1)).

### 2.2 Proposition 68.1 (G2; proved here, conditional on §1)

Fix λ >= 0 and put c_* := c_0/(4·14^d), C_c(λ) := c_EM^d + C_Φ + λC_V. Assume,
for every m = 1, ..., K,

    (CC)  c_* P_m² >= C_c(λ) R_m^{d+2}.

Then for every j and every domain Z occurring in the induction (in particular
every component of Z_j),

    κ_j(Z) >= Φ_j(Z) + λ D_j(Z) + c_* P_j².                                   (68.1)

*Proof.* Induction on j, and for fixed j on the number of domains in the family
of (1.84) (the tree induction of p. 386-387). Claim: s_j(Z) >= λD_j(Z) + c_*P_j².

- Family of one old domain, Z = S(Z_0): by (a), s_{j+1}(Z) = s_j(Z_0) >=
  λD_j(Z_0) + c_*P_j² >= λD_{j+1}(Z) + c_*P_{j+1}² (D_j(Z_0) >= D_{j+1}(Z),
  P_{j+1} <= P_j).
- Family of one new region: by (c) and D_m(Z) <= C_VR_m^d(d'_m(Z)+1),
  s_m(Z) − λD_m(Z) >= (d'_m(Z)+1)[(2c_*)P_m² − C_c(λ)R_m^{d+2}] (using
  c_0/(2·14^d) = 2c_*) >= (d'_m(Z)+1)c_*P_m² >= c_*P_m² by (CC).
- Merge: by (b) and the induction hypothesis for X and Y (at the same scale
  j+1 =: m),
  s(Z) >= s(X) + s(Y) + 2P_m − 2dc_EM^dR_m^{d+1}
       >= λ(D(X)+D(Y)) + 2c_*P_m² − 2dc_EM^dR_m^{d+1}
       >= λD(Z) + c_*P_m² + [c_*P_m² − 2dc_EM^dR_m^{d+1}] >= λD(Z) + c_*P_m²,
  by the subadditivity of D and because (CC) gives c_*P_m² >= C_cR_m^{d+2} >=
  C_ΦR_m^{d+1} >= 2dc_EM^dR_m^{d+1} (C_S = 3(126)^d >= 2d). ∎

(The linear merge gain 2P_m was dropped; it is not needed, see Remark 1.)

**Corollary 68.2 (the improved (1.89) at R = id).** With (P1)'s identification
of the (1.79)-factor, for a large-field component Y of Z_k,

    T_k(Y)1 <= exp(−2P_{j(Y)} − κ_k(Y)) <= exp(−λV_k(Y) − c_*P_k²),

since Φ_k >= 0 and D_k(Y) >= V_k(Y). In particular, for the linear size of
(1.67), d_k(Y) <= c_g V_k(Y) with c_g := d (a spanning tree of a connected union
of M-cubes through the cube centres has at most V−1 edges of length <= M·d), so

    T_k(Y)1 <= exp(−κ_1 d_k(Y) − c_*P_k²)   for  κ_1 := λ/c_g,

for every κ_1 >= 0 once g is small enough (§2.3). This is the missing "−κ_1d_k(X)"
of p. 387, with constant 0 (no "− const"), and with κ_1 arbitrary rather than
II's fixed constant of p. 376. It is also stronger than (1.89) in the other
factor: exp(−c_*P_k²) = exp(−c_*x_k^{2p_0}) instead of exp(−2P_k).

### 2.3 The exponent condition, explicitly

Since x_m >= x_K, R_m <= L x_m^r (x_m >= 1) and P_m = x_m^{p_0}, (CC) holds for
all m <= K as soon as x_K >= 1 and

    x_K^{2p_0 − (d+2)r} >= Λ_1 := C_c(λ) L^{d+2} / c_*.

So the **exponent condition is 2p_0 > (d+2)r, strict** (at equality (CC) would
be a constant inequality between c_* ∝ γ_0A_1² and C_cL^{d+2} that need not
hold). At d = 3 it reads 2p_0 > 5r. Balaban's p_0 >= 5r (CMP 119 p. 246) gives
2p_0 − 5r >= 5r: margin 10 at r = 2, 15 at r = 3, so Λ_1 enters only through
Λ_1^{1/(2p_0−5r)}. Since Λ_1 depends on unspecified constants, only the
exponent is determined; the script (§6) evaluates x_K >= Λ_1^{1/(2p_0 − (d+2)r)}
for sample constants (these are not Balaban's).

**Remarks.**

1. *The mechanism: the creation budget is not spent.* (a) says the surplus s is
   invariant under unprocessed steps, (c) that a creation puts in
   c_*P² (two times, before the λD requirement) against an entropy tail of
   order R^{d+2}, and (b) that a merge of two domains, each carrying a spare
   c_*P², keeps one spare and pays the merge entropy 2dc_EM^dR^{d+1} from the
   other. So the **linear merge condition p_0 > (d+1)r of note 66 §3 is not
   needed** for this induction: the weaker 2p_0 > (d+2)r covers both cases
   ((d+2)r/2 < (d+1)r). II's (1.89) keeps only κ >= 0 because at R on the
   surplus is spent by the extra n_1 + R_{j+1} steps of (1.88) and by the
   second case after (1.83); at R = id none of these exist.
2. The geometry d'_n(S^{n-j}(Z)) <= L^{-(n-j)/2}d'_j(Z) of p. 384-385 (needing
   (C3) of note 66) is not used beyond its weak form (Gm-S): without the
   geometric decay the tail Σ_n is bounded by (K−j) terms, which is still
   R^{d+2}(d'+1), the same form as (1.81). (C3) improves only the power of R
   multiplying d'.
3. *Lemma 65.2 (sum over creation scales).* It is not needed for (68.1). The
   number of histories (creation scales and positions) is inside the sup of
   (1.79): "the summations over the admissible sequences can be replaced by
   the factors exp O(1)(MR_j)^{-d}|Z_j|" (p. 383), i.e. inside c_E M^d R_j^{d+1}
   d'_j. What (68.1) adds to note 65 §5 is that the surviving weight of a
   history created at scale i is not just exp(−cP_i²) with the entropy
   *subtracted* at each step: it is exp(−κ_k) with κ_k >= Φ_k + λD_k + c_*P_k²,
   a bound that is uniform in the creation scale; Lemma 65.2 would be used only
   if one summed histories *without* the entropy absorbed in c_E (L^{ds}
   against exp(−c P_i²), summable by the lemma). Script Part C checks that
   this alternative sum is finite for the constants used.

## 3. (G1): the gas at R = identity

II does not write this. What II writes is (1.72) (R-operation output), (1.98)-(1.101),
and (1.103)-(1.104): after the R-operation, the second-class components Y_i of the
large-field region stay large-field, carry the multiplication operation
(T'_k(Y_i)1) and boundary terms B'^{(k)}(X) with domains X meeting ∪Y_i; the Y_i
are *fixed* in the expansion of (1.103), "there are no summations over these
domains" (p. 391), and the bound has no tree decay for them. At R = id every
component of Z_k is of this kind and the Y_i are summed over. §3 writes the sum
as a polymer gas; the readings it needs are listed in §3.2, none is a printed
statement of II at R = id.

### 3.1 Objects (scale k fixed, d = 3)

- 𝔅: the M-cubes of the scale-k lattice, touching adjacency, Δ := 3^d − 1
  neighbours, c_g := d, and the counting facts (T1) a connected set of n cubes
  containing a given cube: at most (eΔ)^{n−1} such sets; (T2) |A| <= c_t(d_k(A)+1),
  c_t := 2·5^d, for a connected union A of cubes (packing: a maximal
  1-separated set of points on the tree, lengths in units of M, has at most
  2ℓ+1 points, since the ℓ^∞-balls of radius ½ around them are disjoint and
  each contains a piece of the tree of length >= ½; every cube met lies in the
  ℓ^∞-ball of radius 2 around one of them, which meets at most 5^d cubes);
  (T3) d_k(A) <= c_g|A| (§2.2).
- 𝒴: admissible large-field domains Y: connected unions of MR_k-cubes. Footprint
  Ŷ := S(Y) ⊃ Y (cover by LMR_{k+1}-cubes, ten layers); |Ŷ| <= c_+|Y|, c_+ := (21L)^d
  (the cover has at most L^d|Y| M-cubes, the ten layers multiply by 21^d; uses
  R_{k+1} <= R_k).
- A *large-field configuration* 𝒴_0 is a finite set of pairwise non-touching
  Y ∈ 𝒴 (the components of Z_k, or of the part of Z_k that is large-field).
- Weights W_Y(V): complex functions of the configuration V = U_k, depending on
  V|_{Ŷ} only, ‖W_Y‖_∞ <= exp(−λ|Y| − c_*P_k²) (Cor. 68.2, with the local
  characteristic functions of (1.104) of modulus <= 1 included in W_Y).
- Coupling domains: for a configuration 𝒴_0, 𝒳(𝒴_0) is the set of finite
  connected sets X of cubes such that X meets ∪_{Y∈𝒴_0}Ŷ and contains every
  footprint it meets (II p. 377: "the intersection Y ∩ Z~ is a union of
  components of Z~"). 𝒴_X := {Y ∈ 𝒴_0 : Ŷ ∩ X ≠ ∅}, n_out(X) := |X ∖ ∪_{Y∈𝒴_X}Ŷ|.
  Boundary terms B'(X; 𝒴_X)(V), depending on V|_X and 𝒴_X only; f(X; 𝒴_X) :=
  e^{B'(X;𝒴_X)} − 1.

**Definition 68.3 (the gas).** A *polymer* is a finite connected set Γ of cubes.
Two polymers are *compatible* iff they share no cube (Γ ∩ Γ' = ∅; touching is
allowed). For Γ put 𝒞(Γ) := the set of pairs (𝒴_0, 𝒳) with 𝒴_0 ≠ ∅ a
configuration, 𝒳 ⊂ 𝒳(𝒴_0) a finite set, ∪_{Y}Ŷ ∪ ∪_{X∈𝒳}X = Γ, and the overlap
graph of {Ŷ} ∪ {X} (edge iff two members share a cube) connected. The
**activity** of Γ is

    w(Γ) := Σ_{(𝒴_0,𝒳)∈𝒞(Γ)} Π_{Y∈𝒴_0} W_Y · Π_{X∈𝒳} f(X; 𝒴_X),

a function of V|_Γ. A polymer with 𝒞(Γ) ≠ ∅ *contains a large-field domain*.

**Lemma 68.3a (the identity; proved here, given (H-loc) of §3.2).**

    Σ_{𝒴_0} Π_Y W_Y · exp Σ_{X∈𝒳(𝒴_0)} B'(X;𝒴_X)  =  Σ_{{Γ_1,...,Γ_N} pairwise compatible, N >= 0} Π_i w(Γ_i),

the term N = 0 being 𝒴_0 = ∅ (value 1).

*Proof.* exp ΣB' = Π_X(1 + f(X)) = Σ_{𝒳 ⊂ 𝒳(𝒴_0)}Π_{X∈𝒳}f(X;𝒴_X). Fix (𝒴_0, 𝒳)
and split it into connected components of the overlap graph. Distinct
components share no cube, so the unions Γ_i are pairwise disjoint, and a
component's Y's and X's lie in Γ_i; 𝒴_X ⊂ the Y's of the component of X (a
footprint meeting X shares a cube with X). By (H-loc) the product
Π W_Y Π f factorizes over components as a product of functions of V|_{Γ_i}
with 𝒴_X computed inside the component. Conversely a pairwise compatible
family of polymers with decorations recombines to a pair (𝒴_0, 𝒳): the Y's of
different polymers are non-touching (touching Y, Y' would give Ŷ ∩ Ŷ' ≠ ∅ since
the ten layers overlap), each X contains the footprints it meets, and no
footprint of another polymer meets X (that would be a shared cube). The two
maps are inverse. ∎

(So compatibility is *disjointness of supports*; the supports contain the
S-neighbourhoods of the large-field components, which is what makes the Y's of
distinct polymers non-touching, and the X's and Ŷ's of one polymer connected by
overlap. Adjacency of supports is not an interaction: W_Y depends on V|_{Ŷ}, f
on V|_X, nothing on the neighbouring cubes.)

### 3.2 The readings (conditional reduction); sources

| name | content | source in II | status |
|---|---|---|---|
| (H-form) | at R = id, after step k, the density has the form (1.104) with R'^{(k)} = 0 and Y_i = all components of Z_k: ρ_k = e^{A'_k} · Σ_{𝒴_0} Π_Y W_Y · exp Σ_X B'(X;𝒴_X); the factor e^{A'_k} does not depend on 𝒴_0, and whatever dependence on V|_{Ŷ} the large-field region imposes is inside W_Y, W_Y = (history sum of T_k(Y)1) times characteristic functions of modulus <= 1 | (1.72) with n = 0; (1.101)-(1.104), pp. 379, 390-392 | **not written by II at R = id** (G1). Reading |
| (H-loc) | W_Y depends on V|_{Ŷ} only; B'(X;𝒴_X) on V|_X and on the large-field components meeting X only | p. 379: the terms V(Y,U_k) "depend on the sequence {Ω_j^c, Z_j} restricted to the components of Z contained in Y"; (1.103): the activities involve the Y_i contained in the localization domain; p. 377 admissibility | read from the text |
| (H-W) | ‖W_Y‖ <= exp(−λ|Y| − c_*P_k²) | Cor. 68.2 | proved in §2 from the printed geometry and (R-id) |
| (H-C) | summed coupling bound: for ν ∈ (0, ν_0], every 𝒴_0, Σ_{X∈𝒳(𝒴_0)} ‖f(X;𝒴_X)‖ e^{ν n_out(X)} <= β_ν Σ_{Y∈𝒴_0}|Ŷ|, with β_ν, ν_0 independent of k, g and 𝒴_0 | (1.99) with the modifications of p. 391 ("α replaced by O(1)c_1, β by ¼β, e³ per Y_i ⊂ X"), and (1.67) for the relative size; derivation below | **reading**: II proves (1.99) with the Y_i fixed; uniformity in the Y_i is not written |

*Derivation of (H-C) from (1.99), and what it assumes.* (1.99) with the changes
of p. 391 bounds B'(X) by b·exp(−μ_B ρ(X)), b = O(1)c_1 (c_1 = α^{1/3} <= 1,
scale-independent), ρ(X) the relative size of (1.67) with respect to the
large-field domains. By (T2), applied to the cubes of X outside the
footprints (the tree meets all of them), n_out(X) <= c_t(ρ(X)+1). The relative
size with respect to the footprints is at most the one with respect to Y
(fewer cubes to meet), so the bound holds with Ŷ in place of Y. A domain X
attached to the footprints is determined by its outside part and the
footprints it meets (it contains them whole), and the outside parts of
relative length ℓ attached at a given boundary cube of a footprint number at
most e^{c_eℓ} (the tree is counted through the footprint, whose crossing
length is part of ρ). Summing over the at most ΔΣ|Ŷ| attachment cubes gives
(H-C), per footprint cube and not per cube of ∪X, provided μ_B > c_e + νc_t.
The tree-counting step is standard and not redone here (counting input).
The exponent μ_B is (1+β/2)κ_B-type, so (H-C) is where Balaban's κ must be
large.

## 4. KP for the gas, and the activity bound

**Theorem 68.4 (proved here, given (H-form), (H-loc), (H-W), (H-C)).** Fix
ν ∈ (0, ν_0] with ν >= 8 ln(2eΔ), put κ := ν/(4c_g), and choose

    λ := λ_3 + (β_ν + ν) c_+,   λ_3 >= max{ ln(2eΔ), ln(4/ν) }.

Assume (CC) of Prop. 68.1 for this λ (so x_K >= x_*(λ), §2.3). Then for every
polymer Γ containing a large-field domain,

    |w(Γ)| <= A e^{−c_*P_k²} e^{−(ν/4)|Γ|} <= A e^{−c_*P_k²} e^{−κ d_k(Γ)},   A := (8/(eν)) e^{−λ_3},      (68.2)

and, with a(Γ) := ½κ d_k(Γ) + 1,

    σ := sup_{□} Σ_{Γ' ∋ □, Γ' large-field} |w(Γ')| e^{a(Γ')} <= 2eA e^{−ν/8} e^{−c_*P_k²},                (68.3)

so for every large-field polymer Γ_0,

    Σ_{Γ' ∩ Γ_0 ≠ ∅, Γ' large-field} |w(Γ')| e^{a(Γ')} <= c_t σ (d_k(Γ_0) + 1) <= a(Γ_0)      (68.4)

as soon as 2 c_t e A e^{−ν/8} e^{−c_*P_k²} <= min{ κ/2, 1 } (c_t = 2·5^d of (T2)), which
holds for x_K >= x_KP, an explicit threshold (§4.2); in fact it is implied by
(CC). This is the KP condition of note 49 §6 for the
large-field polymers with a(Γ) = ½κd_k(Γ) + 1.

### 4.1 Proof

*Step 1 (the inner sum).* Fix (𝒴_0, 𝒳) ∈ 𝒞(Γ) and put U := ∪Ŷ, O := Γ ∖ U. Every
cube of O lies in some X ∈ 𝒳 outside ∪_{Y∈𝒴_X}Ŷ (a cube of X inside a footprint
Ŷ' forces Y' ∈ 𝒴_X), so |O| <= Σ_X n_out(X). For fixed 𝒴_0, using that the
sum over sets 𝒳 of products is at most the exponential of the sum, and (H-C),

    Σ_{𝒳: union with U equal to Γ} Π ‖f‖  <=  e^{−ν|O|} Σ_𝒳 Π (‖f(X)‖ e^{ν n_out(X)})
        <=  e^{−ν|O|} exp( Σ_{X∈𝒳(𝒴_0)} ‖f(X)‖ e^{ν n_out(X)} )  <=  e^{−ν|O|} exp( β_ν Σ_Y |Ŷ| ).

*Step 2 (the large-field sum).* With (H-W) and |Ŷ| <= c_+|Y|, |U| <= c_+Σ|Y|:

    |w(Γ)| <= e^{−ν|O|} Σ_{𝒴_0 ≠ ∅, Ŷ ⊂ Γ} Π_Y e^{−c_*P_k²} e^{−(λ − β_νc_+)|Y|}
           <= e^{−ν|Γ|} Σ_{𝒴_0 ≠ ∅, Ŷ ⊂ Γ} Π_Y e^{−c_*P_k²} e^{−λ_3|Y|}.

(Here e^{−ν|O|} e^{−νc_+Σ|Y|} <= e^{−ν|O|} e^{−ν|U|} = e^{−ν|Γ|}, using |Γ| = |O| + |U|, i.e.
the definition λ = λ_3 + (β_ν+ν)c_+.) The sum over sets of distinct Y is at most
exp(Σ_{Y⊂Γ} a_Y) − 1, a_Y := e^{−c_*P_k² − λ_3|Y|}, and by (T1) the number of Y ⊂ Γ with
|Y| = n is at most |Γ|(eΔ)^{n−1}, so Σ_{Y⊂Γ}a_Y <= |Γ|η, η := 2e^{−λ_3−c_*P_k²}
(eΔe^{−λ_3} <= ½). Then exp(|Γ|η) − 1 <= |Γ|ηe^{|Γ|η} and η <= ν/2 (λ_3 >= ln(4/ν)):
|w(Γ)| <= |Γ|η e^{−ν|Γ|/2} <= (4/(eν))η e^{−ν|Γ|/4} = A e^{−c_*P_k²}e^{−ν|Γ|/4}.
The second form of (68.2) is (T3): d_k(Γ) <= c_g|Γ|, so e^{−ν|Γ|/4} <= e^{−κd_k(Γ)}.

*Step 3 (KP).* e^{a(Γ')} <= e · e^{½κc_g|Γ'|} = e · e^{ν|Γ'|/8}. By (T1),

    σ <= eA e^{−c_*P_k²} Σ_{m>=1} (eΔ)^{m−1} e^{−νm/8} <= 2eA e^{−ν/8} e^{−c_*P_k²}

(eΔe^{−ν/8} <= ½, i.e. ν >= 8 ln(2eΔ)). A polymer Γ' incompatible with Γ_0
shares a cube with it, so the sum in (68.4) is at most |Γ_0|σ <= c_t(d_k(Γ_0)+1)σ
by (T2), which is <= a(Γ_0) = ½κd_k(Γ_0)+1 if c_tσ <= min{κ/2, 1}. ∎

### 4.2 Constants and thresholds

- ν: the coupling decay (H-C) must supply ν_0 >= 8 ln(2eΔ) and μ_B > c_e + c_tν.
  At d = 3, Δ = 26: ν >= 8 ln(2e·26) = 39.6, so κ = ν/(4c_g) = ν/12 >= 3.3.
  Note 49 §6 asks κ >= 4c_d with c_d = ln(eΔ) = 4.26 (touching connectivity,
  d = 3), i.e. κ >= 17.0, which needs ν >= 12·17.0 = 204.5. These are
  requirements on Balaban's κ_B, as in note 49 §6; this note does not know κ_B.
- λ = λ_3 + (β_ν + ν)c_+, c_+ = (21L)^d. For L = 13, d = 3: c_+ = 273³ = 2.03·10^7,
  so λ is a large constant. Prop. 68.1 pays for it through
  x_K^{2p_0−(d+2)r} >= C_c(λ)L^{d+2}/c_*, with C_c linear in λ: an arbitrary λ
  costs a larger constant under an exponent fixed by 2p_0 > (d+2)r.
- x_KP: 2c_t e A e^{−ν/8} e^{−c_*P_k²} <= min{κ/2, 1}, i.e. c_*P_k² >=
  ln(2c_t e A e^{−ν/8}/min{κ/2,1}). Since A <= 2/e (e^{−λ_3} <= ν/4), the right
  side is at most ln(4c_t/min{κ/2,1}) = O(1), while (CC) gives c_*P_k² >=
  C_c(λ) >= λC_V, which is astronomically larger for the λ above. So x_KP is
  implied by x_K >= x_*(λ).

### 4.3 Where (G2) is essential

(i) Without a size decay of W_Y the large-field sum cannot be shown to converge.
(1.89) as printed gives T_k(Y)1 <= exp(−2P_k), independent of |Y|, while the
number of admissible Y ∋ □ with |Y| = n grows exponentially in n:
Σ_Y e^{−2P_k} = ∞, so KP (indeed absolute convergence) cannot be verified from
(1.89) alone, for any κ. The decay rate per
cube must exceed ln(eΔ) + (the extensive coupling rate β_νc_+), and Prop. 68.1
gives any λ.

(ii) The coupling terms are extensive in the footprint: Σ_X‖f‖ <= β_ν|Ŷ|, with
β_ν built from c_1 = α^{1/3}, *not* a power of g_k. This is the issue noted in
note 66 Q1 ("c_1 = α^{1/3} for polymers touching a large-field domain"):
it is harmless here, because in the gas every polymer touching a large-field
domain *contains* it and so carries the factor e^{−c_*P_k²} of W_Y; the
smallness in g_k comes from W_Y, not from the coupling activity, and the
α^{1/3}-sized couplings only cost e^{β_νc_+|Y|}, which λ beats.

## 5. Conclusion in the form note 61 needs

**Theorem 68.5 (conditional reduction).** Assume (R-id), the printed geometry
(P1)-(P6), the 3D-flow facts (F1)-(F3), the readings (H-form), (H-loc), (H-C),
and the exponent condition 2p_0 > (d+2)r (at d = 3: 2p_0 > 5r, which p_0 >= 5r
satisfies with margin 5r). Then for every q there are x_q and C_q such that for
x_K >= max{x_*(λ), x_KP, x_q}, every scale k <= K, and every polymer Γ (a
touching-connected set of M-cubes of scale k) containing a large-field domain,

    |w(Γ)| <= C_q g_k^q e^{−κ d_k(Γ)},                                                       (68.5)

with κ = ν/(4c_g) (ν as in Thm 68.4), and the KP condition of note 49 §6
holds for the large-field polymers with a(Γ) = ½κd_k(Γ)+1 (68.4), the large-field
sum having margin e^{−c_*P_k²}. Here **"activity" is w(Γ) of Definition 68.3**:
the sum over decompositions of Γ into large-field domains and coupling
domains of the products of the weights T_k(Y)1 (with their characteristic
functions) and the Mayer activities f(X) = e^{B'(X)} − 1 of the boundary terms.

*Proof.* (68.2) gives |w(Γ)| <= A e^{−c_*x_k^{2p_0}} e^{−κd_k(Γ)}, and
e^{−c_*x^{2p_0}} <= C_q e^{−qx/2} = C_q g_k^q for x >= x_* (C_q :=
sup_{x>=x_*} e^{−c_*x^{2p_0}+qx/2} < ∞), because g_k² = e^{−x_k}. ∎

**What is proved here, and what each step rests on.**

| piece | label | rests on |
|---|---|---|
| Prop. 68.1, Cor. 68.2: κ_k(Y) >= Φ_k + λD_k + c_*P_k², T_k(Y)1 <= e^{−λV_k(Y)−c_*P_k²} | **proved here (conditional reduction)** | printed (P1)-(P6) of II pp. 380-387; (R-id) reading of note 66 §3; (F1)-(F3); exponent 2p_0 > (d+2)r |
| Lemma 68.3a, the identity gas = (1.104)-form | proved here | (H-loc) |
| Thm 68.4 (68.2)-(68.4) | proved here | (H-form), (H-loc), (H-W), (H-C) and standard lattice counting (T1)-(T3) |
| Thm 68.5 (68.5) | proved here | the above |
| (H-form): R = id density has the form (1.104) with R' = 0, Y_i = all components, common factor e^{A'_k} | **open (reading)** | not in II (G1) |
| (H-C): uniform summed coupling bound | **open (reading)** | II proves (1.99) with Y_i fixed; uniformity in Y_i and the tree-counting are not written |
| (1.79) for T_k at R = id | open (note 66 Q1) | II states "for all large field regions" (p. 383-384), derives it for T'_k |

**Where it could fail.** No step was found to fail. The steps that are not
established are exactly three: (H-form), (H-C), and (1.79) for the unprocessed
T_k. In particular: (a) the *printed* (1.97)/(1.99) alone do not give the form
|activity| <= C_qg^q e^{−κd} (the constant is α^{1/3}), but the form follows
once the Y's are gas elements, because the factor e^{−c_*P_k²} of W_Y then sits
in every polymer that touches a large-field domain (§4.3 (ii)); (b) the form needs
the volume decay of Prop. 68.1, not (1.89) as printed (§4.3 (i)).

**Translation to note 61 (not done).** Note 61 (LF-act) uses r_*-connected
polymers (r_* >= 2) with blocks of its own; the gas here has touching-connected
polymers of M-cubes of scale k. Passing from one to the other is a coarse-graining
(r_*-connected components of unions of compatible polymers), which changes
constants by standard counting but was not carried out. Likewise the
identification of note 61's k with Balaban's j (note 61's scale k corresponds
to Balaban's K − k, note 65 §0).

## 6. Script, corrections for the lead, not checked

**Script.** `research/scripts/t84_surplus_checks.py`, output
`research/scripts/t84_surplus_checks.out`. Part A: thresholds of §2.3 for
*sample* constants (c_EM^d = 1, γ_0 = 1/2, A_1 = 1, L = 13; Balaban's are not
specified): x_K >= 50.0 (r = 2, p_0 = 10, λ = 0), 26.1 (p_0 = 11), 13.6
(r = 3, p_0 = 15); for λ = 100: 101.6, 47.0, 21.8; at 2p_0 = (d+2)r there is no
threshold. Part B: random histories of the recursion (1.83)/(1.85) on a toy
geometry; the invariant (68.1) holds for t >= 0.047 (c_0 scaled by t) while the
proof's constants give the sufficient t >= 0.337; fact (a) holds to relative error
0. Part C: Lemma 65.2's sum is 1 (only s = 0) for the sample constants.

**Corrections for notes 49, 61, 65, 66 (for the lead to apply).**

1. Note 66 §3 / §5 item 3: for the induction with a spare, the merge step does
   not need p_0 > (d+1)r; the single exponent condition is 2p_0 > (d+2)r. (At
   R on the merge condition of (1.88) is a different matter and is not
   affected.) Note 66's p_0 > (d+1)r should be marked "sufficient, not needed"
   for the R = id induction, and the conclusion of Q1 changed from "(G2) open"
   to "(G2) proved here (note 68 Prop. 68.1) conditional on the same readings".
2. Note 66 Q1: "(1.89) ... exp(−2p_0(g_k))" can be strengthened at R = id to
   exp(−κ_1d_k(Y) − c_*p_0²(g_k)) (note 68 Cor. 68.2). Note 65 (W): the
   unrolled quadratic form is recovered, with the entropy absorbed.
3. Note 61 (LF-act) and Lemma 6b.2: the hypothesis |𝒜_k(Z)| <= C_LFε_k^qe^{−κd(Z)}
   is, at the level of this note, Thm 68.5 (68.5) with the three open readings
   (H-form), (H-C), (1.79 at R = id); it is not a printed statement of II.
4. Note 49 §6: (1.97) is not the large-field activity at R = id (note 66); the KP
   check of §4 above replaces it for the gas at R = id, with a(Γ) = ½κd_k(Γ)+1 and
   the touching connectivity c_d = ln(eΔ) = ln(26e) = 4.26 at d = 3.
5. II (1.85) prints γ_0A_1² for the creation weight where (1.79), (1.82) and p. 381
   use ½γ_0A_1²; the proofs use ½γ_0A_1².

**Not checked.** Page images of II pp. 355-375 (definitions of Z~, Y_i, X_j; the
exact thickness of Z~ vs the footprint S(Y)); the (7.13) series of [I] and its
tree-counting; the identification of the tree entropy c_e; the uniformity of
the constants in (1.92)-(1.97) in the Y_i; whether e^{A'_k} is truly independent
of the large-field configuration. The proofs use d' ≍ #cubes only through the
printed (Gm-V), (Gm-S), (Gm-C), (Gm-M).
