import numpy as np
complex_numbers = np.array([complex(1, 2), complex(3, 4), complex(5, 6), complex(7, 8), complex(9, 10)],dtype=complex)
absolute_values = np.abs(complex_numbers)
real_parts = np.real(complex_numbers)
imaginary_parts = np.imag(complex_numbers)
print("Absolute values:", absolute_values)
print("Real parts:", real_parts)
print("Imaginary parts:", imaginary_parts)
