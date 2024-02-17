from matplotlib.pyplot import *
from numpy import *
t = arange(0,10,.1)
x = 3*(t**4)+5
devx = gradient(x)
plot(t,devx)
show()