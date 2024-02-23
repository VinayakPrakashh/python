try:
     f1 = open("d://sample.py", "r")
     f2 = open("d://prasoon.txt", "w")
     while True:
          l=f1.readline()
          if l=="":
            break
          if l[0]!='#':
            f2.write(l)
     f1.close()
     f2.close()
     print('File is copied')
except:
     print("file does not exist")