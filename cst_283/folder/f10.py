# Read and print a file with all punctuation removed.( university question)
import string
intab = string.punctuation
outtab = " "*len(intab)
trantab = str.maketrans(intab,outtab)
try:
    f1 = open("D://prasoon.txt",'r')
    for line in f1:
        print(line.translate(trantab))
    f1.close()
except:
    print("file does not excist")
