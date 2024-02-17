from matplotlib.pyplot import *
from numpy import *
t = arange(1,10,0.01)
input = sin(t)
output = where(sin(t)>=0,sin(t),0  )
subplot(2,1,1)
plot(t,input)
subplot(2,1,2)
plot(t,output)
show()