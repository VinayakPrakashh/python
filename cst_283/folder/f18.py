f=open("test.dat","w")
l=['mec\n','thrikakara\n','cochin']
f.writelines(l)
f.close()

f=open("test.dat","rb")
f.seek(-6,2)
print(f.read(6).decode('utf-8'))
f.close()
