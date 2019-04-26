a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=list(map(str,a))
c=sorted(b,reverse=True)
d=' '.join(c)
print(d)