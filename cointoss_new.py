
from matplotlib.pyplot import *
import random

x = int(input("Enter the number of tosses: "))
def toss_coin(x):
    recordList =[]
    errorList = []

    for i in range(x):
        flip = random.randint(0,1)
        print(flip)
        if flip ==0:
            recordList.append(0)
        else:
            recordList.append(1)
        probHead = recordList.count(1)/x
        error = abs(0.5 - probHead)
        errorList.append(error)
    return errorList

error = toss_coin(x)
print(error)
t = np.linspace(1,10,x)
plot(t,error)
show()