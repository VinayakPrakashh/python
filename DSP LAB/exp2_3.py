from matplotlib.pyplot import *
import numpy as np
def dft_matrix(N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    omega = np.exp(-2j * np.pi * k * n / N)
    print(omega)
    return omega
def plot_dft_matrix(N):
    VN = dft_matrix(N)
    figure(figsize=(12, 6))
    subplot(1, 2, 1)
    imshow(np.real(VN))
    title(f'Real part of DFT matrix for N={N}')
    colorbar()
    subplot(1, 2, 2)
    imshow(np.imag(VN))
    title(f'Imaginary part of DFT matrix for N={N}')
    colorbar()
    show()
N =(np.random.randint(0,16))
plot_dft_matrix(N)