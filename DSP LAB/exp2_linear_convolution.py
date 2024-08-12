from numpy import *
from matplotlib.pyplot import *
def find_lin_conv(x1,x2):
    N1 = len(x1)
    N2 = len(x2)
    N = N1+N2-1
    y = zeros(N)
    for n in range(N):
        for k in range(N1):
            if n-k>=0 and n-k<N2:
                y[n] += x1[k]*x2[n-k]
    return y
x1 = eval(input("Enter the input sequence: "))
x2 = eval(input("Enter the impulse sequence: "))
y = find_lin_conv(x1,x2)
print("y(n)=",y)
