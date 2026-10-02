# Minimizer regularity (D2) in the abelian 4D theory: exact sup-norm constants

Status: **computation** (T27). Script:
`research/scripts/t27_minimizer_regularity.py`.

- **Result.** In the abelian 4D Gaussian theory with Balaban's linear
  block flux (note 19 (2.1)), the sup-to-sup norm s_L of the map
  "level-m block fluxes ↦ level-(m-1) image fluxes of the fine minimizer",
  restricted to exact coarse fluxes, is **not** O(L^{-2}). Measured on the
  far-corner child row, which is the largest row found:

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
    s_L < 1. This holds for L >= 4 and fails for L = 2, 3.
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

1. **Note 34 Theorem 3** holds with ρ_L = (1-η)/s_L > 1 when L >= 4. For
   L = 4, s ≈ 0.77 at m = 1, and the m-growth seen at L = 2 (about 10%)
   keeps it below 1. Balaban's L is a large fixed integer, so this is
   compatible. L = 2, 3 are excluded.
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

The L = 2, m = 1 corner row at n_0 = 8 (pending at the time of writing; see
the PROGRESS line) checks the n_0-dependence of the exact-restricted value.
