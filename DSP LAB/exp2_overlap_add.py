from numpy import *
from matplotlib.pyplot import *
x1 = eval(input("Enter the input sequence   : "))
x2 = eval(input("Enter the impulse sequence : "))
N=4
M=len(x2)
L = N-M+1
def find_cir_conv(x1,x2):
    N1 = len(x1)
    N2 = len(x2)
    N =max([N1,N2])
    x1 = pad(x1, (0, N - len(x1)))
    x2 = pad(x2, (0, N - len(x2)))
    conv=zeros((N,N))
    for i in range(N):
        conv[:,i]=roll(x1,i)
    result = dot(conv,x2)
    return result
def overlap_add(x1,x2,L,M,N):
    if(len(x1)%L!=0):
        padded_x1 = pad(x1,(0,L-len(x1)%L))
    padded_x2 = pad(x2,(0,N-len(x2)))
    y = zeros(len(padded_x1)+M-1)
    x1_splitted = split(padded_x1,L)
    for i in range(len(x1_splitted)):
        x1_splitted[i] = pad(x1_splitted[i],(0,N-len(x1_splitted)))
        x1_splitted[i] = find_cir_conv(x1_splitted[i],padded_x2)
        y[i*L:i*L+N] += x1_splitted[i]
    return y[:len(x1)+M-1]
print(overlap_add(x1,x2,L,M,N))