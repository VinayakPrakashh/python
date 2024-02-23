# We can also do the above program by reversing the file object
try:
     f1 = open("d://sample.py", "r")
     f2 = open("d://python.py", "a")
     rf1=reversed(list(f1)) # reversing the file object after converting it into a list sequence
     for line in rf1:
        f2.write(line) # writing each line in the new file
     f1.close()
     f2.close()
     print('File is copied')
except:
     print("file does not exist")