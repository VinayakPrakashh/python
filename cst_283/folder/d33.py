# Write a Python program to combine two dictionary adding values for common keys. d1 = {'a':10, 'b': 20, 'c':30} d2 = {'a': 30, 'b': 20, 'd':40} Sample output: {'a': 40, 'b': 40, 'd': 40, 'c': 30}

d1 = {'a':30,'b':40}
d2 ={'a':30,'b':30}
d3 = dict()
for i in d1:
    for j in d2:
        d3[i] = d1[i]+d2[i]
    else:
        d3[key]=d1[key]
    for key in d2:
     if key not in d3:
       d3[key]=d2[key]
print(d3)