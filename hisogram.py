from matplotlib.pyplot import *
from pandas import *
data = read_csv('book1.csv')
ids = data['response_id']
ages = data['ages']
print(ages)
bins2 = [10,20,30,40]
hist(ages, bins = bins2 , edgecolor = 'black',log = True)
title("age response")
xlabel("ages")
ylabel("number of respose")
show()