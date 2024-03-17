f=open("prasoon.txt","w")
while True:
  ln=input("Enter a line of text...type quit to exit\n")
  if ln=='quit':
     break
  f.write(ln+'\n')
#file contents
f.close()