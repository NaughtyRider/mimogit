import numpy as np


def mimo_channel(Nt, Nr):
    H = np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt)/np.sqrt(2)
    return H

Nt, Nr = 4, 4
print(mimo_channel(Nt, Nr))