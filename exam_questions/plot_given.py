import matplotlib.pyplot as plt
import numpy as np

# Define start, end values, and number of points
start_value = 0
end_value = 10
num_points = 100

# Create time points
t = np.linspace(0, 1, num_points)

# Calculate ramp values using linear interpolation
y = start_value + t * (end_value - start_value)

# Plot the ramp wave
plt.plot(t, y)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Ramp Wave')

# Show the plot
plt.show()
