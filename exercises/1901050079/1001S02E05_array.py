a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=list(map(str,a))
c=sorted(b,reverse=True)
d=''.join(c)
e=d[2:8]
f=e[::-1]
g=int(f)
print('十进制')
print(g)
print('二进制')
h=bin(g)
print(h)
print('八进制')
i=oct(g)
print(i)
print('十六进制')
j=hex(g)
print(j)
