a=[0,1,2,3,4,5,6,7,8,9]
b=a[::-1]#反转列表
print(b)
c=[str(i)for i in b]#将列表变为含有‘’列表
print(c)
d=''.join(c)#‘’.join(c)将列表转为字符串
print(d)

e=d[2:8]#选取3到8位字符串
print(e)

f=list(e)#将字符串转化成列表
print(f)
g=f[::-1]#反转列表
print(g)
h=''.join(g)#将含‘’列表转化成字符串
print(h)

j=int(h)#将字符串转化成整型
print(bin(j),oct(j),hex(j))#将整数转化成二进制，八进制，十六进制