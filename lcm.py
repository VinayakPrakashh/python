from numpy import *
def lcm(a, b):
  greater = max(a, b)
  multiple = greater

  while True:
    if multiple % a ==0 & multiple%b==0:
      return multiple
    multiple+=greater
num1 = 16
num2 = 8
lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
