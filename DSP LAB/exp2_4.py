from matplotlib.pyplot import *
import numpy as np
import time
def dft_matrix(N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    omega = np.exp(-2j * np.pi * k * n / N)
    print(omega)
    return omega
for gamma in range(2,4):
    N = 2**gamma
    start_time = time.time()
    dft_matrix(N)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time taken for N={N} is {total_time} seconds")
    
