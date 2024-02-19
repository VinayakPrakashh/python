import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-3,3,1000)
f=np.poly1d([3,0,0,0,5])
fd1=f.deriv()
fd2=fd1.deriv()
plt.plot(t.f)
plt.plot(t,fd1)
plt.plot(t,fd2)