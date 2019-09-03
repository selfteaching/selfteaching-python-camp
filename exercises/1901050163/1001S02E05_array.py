a=[0,1,2,3,4,5,6,7,8,9]
b=list(reversed(a))
print(a)

str=''.join(str(i) for i in b)
print(str)

c=str[2:8]
print(c)

d=c[::-1]
print(d)

e=int(d)

f=bin(e)
print(f)
g=oct(e)
print(g)
h=hex(e)
print(h)