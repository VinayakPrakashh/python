import numpy as np
import random
natural_numbers = np.arange(0,5)
print(natural_numbers)
sine_values = np.sin(natural_numbers)
sinc_values = np.sinc(natural_numbers)
sqrt_values = np.sqrt(natural_numbers)
print("Sine values:", sine_values)
print("Sinc values:", sinc_values)
print("Square root values:", sqrt_values)
choice=random.choice(1,100)
print(choice)