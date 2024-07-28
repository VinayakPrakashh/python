from matplotlib.pyplot import *
import numpy as np
def dft_matrix(N):
    n = np.arange(N)
    k = 0
    print(k)
    omega = np.exp(-2j * np.pi * k * n / N)
    print(np.shape(omega))
    return omega
N = 4
VN = dft_matrix(N)
print(VN)