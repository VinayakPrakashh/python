f1 = open("d://prasoon.txt",'r')
f2 = open("d://prasoon2.txt",'a')
s = f1.read()
f2.write(s)
f1.close()
f2.close()
f3 = open("d://prasoon2.txt",'r')
d = f3.read()
print(d)