from numpy import *
N_values=[5,10,20,50,100,500]
for N in N_values:
    pi_1 = 0
    for k in range(N):
        print(k)
        pi+=((-1)**k/(2*k+1))
    pi*=4
    error = abs(pi_1-pi)
    print(f"the value of pi using {N} terms is {pi},with error {error}")