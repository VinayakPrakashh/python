from matplotlib.pyplot import *
from numpy import *
t = linspace(1,5,1000)
y= 2*(t%1)-1
plot(t,y)
show()