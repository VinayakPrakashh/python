try:
     f1 = open("d://sample.py", "r")
     f2 = open("d://prasoon.txt", "w")
     lst=f1.readlines() # reading lines to a list
     for l in lst:
        if l !='\n':
           f2.write(l)
     f1.close()
     f2.close()
     print('File is copied')
except:
     print("file does not exist")