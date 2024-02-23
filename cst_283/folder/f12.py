# Input n numbers and store the cube of each number in a file
f=open("d://prasoons.txt","w")
n = int(input("Enter n number: "))
for  i in range(0,n):
    val = int(input("enter no: "))
    val = val**3
    f.write(str(val)+"\n")
f.close()