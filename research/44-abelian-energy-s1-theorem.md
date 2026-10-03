# (S1) for first differences, abelian, energy norm: a theorem

Status: **proved** (T37), for the abelian 4D theory with Balaban's linear
block flux: Theorem 1 (first differences, M^{-1}), Corollary 2 (image
differences, L^{-1}) and Theorem 3 (image second differences, L^{-3/2}). The sharp constant is computed in
`research/scripts/t37_energy_s1_constant.py` (output `.out`).

## Statement

Fine torus (Z/(n_0 M))^4 with M = L^m. Fine fluxes F are exact 2-forms, and
the level-m block fluxes Φ = W F are given by note 19 (2.1). For exact
coarse data Φ let F_min be the minimizer of ||F||_2 subject to W F = Φ.
Write ∇_ν F(x) = F(x + e_ν) - F(x).

**Theorem 1.** For every exact Φ and every direction ν,

    ||∇_ν F_min||_2 <= C M^{-1} ||F_min||_2,   C = 2π/√c_0,   c_0 = 1024/π^{10},

so C <= 60.1. Numerically the sharp constant is C_M = 2.71, 3.13, 3.39,
3.65, 3.77, 3.87, 3.91 for M = 2, 3, 4, 6, 8, 12, 16, tending to about 4.

**Corollary 2 (one RG step).** Let Φ' = W_{M/L} F_min be the level-(m-1)
image fluxes, and ∇' the difference operator on the level-(m-1) lattice.
Then

    ||∇'_ν Φ'||_2 <= C L^{-1} ||F_min||_2.

So the first differences of the image (dimension-5 data) are O(L^{-1}) of
the energy, uniformly in m. This bound covers every pair of neighbouring
level-(m-1) cells, including pairs across block faces.

## Proof of Theorem 1

1. *Euler-Lagrange.* Minimizing ||F||² over exact F with W F = Φ gives
   F_min = P_2 W^T λ, where P_2 = d Δ^{-1} d* is the projection onto exact
   2-forms and λ is a Lagrange multiplier. Hence F_min = d Δ^{-1} J with
   J := d* W^T λ. The 1-form J is co-closed.
2. *Exact factorization of J in Fourier.* For coarse momentum K the fine
   aliases are p_ℓ = (K + 2πℓ)/M. By note 19 (2.3) the (μν) component of
   W^T λ has the factor Π_j D_M(p_j) · D_M(p_μ) D_M(p_ν), times λ̂_{μν}(K).
   The divergence multiplies the (νρ) component by the backward difference
   (1 - e^{-ip_ν}), and

       (1 - e^{-ip_ν}) D_M(p_ν) = 1 - e^{-iM p_ν} = 1 - e^{-iK_ν},

   which is the same for every alias. So

       J_ρ(p_ℓ) = A_ρ(p_ℓ) c_ρ(K),   A_ρ(p) := Π_j D_M(p_j) · D_M(p_ρ),

   with c_ρ(K) = M^{-4} Σ_ν (1 - e^{-iK_ν}) λ̂_{νρ}(K), up to unimodular
   phases. All alias dependence sits in the explicit product A_ρ.
3. *Energy of F.* Since J is co-closed, |(dΔ^{-1}J)(p)|² = |J(p)|²/|r(p)|²,
   with |r(p)|² = Σ_j 4 sin²(p_j/2). Choose the alias p_0 with |K_j| <= π.
   Then |r(p_0)|² <= 4π²/M², so

       ||F_min||² >= Σ_K |J(p_0(K))|² M²/(4π²).
4. *Alias-0 fraction.* By the Fejér/Parseval identity
   Σ_ℓ |D_M(p_ℓ,j)|² = M², and |D_M(K_j/M)| >= 2M/π for |K_j| <= π
   (using |sin(K/2)| >= |K|/π and |sin(K/2M)| <= |K|/(2M)):
   - each coordinate j != ρ contributes a fraction |D|²/Σ|D|² >= 4/π²;
   - the coordinate ρ carries |D|⁴, and since Σ_ℓ|D|⁴ <= M² Σ_ℓ|D|² = M⁴,
     its fraction is >= (2M/π)⁴/M⁴ = 16/π⁴.

   Hence |A_ρ(p_0)|² >= c_0 Σ_ℓ |A_ρ(p_ℓ)|² with c_0 = (4/π²)³ · 16/π⁴, and
   so |J(p_0)|² >= c_0 Σ_ℓ |J(p_ℓ)|² for each K. With step 3,
   ||F_min||² >= c_0 M² ||J||²/(4π²).
5. *Gradient.* ∇_ν F = ∇_ν d Δ^{-1} J has Fourier multiplier of modulus
   |e^{ip_ν} - 1| |J|/|r| <= |J|. Hence ||∇_ν F_min|| <= ||J||.
6. Combine steps 4 and 5. ∎

## Proof of Corollary 2

A level-(m-1) cell difference in direction ν equals the image of the fine
shift by M/L sites:

    ∇'_ν Φ' = W_{M/L} (τ_{(M/L)e_ν} F - F).

Telescoping gives ||τ_{(M/L)e} F - F|| <= (M/L) ||∇_ν F||.

Next, ||W_{M_1}||_{2->2} <= 1 with M_1 = M/L. Per coarse momentum, apply
Cauchy-Schwarz over the M_1⁴ aliases. The kernel M_1^{-4} Π_j D · D_μ D_ν
has squared alias sum <= M_1^{-8} · (M_1²)² · (M_1⁴)² = M_1⁴, using
Σ_ℓ |D|² = M_1² for the two transverse coordinates and Σ_ℓ |D|⁴ <= M_1⁴ for
the two tent coordinates. Together with the sampling factor M_1^{-4}, this
gives norm <= 1. The bound is attained on constant fields: a constant flux
F gives Φ' = M_1² F on M_1^{-4} times as many cells.

Apply Theorem 1. ∎

## What this settles, and what it does not

- **Settled.** For the abelian linearization, the energy-norm form of (S1)
  holds for the first irrelevant structure (first differences, dimension 5).
  The rate is the power-counting one, L^{-1} per step, with an explicit
  constant (<= 60 proved, about 4 sharp). It covers all positions,
  including block faces. Note 43's per-row data are a different (dual,
  worst-row) quantity. Their slower cross-face decay at small L does not
  contradict this global energy bound.
- **Why the sup norm failed** (note 35). The theorem uses the co-closed
  factorization, the identity (1 - e^{-ip}) D_M(p) = 1 - e^{-iK}, and the
  energy of the lowest alias. All three are ℓ² facts. The worst-case
  sup-norm configurations of note 35 are inputs whose energy sits mostly in
  high aliases. In the energy norm they are penalized by the factor
  1/|r|², which is large for the lowest alias.
- **Not settled.**
  - Higher differences (dimension >= 6) need the same argument with ∇²; the
    same factorization should give M^{-2}.
  - The non-abelian theory linearizes to this one (note 36), with nonlinear
    remainders controlled in Balaban's sup norms.
  - The full (S1) also needs the generated (non-transport) terms. Those are
    (S2) (note 42).

So (S1)'s transport part is now a theorem in the abelian linearization. The
remaining (S1) work is the nonlinear, non-abelian transfer.

## Addendum: second differences (dimension 6), computed

Sharp ratios sup ||∇_μ∇_ν F_min|| / ||F_min|| (same script, `run2`):

| M | ratio | M × ratio | M^{1.5} × ratio |
|---|---|---|---|
| 2 | 1.897 | 3.79 | 5.37 |
| 4 | 1.025 | 4.10 | 8.20 |
| 8 | 0.475 | 3.80 | 10.75 |
| 16 | 0.193 | 3.08 | 12.33 |

The local exponent rises from 1.0 to 1.3 (M = 8 -> 16). It appears to
tend to 3/2, not 2.

The reason is that J = d* W^T λ has jumps: the derivatives of the tent
factors are piecewise constant. So ∇F_min has kinks on block faces, and
F_min is in H^{3/2-} but not H². This matches Balaban's C^{1,β} (β < 1)
regularity of minimal configurations (CMP 102b (9), with constant
B_4(β_0)).

For one RG step this gives a heuristic estimate. Second differences of the
level-(m-1) image over cells of size M/L see the kinks only within M/L of a
face. The energy is then about (M/L)·(F/M) in amplitude on a fraction
(M/L)/M of the positions, so the norm gain is about L^{-3/2}.
Dimension-6 data therefore contract by about L^{-3/2} per step in the
energy norm, not L^{-2}. That is still a contraction, but weaker than naive
power counting. This part is computed, not proved.

## Theorem 3 (second differences of images; proved)

With M_1 = M/L and Δ²_ν := (τ_{M_1 e_ν} - 1)²,

    ||W_{M_1} Δ²_ν F_min||_2 <= ||Δ²_ν F_min||_2 <= C_3 L^{-3/2} ||F_min||_2,

where C_3 depends only on d = 4 (an explicit, crude constant). So
dimension-6 data on the level-(m-1) lattice contract by L^{-3/2} per step in
the energy norm, uniformly in the depth m.

*Proof.*

1. *Multiplier.* ||Δ²_ν F||² = Σ_K Σ_ℓ |e^{iM_1 p_ν} - 1|⁴ |J(p_ℓ)|²/|r(p_ℓ)|².
   Since |e^{ix} - 1| <= min(|x|, 2) and |p| <= (π/2)|r_ν| for |p| <= π,
   we have |e^{iM_1 p_ν} - 1|⁴ <= min((π/2)⁴ M_1⁴ |r_ν|⁴, 16). Also
   1/|r|² <= 1/|r_ν|².
2. *The ν coordinate.* Write J_ρ = A_ρ c_ρ, as in Theorem 1. A_ρ contains
   |D_M(p_ν)|², and |r_ν|² |D_M(p_ν)|² = |1 - e^{-iK_ν}|² <= K_ν². So the
   ν factor is

       Σ_{ℓ_ν} min((π/2)⁴ M_1⁴, 16/|r_ν(p_ℓ)|⁴) K_ν².

   The alias at distance d >= 1 from the lowest has |r_ν| >= 2(2d - 1)/M.
   Splitting at d ~ L gives a total <= C(L M_1⁴ + M⁴/L³) = 2C M⁴/L³.
3. *Other coordinates.* Use the Parseval identities of Theorem 1: Σ_ℓ |D|² = M²
   and Σ_ℓ |D|⁴ <= M⁴. They give at most M⁸ (for ν = ρ the extra |D_ν|²
   gives the same total). Hence ||Δ²_ν F||² <= C|K|² M^{12} L^{-3} Σ_K |c|².
4. *Lower bound.* As in Theorem 1, steps 3-4,
   ||F_min||² >= (M²/4π²)(2/π)^{10} M^{10} Σ_K |c|².
5. Divide, using |K| <= 2π. ||W_{M_1}|| <= 1 by the Corollary 2 proof. ∎

This turns the addendum's heuristic L^{-3/2} into a theorem. The computed
fine-scale exponent rises towards 3/2 (local 1.3 at M = 16), which is
consistent: the M^{-3/2} rate for fine second differences follows from the
same proof with M_1 = 1.
