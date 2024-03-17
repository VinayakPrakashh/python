x = int(input("ENter the number of  values: "))
val = []
print("Enter the values")
for i in range(x):
    s = int(input())
    val.append(s)
print(val)
sum = 0
for j in range(len(val)):
    if val[j] %2 == 0:
        sum+= val[j]
print(sum)