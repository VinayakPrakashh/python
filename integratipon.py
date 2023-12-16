from  numpy import *
from scipy.integrate import quad
t=arange(-2,2,-0.01)
def fun(t):
    return 4*t**2+3
max=2
min=-2
res,e=quad(fun,min,max)
print(res)