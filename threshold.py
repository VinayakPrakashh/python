from numpy import *
from matplotlib.pyplot import *

s = random.uniform(0,10,30)
plot(s)
show()
threshold = 2
crossed_vt = count_nonzero(s >= threshold)
below_vt = count_nonzero(s<threshold)
print(crossed_vt)
print(below_vt)