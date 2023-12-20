from scipy.integrate import odeint
from matplotlib.pyplot import *
from numpy import *

def model(x,t,k):
    dxdt = -(k*x+exp(x))
    return dxdt
x0 = 5

t = linspace(0,10)
k = 0
x = odeint(model,x0,t,args=(k,))

plot(x,t)
show()