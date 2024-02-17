from matplotlib.pyplot import *
from numpy import *
a = int(input("Lower limit: "))
b = int(input("Upper limit: "))
n = int(input("Num of Strips: "))

h = (b-a)/n
def f(x):
    return 1/(1+x)
sum =0
k = 0
while k<n:
    x= a+(k*h)
    if k%2==0:
        sum += 2*f(x)
    else: 
        sum+= 4*f(x)

    k = k+1
int_a = (h/3)*((f(a)+f(b))+sum)
print(int_a)
    