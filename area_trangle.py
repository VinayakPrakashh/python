x =159
sum = 0
length = len(str(x))
for digit in str(x):
    sum=sum+(int(digit))**length
if sum == x:
    print("number is armstrong")
else:
    print("number is not armstrong")