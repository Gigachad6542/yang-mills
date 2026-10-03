# Transport in the energy norm: the gain sup norms miss

Status: **computation** (T36). Script and output:
`research/scripts/t36_l2_rows.py`, `t36_l2_rows.out`.

## Question

Note 35 found that, in plain sup norms over the coarse small-field domain,
the minimizer's image fluxes are only about L^{-1.1} times the coarse fluxes,
not L^{-2}. CMP 109 p. 259 says Balaban's irrelevance bound (0.29) is not a
per-step RG contraction (note 29 §3; T35). So (S1) is a new theorem, and the
choice of norm matters. This note asks what the same transport looks like in
the **energy (ℓ²) norm**. That is the norm in which Gaussian and
measure-averaged statements live (notes 19, 32, 33).

## Method

Abelian 4D theory, Balaban's linear block flux, fine minimizer given level-m
fluxes, level-(m-1) image fluxes (as in note 35), coarse torus 8⁴.

For a kernel row g, the norm of Φ ↦ ⟨g, Φ⟩ on **exact** coarse fluxes in ℓ²
is ||P_ex g||_2, where P_ex is the orthogonal projection onto exact coarse
2-forms. This is computed by FFT, with no linear program needed.

## Results

**Single rows** (m = 1; for L = 2 also m = 2, 3):

| L | max_rows ||P_ex g||_2 | mean over rows | L⁴ · mean² |
|---|---|---|---|
| 2 | 0.353 | 0.193 | 0.59 |
| 3 | 0.255 | 0.099 | 0.79 |
| 4 | 0.164 | 0.059 | 0.90 |
| 5 | 0.119 | 0.039 | 0.97 |

At L = 2 the maximum is 0.353, 0.339, 0.334 for m = 1, 2, 3, so it is
stable in m.

**Neighbouring children** (u and u + e_ν in the same block). These are the
rows of a dimension-5 difference operator:

| L | max ||P_ex(g_u - g_{u+e})||_2 | L² × max | mean of ||P_ex(g_u - g_{u+e})|| / ||P_ex g_u|| | L × mean ratio |
|---|---|---|---|---|
| 2 | 0.302 | 1.21 | 1.130 | 2.26 |
| 3 | 0.157 | 1.41 | 0.744 | 2.23 |
| 4 | 0.081 | 1.29 | 0.573 | 2.29 |
| 5 | 0.048 | 1.21 | 0.466 | 2.33 |

## Reading

1. **Energy is conserved by transport.** L⁴·(mean row)² tends to 1. The
   image fluxes of the L⁴ children carry the coarse energy, with neither
   amplification nor loss. This is 4D scale invariance at the level of
   kernels, the marginal structure.
2. **Differences gain exactly L^{-1} in the energy norm.** The mean ratio is
   2.3/L to within 3% for L = 2-5. The largest difference row is about
   1.3 L^{-2} at every L. A dimension-5 structure is thus suppressed by the
   power-counting factor L^{-1} per step, with constant about 2.3. So
   2.3/L < 1 already for L >= 3.
3. **Contrast with sup norms** (note 35). There the single-row constant is
   about 3.4 L^{-1.1}, and summing over the L^d children per block destroys
   any gain. The obstruction comes from worst-case configurations that
   oscillate at the block scale. In the energy norm those configurations
   cost coarse energy, and the gain reappears.

## Consequence for (S1)

(S1), the per-step contraction of irrelevant data, should be formulated in
an energy-type (ℓ², or measure-averaged) norm, not in Balaban's sup norms
over small-field domains. In that norm:

- the marginal (charge) part is transported with norm about 1. That is note
  33's charge conservation, and here it is seen in kernels;
- the first irrelevant (difference, dimension 5) part contracts by about
  2.3/L per step, which is the power-counting rate.

This is a computation in the abelian (linear) theory. The non-abelian
statement would linearize as in note 36. The analytic (sup-norm) control of
Balaban's activities is still needed for the nonlinear remainders. The
proposed structure is mixed: energy norms for transport and contraction,
sup norms for the analytic remainders.
