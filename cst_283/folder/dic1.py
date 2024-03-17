S=input("Enter the string…..")
d = dict()
for c in S:
    d[c] = d.get(c,0)+1
s = list(d.items())
s.sort(key=lambda v:v[1],reverse=True)
print(s)
