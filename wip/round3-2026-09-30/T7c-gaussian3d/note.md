# T7c: exactly solvable Gaussian 3D check of terminal block-flux convergence

Status: DRAFT (in progress). Scratch: /private/tmp/ym-r3/T7c-gaussian3d/

## Plan
1. Setup: free abelian lattice gauge theory on fine torus (Z/nM)^3, M = L^N, action (1/2g_0^2)|dA|^2, g_0^2 = g^2 eps, eps = eps_0/M.
2. Block map (research/10 (7.1)-(7.2)) at the level of fluxes: d_c Q = q d with explicit q (radial Lambda terms cancel).
3. Fourier formula for the terminal flux covariance C_N; depends on N only through M = L^N.
4. Theorem: |C_N - C_inf| = O(L^{-2N}) with explicit leading coefficient; adjacent difference.
5. Numerics: brute-force real-space check (full Q with axis-ordered contours), Fourier/Schwinger evaluation for large N.
6. What it validates / does not validate for the interacting 3D case.
