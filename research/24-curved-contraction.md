# Curved-background contraction for the CMP 109 average: note 12's (3.3) proved

Status, item by item:

- **Proved here.**
  - Theorem 1: note 12's open estimate (3.3) for Balaban's
    Euclidean-symmetric average (CMP 109 Eq. (0.4)), with explicit
    constants. If the background has small plaquette curvature κ on a
    4L-neighborhood, the pull-back of covariantly conserved coarse currents
    obeys ||DQ(U)^*τ||_∞ <= (L^{1-d} + c_{d,L} κ)||τ||_∞. The flat value
    L^{1-d} is exact (note 15).
  - Corollary 2: the contraction half of note 12's "H6-uniform" on regular
    backgrounds. Note 15 Prop. 4 (the first-layer path bound) holds at
    **any** exterior field on its branch-gap event.
  - Together these reduce H6_Σ to H7_Σ (the probability of the irregular
    event) plus the component-counting second moment (note 11 (3.11)).
- **Computation.** Exact operator norms via second-order cone programs
  (`research/scripts/t15_*.py`):
  - pure-gauge backgrounds reproduce the flat value exactly, which checks
    gauge invariance and the code;
  - the measured θ - L^{1-d} is linear in κ, with constants far below the
    proved c_{d,L}.
- **Open.** H7_Σ, the component-counting input, and H8_Σ are untouched.

Note 12 §3 worried that at curved backgrounds the radial (hub) residual could
be "order one relative to the flat L^{1-d} weight on a hub bond". Theorem 1
shows this residual is O(κ). That is exactly the additive form (3.3) which
note 12 conjectured and called a "strong uniform route".

## 1. Setting

The map is Q = CMP 109 (0.4) (note 15 (1.3)), with SU(2) and odd L. Tangent
vectors are right-trivialized: a fine perturbation U_b -> U_b e^{iεa·σ} has
components a ∈ R³, and coarse variations are V^{-1}δV = i x·σ. The per-bond
norm |·| is Euclidean in these components, which is Ad-invariant, and
||τ||_∞ = max_bonds |τ(c)|. Let J = DQ(U) and P_U = J^T, which maps coarse
currents to fine currents.

ϑ(H) := ||(1/i) log H||_op ∈ [0, π] is the bi-invariant distance from H to 1
in SU(2). It satisfies ϑ(AB) <= ϑ(A) + ϑ(B) and ϑ(gHg^{-1}) = ϑ(H).

A coarse current τ is **covariantly conserved at V** if it annihilates every
infinitesimal coarse gauge direction:

    Σ_{c: c_- = y} Ad(V_c) τ(c) - Σ_{c: c_+ = y} τ(c) = 0   for every coarse site y.   (1.1)

(The variation of V_c under ω is Ad(V_c^{-1})ω(c_-) - ω(c_+).) The terminal
differential of a gauge-invariant function is conserved in this sense, and
P_U maps conserved currents to conserved currents (note 12 Lemma 1).

## 2. Four lemmas

**Lemma A (gauge invariance of the operator norm).** For a fine gauge
transformation u with coarse restriction u_c (its values at block centers),
Q(U^u) = Q(U)^{u_c}. In right-trivialized coordinates, P_{U^u} = O_f P_U O_c^{-1}
with O_f, O_c block-diagonal rotations Ad(u(·)), which preserve |·| and map
the conserved subspace at V to the one at V^{u_c}. Hence
θ(U) := sup{||P_Uτ||_∞ : τ conserved, ||τ||_∞ <= 1} is gauge invariant.
*Proof.* Each contour transporter in (0.4) transforms by its endpoint values,
and the relative holonomies by conjugation at c_-. The logs and the
exponential are Ad-equivariant, so Q is gauge covariant with the stated
coarse transformation. Differentiate. ∎ (Numerical check: pure-gauge
backgrounds give θ = L^{1-d} exactly; §5.)

**Lemma B (axial gauge).** Let Ω be a box of side R in which every plaquette
has ϑ <= κ. Then in the complete axial gauge on Ω (tree: (x, μ) with
x_ν = 0 for every ν > μ), every link satisfies ϑ(U_b) <= (d-1)Rκ.
*Proof.* A non-tree link's value is the holonomy of the loop formed by
tree(x), the link b, and tree(x+e_μ)^{-1}. The two tree paths agree up to
axis μ-1. After that they run parallel, displaced by e_μ, along the axes
ν > μ. The enclosed strip has at most (d-1)R plaquettes. By the lasso
decomposition the loop holonomy is an ordered product of conjugates of these
plaquette holonomies. Subadditivity and conjugation invariance of ϑ finish
the proof. ∎

**Lemma C (flat decomposition; from note 15 §3).** For **every** coarse
current τ (conserved or not),

    P_1 τ = S^*τ + Λ_sym^*(div τ),   ||S^*τ||_∞ <= L^{1-d}||τ||_∞,   |Λ_sym^*(ρ)(b)| <= |ρ(y_b)|,   (2.1)

where div is the flat divergence (note 15 (3.3)) and y_b is the block whose
radial paths contain b.
*Proof.* Pair note 15 (3.1) with τ. The endpoint terms give
Σ_y ⟨div τ(y), Λ_sym(y)⟩, and the segment term gives S^*τ, whose sup bound is
note 15's (3.5) (it never used div τ = 0). Radial paths of B(y) stay in B(y).
For a single bond b, the normalized radial weight Σ_{x,Γ} L^{-d}|G|^{-1}1[b∈Γ]
is at most 1, since a shortest path passes b at most once and the weights
sum to 1. ∎

The hub bonds next to block centers are exactly where the radial weight in
Lemma C is of order one. Lemma C shows they multiply only div τ.

**Lemma D (divergence defect).** If τ is conserved at V, then
|div τ(y)| <= 2d max_c ϑ(V_c) ||τ||_∞.
*Proof.* By (1.1), div τ(y) = Σ_{c_- = y}(1 - Ad(V_c))τ(c). Ad(V_c) is a
rotation by angle 2ϑ(V_c), so ||1 - Ad(V_c)||_op = 2 sin ϑ(V_c) <= 2ϑ(V_c).
There are d bonds with c_- = y. ∎

**Lemma E (Lipschitz derivative).** Let λ = (d+1)L bound the contour lengths
in (0.4), and suppose every fine link in the support has ϑ <= r with
σ := (7d+16)L r <= 1. Then

    ||P_U - P_1||_{∞→∞} = max_b Σ_c ||∂_b Q_c(U) - ∂_b Q_c(1)||_op <= 2(2d+3)(7d+16) L r.   (2.2)

*Proof.* Right-trivialized,

    ∂_bQ_c = Ad(U_c^{-1}) dexp_X [ Σ_ℓ w_ℓ dlog_{Z_ℓ}( Ad(U_c)[∂_b H_ℓ - ∂_b U_c] ) ] + ∂_b U_c,

with Z_ℓ = (1/i)log(H_ℓ U_c^{-1}) and X = Σ w_ℓ Z_ℓ. Here ∂_b H_ℓ is a signed
sum, over the occurrences of b in ℓ, of Ad(suffix^{-1}) applied to the unit
generator. At U = 1 every Ad, dexp and dlog is the identity. At U:

- ||Ad(U_c^{±1}) - 1|| <= 2Lr;
- each suffix Ad is within 2λr of the identity;
- ϑ(Z_ℓ), |X| <= a := (λ+L)r <= 1, so ||dexp_X - 1|| <= 3a and
  ||dlog_Z - 1|| <= 2a (the series of (1 - e^{-ad})/ad and of its inverse,
  the Bernoulli series with radius 2π, using ||ad_Z|| <= 2|Z| <= 2).

In each term the product of these factors therefore deviates from the
identity by at most e^σ - 1 <= 2σ, where σ = 4Lr + 5a + 2λr <= (7d+16)L r.
The flat coefficients have Σ_c Σ_ℓ w_ℓ N_b(ℓ) <= K_{d,L} <= 2d+1 (note 15
(4.3)), plus at most 2 for the central-transporter terms. ∎

## 3. The theorem

**Theorem 1.** Let b be a fine bond, and let Ω_b be the box of side 4L
centered at the block of b, which contains the contours of every coarse bond
whose support or endpoint conservation involves b. Suppose every plaquette in
Ω_b has ϑ <= κ, with κ <= κ_0 := 1/(4(d-1)(7d+16)L²). Then for every τ
conserved at V = Q(U),

    |(P_U τ)(b)| <= (L^{1-d} + c_{d,L} κ) ||τ||_∞,
    c_{d,L} = 4(d-1)[2d(d+3) + 2(2d+3)(7d+16)] L².   (3.1)

So if κ bounds the curvature everywhere, θ(U) <= L^{1-d} + c_{d,L}κ, which is
note 12 (3.3) with a gauge-invariant curvature size.

*Proof.*

1. By Lemma A, compute in the axial gauge of Lemma B on Ω_b. There
   r := ϑ_max(U) <= 4(d-1)Lκ, and σ <= 1 by the choice of κ_0. The value
   (P_Uτ)(b) depends only on U on Ω_b and τ on nearby coarse bonds. Lemma A
   applied to a gauge transformation equal to the axial one on Ω_b and
   arbitrary elsewhere leaves |(P_Uτ)(b)| unchanged.
2. Coarse links satisfy ϑ(V_c) <= |X| + ϑ(U_c) <= (λ+2L)r = (d+3)Lr.
3. Split P_Uτ = P_1τ + (P_U - P_1)τ. Lemma C with Lemma D gives
   |(P_1τ)(b)| <= L^{1-d}||τ|| + 2d(d+3)Lr||τ||.
4. Lemma E gives |((P_U - P_1)τ)(b)| <= 2(2d+3)(7d+16)Lr||τ||.
5. Substitute r <= 4(d-1)Lκ. ∎

The constant is crude. In d = 4, c_{4,L} = 12288 L². §5 measures the true
constant to be of order one.

## 4. Consequences for H6

**Corollary 2 (H6-uniform on regular backgrounds).** In d = 4, fix δ ∈ (0,1)
and put κ_* := (L^{-2-δ} - L^{-3})/c_{4,L}. On the event Reg_* where:

- (a) the first affected layer satisfies note 15's branch-gap condition (4.1)
  at the actual exterior field, and
- (b) every later image U_j(t), for every t ∈ [0,1], has plaquette curvature
  <= min(κ_*, κ_0) on the transport neighborhoods,

the terminal oscillation of a gauge-invariant terminal coordinate with
differential bounded by C_F satisfies

    |Φ_K(W(1)) - Φ_K(W(0))| <= C_F C_0(d,L,δ_br)(s + L^d) L^{-(2+δ)(m-1)},   (4.1)

with C_0 from note 15 (4.5). Hence L^d θ² <= L^{-2δ} < 1 (note 12 (3.4)).
Summing the squared oscillation over the L^{4m} placements per terminal block
gives a convergent series, given note 11's second-moment component count
(3.11). This is H6_Σ restricted to Reg_*.

*Proof.* Note 15 Prop. 4 never used the trivial exterior. Its proof uses
only:

- that the right-trivialized velocity of a path holonomy is a sum of unitary
  conjugates of bond velocities (true at any background);
- Lemma 3 on the branch-gap domain;
- Duhamel.

So (4.4)-(4.5) there hold verbatim at any exterior on the event (4.1). The
later levels contract by θ <= L^{-3} + c_{4,L}κ_* = L^{-2-δ} (Theorem 1).
Note 12 Lemmas 2 and 4 then give (4.1). ∎

**What remains of H6_Σ.** Only the complement of Reg_*, which belongs to
H7_Σ, and the component-counting input. Regularity (b) is Balaban's
small-field condition at each scale, provided his constant ε_1 is taken
<= min(κ_*, κ_0), an extra smallness requirement on ε_1 in terms of L. CMP
109 leaves ε_0, ε_1 "sufficiently small" subject to "numerous restrictions",
so one more is consistent with the construction. Whether the R-regions'
coarse images satisfy (b) after the first layer is part of H7_Σ.

## 5. Computation

`t15_curved_contraction.py` is the reference implementation (dense matrices,
finite-difference Jacobian). `t15_fast.py` is a vectorized quaternion
version. θ is computed as max over fine bonds b of
max {|(P_Uτ)(b)|_2 : τ ∈ ker G^T, |τ(c)|_2 <= 1}. Each inner problem is a
second-order cone program (CVXPY/Clarabel), with alternating maximization
over the output direction, so the value is a certified lower bound and in
practice the maximum. G spans the coarse gauge directions at V.
Backgrounds:

- flat;
- pure gauge (random gauge transformation of the flat field);
- smooth (slowly varying non-abelian A);
- rough (i.i.d. small links).

κ is the maximal plaquette angle.

**d = 2, L = 3, 3×3 coarse torus** (flat value 1/3):

| background | κ | θ | (θ - L^{1-d})/κ |
|---|---|---|---|
| flat | 0 | 0.333333 | - |
| pure gauge | 0 | 0.333333 | - |
| smooth | 0.031 | 0.34990 | 0.53 |
| smooth | 0.064 | 0.36899 | 0.56 |
| smooth | 0.248 | 0.50264 | 0.68 |
| rough | 0.073 | 0.35018 | 0.23 |
| rough | 0.169 | 0.38571 | 0.31 |
| rough | 0.326 | 0.42701 | 0.29 |
| rough | 0.696 | 0.57349 | 0.35 |

The box-norm (non-Ad-invariant) version gives a pure-gauge value 0.576,
which is why the Ad-invariant norm is required.

**d = 3, L = 3, 2³ coarse torus** (flat value 1/9; 648 fine bonds, 343 contours per coarse bond):

| background | κ | θ | (θ - L^{1-d})/κ |
|---|---|---|---|
| flat | 0 | 0.111111 | - |
| pure gauge | 0 | 0.111111 | - |
| smooth | 0.077 | 0.13493 | 0.31 |
| smooth | 0.140 | 0.14441 | 0.24 |
| rough | 0.078 | 0.12357 | 0.16 |
| rough | 0.189 | 0.15493 | 0.23 |
| rough | 0.379 | 0.19852 | 0.23 |

**d = 4, L = 3:** `t15_d4.out` (running at the time of writing; appended when complete).

In both dimensions θ - L^{1-d} is linear in κ with a constant of order 0.2-0.7, and there is no order-one hub jump.

## 6. Status change

| Item | Before | After |
|---|---|---|
| note 12 (3.3) for CMP 109 (0.4) | conjectured strong route; hub worry | proved (Thm. 1), explicit c_{d,L} |
| note 15 Prop. 4 at curved exterior | trivial exterior only | any exterior, same constant |
| H6_Σ | open | reduced to H7_Σ on Reg_* plus component counting |
