from numpy import *
from matplotlib.pyplot import *

s = random.uniform(0,10,30)
axhline(y = 2)
print(print)
plot(s)


show()
threshold = 2
above_vt = count_nonzero(s>=threshold)
below = count_nonzero(s<threshold)
print(above_vt,below)
