from matplotlib.pyplot import *
from numpy import *
t = arange(0,10,.01)
x1 = abs(sin(t))
x=where(x1>= .2,.2,x1)
plot(t,x)
show()