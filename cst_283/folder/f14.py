# Write a program to read numbers stored in one file and store the sorted
# numbers in another file after deleting duplicates.(university question)
try:
     f1=open("file1.dat","r") # numbers are stored line by line
     lst=f1.readlines() # read the numbers into a list
     nlst=list(set(lst)) # removing duplicates easy method is to make a set
     nlst.sort() # sorting the list
     f2=open("file2.dat","w") #writing into a new file
     f2.writelines(nlst)
     f1.close()
     f2.close()
     print("sorted file file2.dat is created")
except:
     print("File not found..")