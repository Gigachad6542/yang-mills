import numpy as np
np.set_printoptions(linewidth=150)
for n in (2,3):
    A2 = np.load(f'seq_n{n}_L2.npy'); A3 = np.load(f'seq_n{n}_L3.npy')
    # C_inf via Richardson (M^-2) on L=2 last two, compare with L=3
    Cinf2 = A2[-1] + (A2[-1]-A2[-2])/3
    Cinf3 = A3[-1] + (A3[-1]-A3[-2])/8
    print(f'n={n}: |Cinf(L=2) - Cinf(L=3)|max = {np.abs(Cinf2-Cinf3).max():.2e}; Cinf00={Cinf2[0,0]:.13f}')
    Cinf = Cinf2
    np.save(f'Cinf_n{n}.npy', Cinf)
    for L,A in ((2,A2),(3,A3)):
        print(f' n={n} L={L}:  N  M  maxdiff(D_N=C_{{N+1}}-C_N)  ratio D_N/D_(N+1)  M^2*max|C_N-Cinf|  M^2*(C_N-Cinf)[0,0]  M^2*(C_N-Cinf)[0,1]')
        for N in range(len(A)):
            M = L**N
            D = np.abs(A[N+1]-A[N]).max() if N+1 < len(A) else np.nan
            r = D/np.abs(A[N+2]-A[N+1]).max() if N+2 < len(A) else np.nan
            e = A[N]-Cinf
            print(f'  {N:2d} {M:6d}  {D:.4e}  {r:8.4f}  {M**2*np.abs(e).max():.6f}  {M**2*e[0,0]:+.6f}  {M**2*e[0,1]:+.6f}')
