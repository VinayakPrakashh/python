import numpy as np
import matplotlib.pyplot as plt

# Define carrier and modulating signals
carrier_freq = 1000  # Hz
carrier_amp = 1

message_freq = 100  # Hz
message_amp = 0.5

# Generate time samples
t = np.linspace(0, 1, 1000)  # 1 second with 1000 samples

# Generate carrier and modulating signals
carrier_signal = carrier_amp * np.sin(2 * np.pi * carrier_freq * t)
message_signal = message_amp * np.sin(2 * np.pi * message_freq * t)

# Modulate the carrier with the message (double-sideband AM)
modulated_signal = carrier_amp * (1 + message_amp * message_signal)

# Plot all signals
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal, label='Carrier')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier Signal')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, message_signal, label='Message')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, label='Modulated')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modulated Signal (AM)')
plt.legend()

plt.tight_layout()
plt.show()
