def hcf_loop(a, b):
  hcf = 1
  for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      hcf = i
  return hcf
num1 = 6
num2 = 2

hcf_result = hcf_loop(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf_result}")
