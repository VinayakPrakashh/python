import os
os.chdir('d://Github')
x = os.listdir()
count = 0
for i in x:
    if os.path.isdir('d://Github'):
        count = count +1
print(count)