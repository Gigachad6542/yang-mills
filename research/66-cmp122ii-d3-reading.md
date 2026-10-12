# CMP 122 II (1.79)-(1.99) at d = 3 with R = identity, read from the page images (T72)

**One-line verdict.** The domain-factor bookkeeping (1.79)-(1.89) survives at
d = 3 with R = identity after three changes (conditional reduction), and gives
the weight bound T_k(Y)1 <= exp(-2p_0(g_k) - κ_1 d_k(Y)) for unprocessed
large-field domains; but the exponentiated expansion (1.90)-(1.99) is the
R-operation's expansion of its first-class components, is vacuous at R = id,
has activity constant α^{1/3} (not a power of g_k) for polymers touching a
large-field domain, and does **not** localize CMP 102's sixth-order remainder.
So (H4a) stays a conditional reduction with two named gaps (§4, Q1).

Status:

- **Published input (d = 4, R on), read from the page images.** (1.79)-(1.99)
  and the pages around them (printed pp. 376-392), equation by equation (§2).
  The imported estimates ([I], [III], [IV], [14], [15], [16]) were not rechecked.
- **Conditional reduction (our reading at d = 3, R = identity).** The induction
  (1.80)-(1.88) closes at R = id with: (1) K replaced by K_end - j, and
  K_end - j < R_j on the exact 3D flow; (2) the extra-steps term of (1.88)
  dropped; (3) the product Π' of (1.79) deleted. Exponent conditions at d = 3:
  2p_0 > 5r (base, (1.82)) and p_0 > 4r (merge, refined) (§3). It rests on
  (1.79) for the unprocessed operations T_k, which II states for "all large
  field regions" (p. 383-384) but derives for the R-modified T'_k (§4, Q1).
- **Not a CMP 122 II statement / does not apply.** (1.97)-(1.99) as the
  large-field activity bound of note 65 §5; (1.92)-(1.99) as the localization
  of CMP 102 (22)-(24) (§4, Q3).
- **Corrections for notes 49, 61, 65 (§5, for the lead to apply).**

Script: `research/scripts/t72_cmp122ii_d3_checks.py`, output
`research/scripts/t72_cmp122ii_d3_checks.out` (scalar checks on the exact 3D
flow and the exponent conditions; Balaban's constants are not specified, so
only exponents and d-dependent inequalities are tested). Every number below
is printed there. It re-creates the salvaged wip script (only its .out
survived).

## 0. Sources, notation, what was read

- PDF `sources/papers/Balaban1989-CMP122-large-field-II.pdf`; printed page =
  PDF page + 354. Pages rendered and read as images: printed pp. 376-392
  (PDF 22-38). Not read as images: pp. 355-375 (definitions of Y_i, X_j and
  the preparatory steps; only the OCR was consulted for (i), (ii) of
  CMP 122 I, p. 177).
- Reference numbers inside II: [I] = CMP 109, [II] = CMP 116, [III] = CMP 119,
  [IV] = CMP 122 I, [14] = CMP 99 (regular configurations), [15] = CMP 102
  (variational problem), [16] = CMP 102 (UV stability, 3D).
- In II, p_0(g) = (log g^{-2})^{p_0} with A_0 pulled out (CMP 119 writes
  A_0(log g^{-2})^{p_0}); p_1(g) is a second power (A_1 p_1(g_j) =
  g_j^{-1}δ'_j, p. 383), probably p_1 < p_0 (CMP 122 I p. 186 (OCR): the ratio
  p_1(γ)/p_0(γ) "can be made arbitrarily small by choosing γ"); R_j is the
  smallest power of L with R_j >= (log g_j^{-2})^{r_0}, r_0 = r. d'_j(Z) is the
  linear size measured in MR_j-cubes. S(Z) = Z'^{~10}: the cover by
  LMR_{j+1}-cubes plus ten layers (p. 384). Conditions (i): contained in a
  cube of size 100MR_k; (ii): no new large field in the last N steps; N = R_j
  in (1.80).
- 3D flow (CMP 109 p. 259, note 65 §0): g_j² = g² L^{j-K}, x_j := log g_j^{-2} =
  x_K + (K-j) ln L; j increases toward the unit lattice K; x_j decreases in j.
  K_end = K is the unit-lattice index.
- Misprints noted: p. 385 prints "(then R_{m+1} = L R_m)"; the no-gain steps
  are those with R_{m+1} = R_m/L (CMP 122 I, p. 177: "in some steps the number
  R_k decreases by the factor L^{-1}"). The κ_1 of "−κ_1 d_k(X)" after (1.89)
  is the constant of p. 376 ("(κ_1 - 1)M^{-d}|Y'|"), not an index.

## 1. Structure of II §1, as read

1. pp. 378-383. The R-operation output is (1.72): a sum over large-field
   regions; components X_j of the first class become small field (operations
   T'_k(X_j)), components Y_i of the second class stay large-field. T'_k(X) of
   (1.71) integrates over the fluctuation field B, the fields V_h of the last N
   steps, and includes T_h(Z_h ∩ X). (1.73)-(1.75) reduce to T'_k(X)1.
2. (1.76)-(1.89). Bound for T'_k(X)1: (1.79) is the product of the one-step
   large-field factors with an entropy loss; (1.80)-(1.88) is the induction
   that the creation weight κ pays for all later steps; (1.89) is the
   consequence.
3. (1.90)-(1.99). Mayer expansion and exponentiation of the curly bracket of
   (1.72), the sum over first-class components X_j with the already localized
   small-field terms V(Y) of (1.68) as input; result (1.98)-(1.99).
4. (1.100)-(1.104) (context). R-terms with domain disjoint from the large
   field carry exp(-p_0(g_k)); the large-field domains Y_i in (1.104) have "no
   integral operations connected with them", only the multiplication by
   T'_k(Y_i)1 (p. 391-392).

## 2. Table: (1.79)-(1.99), page by page

Codes for "d = 3, R = id": `=` holds unchanged; `c` holds with the stated
change of constant, exponent or range; `0` absent or vacuous at R = id (the
R-operation produces nothing there); `!` the printed form is not what the
earlier notes use. "Entropy" columns give powers of R_j and M.

| p. | eq. | what it says | d = 3, R = id | d-dependence |
|---|---|---|---|---|
| 380 | text after (1.75) | every large-field domain Z_j contributes O(1) log g_j^{-2} \|Z_j\| <= O(1) M^d R_j^{d+1} d'_j(Z_j); normalization constants cost O(log g_j^{-2}) per site, not O(1) | `=`; `!` for note 65 input (E), which has O(1) per point | R_j^{d+1}, M^d |
| 380-381 | text, 381 top | fundamental large-field factors exp(-γ_0 min{B_3^{-2}A_0²/2, 2A_1², A_1²} p_0²(g_j)(d'_j(Z_j^(i)) + 1)) <= exp(-½γ_0A_1²p_0²(g_j)(d'+1) - 2p_0(g_j)); "almost exactly the same as in [16]" | `=` | none |
| 381 | (1.76) | Z_j ⊂ Z'_{j-1}^{~10} ∪ ∪_i (Z_j^(i))^{~2} | `=` (this is input (D) of note 65, m_0 = 10) | none |
| 381-383 | prose, (1.77)-(1.78) | preparatory-step factor exp(-R_j^{-d-5}p_1²(g_j)) <= exp(-p_0(g_j)) if 2p_1 - (d+5)r_0 > p_0; uses 6(100M(L+1)N^{β_0}R_j)^{d+2} (p. 382), a multi-step form of CMP 119 (2.9) second line | `0` (preparatory steps exist only with R) | (d+5)r_0; N^{β_0(d+2)} |
| 383 | (1.79) | T'_k(X)1 <= sup exp{Σ_{j=1}^k O(1)M^dR_j^{d+1}d'_j(Z_j)} Π_jΠ_i exp(-½γ_0A_1²p_0²(g_j)(d'_j(Z_j^(i))+1) - 2p_0(g_j)) Π' exp(-p_0(g_j)); Π' over components with (i), (ii) where large fields were created in the preparatory steps. p. 383-384: holds for all large-field regions, not only those with (i), (ii); sup over admissible histories (their count is inside the entropy term, "exp O(1)(MR_j)^{-d}\|Z_j\|", p. 383) | `c`: Π' deleted. The first two factors keep their form. Derived for the R-modified T'_k(X); for T_k at R = id the same one-step estimates apply (§3), not re-derived | R^{d+1}, M^d |
| 384 | (1.80) | κ_j(Z) >= Σ_{n=j+1}^{j+K} O(1)M^dR_n^{d+1}d'_n(S^{n-j}(Z)); K smallest with S^K(Z) obeying (i), (ii), N = R_j | `c`: K -> K_end - j; K_end - j < R_j on the 3D flow (script Part C1) | R^{d+1}, M^d |
| 384-385 | text after (1.80) | geometry: L_{n-j} <= 42(1-L^{-(n-j)})/(1-L^{-1}) < 63 (L >= 3); d'_n(Z^{(n-j)}) <= L^{-(n-j)/2}d'_j(Z) <= 2^{-(n-j)}d'_j(Z) (L >= 4, at most half of the steps with R_{m+1} = R_m/L); scaling (6.31) [I] | `=`; the half-of-steps count holds on the 3D flow for x_K above a threshold (script Part C3: e.g. L = 13, r = 2: x_K >= 1.25; analytic x_c = 7.37) | 63^d, 64^d via cube counting |
| 385 | (1.81) | Σ <= O(1)3(126)^dM^dL^{d+1}R_j^{d+1}d'_j(Z) + O(1)(64)^dM^dL^{d+1}R_j^{d+2}(d'_j(Z)+1); uses R_n <= L R_j (n > j) and K <= n_0 - j + R_j | `=`: at R = id the tail has K_end - j < R_j steps, so the same bound; R_n <= R_j holds on the 3D flow | (126)^d, (64)^d, L^{d+1}, R^{d+1}, R^{d+2} |
| 385 | (1.82) | κ_1(Z) >= ¼γ_0 14^{-d}A_1²p_0²(g_1)(d'_1(Z)+1) - O(1)M^dR_1^{d+1}d'_1(Z); the following condition ¼γ_0 14^{-d}A_1²p_0²(g_1) >= O(1)2(64)^dM^dL^{d+1}R_1^{d+2} holds "for p_0 large and g_1 small" | `c`: exponent condition 2p_0 > (d+2)r: 5r at d = 3 (6r at d = 4). Applied at every scale j+1 for a newly created region ("first induction step") | 14^{-d}; R^{d+2} |
| 385 | (1.83) | κ_{j+1}(Z) = κ_j(Z_0) - O(1)M^dR_{j+1}^{d+1}d'_{j+1}(Z), Z = S(Z_0), no new large field | `=`. This is the per-step entropy loss of an unprocessed domain; exponent R^{d+1}, not R^d | R^{d+1}, M^d |
| 385-386 | unnumbered | Z_0 obeys (i), (ii), a new large field arose in the preparatory steps: κ_{j+1}(Z) = p_0(g_j) - O(1)M^dR_{j+1}^{d+1}d'_{j+1}(Z), K = R_{j+1} | `0` | R^{d+1} |
| 386 | (1.84) | merge: Z ⊂ ∪_n(Z_j^(n))^{~10} ∪ ∪_i(Z_{j+1}^(i))^{~2} | `=` | none |
| 386 | (1.85) | definition of κ_{j+1}(Z): Σ_n(κ_j(Z_j^(n)) + 2p_0(g_{j(Z_j^(n))})) + Σ_i(γ_0A_1²p_0²(g_{j+1})(d'+1) + 2p_0(g_{j+1})) - O(1)M^dR_{j+1}^{d+1}d'_{j+1}(Z) - 2p_0(g_{j(Z)}) | `=` | R^{d+1} |
| 386 | (1.86) | tree-graph step (endpoint X, rest Y); 2p_0(g_{j(X)}) + 2p_0(g_{j(Y)}) - 2p_0(g_{j(Z)}) >= 2(1+β_0)^{-1}p_0(g_{j+1}); d'_{j+1}(X) + d'_{j+1}(Y) + 2d >= d'_{j+1}(Z) | `=`. The p_0 comparison is CMP 119 (2.7) first line with n - m arbitrary; on the 3D flow it holds with β_0 = 0 (x_m >= x_n for m <= n) | 2d |
| 387 | (1.87) | κ_{j+1}(Z) >= κ_{j+1}(X) + κ_{j+1}(Y) + 2(1+β_0)^{-1}p_0(g_{j+1}) - O(1)2dM^dR_{j+1}^{d+1} | `=` | d, R^{d+1} |
| 387 | (1.88) | closing the induction: S^{n-j-1}(Z) is covered by those of X and Y (they touch, 20MR_n-cube), K <= K_2 + n_1 + R_{j+1}; extra n_1 + R_{j+1} steps cost O(1)3(100M)^dR_{j+1}^{d+2} <= 2(1+β_0)^{-1}p_0(g_{j+1}) | `c`: at R = id both budgets already run to K_end, no extra steps; (1.87) alone needs p_0 > (d+1)r (4r); the verbatim form needs p_0 > (d+2)r (5r) | (100M)^d, R^{d+2} |
| 387 | (1.89) | T'_k(X)1 <= exp(-2(1+β_0)^{-1}p_0(g_k)) for X with K = 0 (κ_k(X) >= 0). Then: (1.79) and (1.80) hold for the T-operation of an arbitrary large-field region, "hence also an improved bound (1.89), with the additional term -κ_1 d_k(X)"; this gives (2.50) [III], Cor. 3 | `c`: for T_k(Y), exp(-2p_0(g_{j(Y)}) - κ_k(Y)), κ_k >= 0, and p_0(g_{j(Y)}) >= p_0(g_k) at d = 3. The -κ_1 d_k(X) term is asserted in one sentence, not proved | none |
| 388 | (1.90) | after the Mayer expansion of the exponential (as (7.1) [I]): {...} = 1 + Σ_{r>=1}Σ_{X'_1,...,X'_r} Π F(X'_p) | `0`: the bracket sums over first-class components X_j, which the R-operation creates; at R = id there are none (q = 0 only) | lattice entropy c_d |
| 388 | (1.91) | F(X') = Σ_qΣ'_{X_{j_1..j_q}}Σ'_DΠ∫dt(Y)Π_h T'_k(X_{j_h})Π_Y V(Y)exp Σ t(Y)V(Y) | `0` | none |
| 388 | (1.92) | \|F(X')\| <= Σ Π_h exp(-2(1+β_0)^{-1}p_0(g_k) + 1) Π_Y α exp(-(1+2β)κd_{k,Z'}(Y)) exp Σ α exp(...); inputs (1.68), (1.73) (\|σ\| <= 1), (1.89) | `0` | none |
| 388 | (1.93) | resummation of the Y-product; uses α^{1/3} <= exp(-(1+β)κ2d) | `0`; the condition is weaker at d = 3 (2d = 6) | 2^d, M^{-d}, 2d |
| 389 | (1.94) | Σ_D <= c_0 exp O(1)α^{1/3}M^{-d}\|X' \ Z'\|, c_0 = 1 (empty D allowed) or α^{1/3} | `0` | M^{-d} |
| 389 | (1.95) | \|F(X')\| <= Σ exp(-q·(3/2)p_0(g_k))c_0 exp(-(1+β)κd_{k,∪Y_i}(X')) exp(-βκM^{-d}\|X' \ ∪Y_i\|/(6·2^d)); assumes -2(1+β_0)^{-1}p_0(g_k) + 1 + 2κ(100R_k)^d <= -(3/2)p_0(g_k) (β_0 = 1/7: -¼p_0 + 1 + 2κ(100R_k)^d <= 0) | `0`; the condition needs p_0 > dr (3r at d = 3) | (100R_k)^d, 6·2^d |
| 389 | (1.96) | Σ_qΣ' <= exp(exp(-½p_0(g_k))100^d(MR_k)^{-d}\|X' \ ∪Y_i\|) | `0` | 100^d, R_k^{-d} |
| 389-390 | (1.97) | \|F(X')\| <= c_1 exp(-(1+β)κd_{k,∪Y_i}(X')); c_1 = exp(-p_0(g_k)) if X' misses all Y_i (then q >= 1), c_1 = α^{1/3} otherwise | `0`. α is the constant of (1.68), "arbitrarily small for γ small", independent of k: not a power of g_k | none |
| 390 | (1.98) | {...} = exp R'^{(k)} = exp Σ_X R'^{(k)}(X), X ∈ D_k meeting Z_k^c (as printed); the series (7.13) [I] | `0` | none |
| 390 | (1.99) | \|R'^{(k)}(X,(U,J))\| <= O(1)c_1 exp(-(1+β/2)κd_{k,∪Y_i}(X)); analytic on Ũ_k^c(X, α̃_0, α̃_1) | `0` | none |
| 390 | (1.100) (context) | the R-terms (X disjoint from the large field) satisfy exp(-p_0(g_k))exp(-κd_k(X)); the rest are boundary terms B'^{(k)} | `0` | none |

## 3. (1.80)-(1.88) at d = 3 with R = identity (conditional reduction)

**What R = identity removes.** All of II's processing: the preparatory steps
(p. 381-383, (1.77)-(1.78), Π' in (1.79), the unnumbered second case after
(1.83)), the first-class components, and with them (1.90)-(1.99). What stays:
the one-step large-field operations T^{(j+1)} composed as T_{j+1} =
T^{(j+1)}T_j (CMP 119 (3.23)), and the large-field regions with S, (1.76),
(1.84).

**Statement (R = id).** Define κ_j(Z) by (1.83) (no new large field) and
(1.85) (merge or creation). Let Φ_j(Z) = Σ_{n=j+1}^{K_end} O(1)M^dR_n^{d+1}
d'_n(S^{n-j}(Z)). Then κ_j(Z) >= Φ_j(Z) for every component Z of Z_j.

*Proof sketch* (II's induction with K_end - j in place of K).

- No new large field: Z = S(Z_0), S^{n-j}(Z_0) = S^{n-j-1}(Z), so
  Φ_{j+1}(Z) = Φ_j(Z_0) - (term n = j+1) and (1.83) gives κ_{j+1}(Z) >=
  Φ_{j+1}(Z). No condition.
- One new region: the first induction step, (1.82). Needs Φ_{j+1}(Z) <= the
  p_0² term. By (1.81) with the tail Σ_{n>n_0}R_n^{d+1}(64)^d over at most
  K_end - j - 1 < R_{j+1} steps and R_n <= L R_{j+1}: Φ_{j+1}(Z) <=
  O(1)(d'+1)R_{j+1}^{d+2}. Condition 2p_0 > (d+2)r. (Refined: the tail has
  <= x/ln L steps, 2p_0 > (d+1)r + 1; script Part D shows the ratio
  Σ_{n>i}R_n^{d+1}/R_i^{d+2} <= 0.016 for the cases run.)
- Merge: (1.84)-(1.87) verbatim, using only (2.7) first line. Subadditivity
  Φ_{j+1}(Z) <= Φ_{j+1}(X) + Φ_{j+1}(Y) holds because Z ⊂ X ∪ Y and X, Y touch
  (p. 387: the intersection of S^{n-j-1}(X), S^{n-j-1}(Y) contains a cube of
  size 20MR_n). So only 2(1+β_0)^{-1}p_0(g_{j+1}) >= O(1)2dM^dR_{j+1}^{d+1}
  is needed: p_0 > (d+1)r. In II's verbatim form (with the extra n_1 + R_{j+1}
  steps) p_0 > (d+2)r.

**The facts about the 3D flow used** (script Part C; K = 300 steps, all j):

- (C0) R_n <= R_j for n > j, hence R_n <= L R_j (used in (1.81)): holds from
  x_K >= 1.
- (C1) K_end - j < R_j for every j: analytic (K - j = (x_j - x_K)/ln L < x_j <=
  x_j^r for L >= 3, x_j >= 1); verified from x_K >= 1. This is II's own bound
  K <= n_0 - j + R_j, so (1.81) holds verbatim.
- (C2) R_{j+1} ∈ {R_j, R_j/L}: from x_K >= 1.0 (L = 13, r = 2) and 1.25
  (L = 3, 4, 5, r = 2) up to 2.25 (L = 3, r = 3); analytic x_b = ln L/(1 - L^{-1/r}) ≈ 2.6-4.5.
- (C3) at most half of the steps in every window of w >= 2 steps are
  no-gain steps, i.e. R_j/R_n <= L^{(n-j)/2} (the source of 2^{-(n-j)} in
  (1.81)): from x_K >= 1.25 (L = 13, r = 2) to 6.5 (L = 4, r = 3); analytic
  sufficient x_c = ln L/(1 - L^{-1/(3r)}) ≈ 6.6-10.3, i.e. g² <~ 1e-3 to 3e-5.
  The drop frequency per step is about r/x, so (C3) is a large-x_K statement.
  This is a multi-step inequality for R_j/R_n that is of second-line type
  (2.9) but with an exponential, not polynomial, allowance; it holds on the
  3D flow where the polynomial form (2.9) second line fails (note 65 §3.1).

**Mechanism (answer to "growth of the seed weight").** II compensates the
per-step loss (1.83) by a one-time budget: κ at creation is about
¼γ_0 14^{-d}A_1²p_0²(g_i)(d'+1), and (1.80) says that this covers every later
step's loss. The weight does not need to grow along the flow. The 3D flow
enters only through (C1)-(C3) and through (2.7) first line, which is easier
at d = 3 (p_0(g_m) >= p_0(g_n) for m <= n, β_0 = 0). Margin: the ratio
x_i^{2p_0}/Σ_{n>i}R_n^{d+1} is >= 3.5e10 in every case of script Part D
(L = 4, 13, r = 2, 3, p_0 = 5r, x_K = 8, 20, 60); it grows like
x^{2p_0 - (d+1)r - 1}. The creation-position entropy (the L^{ds} of
note 65 Lemma 65.2) is inside II's loss term: the history sum is
"exp O(1)(MR_j)^{-d}|Z_j|" per step (p. 383).

**Exponent conditions** (script Part A, d = 3 and 4, r = 2, 3):

| condition | source | d = 3 (r = 2) | d = 4 (r = 2) |
|---|---|---|---|
| p_0 > (d+5)r (if p_1 <= p_0) | p. 383 prose, R on | 17 | 19 |
| p_0 > (d+2)r | (1.88), R on | 11 | 13 |
| 2p_0 > (d+2)r | (1.82), R on or id | 6 | 7 |
| p_0 > dr | (1.95), R on | 7 | 9 |
| p_0 > (d+1)r | (1.87), R = id | 9 | (11) |
| 2p_0 > (d+1)r + 1 | (1.82) refined, R = id | 5 | (6) |

(minimal integer p_0; the d = 4 column for the R = id rows is not a claim.)
CMP 119 (1.1) fixes p_0 >= 5r (p_0 >= 10 at r = 2). At d = 3 with R = id the
binding condition is p_0 > 4r (refined) or 2p_0 > 5r and p_0 > 5r (verbatim);
p_0 >= 5r meets the first and, if "large" is read as > 5r, the second. For
R on, the p. 383 condition (if p_1 <= p_0) is p_0 > 9r at d = 4, which does
not follow from p_0 >= 5r of CMP 119 (1.1); I could not locate the
definition of p_1, so this is flagged, not claimed. It does not matter at
R = id.

## 4. The three questions and the (2.6)-(2.9) question

### Q1. (H4a): do (1.79)-(1.89) and (1.97)-(1.99) hold at d = 3, R = id so that note 49's rooted KP lemma applies?

- **Domain factors (1.79)-(1.89): yes after three changes** (§3), status
  conditional reduction. The per-step entropy loss of an unprocessed domain is
  (1.83): O(1)M^dR_{j+1}^{d+1}d'_{j+1}(Z), from the normalization constants'
  O(log g_j^{-2}) per site (p. 380). It is compensated, with R = id, by the
  creation budget (the p_0² term), not by growth of the weight along the
  flow; that the remaining number of steps is below R_j is automatic on the
  3D flow. The conclusion is the weight bound for an unprocessed large-field
  region Y at scale k: T_k(Y)1 <= exp(-2p_0(g_{j(Y)}) - κ_k(Y)) with
  κ_k >= 0, hence <= exp(-2p_0(g_k)) at d = 3 ((1.89) with β_0 = 0), and
  exp(-2p_0(g)) <= g^q for every q (script Part E: x >= 1.85 for q = 1000,
  p_0 = 10, A_0 = 1). This is linear in p_0(g), not exp(-c p_0²).
- **Final activity bound (1.97)-(1.99): no.** At R = id the expansion is
  vacuous: the bracket {...} of (1.72) sums over first-class components X_j,
  and there are none. Where it does apply (R on, d = 4), (1.97) gives c_1 =
  exp(-p_0(g_k)) for X' missing every large-field domain Y_i, but c_1 =
  α^{1/3} for X' meeting one, and α is the scale-independent constant of
  (1.68). So the form |activity(X)| <= C_q g_j^q e^{-κd(X)} for polymers
  touching a large-field domain is not (1.97). The smallness is in the
  weights T'_k(Y_i)1 of (1.89), which sit outside the activities (the Y_i are
  fixed in (1.103), p. 391).
- **Rooted KP lemma (note 49 Lemma 1): not yet applicable at R = id.**
  Two gaps:
  - (G1) A polymer representation of the density at R = id whose polymers are
    the large-field domains Y with activity <= exp(-2p_0(g_k) - κ_1d_k(Y))
    times the boundary-term factors, with KP convergence. II proves the
    analogue only for the R-operation output (1.103)-(1.104), with the Y_i
    fixed and no sum over them; the same estimates (1.92)-(1.97) with T'_k(X_j)
    replaced by T_k(Y_i) and tree-decay from (1.89) would give it, but this is
    not written in II. Boundary terms near Y carry only B_0 = O(p_0³(g_k))
    (note 65 §4.1), which exp(-2p_0) absorbs.
  - (G2) The decay -κ_1 d_k(X) in (1.89) for arbitrary large-field regions is
    asserted in one sentence (p. 387). Note 49 §6's KP count for (1.97) is a
    correct count for that expansion's activities, but it is not the gas of
    Proposition 2 at R = id.
- Status of (H4a) at d = 3, R = id: **conditional reduction** (domain weights),
  with (G1), (G2) open. [Update, T84 (note 68): (G2) is proved at R = id
  (Prop. 68.1, Cor. 68.2: T_k(Y)1 <= exp(-κ_1 d_k(Y) - c_* p_0²(g_k)) for every
  κ_1, from the printed geometry of pp. 380-387 and this note's R = id
  reading), under the single exponent condition 2p_0 > (d+2)r; the merge
  condition p_0 > (d+1)r of §3 is sufficient but not needed. (G1) is reduced
  (note 68 §3-§5: the gas, KP with a = ½κd + 1, and the activity bound
  C_q g_k^q e^{-κ d_k}) to three readings not printed in II: (H-form), (H-C),
  and (1.79) for the unprocessed T_k. CMP 122 II (1.85) prints γ_0 A_1² where
  (1.79), (1.82) and p. 381 use ½γ_0 A_1².]

### Q2. Are inputs (W), (E), (D) of note 65 §5 statements of CMP 122 II at d = 3, R = id?

- **(W) seed weight.** At creation: yes, p. 380-381 (fundamental large-field
  factors) and the creation term of (1.79), (1.82), (1.85):
  exp(-½γ_0A_1²p_0²(g_j)(d'+1) - 2p_0(g_j)). Persistence "without loss": (1.83),
  (1.85) are the definitions of the bookkeeping κ_j that subtract the entropy
  loss step by step; II only states κ_j >= Φ_j >= 0 (1.80) and the consequence
  (1.89), a linear weight exp(-2p_0(g_{j(Z)})). The unrolled quadratic form
  c p_0²(g_i)(d'+1) minus accumulated entropy is (1.79) read without the
  final induction; it is not stated as such. The linear form is enough for
  the requested g^q bound.
- **(E) per-point loss e^{O(1)}.** **No**, as stated. II has O(log g_j^{-2}) per
  lattice point of Z_j (p. 380), total O(1)M^dR_j^{d+1}d'_j(Z_j) per step,
  exponent R^{d+1} (note 65's exponent counting used R^d; Prop. 65.4's
  degree rd + 1 becomes (d+1)r + 1; the condition 2p_0 >= 10r > (d+1)r + 1
  still holds at d = 3, r >= 1).
- **(D) domain growth.** Yes: (1.76), (1.84) with ten layers of
  LMR_{j+1}-cubes (m_0 = 10), the operation S (p. 384).

### Q3. Does (1.92)-(1.99) localize CMP 102's sixth-order remainder (22)-(24)?

**No.** CMP 102 (22)-(24) concern the fluctuation integral ∫dμ χ exp V over
the small-field region Ω_1: expanded to sixth order in g_0, remainder
O(g_0^7p^{18})|Ω_1| (extensive), the rest a cumulant expansion localized by
random walks with bound (23)/(24) (p. 262; the paper says the integral "can be
expressed naturally by an exponentiated cluster expansion" but does not do
so). In II, (1.90)-(1.99) exponentiate a different bracket: the sum over
first-class large-field components X_j with insertions T'_k(X_j), weighted
by the already localized small-field terms V(Y) of (1.68), which are old
E, R, B terms re-resummed in domains Y (pp. 375-377, (1.66)-(1.69)). The
polymers are connected unions of the X_j and of the domains of the V(Y); the
activities (1.97) carry exp(-p_0(g_k)) or α^{1/3}; (1.99) bounds R'(X), the
large-field-induced R-terms. None of this expands the small-field
fluctuation integral. At R = id it is vacuous in addition. The statement
CMP 102's remainder needs, "R_6 = Σ_X r_X with e^{-κ'd(X)} decay", is the
localized expansion E^{(k+1)}(X) of CMP 119 Sect. 3, (3.39)-(3.47), with the
exponentiated expansion imported from CMP 109 [I] Sect. 7 (note 65 §2 and
§3), at d = 3 "survives with four changes". So note 61 §6b.4 item 1 should
point to CMP 119 (3.44)-(3.47) and note 65, not to II (1.92)-(1.99). Status:
(I-L) for T4 remains open as before (the replacement of the sixth-order
remainder by the CMP 119 expansion is the d = 3 reading of note 65, with the
imported estimates not rechecked).

### Q4. Does II's induction use CMP 119 (2.6)-(2.9) with n - m > 1?

Yes, implicitly (II never cites the numbers), in the (1.79)-(1.99) range:

- (2.9) first line, R_n <= L R_m for n > m, any n - m: (1.81) (p. 385, twice).
  Holds on the 3D flow with room (R_n <= R_m).
- (2.7) first line, (log g_n^{-2})^p <= (1+β_0)(log g_m^{-2})^p for n > m, any
  n - m: (1.86), p. 386 (m = j(X) or j(Y) <= j+1 = n), and p. 381 for
  j - N <= m <= j. Holds on the 3D flow with β_0 = 0.
- A multi-step bound for R_j/R_n: p. 384-385, d'_n <= L^{-(n-j)/2}d'_j, i.e.
  R_j/R_n <= L^{(n-j)/2} (no more than half of the steps drop R). Not one of
  (2.6)-(2.9) but of second-line type. Holds on the 3D flow above a threshold
  x_K (script Part C3), where the polynomial second line (2.9) fails (note 65
  §3.1, Part H).
- **The failing inequalities** ((2.6) and (2.8) first lines for every n - m
  >= 1; (2.7) and (2.9) second lines beyond a window; note 65 §3.1) are used
  only in the preparatory-step estimate p. 381-383: p. 382 top,
  6(100MR_{j-N+1})²ε <= 6(100M(L+1)N^{β_0}R_j)²ε with n - m = N - 1 up to
  R_j - 1 steps (a (2.9) second-line form), feeding (1.78) and Π'. That is
  absent at R = id. In (1.90)-(1.99) there is no multi-scale coupling
  inequality: (1.92)-(1.97) are at the single scale k.

## 5. Corrections for the lead (notes 49, 61, 65)

1. Note 49 §1 and §3 step 3 write the entropy loss as O(1)M^dR^dd'. The printed
   (1.83) (p. 385) and p. 380 have R_{j+1}^{d+1}. Replace R^d by R^{d+1}.
2. Note 49 §1: K <= n_0 + R_j should be K <= n_0 - j + R_j ((1.81), p. 385).
3. Note 49 §5 and note 61 §6a ("2p_0 > 4r instead of 2p_0 > 5r"): (1.82) has
   R^{d+2}, so the base condition is 2p_0 > (d+2)r: 5r at d = 3, 6r at d = 4.
   The (1.88) merge step in II's form needs p_0 > (d+2)r; at R = id,
   p_0 > (d+1)r suffices (§3).
4. Note 49 §6 and note 61 §6b.4 item 1: (1.92)-(1.99) is the expansion of the
   R-operation's first-class components; its activity constant for polymers
   touching a large-field domain is α^{1/3}, scale-independent; it is not the
   exponentiated expansion of the fluctuation integral and not a d = 3
   statement. For T4 the relevant source is CMP 119 (3.44)-(3.47) (note 65).
5. Note 61 §6 (H4) / §6a: the g_j^q smallness of a persisting large-field
   region comes from the weight (1.89), linear in p_0(g), not from the
   activity (1.97); the H4a input is "conditional reduction with (G1), (G2)".
6. Note 65 §5 inputs: (E) is O(log g_j^{-2}) per site, not O(1) (p. 380); degree
   of the polynomial in Prop. 65.4 is (d+1)r + 1, still below 2p_0. (W) is
   p. 380-381 plus (1.79), (1.85); the persistence is (1.80), (1.89). (D) is
   (1.76), m_0 = 10.
7. Note 49 §3 (4D, R on; a remark only): the unnumbered second case after (1.83)
   gives a fresh factor exp(-p_0(g_j)), linear in p_0, each time a processed
   domain stays large-field, so per R-cycle the gain is linear in p_0, not
   p_0². Not checked further; it concerns a_eff at d = 4.

## 6. Not read, not checked

- Printed pp. 355-375 of II were not read as images (OCR only for conditions
  (i), (ii)); the definition of p_1 and of the constants A_1, γ_0 is not in
  the pages read. The claim p_1 < p_0 is inferred from CMP 122 I p. 186 (OCR).
- The (7.13) series and the Mayer expansion (7.1) of CMP 109 were not read.
- (1.79) at R = id is not re-derived; the claim that the preparatory-step
  estimates are the only R-specific ones rests on the structure of pp. 380-383.
  The "improved bound" with -κ_1 d_k(X) is asserted in II (p. 387), not proved.
- The scalar checks use R_j = smallest power of L >= x_j^r and the exact flow;
  Balaban's constants are unspecified.
