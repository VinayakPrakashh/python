try:
    f1 = open("d://s.png", "rb")
    f2 = open("d://s2.png", "wb")
    content=f1.read()
    f2.write(content)
    f1.close()
    f2.close()
    print('File is copied')
except:
    print("file does not exist")