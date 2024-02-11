from numpy import *
from matplotlib.pyplot import *
ac = float(input("enter carrier amplitude"))
fc = float(input("enter carrier frequency"))
am = float(input("enter message amplitude"))
fm = float(input("enter message frequency"))
mi = float(input("modulation index: "))

t = linspace(1,10,1000)
carrier = ac*cos(2*pi*fc*t)
message = am*cos(2*pi*fm*t)
modulated = ac*(1+mi*cos(2*pi*fm*t))*cos(2*pi*fc*t)

subplot(3,1,1)
plot(t,carrier)
title = 'carrier'
subplot(3,1,2)
plot(t,message)
title = 'message'
subplot(3,1,3)
plot(t,modulated) 
title = 'modulated'
show()