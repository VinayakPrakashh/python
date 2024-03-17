# Read and print a file with all punctuation removed.( university question)
import string
intab = string.punctuation
outtab = " "*len(intab)
trantab = str.maketrans(intab,outtab)
try:
    f1 = open("dd",'r')
    for line in f1:
        print(s = line.translate(trantab))
except KeyError:
    

