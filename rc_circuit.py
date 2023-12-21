import numpy as np
from matplotlib.pyplot import*

# plt.style.use('ggplot')
t = np.linspace(0,1,1000)
vs= 5
r = 3000 #R Value
c = 100 * 10 ** (-6) #C value
vt = vs*(1-np.exp(-t/(r*c)))
i = (vs/r)*np.exp((-1/(r*c))*t)
print(vt,i)
plot(t,vt)
plot(t,i)
show()