# Monte Carlo test of M1-3D: terminal block observables converge across depths

Status: **computation** (T50). Script:
`research/scripts/t50_mc_terminal_convergence.py`. Output:
`t50_mc_terminal_convergence.out`. This is numerical evidence for the
conjecture P4-3D / M1-3D. It is not a proof.

## Setup

- Model: SU(2), Wilson action, d = 3. The lattice at depth N is
  (Z/(n_0 L^N))³ with n_0 = 4 and L = 2.
- Coupling: β_N = β_0 L^N, which is CMP 102 (1) with g²ε_0 fixed. In 3D
  this is the exact bare scaling; there is no coupling renormalization to
  tune.
- Terminal map: each configuration is mapped N times through Balaban's
  one-step average (CMP 98 (42), corner blocks, contours of CMP 95 (1.7))
  to the terminal lattice (Z/4)³.
- Observables, on the terminal lattice:
  - the averaged plaquette P = ⟨½ tr V(∂p)⟩;
  - the 1×2 loop W12;
  - |½ tr Polyakov|², denoted PL2.
- Sampling: Creutz heat bath with two over-relaxation sweeps per update.
  200 thermalization updates, then 400 measurements, one every 2 updates.
  Errors come from 10 bins.
- Checks:
  - quaternion algebra, and log/exp, to 1e-16;
  - gauge covariance of the implemented average, Q(U^g) = Q(U)^{g_c}, to
    4e-15;
  - the heat-bath plaquette at β = 0.5 matches the strong-coupling value
    I_2/I_1 to 0.5%;
  - a hot-start rerun of (β_0 = 2, N = 2) reproduces the cold-start value
    within errors (0.6470(20) vs 0.6474(14)).

## Results

| β_0 | N | fine lattice | β_N | P | W12 | PL2 | fine plaquette |
|---|---|---|---|---|---|---|---|
| 4 | 0 | 4³ | 4 | 0.7292(12) | 0.5497(26) | 0.262(2) | 0.7292 |
| 4 | 1 | 8³ | 8 | 0.8183(6) | 0.6564(11) | 0.274(3) | 0.8708 |
| 4 | 2 | 16³ | 16 | 0.8504(7) | 0.7057(17) | 0.295(8) | 0.9365 |
| 4 | 3 | 32³ | 32 | 0.8627(7) | 0.7251(19) | 0.271(8) | 0.9685 |
| 4 | 4 | 64³ | 64 | 0.8681(16) | 0.7321(39) | 0.315(14) | 0.9843 |
| 2 | 0 | 4³ | 2 | 0.4534(22) | 0.2078(22) | 0.249(2) | 0.4534 |
| 2 | 1 | 8³ | 4 | 0.5530(16) | 0.2773(23) | 0.249(2) | 0.7275 |
| 2 | 2 | 16³ | 8 | 0.6474(14) | 0.3754(25) | 0.250(2) | 0.8705 |
| 2 | 3 | 32³ | 16 | 0.6830(19) | 0.4178(39) | 0.252(2) | 0.9365 |

Increments Δ_N = X_{N+1} - X_N and their successive ratios:

| β_0 | X | Δ_0, Δ_1, ... | ratios | geometric extrapolation |
|---|---|---|---|---|
| 4 | P | 0.089, 0.032, 0.012, 0.0054 | 2.77, 2.61, 2.3 | 0.872 |
| 4 | W12 | 0.107, 0.049, 0.020, 0.0069 | 2.17, 2.53, 2.8 | 0.736 |
| 2 | P | 0.100, 0.094, 0.036 | 1.06, 2.65 | 0.705 |
| 2 | W12 | 0.069, 0.098, 0.042 | 0.71, 2.32 | 0.450 |

## What this shows

1. **Convergence.** The terminal Balaban-averaged observables converge as
   the cutoff is removed at fixed g²ε_0. The fine-lattice plaquette, in
   contrast, tends to 1. At β_0 = 4 the increments decay geometrically from
   the first step, with ratio about 2.6 ≈ L^{1.4}. That gives an empirical
   σ ≈ 1.4 in note 18's L^{-σN}, consistent with σ >= 1 from the O(g²ε_N)
   one-step defects.
2. **Onset at stronger coupling.** At β_0 = 2 (g²ε_0 = 2, so g²ℓ = 8) the
   first two increments are flat. Geometric decay with the same ratio,
   about 2.5, sets in once the finest coupling β_N >= 8. This matches the
   RG picture: the decay starts when the fine steps are weakly coupled.
3. **The iterated average is essential.** Each step's contours are O(L)
   links of the current lattice, so the contour self-energy per step is
   O(g_k²), which is summable in 3D. A one-shot average along contours of
   physical length would carry a logarithmically divergent self-energy.
4. **Polyakov loops.** PL2 stays near the Haar value 1/4 at β_0 = 2. At
   β_0 = 4 it lies between 0.26 and 0.32, with larger errors, because of
   slow tunnelling in this small box. It is not used for rates.

## Limits

- The data reach N <= 4 (64³) at β_0 = 4 and N <= 3 at β_0 = 2. The N = 4
  point has larger errors (one run, 5800 s). Its increments, 0.0054 for P
  and 0.0069 for W12, continue the geometric decay, and the predicted limits
  of P (0.870 from N <= 3, 0.872 with N = 4) agree.
- n_0 = 4 is a small terminal lattice, and the statistics are modest. The
  geometric extrapolations are indicative only.
- Only L = 2 was tested. CMP 109 uses odd L > 11 for symmetry, and CMP 98's
  average is defined for any L.
