from numpy import *
from matplotlib.pyplot import *
t = linspace(0, 2*pi, 1000)

def full_wave_rectifier(t):
    return np.abs(np.sin(t))

N=100
n = 0
fun = 0
while(n<N):
    fun += abs((sin(t)))
    n=n+1
subplot(1,2,1)
plot(t, full_wave_rectifier(t))
xlabel('Time (t)')
ylabel('Voltage (V)')
title('Full Wave Rectifier')
grid(True)
subplot(1,2,2)
plot(fun,t)
show()