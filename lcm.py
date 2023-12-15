from numpy import *
def lcm(a, b):
  greater = max(a, b)
  multiple = greater

  while True:
    if multiple % a == 0 and multiple % b == 0:
      return multiple
    multiple += greater
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
