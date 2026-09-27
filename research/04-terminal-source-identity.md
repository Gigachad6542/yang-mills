# Exact transport of terminal sources through a block kernel

Status: **proved here for the exact \(T\)-kernel**, with that kernel matched to
Balaban's published formulas. The identity does not extend automatically to the
measure-changing large-field \(R\)-operation; the required terminal-test
extension of \(R\) remains open.

## One exact RG step

Let \(\Omega_k\) and \(\Omega_{k+1}\) be compact configuration spaces, let
\(\eta_k\) be a finite positive measure on \(\Omega_k\), and let
\(K_k(U,dV)\) be a finite positive block kernel. No normalization of \(K_k\) is
needed. Define the next unnormalized measure by

\[
 \eta_{k+1}(dV)=\int_{\Omega_k}\eta_k(dU)K_k(U,dV).
\]

For a bounded measurable terminal observable \(F:\Omega_{k+1}\to\mathbb C\),
insert the source in the joint block integral:

\[
 \eta_{k+1}^{z,F}(dV)
 =\int_{\Omega_k}\eta_k(dU)K_k(U,dV)e^{zF(V)}.
\]

Then, exactly,

\[
 \boxed{\eta_{k+1}^{z,F}(dV)=e^{zF(V)}\eta_{k+1}(dV).}
\]

This is simply because the source factor depends only on \(V\), so it can be
pulled through the \(U\)-integration. The statement is unchanged by
field-independent vacuum-energy factors multiplying either measure.

## Iteration

For composable kernels \(K_0,\ldots,K_{n-1}\), let

\[
 K_{0:n}(U_0,dV)
 =\int K_0(U_0,dU_1)\cdots K_{n-1}(U_{n-1},dV).
\]

Repeated use of the one-step identity gives

\[
 \int\eta_0(dU_0)K_{0:n}(U_0,dV)e^{zF(V)}
 =e^{zF(V)}\eta_n(dV).
\]

Consequently the normalized generating function is

\[
 \frac{\displaystyle\int e^{zF(V)}\eta_n(dV)}
      {\displaystyle\int\eta_n(dV)}.
\]

All multiplicative normalizations accumulated in the vacuum RG cancel in this
ratio.

## Match to Balaban's exact transformation

Balaban's nonlinear coarse connection \(\bar U\) is a deterministic,
gauge-covariant function of the fine connection. In *Averaging Operations for
Lattice Gauge Theories*, printed pp. 19--20, Eq. (10) defines

\[
 \rho'(V)=\int dU\,\delta(V\bar U^{-1})\rho(U).
\]

Equations (11), (14), and (15) give its covariance, linearization, and a concrete
average. The four-dimensional construction uses Euclidean-symmetric deterministic
averages in Eqs. (0.4) and (0.12) of CMP **109** (printed pp. 253--254). The
complete transformation is restated in CMP **119**, Eq. (0.1), printed p. 243:

\[
 (T\rho)(V)=\int dU\,\delta(\bar U V^{-1})\rho(U).
\]

Thus \(\bar U\) is the deterministic map inside the delta constraint; it is not
a random kernel. For a terminal gauge-invariant function \(F\), the sourced
transformation satisfies

\[
 \begin{aligned}
 (T_z\rho)(V)
 &=\int dU\,\delta(\bar U V^{-1})\rho(U)e^{zF(\bar U)}\\
 &=e^{zF(V)}(T\rho)(V).
 \end{aligned}
\]

The second line is the defining property of the group delta distribution. The
normalization identity \(\int dV\,T\rho=\int dU\,\rho\) also appears as Eq. (10)
in Balaban's 1986 ICM account. This establishes P0b at the algebraic level.

## Boundary at the large-field \(R\)-operation

The displayed identity concerns Balaban's exact group-delta map \(T\). In the
four-dimensional stability proof it is followed by a large-field
\(R\)-operation. CMP **122 I**, Eq. (0.4), p. 176, gives only

\[
 \int dV\,(R\rho)(V)=\int dV\,\rho(V).
\]

The paper later states explicitly that this step may change the density while
preserving its integral (printed pp. 194 and 200). It therefore does not follow
that

\[
 \int dV\,e^{zF(V)}(R\rho)(V)
 =\int dV\,e^{zF(V)}\rho(V).
\]

Mass preservation is enough for vacuum stability but not for a nonconstant
terminal observable. The exact \(T\)-identity eliminates source vertices inside
the block integrations; it does not eliminate the need for a source/test-stable
\(R\)-step. The distinction and a two-point counterexample are in
`09-common-space-and-r-obstruction.md`.

## Deterministic and general kernels

For Balaban's transformation the terminal source is therefore the fine-lattice
observable
\(e^{zF(\bar U^{(n)})}\), where \(\bar U^{(n)}\) is the iterated deterministic
average. The abstract kernel formulation remains useful for comparing other RG
schemes; for a genuinely stochastic kernel, the terminal variable instead lives
naturally in the extended joint measure.

## Gauge covariance

Suppose gauge groups \(\mathcal G_k\) and \(\mathcal G_{k+1}\) act on the two
spaces, the kernel intertwines the actions, and \(F\) is invariant under
\(\mathcal G_{k+1}\). Then the sourced terminal measure has the same covariance
as the unsourced measure. A gauge-fixed coordinate formula can be used only after
checking that its Faddeev--Popov/Jacobian factors reproduce this exact marginal;
formal covariance of an analogous averaging map is not enough.

## The weakest convergence norm actually needed

Let \(\nu_n=\eta_n/\eta_n(1)\), let
\(|F_j|\le B_j\), and define

\[
 \mathcal T_\rho
 =\left\{V\mapsto e^{\sum_jz_jF_j(V)}:z\in D_\rho\right\}.
\]

Introduce the source-test dual seminorm

\[
 \lVert\nu-\nu'\rVert_{\mathcal T_\rho}
 =\sup_{f\in\mathcal T_\rho}
   \left|\int f\,d(\nu-\nu')\right|.
\]

Then, tautologically,

\[
 \sup_{z\in D_\rho}|Z_n(z)-Z_m(z)|
 =\lVert\nu_n-\nu_m\rVert_{\mathcal T_\rho}.
\]

Thus M1 does **not** logically require convergence of the full effective density
in total variation. It requires a summable Cauchy estimate only in this much
weaker observable-tested norm. Total variation is a sufficient fallback because

\[
 \lVert\nu_n-\nu_m\rVert_{\mathcal T_\rho}
 \le e^{\sum_jB_j\rho_j}
      \lVert\nu_n-\nu_m\rVert_{\mathrm{TV},*},
\]

where
\(\lVert\sigma\rVert_{\mathrm{TV},*}
=\sup_{\lVert f\rVert_\infty\le1}|\int f\,d\sigma|\).
The project should first seek the source-test estimate rather than impose an
unnecessarily strong full-measure convergence theorem.

## What this identity does not prove

It proves no RG norm estimate, no cutoff comparison, and no convergence. It shows
only that a terminal source introduces no new vertex inside earlier exact
\(T\)-integrations. Its behavior under the large-field \(R\)-replacement is the
open Robs obligation, and the subsequent physical cutoff comparison is P4.

## Primary formula sources

- T. Bałaban, *Averaging Operations for Lattice Gauge Theories*, CMP **98**
  (1985), 17--51. [DOI](https://doi.org/10.1007/BF01211042).
- T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*,
  CMP **109** (1987), 249--301.
  [DOI](https://doi.org/10.1007/BF01215223).
- T. Bałaban, *Convergent Renormalization Expansions for Lattice Gauge Theories*,
  CMP **119** (1988), 243--285.
  [DOI](https://doi.org/10.1007/BF01217741).
- T. Bałaban, *Recent Results in Constructing Gauge Fields*, Proceedings of the
  1986 ICM, pp. 1259--1266.
  [Proceedings PDF](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1986.2/ICM1986.2.ocr.pdf).
