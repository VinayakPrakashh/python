from numpy import *
import matplotlib.pyplot as plt

# Generate time values
t = linspace(0, 4*pi, 200)
sine_wave = sin(t)
half_wave_rect = where(sine_wave >= 0, sine_wave, 0)
plt.plot(t,half_wave_rect)
plt.show()