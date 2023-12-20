from numpy import *
from matplotlib.pyplot import *

t = arange(0,10,0.1)
print(t)
y = 5*cos(t)+sin(10*t)

hist(y, bins=5)
show()
