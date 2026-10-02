# Note 29's single-step hypotheses in the 4D SU(2) Migdal-Kadanoff RG

Status: **computation** (T32). Script and output:
`research/scripts/t32_mk_single_step.py`, `t32_mk_single_step.out`.

**Model.** This is the exactly computable Migdal-Kadanoff (MK) recursion
for SU(2) lattice gauge theory in d = 4 with L = 2. The plaquette weight f is
a class function with character coefficients c_m = a_m/(d_m a_0), m = 2j.
One step:

- bond moving: f -> f^{L^{d-2}} = f⁴ (pointwise on the group);
- decimation: c_m -> c_m^{L²} = c_m⁴.

MK is not Balaban's RG. It is a nonlinear, asymptotically free 4D gauge
recursion with a marginal coupling and irrelevant shape data. That makes it
a test of whether the hypotheses of note 29 (shooting lemma) are mutually
consistent and have the claimed orders.

**Coordinates.**

- Inverse coupling x = 1/t, where c_1 = e^{-t C_2(1)} and C_2 = m(m+2)/4.
- Irrelevant shape coordinate w = u/t², from the fit
  -log c_m = t C_2 + u C_2² over the visible range t C_2 <= 8.

The one-step Jacobian is computed by central differences.

## Results

At the heat-kernel shape (w = 0):

| t | x' - x | e = \|∂x'/∂x - 1\| | c = \|∂x'/∂w\| | b = \|∂w'/∂x\| | θ = \|∂w'/∂w\| |
|---|---|---|---|---|---|
| 0.400 | -0.1272 | 9.4e-4 | 8.8 | 4.2e-5 | 0.0691 |
| 0.200 | -0.1261 | 2.2e-4 | 18.2 | 4.7e-6 | 0.0657 |
| 0.100 | -0.1255 | 5.4e-5 | 36.9 | 5.5e-7 | 0.0641 |
| 0.050 | -0.1253 | 1.3e-5 | 74.4 | 6.7e-8 | 0.0633 |
| 0.025 | -0.1251 | 3.3e-6 | 149 | 8.3e-9 | 0.0629 |

Away from it (w > 0; for w < 0 the c_m grow and f is not a positive
weight):

| t | w | e | c | b | θ | b·c |
|---|---|---|---|---|---|---|
| 0.2 | 0.01 | 0.034 | 15.6 | 1.6e-6 | 0.050 | 2.5e-5 |
| 0.2 | 0.05 | 0.136 | 9.9 | 2.6e-5 | 0.024 | 2.6e-4 |
| 0.05 | 0.01 | 0.035 | 63.7 | 3.4e-7 | 0.048 | 2.2e-5 |
| 0.05 | 0.05 | 0.136 | 40.2 | 2.7e-6 | 0.023 | 1.1e-4 |

## What this shows

1. **Asymptotic freedom.** x' - x -> -1/8 per step, a constant decrease of
   1/g². This is MK's one-loop coefficient.
2. **θ -> 1/16 = L^{-4}.** This is the scaling of the leading irrelevant
   (F⁴-type, dimension 8) shape coordinate, as power counting predicts. It
   is (S1) with a large margin.
3. **e = O(t²) = O(g⁴) at the heat-kernel shape.** The ratios are 4.26,
   4.12, 4.06, 4.03 per halving of t, matching note 29's ē = O(γ⁴). This is
   the summability-free marginal Lipschitz constant (S3).
4. **Only the product b·c is small, and it is O(t²).** Individually
   b ∝ t³ and c ∝ 1/t at w = 0. The product is invariant under rescaling
   the irrelevant coordinate, and it is exactly the quantity in note 29
   Theorem 1's condition (2.1), b̄c̄ <= ½(θ_1 - θ)(1 - θ_1 - ē).
   - Correction to note 29's §3 heuristic: "b, c = O(γ²) each" is
     coordinate dependent. The invariant statement is b̄c̄ = O(γ⁴) at the
     heat-kernel shape. Note 29 Theorem 1 itself needs only the product, so
     it is unaffected.
5. **e depends on the irrelevant data.** e ≈ 3.4 w, independent of t. So the
   marginal Lipschitz constant has a term linear in the current size of the
   irrelevant data. Along the flow w is tiny (w' = 0.0000 to four digits
   after one step from the heat kernel), so e_k stays O(g⁴). In the
   framework of note 29 this means e_k should be stated as
   e_k <= C(γ⁴ + δ̄_k), where δ̄_k is the irrelevant size of the flows.
   That is still compatible with ē < 1 - θ_1.

## Consequence for the programme

In an exactly computable asymptotically free 4D gauge RG:

- the hypotheses of note 29 Theorem 1 hold;
- θ = L^{-4} for the shape data;
- the constants have the predicted orders, once b and c are read as the
  invariant product.

This does not prove (S1)-(S3) for Balaban's RG. It shows that the reduction
of memory decay to single-step bounds asks for nothing inconsistent with
asymptotic freedom.
