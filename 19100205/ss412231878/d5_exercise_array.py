#数组操作，进制转换

a=[0,1,2,3,4,5,6,7,8,9]

#翻转
a.reverse()
print(a)

#转换成字符串
b=''.join(str(x) for x in a)
print(b)

#切片
c=b[2:8]
print(c)

#再翻转
d=c[::-1]
print(d)

#转换成int
e=int(d)
print(e)

#转换成2进制、8进制、16进制
print(e,"的2进制为",bin(e))
print(e,"的2进制为",oct(e))
print(e,"的2进制为",hex(e))