# Create a file with 10 integer numbers and finding the average of odd numbers
f1 = open("d://prasoon.txt",'w')
for i in range(0,4):
    x = int(input("No: "))
    f1.write(str(x)+"\n")
f1.close()
f2 = open("d://prasoon.txt",'r')
s = 0
c = 0
for f in f2:
    x = int(f)
    if x%2 != 0:
        s +=x
        c+=1

print(s,c)

