a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#翻转
a.reverse()
print(a)
#拼接成字符串
b=[str(x) for x in a]
c="".join(b)
print(c)
#取出第三到第八个字符
d=c[2:8]
print(d)
#字符串进行翻转
e=d[::-1]
print(e)
#转换为 int 类型
f=int(e)
print(f)
#转换成二进制，八进制，十六进制
n1=bin(f)
n2=oct(f)
n3=hex(f)
print(n1,n2,n3,sep='\n')