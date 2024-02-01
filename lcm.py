from numpy import *
def lcm(a, b):
  higher = max(a,b)
  value = higher
  while True:
   if higher%a == 0 and higher%b == 0:
    print(f"LCM is {higher}")
    break
   else:
    higher = higher+value
lcm(24,36)