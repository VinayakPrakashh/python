# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
def fibonacci_iterative(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

# Example usage
n = 10
fibonacci_number = fibonacci_iterative(n)
print(f"The {n}th Fibonacci number is: {fibonacci_number}")
