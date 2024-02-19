import random
from matplotlib.pyplot import *
def coinToss(number):
    
    errorList =[]
    for i in range(len(number)):
        recordList =[]
        for j in range(number[i]):
            flip = random.randint(0,1)
            if flip == 0:
                recordList.append(0)
            else :
                recordList.append(1)
        probHead = recordList.count(1)/number[i]
        error = abs(0.5 - probHead)
        errorList.append(error)
    return errorList
x=[50,100,500,1000,10000]
error = coinToss(x)
print(error)
plot(x,error)
show()