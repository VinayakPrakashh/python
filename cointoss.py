import random
from matplotlib.pyplot import *
def coinToss(number):
    recordList = []
    errorlist = []
    for _ in range(len(number)):
      recordList.append([])
      errorlist.append([])
    for i in range(0,len(number)):
        for j in range(number[i]):
            flip=random.randint(0,1)
            if(flip==0):
                recordList[i].append(0)
            else:
                recordList[i].append(1)
        probHead = recordList[i].count(1)/number[i]
        error = 0.5 -probHead
        errorlist[i].append(abs(error))
    return errorlist

num = int(input("enter the number of tosses: "))
test = [0]*num
for i in range(0,num):
    test[i]=int(input(f"{i}. "))
print(test)
result = coinToss(test)
plot(test,result)
show()