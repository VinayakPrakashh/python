from matplotlib.pyplot import *
import numpy as np
import time

def dft_matrix(N):
    
    n = np.arange(N)
   
    k = n.reshape((N, 1))
    
    omega = np.exp(-2j * np.pi * k * n / N)
 
    return omega

def compute_dft(sequence):
    N = len(sequence)
    VN = dft_matrix(N)
    
  
gammas = range(2, 11)
dft_times = []
fft_times = []

for gamma in gammas:
    N = 2 ** gamma
    
    sequence = np.random.rand(N)
    
    # Measure DFT time
    start_time = time.time()
    compute_dft(sequence)
    end_time = time.time()
    dft_times.append(end_time - start_time)
    
    # Measure FFT time
    start_time = time.time()
    np.fft.fft(sequence)
    end_time = time.time()
    fft_times.append(end_time - start_time)
figure(figsize=(10, 6))
plot(gammas, dft_times, label='DFT Computation Time', marker='o')
plot(gammas, fft_times, label='FFT Computation Time', marker='x')
xlabel('γ')
ylabel('Time (seconds)')
title('Computation Time for DFT and FFT')
legend()
show()