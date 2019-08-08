x = [0,1,2,3,4,5,6,7,8,9]
x.reverse()

y = ''.join(str(i) for i in x)

z = y[2:8]
print(z)

a = z[::-1]
print(a)

b=int(a)

c = bin(b)
print(c)
d = oct(b)
print(d)
e = hex(b)
print(e)