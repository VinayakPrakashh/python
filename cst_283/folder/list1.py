# Program to read list of names and sort the list in alphabetical order.( university question)
n=int(input("Enter the number of names...."))
name=[]
print("enter the names")
for i  in range(n):
    x = input()
    name.append(x)
name.sort()
print(name)