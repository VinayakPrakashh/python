f = open("new.py",'r+t',encoding='cp1252')
if f:
    print(f.name)
for i in range(1,11):
    f.write(str(i)+"\n")
f.close()
f = open("new.py",'r+t',encoding='cp1252')
x = f.read(8)
y = f.readline()
print(y)