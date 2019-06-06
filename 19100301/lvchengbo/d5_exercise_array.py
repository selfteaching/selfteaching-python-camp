a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)

# 参考 https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
b = ''.join(map(str, a))
print(b)

c = b[2:8]
print(c)

d = c[2:8][::-1]
print(d)

e = int(d)
print(e)

f = bin(e)
g = oct(e)
h = hex(e)
print(f,g,h)