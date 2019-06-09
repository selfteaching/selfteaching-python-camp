def Reverse(a):
    a.reverse()
    return a

a = [0,1,2,3,4,5,6,7,8,9]
b = Reverse(a)
c = ''.join(str(i) for i in b)
d = c[2:8]
e = int(d[: : -1])
f = bin(e)
g = oct(e)
h = hex(e)
print(f,g,h)