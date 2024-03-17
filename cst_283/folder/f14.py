# Write a program to read numbers stored in one file and store the sorted
# numbers in another file after deleting duplicates.(university question)
try:
     f1=open("file1.dat","r") # numbers are stored line by line
     f2 = open("file2.dat",'w')
     lst = f1.readlines()
     s = list(set(lst))
     s.sort()
     f2.writelines(s)
     f2.close()
     print("sorted file file2.dat is created")
except:
     print("File not found..")