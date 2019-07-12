a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.sort(reverse=True)
print(a)

b = [str(i) for i in a]
print(b)

c = ''.join(b)
print(c)
print(type(c))
print(c[3:9])

d = (c[::-1])
print(d)

e = int(d)
print(e)

print(bin(e))
print(oct(e))
print(hex(e))
