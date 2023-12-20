from matplotlib.pyplot import *
from scipy.integrate import odeint
from numpy import *
def dx_dt(X,t):
    return X[1], -2*X[1]-1*X[0]+exp(-t)
x0 = [0,0]

t = linspace(0,20)

ans = odeint(dx_dt,x0,t)
print(ans)
ys = ans[:,0]

plot(t,ys)

show()
