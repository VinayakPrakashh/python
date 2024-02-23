f1 =open('d://sample.py','r')
f2 = open('d://prasoon.txt','w')
while True:
    f1.readline()
    s = f1.readline()
    if s =="":
        break
    f2.write(s)
f1.close()
f2.close()
