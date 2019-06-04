a=[0,1,2,3,4,5,6,7,8,9]
a1=list(reversed(a))   #翻转a
print(a1)

str = ''.join(str(i) for i in a1)   #翻转后的数组拼接成字符串
print(str)

a2=str[2:8]   #用字符串切片的方式取出第三到第八个字符
print(a2)

result=a2[::-1]   #翻转字符串
print(result)

int(result)   #转换成int
print(int(result))

dec=int(result)
print(bin(dec))   #转换成二进制
print(oct(dec))   #转换成八进制
print(hex(dec))   #转换成十六进制