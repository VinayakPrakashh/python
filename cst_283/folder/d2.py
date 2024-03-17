d = {}
for i in range(5):
    x = input("enter rollno:  ")
    y = input("Enter name: ")
    d[x] = y
l=list(d.items())
print(l)
l.sort(key=lambda v:v[1])
print("name and roll number in sorted order of name")
for i in l:
    print(i[1],":",i[0]) 