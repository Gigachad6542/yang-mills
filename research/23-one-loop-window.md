# One-loop window sums: exact scalar calibration and the SU(2) stopping point

Status:

- **Exact computation:** the two-dimensional \(O(3)\) sigma-model analogue
  for \(L=2,3\) and window depths \(n=1,\ldots,6\).  A constant-twist
  determinant gives the complete one-loop inverse-coupling decrement.  Its
  slope converges to \((N-2)\log L/(2\pi)\), and the edge
  \(\beta^\sigma_{[0,n]}-n(N-2)\log L/(2\pi)\) converges to a constant.
- **Exact block-constraint calibration:** the scalar covariance constrained
  to have zero \(M\)-box average on every terminal cell is evaluated by an
  alias-space Schur complement.  Through depth six its edge approaches the
  same finite value for \(L=2\) and \(L=3\); this is numerical evidence, not
  an asymptotic proof for the multi-cell filter.
- **Failed SU(2) computation:** the constrained gluon-plus-ghost determinant
  and its exact second-derivative trace are written in (2.2)--(2.4), but no
  SU(2) numbers are reported.  The missing implementation is the pair of
  background derivatives of the lattice Wilson Hessian, ghost operator, and
  (for a covariant scheme) block constraint.  A direct composite sum at
  \(L=3,n=6\) has \(729^4=2.8243\times10^{11}\) aliases per coarse momentum.
  Replacing the vertices by a scalar trace would put in the universal
  \(11C_A/3\) numerator by hand and would not compute the scheme edge.

Thus this note fulfills the scalar fallback explicitly authorized in T13.  It
does **not** prove research note 22's hypothesis (U).

## 1. The requested SU(2) quantity

Put \(M=L^n\), take \(T^a=-i\sigma^a/2\), and normalize

$$
 -2\operatorname{Tr}_F(T^aT^b)=\delta^{ab},
 \qquad
 S_W(U)=\frac4{g^2}\sum_p
 \left(1-\frac12\operatorname{ReTr}_F U_p\right).
$$

Here \(\operatorname{Tr}_F\) is the fundamental \(2\times2\) trace.  Split
\(U=e^{ga}V_B\), and use fixed-background Feynman gauge.  Let

- \(H_1(B)\) be the color-vector Hessian of the Wilson action plus background
  gauge fixing at background \(B\);
- \(\mathcal M(B)=D_B^*D_B\) be the Faddeev--Popov ghost operator;
- \(Q_1\) be the composite linear link average, and \(Q_0\) the corresponding
  site-box average.

For the simplified fixed-linear-\(Q\) scheme, the one-loop window action is

$$
 \Gamma_M^{(1)}(B)
 =\frac12\log\det_{\ker Q_1}H_1(B)
  -\log\det_{\ker Q_0}\mathcal M(B).
 \tag{1.1}
$$

The omitted constants are independent of \(B\).  In (1.1), \(B\) must be
the constrained minimizing fine-lattice lift of the terminal background;
its first and second derivatives are therefore part of the vertices below.
With that lift, gauge convention, and block map fixed, the transverse
quadratic coefficient is the simplified-scheme analogue of the requested
\(\beta^0_{[i,i+n]}\).  Universality predicts

$$
 \beta^0_{[i,i+n]}
 =2b_0n\log L+O(1),
 \qquad
 b_0=\frac{11C_A}{48\pi^2},
 \qquad C_A=2.
 \tag{1.2}
$$

For reference, the predicted slopes per block step are

| \(L\) | \(2b_0\log L\) |
|---:|---:|
| 2 | 0.0643779517083 |
| 3 | 0.102036639331 |

These are targets, not outputs of the present computation.

## 2. Exact constrained trace formula

Let \(G\) be an unconstrained inverse Hessian at \(B=0\).  The covariance
embedded back into the full field space after imposing \(Q\phi=0\) is

$$
 G_Q
 =G-GQ^*(QGQ^*)^{-1}QG.
 \tag{2.1}
$$

Choose two external background waves \(\mathcal B_1,\mathcal B_2\), and
write

$$
 H_i=\partial_{t_i}H_1(t_1\mathcal B_1+t_2\mathcal B_2)\big|_0,
 \qquad
 H_{12}=\partial_{t_1}\partial_{t_2}H_1
       (t_1\mathcal B_1+t_2\mathcal B_2)\big|_0,
 \tag{2.2}
$$

with \(\mathcal M_i,\mathcal M_{12}\) denoting the analogous ghost vertices.
If \(G_A,G_c\)
are (2.1) for the vector and ghost operators, differentiation of (1.1)
gives exactly

$$
 \begin{aligned}
 \partial_1\partial_2\Gamma_M^{(1)}(0)
 ={}&
 \frac12\operatorname{Tr}
   \left(G_AH_{12}-G_AH_1G_AH_2\right)\\
 &-\operatorname{Tr}
   \left(G_c\mathcal M_{12}-G_c\mathcal M_1G_c\mathcal M_2\right).
 \end{aligned}
 \tag{2.3}
$$

Here \(\operatorname{Tr}\) is the functional trace over lattice positions,
link directions, and adjoint color.  The terms containing \(H_{12}\) and
\(\mathcal M_{12}\) are the gluon and ghost seagulls; the terms quadratic in the
first derivatives are their bubbles.  Thus no diagram or multiplicity is
missing from the fully specified fixed-\(Q\) determinant (1.1).  For a
transverse external wave of color \(a\), with \(q_\rho=0\), define
\(\Pi_{\rho\rho}^{aa}(q)/|\Lambda|\) with no sum on \(a\).  Then

$$
 \beta^0_{[i,i+n]}
 =-\lim_{q\to0}
 \frac{\Pi_{\rho\rho}^{aa}(q)-\Pi_{\rho\rho}^{aa}(0)}
      {|\Lambda|\,\widehat q^{\,2}},
 \tag{2.4}
$$

with the sign chosen so the asymptotically free decrement is positive.

### Where the attempted computation stops

At \(B=0\), all objects in (2.3) are translation invariant.  For each coarse
momentum \(K\), \(Q\) couples the aliases

$$
 p_\ell=\frac{K+2\pi\ell}{M},
 \qquad \ell\in[0,M)^4.
 \tag{2.5}
$$

The constraint is low rank in each alias sector, so (2.1) can be streamed
without forming a dense \(M^4\times M^4\) matrix.  That still leaves \(M^4\)
loop momenta.  At the largest requested point, \(M=3^6=729\), this is
\(2.8243\times10^{11}\) terms before sampling even one nontrivial coarse
momentum.

Note 22's Schur-complement identity permits an exact stepwise factorization.
The corresponding background lift at one step is

$$
 L_Q=GQ^*(QGQ^*)^{-1}.
 \tag{2.6}
$$

The determinant factorization alone does not reduce the total mode count:
the successive steps still contain all intermediate momentum sectors and
cost \(O(M^4)\) in aggregate.  An \(O(nL^4)\) alias recursion per terminal
coarse momentum would require a closed recursion for the momentum-dependent
effective Hessian, its first and second background vertices, and the lift
\(L_Q\).  No such recursion is derived here.  The T7/T8 code supplies only
the free linear average and propagator, not these vertices.

There is a second scheme choice.  A fixed linear \(Q\) makes (1.1)
well-defined, but it is not background gauge covariant away from \(B=0\);
longitudinal artifacts must be subtracted in (2.4).  A covariant \(Q_B\)
restores the background Ward identity but contributes its own first and
second derivatives to (2.3).  Neither choice can be silently inferred from
the trivial-background T7 kernel.  These are the exact reasons the SU(2)
table was not produced.

## 3. Exact \(O(N)\) sigma-model calibration

The scalar fallback retains all features needed to test the window
arithmetic: a marginal coupling, a one-loop determinant, a block constraint,
and an exact momentum sum.

On the \(M\times M\) square lattice, take

$$
 S_h(s)=h\sum_{x,\mu}\left(1-s_x\cdot s_{x+e_\mu}\right),
 \qquad s_x\in S^{N-1}.
 \tag{3.1}
$$

Impose a total twist \(\varphi\) in direction 1.  The classical background
rotates through the angle \(\theta=\varphi/M\) per bond, so

$$
 S_h(s_{\mathrm{bg}})
 =hM^2(1-\cos\theta)
 =\frac h2\varphi^2+O(\varphi^4/M^2).
 \tag{3.2}
$$

We impose the box-zero constraint componentwise in the moving parallel
tangent frame.  With one terminal cell, the composite \(M\)-box constraint
then removes the global fluctuation zero mode.  A fixed Cartesian constraint
would acquire twist derivatives in this frame and define a different scheme.
The nonzero-mode Hessian eigenvalues are

$$
 \lambda_\parallel(k,\theta)
 =\cos\theta\,\widehat k_1^{\,2}+\widehat k_2^{\,2},
 \qquad
 \lambda_\perp(k,\theta)
 =\widehat k^{\,2}+2(\cos\theta-1),
 \tag{3.3}
$$

where \(\lambda_\perp\) has multiplicity \(N-2\) and

$$
 \widehat k_\mu=2\sin(k_\mu/2),
 \qquad k_\mu=\frac{2\pi j_\mu}{M}.
$$

The one-loop determinant is

$$
 \Gamma_M^{(1)}(\varphi)
 =\frac12\sum_{k\ne0}\log\lambda_\parallel(k,\theta)
 +\frac{N-2}{2}\sum_{k\ne0}\log\lambda_\perp(k,\theta).
 \tag{3.4}
$$

Expanding (3.4) to second order and using square-lattice symmetry,

$$
 \sum_{k\ne0}\frac{\widehat k_1^{\,2}}{\widehat k^{\,2}}
 =\frac{M^2-1}{2},
$$

gives the exact positive inverse-coupling decrement

$$
 \boxed{
 \beta^\sigma(M)
 =\frac14(1-M^{-2})
  +\frac{N-2}{M^2}
   \sum_{k\ne0}\frac1{\widehat k^{\,2}}.}
 \tag{3.5}
$$

The first term is a bounded longitudinal edge.  The lattice Green-function
asymptotic

$$
 \frac1{M^2}\sum_{k\ne0}\frac1{\widehat k^{\,2}}
 =\frac1{2\pi}\log M+c_{\mathrm{lat}}+o(1)
 \tag{3.6}
$$

then proves

$$
 \beta^\sigma(L^n)
 =\frac{N-2}{2\pi}n\log L+O(1).
 \tag{3.7}
$$

This is the scalar version of hypothesis (U), including its bounded edge.

## 4. Exact sigma-model table

The script research/scripts/t13_sigma_window.py evaluates (3.5) for \(N=3\).

### \(L=2\)

| \(n\) | \(M\) | \(\beta^\sigma(M)\) | edge \(\beta^\sigma-n\log2/(2\pi)\) | increment |
|---:|---:|---:|---:|---:|
| 1 | 2 | 0.343750000000 | 0.233432199924 | |
| 2 | 4 | 0.502604166667 | 0.281968566514 | 0.158854166667 |
| 3 | 8 | 0.625388436625 | 0.294435036396 | 0.122784269958 |
| 4 | 16 | 0.738947932096 | 0.297676731791 | 0.113559495471 |
| 5 | 32 | 0.850082053054 | 0.298493052672 | 0.111134120958 |
| 6 | 64 | 0.960604266730 | 0.298697466272 | 0.110522213676 |

The target increment is \(\log2/(2\pi)=0.110317800076\).  A fit to
\(n=4,5,6\) gives \(0.110828167317\), a relative error \(4.63\times10^{-3}\);
the last increment is already within \(1.85\times10^{-3}\) relatively.

### \(L=3\)

| \(n\) | \(M\) | \(\beta^\sigma(M)\) | edge \(\beta^\sigma-n\log3/(2\pi)\) | increment |
|---:|---:|---:|---:|---:|
| 1 | 3 | 0.444444444444 | 0.269594868161 | |
| 2 | 9 | 0.645037194057 | 0.295338041491 | 0.200592749612 |
| 3 | 27 | 0.822931544417 | 0.298382815568 | 0.177894350361 |
| 4 | 81 | 0.998121380348 | 0.298723075216 | 0.175189835931 |
| 5 | 243 | 1.173008785646 | 0.298760904231 | 0.174887405298 |
| 6 | 729 | 1.347862565427 | 0.298765107729 | 0.174853779781 |

The target increment is \(\log3/(2\pi)=0.174849576283\).  The \(n=4,5,6\)
fit gives \(0.174870592539\), a relative error \(1.20\times10^{-4}\), and
the last increment differs by only \(4.20\times10^{-6}\).

The edge approaches the same constant, \(0.298765\ldots\), for both block
factors.  This is the desired bounded-edge behavior, not just a fitted
slope.

## 5. Multi-cell box constraint

For a closer check of the actual block geometry, let the terminal torus have
\(n_0^2\) cells and impose zero \(M\)-box average on each.  In a coarse
momentum sector \(K\), with \(\ell\in[0,M)^2\), let

$$
 p_\ell=\frac{K+2\pi\ell}{M},
 \quad
 g_\ell=\widehat p_\ell^{-2},
 \quad
 q_\ell=M^{-2}D_M(p_{\ell,1})D_M(p_{\ell,2}),
 \qquad
 D_M(p)=\sum_{u=0}^{M-1}e^{-ipu}.
$$

For \(K\ne0\), the constrained covariance is a rank-one Schur complement.
Its trace in that alias sector is exactly

$$
 T_K
 =\sum_\ell g_\ell
  -\frac{\sum_\ell |q_\ell|^2g_\ell^2}
         {\sum_\ell |q_\ell|^2g_\ell}.
 \tag{5.1}
$$

At \(K=0\), (5.1) is understood with the Laplacian pseudoinverse:
\(g_{(0,0)}=0\) and
\(T_0=\sum_{\ell\ne(0,0)}g_\ell\).  Equivalently, introduce a positive
mass and take it to zero after imposing the block constraint.  This is the
convention used by the script.

The normalized transverse contribution is

$$
 I_M=\frac1{(n_0M)^2}\sum_K T_K.
 \tag{5.2}
$$

For \(n_0=4\), the script gives

| \(L\) | \(I_{L^1},\ldots,I_{L^6}\) | final edge \(I_{L^6}-6\log L/(2\pi)\) |
|---:|:---|---:|
| 2 | 0.182666575153, 0.304872965707, 0.416808109374, 0.527376547635, 0.637744748798, 0.748074292386 | 0.086167491928 |
| 3 | 0.256656573172, 0.435631427920, 0.610697993759, 0.785567241969, 0.960418941395, 1.135268752738 | 0.086171295039 |

This second calculation uses the actual box filter rather than only the
global zero mode.  Through \(n=6\), the two edges approach the common value
\(0.08617\ldots\), different from the one-cell edge as a scheme-dependent
constant should be.  The table supplies strong convergence evidence, but
not a proof of the multi-cell asymptotic.

As an independent check at \(n_0=4,M=2\), the script constructs the
\(64\times64\) real-space Laplacian, finds an orthonormal basis of the
48-dimensional null space of the \(16\times64\) block-average matrix, and
computes the restricted inverse by eigendecomposition.  It gives
\(0.182666575152788\), while (5.1) gives \(0.182666575152788\); the absolute
error is \(2.78\times10^{-17}\), and the smallest restricted eigenvalue is
2.

A numerical detail matters.  Evaluating
\((1-e^{-iMp})/(1-e^{-ip})\) directly contaminates the exact alias zeros at
large \(M\).  The script instead uses

$$
 D_M\left(\frac{K+2\pi\ell}{M}\right)
 =e^{-ip(M-1)/2}(-1)^\ell
  \frac{\sin(K/2)}{\sin(p/2)}
 \tag{5.3}
$$

and sets the \(K=0\) zeros exactly.

## 6. What this establishes

The scalar calculation and the general determinant identity establish the
following, with the status of each item explicit:

1. the window coefficient is an exact constrained Gaussian determinant;
2. the standard square-lattice Green-function asymptotic proves that the
   one-cell leading term is universal and linear in \(n\log L\), with a
   bounded edge;
3. the multi-cell block-constraint table gives numerical evidence through
   depth six for the same slope and a different bounded edge;
4. independently of the script, note 22's determinant/Schur identity
   guarantees equality of composite and sequential Gaussian integration
   when every intermediate effective Hessian and background lift is retained.

It also shows what remains specifically non-Abelian.  The universal
beta-function numerator \(11C_A/3=22/3\) for SU(2) arises only after the
lattice gluon bubbles, seagulls, and ghosts in (2.3) cancel their longitudinal
parts, using \(f^{acd}f^{bcd}=C_A\delta^{ab}\).  It is not a scalar trace
multiplicity.  Inserting that numerator by hand would verify the already-known
logarithm while discarding exactly the edge constant T13 was meant to measure.
The next implementation step is therefore unambiguous: generate the four vertex
operators in (2.2), preferably by automatic differentiation of one Wilson
plaquette and the ghost stencil, and propagate their traces recursively
through the \(L^4\)-alias Schur complement.

## 7. T19 (lead, 2026-10-02): scoped failed attempt for SU(2)

T19 asked to finish the SU(2) window. Three routes were assessed. Each stops
at an identified step.

1. **Balaban's actual scheme.** The scheme has a block-constrained,
   axial-gauge fluctuation operator around the background-dependent
   minimizer. The F² coefficient needs the first and second background
   derivatives of that minimizer and of the CMP 109 (0.4) composite average
   (T13 §2, (2.2)-(2.4)). The averaging-map derivatives exist in
   `research/scripts/t15_fast.py` (first order, at curved backgrounds). The
   second-order derivatives and the constrained-minimizer lift do not. This
   is the missing implementation, estimated at several working sessions.
2. **Wilson action on a torus, no block constraint.** This is feasible, but
   its universal part is already published. Dashen-Gross (CMP 109 ref. [27])
   and Hasenfratz-Hasenfratz give the one-loop bare-Wilson to continuum
   relation with coefficient 2b_0. It would add nothing to (S) beyond what
   note 22 already cites.
3. **Constant-field (spectral) method on the lattice.** With a covariantly
   constant σ³ background, Landau gauge in x_1 and Fourier in x_2, x_3, x_4,
   the fluctuation operator block-diagonalizes into 12N_1-dimensional blocks.
   But in background Feynman gauge the charged spin-aligned lowest Landau
   level has eigenvalue -f (the Nielsen-Olesen unstable mode). So
   log det is not real. Flux quantization φ >= 2π/N_1 also prevents the
   weak-field limit needed for the f² coefficient on feasible lattices. The
   method stops here unless one uses the real part with an IR prescription,
   which would make the edge constant prescription-dependent.

**Verdict.** The universal coefficient in (S) is published input (note 22,
literature status). (C) is supported by the scalar calibration of §4-5
(geometric convergence of the edge, ratio about L^{-2} per level). The
scheme-specific SU(2) edge constant needs route 1. That stays open and is
not on the critical path, because note 22 Prop. D needs only boundedness of
the edge, which is a finite one-loop matching.
