from numpy import *
from matplotlib.pyplot import *

ac = float(input("Enter the amplitude of carrier signal: "))
fc = float(input("Enter the frequency of carrier signal: "))
am = float(input("Enter the amplitude of message signal: "))
fm = float(input("Enter the frequency of message signal: "))
mi = float(input("Enter the modulation index: "))
t = linspace(1,10,1000)
carrier = ac*cos(2*pi*fc*t)
message = am*cos(2*pi*fm*t)
modulated = ac*(1+mi*cos(2*pi*fm*t))*cos(2*pi*fc*t)
subplot(3,1,1)
plot(t,carrier)
subplot(3,1,2)
plot(t,message)

subplot(3,1,3)
plot(t,modulated)
show()
