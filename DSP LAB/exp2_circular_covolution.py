from numpy import *
from matplotlib.pyplot import *
def find_cir_conv(x1,x2):
    N1 = len(x1)
    N2 = len(x2)
    N =max([N1,N2])
    print(N)
    x1 = pad(x1, (0, N - len(x1)))
    x2 = pad(x2, (0, N - len(x2)))
    conv=zeros((N,N))
    
    for i in range(N):
        conv[:,i]=roll(x1,i)
    result = dot(conv,x2)
    return result
x1 = eval(input("Enter the input sequence   : "))
x2 = eval(input("Enter the impulse sequence : "))
y = find_cir_conv(x1,x2)

print("y(n)=",y)