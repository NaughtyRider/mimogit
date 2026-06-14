import numpy as np


def mimo_channel(Nt, Nr):
    H = np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt)/np.sqrt(2)
    return H

Nt, Nr = 4, 4
noise = np.random.randn(Nr) + 1j * np.random.randn(Nr)/np.sqrt(2)
print("Noise:", noise)
# for i, element in enumerate(mimo_channel(Nt, Nr)):
    # print(f"{i} element:", element)
bpsk = np.array([1, -1, 1, -1])  # BPSK modulation symbols
print("BPSK symbols:", bpsk)
channel=mimo_channel(Nt, Nr)
y = channel @ bpsk + noise
print("Received signal y:", y)
print("Noise:", y-bpsk)
print("channel:", channel)
# as we can see, the received signal y is a combination of the transmitted BPSK symbols, the channel effects, and the noise. The noise can be observed by subtracting the transmitted symbols from the received signal. The channel matrix represents the effects of the wireless channel on the transmitted signal, and it can cause distortion and fading. The received signal is a complex vector that contains both the real and imaginary parts, which are influenced by the channel and noise.
