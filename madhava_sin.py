def madhava_sine(x, n):
  sine = x
  sign = 1
  for i in range(1, n+1):
    sine += sign * (x**3 / (3*i**2) - x**5 / (5*i**4) + x**7 / (7*i**6))
    sign *= -1
  return sine

# Example usage
angle = 0.5
terms = 10
sine_approx = madhava_sine(angle, terms)
print(f"Sine of {angle} radians (Madhava series, {terms} terms): {sine_approx}")
