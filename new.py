import matplotlib.pyplot as plt
import numpy as np

# Define a function to plot and find local minima
def plot_and_find_minima(func, x_min, x_max, num_points):
  # Generate x-axis values
  x = np.linspace(x_min, x_max, num_points)

  # Calculate y-axis values
  y = func(x)

  # Plot the function
  plt.plot(x, y)

  # Find local minima
  local_minima = []
  for i in range(1, len(y) - 1):
    if y[i-1]>y[i]and y[i]<y[i+1]:
      local_minima.append(x[i])

  # Print local minima
  print("Local minima:", local_minima)

  # Show the plot
  plt.show()

# Define the function to plot
def f(x):
  return x**3 - 3*x**2 + 2*x

# Set plot parameters
x_min = -2
x_max = 4
num_points = 100

# Plot the function and find local minima
plot_and_find_minima(f, x_min, x_max, num_points)
