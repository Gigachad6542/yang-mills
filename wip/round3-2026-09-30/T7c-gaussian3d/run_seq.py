import numpy as np, sys, time
sys.path.insert(0,'.')
from schwinger import C_schwinger, to_matrix
res = {}
for n in (2,3):
    for L,Nmax in ((2,16),(3,10)):
        Cs=[]
        for N in range(Nmax+1):
            M=L**N; t=time.time()
            Cs.append(to_matrix(C_schwinger(n,M),n))
            print(n,L,N,M,'C00=%.15f'%Cs[-1][0,0], '%.1fs'%(time.time()-t), flush=True)
        res[(n,L)] = np.array(Cs)
        np.save(f'seq_n{n}_L{L}.npy', res[(n,L)])
