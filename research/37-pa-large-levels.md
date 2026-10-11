# (PA) on all events: large levels cost a fixed action each

Status:

- **Proved here.**
  - Lemma 1 (abelian annular bound): a level-i block flux bounded below by
    ε_0 forces Σ_r L^{-2r} a_{i-r} >= δ_ab, where a_l is the action in the
    l-th annulus around Λ and δ_ab is explicit.
  - Lemma 2 (summation): if every level in a set I satisfies such a bound,
    the total action is >= |I| δ (1 - L^{-2}).
  - Theorem 3: the non-abelian (PA) of note 26 holds **on all events**
    (no ε_0-small restriction), under:
    - (D1), (D2) of note 34 on small levels (published-input derivation in
      note 36);
    - (SER), a lattice ε-regularity statement whose abelian case is Lemma 1.
- **Open.** (SER) for SU(2). It is a small-energy regularity statement of
  Uhlenbeck type on the lattice, with Balaban's average. It is not in the
  published sources of this repository.
- **Effect.** Note 34 §5 item 2 (the ε_0-large event) is closed modulo
  (SER). Each large level costs g_k^{-2}δ >= δ/γ², which is much larger
  than 4 log L for small γ.

## 1. Geometry

Fix the region Λ at scale k.

- N_l is the cube of side 3C L^l (scale-k units) centred on Λ, for l >= 0.
  N_{-1} := ∅.
- ann_l := N_l \ N_{l-1} is the l-th annulus.
- a_l := A_k(U | ann_l) is the Wilson action on plaquettes in ann_l.
- The annuli are disjoint, so Σ_l a_l <= A_k(U).

Every level-i image plaquette p within C L^i of Λ has its averaging kernel
supported in N_i.

A level i is **large** if some such plaquette has ϑ_i(p) > ε_0. Let I be the
set of large levels among 1, ..., t + R.

## 2. The abelian annular bound

**Lemma 1.** Abelian theory, a = ½||F||² per plaquette set. If a level-i
plaquette p within C L^i of Λ has |Φ_i(p)| >= ε_0, then

    Σ_{r=0}^{i} L^{-2r} a_{i-r} >= δ_ab := ε_0² (1 - L^{-2}) / (2C'²),   C' := max(1, 9C²).

*Proof.*

1. Φ_i(p) = ⟨w_i, F⟩ = Σ_{r=0}^{i} ⟨w_i 1_{ann_{i-r}}, F⟩, with w_i the
   level-i kernel (note 26 §7).
2. Size of the pieces:
   - r = 0: ||w_i||_2 <= 1 (note 26 §7).
   - r >= 1: ||w_i 1_{ann_{i-r}}||_2 <= ||w_i||_∞ |N_{i-r}|^{1/2}
     <= L^{-2i} · 9C² L^{2(i-r)} = 9C² L^{-2r}.

   So |Φ_i(p)| <= C' Σ_r L^{-2r} (2a_{i-r})^{1/2}.
3. Cauchy-Schwarz, splitting L^{-2r} = L^{-r} · L^{-r}:
   ε_0² <= C'² (Σ_r L^{-2r}) (Σ_r L^{-2r} 2a_{i-r})
   <= C'² (1 - L^{-2})^{-1} · 2 Σ_r L^{-2r} a_{i-r}. ∎

**Lemma 2 (summation).** Suppose every i ∈ I satisfies
Σ_{r>=0} L^{-2r} a_{i-r} >= δ. Then

    A_k(U) >= |I| δ (1 - L^{-2}).

*Proof.* Exchange the sums:

    |I| δ <= Σ_{i∈I} Σ_r L^{-2r} a_{i-r} = Σ_l a_l Σ_{i∈I, i>=l} L^{-2(i-l)}
          <= (1 - L^{-2})^{-1} Σ_l a_l <= (1 - L^{-2})^{-1} A_k(U). ∎

The point is that a large level costs a **fixed** amount of action. The same
energy cannot be reused by many large levels, because its weight decays like
L^{-2(i-l)} in the level distance. In particular, a lump of energy at scale
L^l makes only O(1) levels near l large.

## 3. The non-abelian hypothesis

**(SER) Small-energy regularity.** There is δ_SER > 0, depending on d, L and
ε_0, such that for every SU(2) field U on the scale-k lattice and every
level-i image plaquette p within C L^i of Λ,

    Σ_{r>=0} L^{-2r} a_{i-r} < δ_SER   implies   ϑ_i(p) <= ε_0.

The abelian case is Lemma 1 (contrapositive) with δ_SER = δ_ab.

*Why it is plausible.* The left side is a Morrey-type energy at scale L^i,
in 4D scale-invariant units. In the continuum, small energy in a ball gives
a Coulomb gauge with small connection (Uhlenbeck's gauge theorem). Then the
holonomies of loops of size about L^i are close to 1, and so is Balaban's
average of them. On the lattice two extra points arise:

- a fine plaquette with angle near π costs only O(1) action, so it is
  already excluded by small energy;
- the Morrey weights L^{-2r} control the inner annuli, as in Lemma 1.

A proof would combine a lattice Uhlenbeck gauge with Balaban's bounds for
averages of small fields (CMP 98). This is not done here.

*Literature check (2026-10-02, web search).* I found no lattice version of
Uhlenbeck's small-energy gauge theorem. The continuum results found are
Uhlenbeck's theorem and its extensions (e.g. arXiv:2202.09535,
arXiv:1505.06995). The nearest lattice work handles axial gauges with small
plaquettes, but not small energy: Chatterjee, arXiv:1602.01222;
Brennecke, arXiv:2511.07297. (SER) therefore looks like a genuinely new
lattice statement.

## 4. Theorem 3: (PA) on all events

**Theorem 3.** Assume:

- (D1) and (D2) of note 34 at every level that is not large, in the local
  form near the chain;
- (SER);
- s_L < 1 - η (in the abelian limit, note 35's computed rows suggest this
  for L >= 4; they are lower bounds for s_L, so it is not established).

Let U be persistent on levels 1, ..., t (note 26 §3). Then

    g_k^{-2} A_k(U) >= (1/(2(R+1))) Σ_{j=1}^{t} min( c_1 η² p(g_{k+j})² / C_F²,
                                                     δ_SER (1 - L^{-2}) / g_k² ),

with R = ⌈log(ε_0/ε_min)/log ρ_L⌉ as in note 34.

*Proof.*

1. *Chains.* For each persistent level j, run the chain of note 34
   Theorem 3, step 2, from the witness p_j. Within R levels it does one of
   two things:
   - it reaches a level σ(j) where (G) holds, with
     |φ_{σ(j)}|_∞ >= ηε_j/C_F (all angles on the way are <= ε_0, so (D1)
     and (D2) apply there);
   - it reaches a large level λ(j) ∈ I, where some angle exceeds ε_0.
2. *Pigeonhole.* Let J_G be the set of j of the first kind and J_I the rest.
   Each level is σ(j) or λ(j) for at most R + 1 values of j. As in note 34,

       Σ_{i} |φ_i|_∞² >= (η²/(C_F²(R+1))) Σ_{j∈J_G} ε_j²,   |I| >= |J_I| / (R+1).
3. *Two lower bounds on the same action.*
   - Telescoping (note 34 Lemma 2) with (D1) at the G-levels gives
     A_k >= c_1 Σ_i |φ_i|_∞².
   - (SER) and Lemma 2 give A_k >= |I| δ_SER (1 - L^{-2}).

   Hence A_k >= ½(first + second).
4. *Collect.* Multiply by g_k^{-2}. Use ε_j²/g_k² >= ε_j²/g_{k+j}² = p(g_{k+j})²
   and |J_G| + |J_I| = t. ∎

**Rate.** Each persistent level costs at least

    a = (1/(2(R+1))) min( c_1 η² p(γ)²/C_F², δ_SER(1 - L^{-2})/γ² ) - C',

using g_k <= γ. Both terms in the minimum grow as γ -> 0. The first grows
like (log γ^{-1})^{2p_0}, the second like γ^{-2}. R grows only like
log(1/γ). So L⁴e^{-a} < 1 for small γ. Combined with the multi-scale bound
(UB-ms) of note 38, this gives (P). (Note 26 Prop. 1 with a single-scale
(UB) is incomplete because of entropy; see note 38.) (PA) is now reduced to
(D1), (D2) (note 36) and (SER).

## 5. Status of (P) after notes 34-37

(P) ⇐ (UB-ms) + (SER) + [(D1), (D2): published-input derivation in note 36,
with localization sketched]. The abelian versions of (SER), (D1) and (D2)
are proved or computed exactly (Lemma 1; notes 35, 36). The two genuinely
open statements are:

- (UB-ms): the multi-scale, per-level action-weighted bound for the
  pre-replacement R'-label and its future history (note 38 §4);
- (SER): lattice small-energy regularity for Balaban's average.
