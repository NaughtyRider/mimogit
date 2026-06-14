import numpy as np


def mimo_channel(Nt, Nr):
    H = np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt)/np.sqrt(2)
    return H

Nt, Nr = 4, 4
for i, element in enumerate(mimo_channel(Nt, Nr)):
    print(f"{i} element:", element)

