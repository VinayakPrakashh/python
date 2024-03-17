def fact(x):

    if x == 0:
        return 1
    else:
        return x*fact(x-1)
x = int(input("Enter the number: "))
factorial = fact(x)
count =0
for digit in str(factorial):
    count+=1
print(count)