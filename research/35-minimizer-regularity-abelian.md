# Minimizer regularity (D2) in the abelian 4D theory: exact sup-norm constants

Status: **computation** (T27). Script:
`research/scripts/t27_minimizer_regularity.py`.

- **Result.** In the abelian 4D Gaussian theory with Balaban's linear
  block flux (note 19 (2.1)), the sup-to-sup norm s_L of the map
  "level-m block fluxes ↦ level-(m-1) image fluxes of the fine minimizer",
  restricted to exact coarse fluxes, is **not** O(L^{-2}). Measured on the
  far-corner child row, which is the largest row found here [T53: for
  L >= 3 other rows are larger, by 12-23% at n_0 = 6; §5]:

  | L | s_L (m = 1) |
  |---|---|
  | 2 | 1.539 |
  | 3 | 1.122 |
  | 4 | 0.773 |
  | 5 | 0.547 |

  That is roughly s_L ≈ 3.4 L^{-1.1}.
- **Dependence on the depth** (L = 2): s = 1.539, 1.633, 1.688 for
  m = 1, 2, 3. The increments shrink (0.094, 0.055), consistent with a
  limit near 1.76.
- **Consequences.**
  - The chain lemma of note 34 (Theorem 3, with the η-split) needs
    s_L < 1. It fails for L = 2, 3 (the computed rows already exceed 1).
    For L >= 4 the computed rows are below 1, but they are only lower bounds
    for s_L (§2: some rows, one 6⁴ torus), so s_L < 1 is suggested there,
    not established. [Audit 2026-10-09, T82: the values of §2 are lower bounds for s_L.]
    [T53, §5: larger rows give 0.88 for L = 4 at m = 1, about 0.97-1.01 with
    the depth growth, so s_L < 1 is suggested only for L >= 5. The twisted
    sectors of note 54 change the largest rows by under 0.1% upward at
    n_0 = 6.]
  - The reading "fine curvature = coarse curvature / L²" in note 33 §1 holds
    only for coarse fields that are smooth on the block scale. It is
    corrected there.

## 1. What is computed

Fine torus (Z/(n_0 M))^4 with M = L^m, abelian action ||dA||².

- Φ_m: the level-m block fluxes, from the linear block map, which note 19
  (2.1) shows is exact.
- F_min: the minimizer of ||F||² over exact F with prescribed Φ_m. It is the
  Gaussian conditional mean E[F | Φ_m].
- Φ_{m-1} = G Φ_m: its level-(m-1) block fluxes. G is translation
  invariant under level-m shifts and is computed exactly by alias sums in
  Fourier space, using an eigh pseudo-inverse of the 6×6 level-m flux
  covariance.

Sanity check: for a smooth exact Φ_m, the sum of G Φ_m over the L⁴ children
equals L²Φ_m (that is, L⁴ · Φ_m/L²) to machine precision.

**Restriction to exact fluxes.** The pseudo-inverse representation of G is
not ℓ¹-summable. Its row sums grow like log n_0: 3.30, 3.58, 3.78 for
n_0 = 6, 8, 10 at L = 2, m = 1. The reason is that projecting onto exact
2-forms is nonlocal (a |x|^{-4} kernel). The correct quantity is the norm
of the row on the subspace of exact coarse 2-forms. By duality, that is the
minimal ℓ¹ norm over all extensions:

    s(row) = min_{c, h} || g - d'^T c - h ||_1,

over coarse 3-forms c and per-orientation constants h. These span the
annihilator of the exact 2-forms on the torus. The script solves this as a
linear program with HiGHS.

## 2. Results (n_0 = 6)

Rows are (child offset u, orientation a). The table gives the
exact-restricted norm and, in brackets, the pseudo-inverse ℓ¹ sum.

| L, m | row (corner, a = 01) | other rows |
|---|---|---|
| 2, 1 | 1.539 [3.30] | origin 0.612 [1.47]; (u = 5, a = 03) 1.213 [2.33] |
| 2, 2 | 1.633 [3.30] | origin 0.905 [1.69]; (u = 5, a = 03) 1.437 [2.53] |
| 2, 3 | 1.688 [3.35] | — |
| 3, 1 | 1.122 [1.99] | origin 0.414 [0.86]; center 0.353 [0.95]; corner, a = 23: 1.122 |
| 4, 1 | 0.773 [1.30] | — |
| 5, 1 | 0.547 [0.89] | — |

Each value is the exact norm of that row on the 6⁴ coarse torus. So it is a
lower bound for s_L there (s_L is the maximum over rows), and only the rows
listed were computed. Torus-size dependence: see §4.

## 3. Interpretation

Coarse flux patterns that alternate at the block scale (coarse momenta near
π) are strongly suppressed by the block-averaging kernel, whose multiplier
is a product of Dirichlet kernels. To reproduce such a coarse pattern with
unit amplitude, the fine minimizer needs fine fluxes of order one in some
children. These are the children at the far corner of the block, where the
averaging squares of several coarse plaquettes overlap. Smooth coarse
fields give children of size Φ/L², as expected. The sup norm sees the
oscillating ones.

For the programme:

1. **Note 34 Theorem 3** needs ρ_L = (1-η)/s_L > 1. For L = 2, 3 it fails.
   For L = 4 the corner row gives 0.77 at m = 1 (about 0.85 with the m-growth
   seen at L = 2), but that is a lower bound for s_L (§2), so the condition
   is suggested for L >= 4 and not established; it would need every row and
   the torus-size dependence (§4). Balaban's L is a large fixed integer
   (odd, > 11, CMP 109 p. 251), where the fitted s_L ≈ 3.4 L^{-1.1} is small,
   but the same caveat applies. [Audit 2026-10-09, T82: the values of §2 are lower bounds for s_L.]
   [T53, §5: the largest L = 4 row found is 0.88 (m = 1, n_0 = 6), about
   0.97-1.01 with the m-growth, so the condition is not suggested for L = 4;
   for L = 5 the largest row found gives about 0.74-0.77.]
2. **Note 33 §1 reading**: the L^{-4} per level for transported
   gauge-invariant functions is a low-momentum statement only. Note 33's
   Theorem 3 does not depend on it.
3. **(S1) in plain sup norms.** For transported irrelevant polymers, the
   per-step factor in sup norm over the coarse domain is at best about
   L^d s_L^n for degree-n vanishing. With s_L ~ L^{-1.1} and d = 3, n = 2,
   this exceeds 1. So the contraction in (S1) must use the regularity
   (derivative) conditions of Balaban's domains. README caveat added.
4. An **energy (ℓ²)** form of (D2) would avoid the oscillating patterns,
   because they cost coarse action. It is not developed here.

## 4. Torus size

**Not verified.** The L = 2, m = 1 corner row on an 8⁴ coarse torus was
attempted twice. One run was lost to a container restart. The other was
stopped at the 2-hour background limit before HiGHS finished. That LP has
6 · 8⁴ residual variables and 4 · 8⁴ + 6 free variables.

So all exact-restricted values in §2 are for the 6⁴ coarse torus only.
Their n_0-dependence is unknown. For comparison, the pseudo-inverse row
sums grow with n_0 (3.30, 3.58, 3.78 for n_0 = 6, 8, 10), but those are not
the exact-restricted norms. If this check is repeated, a first-order method
or a smaller symmetric subproblem (cubic symmetry of the corner row) would be
needed.

## 5. Twisted Bloch sectors (T53)

Note 36 (holonomy caveat) says that the sup-norm constant of the twisted
abelian map (note 54 §1) equals s_L^{ab} up to wrap-around corrections
O(e^{-δ n_0}), because unimodular phases do not change |kernel|. It was not
recomputed. This section recomputes it with the exact-flux norm of §1.

Script: `twist` and `twistcheck` modes of
`research/scripts/t27_minimizer_regularity.py`. Output:
`research/scripts/t27_minimizer_regularity_twist.out`.

**Setup.**

- *Sector.* Fields are quasi-periodic, Φ(Y + n_0 e_μ) = e^{iθ_μ} Φ(Y). The
  coarse momenta are K ∈ (2π/n_0)(Z⁴ + θ/(2π)). The fine aliases
  (K + 2πℓ)/M and the per-K formula for the minimizer are unchanged (note 54
  §1). Main runs use the diagonal twist θ_μ = θ, with θ = π/4 and π/2. One
  further run uses the one-direction twist (θ, 0, 0, 0) for L = 2. The
  twists θ and -θ give the same norms (complex conjugation).
- *Norm.* The twisted fields are complex (the charged components), so the
  sup norm uses the complex modulus. The twisted complex has no cohomology:
  dim ker D_θ = 3 n_0⁴ (checked at n_0 = 4), the dimension of the exact
  2-forms. So exact =
  closed, and the row norm is s(row) = min_c Σ_b |g_b - (D_θ^T c)_b|, with
  D_θ the twisted Bianchi map and no constants h.
- *Solver.* The complex ℓ¹ norm is not an LP, so it is bracketed:
  - lo: the LP with |z| replaced by max_k Re(z e^{-2πik/n_dir}), which is
    <= s (n_dir = 32 at n_0 = 4, 16 at n_0 = 6);
  - hi: the complex ℓ¹ norm of the LP's residual, which is >= s.

  At θ = 0 the rows are real, and n_dir = 4 gives s exactly.
- *Checks* (`twistcheck`): θ = 2π reproduces θ = 0, and θ = 0 reproduces
  the T27 rows (both to 1e-16); the twisted row reproduces the multiplier on
  twisted plane waves (1e-15); D_θ annihilates twisted curls (1e-15). The
  θ = 0 path reproduces T27's 1.5392 (L = 2, far corner, n_0 = 6). Rows
  related by an axis permutation agree.
- *Rows.* A row is (u, a): the child offset u = (u_0, u_1, u_2, u_3) in
  {0, ..., L-1}⁴ and the orientation a = μν of the image plaquette, as in §2
  (the far corner is u = (L-1, ..., L-1)).

**Full row maxima at n_0 = 4.** For θ = 0 and for the diagonal twist, the
axis permutations are symmetries. So one row per orbit (9, 36 and 100 rows
for L = 2, 3, 4) gives the maximum over all rows, that is, s_L on the 4⁴
coarse torus, up to the bracket:

| L | s_L(0) | s_L(π/4) | s_L(π/2) | largest row (all three θ) |
|---|---|---|---|---|
| 2 | 1.5011 | [1.4918, 1.4922] | [1.4462, 1.4469] | far corner |
| 3 | 1.2400 | [1.2144, 1.2152] | [1.1418, 1.1429] | u = (1,1,2,2), a = 23 |
| 4 | 0.8606 | [0.8434, 0.8441] | [0.7897, 0.7905] | u = (1,1,3,3) (ties: (1,2,3,3), (2,2,3,3)), a = 23 |

For L = 3 and 4 the largest row is **not** the far-corner row of §2. It is
the child at the far corner in the plaquette's own plane and in the
interior of the block in the other two directions. At n_0 = 4 the far-corner
rows are 1.0770 (L = 3) and 0.7366 (L = 4). For L = 2 the block has no
interior, and the far corner is largest (tied with every row at the far
corner of the plaquette's plane).

**Rows at n_0 = 6.** These are the same kind of values as §2: exact norms of
single rows, so lower bounds for s_L(θ). The θ = 0 entries marked * are the
T27 values of §2; the others are new.

| L | row | θ = 0 | θ = π/4 | θ = π/2 |
|---|---|---|---|---|
| 2 | far corner, a = 01 | 1.5392* | [1.5360, 1.5371] | [1.5255, 1.5274] |
| 2 | u = (0,1,0,1), a = 03 | 1.2133* | [1.2186, 1.2196] | [1.2244, 1.2257] |
| 2 | origin, a = 01 | 0.6117* | [0.6149, 0.6156] | [0.6214, 0.6222] |
| 3 | u = (1,1,2,2), a = 23 | 1.2576 | [1.2496, 1.2508] | [1.2299, 1.2311] |
| 3 | u = (0,1,2,2), a = 23 | 1.1874 | [1.1815, 1.1826] | [1.1651, 1.1662] |
| 3 | far corner, a = 01 | 1.1220* | [1.1178, 1.1189] | [1.1043, 1.1054] |
| 3 | origin, a = 01 | 0.4139* | [0.4188, 0.4193] | [0.4272, 0.4279] |
| 3 | u = (1,1,1,1), a = 01 | 0.3531* | [0.3574, 0.3586] | [0.3646, 0.3661] |
| 4 | u = (1,1,3,3), a = 23 | 0.8807 | [0.8746, 0.8755] | [0.8585, 0.8594] |
| 4 | far corner, a = 01 | 0.7731* | [0.7696, 0.7704] | [0.7588, 0.7596] |
| 4 | origin, a = 01 | 0.2875 | [0.2907, 0.2910] | [0.2960, 0.2965] |
| 5 | u = (2,2,4,4), a = 23 | 0.6747 | — | — |
| 5 | far corner, a = 01 | 0.5467* | — | — |

**What the numbers show.**

1. *Size of the effect.* The twist lowers the largest rows and raises the
   small ones. At θ = π/2:
   - the largest row drops by 3.6%, 7.9% and 8.2% (L = 2, 3, 4) at
     n_0 = 4, and by 0.8%, 2.2% and 2.5% at n_0 = 6;
   - the origin rows rise by 12-15% at n_0 = 4, and by 1.7-3.3% at
     n_0 = 6.

   At θ = π/4 the changes are a quarter to a half of these. From n_0 = 4 to
   n_0 = 6 the gaps shrink by a factor of 3 to 8. This fits note 36's
   statement that the difference is a wrap-around effect that vanishes as
   n_0 -> ∞. Two torus sizes do not fix the rate (e^{-δ n_0} or a power of
   n_0), so note 36's O(e^{-δ n_0}) is not confirmed.
2. *Direction.* For the diagonal twist, the twisted maximum is at most the
   periodic one in every computed case: the full maxima at n_0 = 4
   (L = 2, 3, 4, both θ) and the largest-row class at n_0 = 6. The
   one-direction twist (θ, 0, 0, 0) can raise it slightly (L = 2; one row
   per orbit of the permutations of axes 1-3, 24 rows):

   | n_0 | s_L(0) | θ = π/4 | θ = π/2 |
   |---|---|---|---|
   | 4 | 1.5011 | [1.5047, 1.5049] (+0.25%) | [1.5078, 1.5082] (+0.46%) |
   | 6 | 1.5392 | [1.5398, 1.5401] (+0.05%) | [1.5403, 1.5404] (+0.07%) |

   At n_0 = 4 these are full maxima. At n_0 = 6 they are the two rows that
   are largest at n_0 = 4: plaquettes in planes orthogonal to the twisted
   direction, at the far corner of their plane. So the twisted sectors can
   raise the sup-norm constant, but by an amount that shrinks with n_0
   (here by a factor of 5 to 7 from n_0 = 4 to 6). In note 36's bound
   s_L^{NA} <= s_L^{ab}(1 + Cε_0) + Cε_0, s_L^{ab} must be the maximum over
   sectors, not the periodic value. Numerically the two differ by less than
   the other uncertainties (rows, torus size, depth). This is numerical
   evidence, not a proof.
3. *Note 36's reason is not a proof.* The twisted kernel is the image sum
   Σ_n e^{-iθ·n} G_∞(D + n_0 n). That is not a phase times the periodic
   image sum Σ_n G_∞(D + n_0 n). The exact-flux subspace also changes: for
   θ ≠ 0 there are no harmonic constants, so the dual problem changes too.
   Both are wrap-around effects, but their size depends on the decay of the
   exact-restricted kernel, which is not known. The pseudo-inverse
   representation decays only like |x|^{-4} (§1).
4. *Consequence for §§2-3 (θ = 0).* The far-corner rows underestimate s_L
   for L >= 3. At n_0 = 6, m = 1, the largest rows found are:
   - L = 3: 1.2576 (far corner 1.122);
   - L = 4: 0.8807 (far corner 0.773);
   - L = 5: 0.6747, row u = (2,2,4,4), a = 23 (far corner 0.547). Only
     four L = 5 rows were computed: the far corner and u = (1,1,4,4),
     (1,2,4,4), (2,2,4,4) in plane 23 (0.6079, 0.6380, 0.6747).

   Apply the depth growth seen at L = 2 (m = 1 -> 3: factor 1.097; the
   extrapolated limit 1.76 gives 1.14). Then L = 4 gives 0.97-1.01 and
   L = 5 gives 0.74-0.77. So s_L < 1 is no longer suggested for L = 4, only
   for L >= 5. All of these are still lower bounds: some rows, one torus,
   and m = 1 with a depth factor borrowed from L = 2.
5. *Not computed:* m >= 2; n_0 >= 8; twists other than those listed; at
   n_0 = 6, rows other than those listed; twisted sectors for L >= 5.
