# Read a text file and print each word and its length in sorted order
try:
    f = open("d://prasoon.txt",'r')
    s = f.read()
    s = s.replace("/n"," ")
    words = s.split()
    for i in words:
        if len(i)!=0:
            print(i,len(i))
        f.close()

except:
    print("file does not excist")