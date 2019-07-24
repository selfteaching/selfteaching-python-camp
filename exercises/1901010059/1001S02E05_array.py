a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()

b = [str(i) for i in a]
c =''.join(b)

d = c[2:8]
print(d)
e = d[::-1]

f = int(e)

g = bin(f)
print(g)
h = oct(f)
print(h)
j = hex(f)
print(j)