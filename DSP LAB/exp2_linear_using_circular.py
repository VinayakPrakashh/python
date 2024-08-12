from numpy import *
from matplotlib.pyplot import *
def find_cir_conv(x1,x2):
    N = len(x1)
   
    conv=zeros((N,N)) 
    for i in range(N):
        conv[:,i]=roll(x1,i)
    result = dot(conv,x2)
    return result  
x1 = eval(input("Enter the input sequence   : "))
x2 = eval(input("Enter the impulse sequence : "))
l1=len(x1)
m1=len(x2)
N=l1+m1-1
x1=np.pad(x1,(0,N-l1))
x2=np.pad(x2,(0,N-m1))
y = find_cir_conv(x1,x2)
print("y(n)=",y)