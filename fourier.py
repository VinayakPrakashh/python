from numpy import *
from matplotlib.pyplot import *
N = 100
n = 0
x = linspace(0,10,1000)
sum = 0
while(N>n):
    sin_fun=sin(((2*n)+1)*x)/((2*n)+1)
    n=n+1
    sum=sum+sin_fun


plot(x,sum)
show()
