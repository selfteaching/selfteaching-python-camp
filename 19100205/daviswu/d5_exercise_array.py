a = []
for i in range(10):
    a.append(i)
print(a)
a = list(reversed(a))
b = "".join(str(i) for i in a)
print(b)
c = b[2:8]
print(c)
d = c[::-1]
print(d)
e = int(d)
f = bin(e)
g = oct(e)
h = hex(e)
print(f,g,h)