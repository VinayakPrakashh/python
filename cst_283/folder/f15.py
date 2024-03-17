# Printing and Finding the count of four letter words in a file ( University Question)
try:
     f=open("data.txt","r")
     st=f.read()
     stn=st.replace("\n"," ")
     words=stn.split(" ")
     c=0
     for w in words:
          if len(w)==4:
            print(w)
            c=c+1
     print("Count of 4 letter words=",c)
     f.close()
except:
     print("File not found..")