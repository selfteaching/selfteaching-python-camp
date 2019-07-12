a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#翻转
a0=a[::-1]
print(a0)

#将数组转为字符串
b=[str(i) for i in a0]
print(b)
#将字符串拼接
c="".join(b)
print(c)
#切片方式获取第三-第八个数字
d=c[2:8]
print(d)
#对字符串翻转
e=d[::-1]
print(e)
#结果转为int类型
f=int(e)
print(f)
#转为二进制
g=bin(f)
print(g)
#转为八进制
h=oct(f)
print(h)
#转为十六进制
i=str(f)
print(i)