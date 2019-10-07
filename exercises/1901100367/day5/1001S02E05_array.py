
a=[0,1,2,3,4,5,6,7,8,9]
b=[0,1]
#1 把数组倒叙翻转
a.sort(reverse=True)
#print(a)

#2  把数组列表转换为字符串
#给列表的数字加上单引号，不加的话直接使用#c=''.join(d)会报数字类型错误
d=[str(i) for i in a]
c=''.join(d)

#3 切片

c=c[2:8]

#4 将获得的字符串进行翻转
c=c[::-1]

#5 数字类型转换
f=int(c)
print(f,"二进制是：",bin(f))
print(f,"八进制是：",oct(f))
print(f,"十六进制是：",hex(f))


