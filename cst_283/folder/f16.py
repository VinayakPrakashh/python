# Assume that there is a text file named “numbers.txt”. Write a python program to find the median of list of numbers in the file without using standard function for median ( University Question)
f1=open("numbers.txt","r") # numbers are stored line by line
lst=f1.readlines() # read the numbers into a list
lst.sort()
if len(lst)%2 == 0:
    med = (int(lst(len//2))+int(lst(len(lst)//2+1)))/2
else:
    med = int(lst(len(lst)/2))
print(med)