import numpy as np, sys
sys.path.insert(0,'.')
from fourier import *
from brute import brute
Cb = np.load('brute_n2_L2_N2.npy'); Cf = C_fourier_direct(2,4)
d = Cb-Cf; i,j = np.unravel_index(np.abs(d).argmax(), d.shape); print(i,j,Cb[i,j],Cf[i,j])
print(np.round(d[:6,:6]*1e6,3))
# symmetry of brute
print('brute asym', np.abs(Cb-Cb.T).max())
C,T,D = brute(2,2,2)
s=8; G = D.T@D; w,V = np.linalg.eigh(G); print('eig small', np.sort(w)[:520][-10:], np.sort(w)[508:516])
