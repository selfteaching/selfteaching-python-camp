a=[0,1,2,3,4,5,6,7,8,9]
a.reverse()
#print(a)
b=[str(i) for i in a]
c="".join(b)
#print(c)
d=c[2:8]
e=int(d[::-1])
#print(e)
print(bin(e),oct(e),hex(e))
