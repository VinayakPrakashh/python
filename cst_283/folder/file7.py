# Read a file and writes out a file with the lines in reversed order.
try:
     f1 = open("d://sample.py", "r")
     f2 = open("d://python.py", "a")
     lst=f1.readlines() # read the entire contents into a list
     rlst=reversed(lst) #reversing the list
     f2.writelines(rlst) # writing each line in the new file
     f1.close()
     f2.close()
     print('File is copied')
except:
     print("file does not exist")