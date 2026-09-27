# Exact transport of terminal sources through a block kernel

Status: **proved here as an abstract finite-dimensional identity**. Its
identification with Balaban's precise constrained averaging is P0b and remains
open pending the primary-source audit.

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

## Deterministic and constrained block maps

If \(K_k(U,dV)=\delta_{Q_kU}(dV)\), the terminal source is the fine-lattice
observable \(e^{zF(Q_{n-1}\cdots Q_0U)}\). For a genuinely stochastic or
constrained kernel, the exact observable belongs naturally to the extended joint
measure; it must not be silently rewritten as a deterministic \(F(Q^{(n)}U)\).
Determining which case Balaban's construction realizes, including gauge-fixing
constraints and Jacobians, is precisely P0b/P1.

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

It proves no RG norm estimate, no cutoff comparison, and no convergence. It only
shows that once an exact block kernel is fixed, a terminal source introduces no
new ultraviolet dependence inside earlier integrations. That structural fact is
why terminal block observables are the primary M1 family.
