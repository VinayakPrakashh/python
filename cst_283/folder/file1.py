# i)writes the text ”PROGRAMMING IN PYTHON” to a file with name code.txt
 # ii) then reads the text again and prints it to the screen.

f = open("d://prasoon.txt",'w')
f.write("Hello World")
f.close()
f= open("d://prasoon.txt",'r')
s = f.read()
print(s)
f.close