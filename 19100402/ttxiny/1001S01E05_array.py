a=[0,1,2,3,4,5,6,7,8,9]
a.reverse()
b=[str(i) for i in a]
c="".join(b)
d=c[2:8]
e=int(d[::-1])
print('二进制：'+bin(e)+'\n八进制:'+oct(e)+'\n十六进制:'+hex(e))

