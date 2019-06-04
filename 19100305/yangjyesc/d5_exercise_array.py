array=[1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)

str1=''.join(str(i)for i in array)
print(str1)

str2=str1[2:9]

str3=str2[::-1]
print(str3)

int1=int(str3)
print(int1)

print('十进制整数为：',int1)
print('转换成二进制为：',bin(int1))
print('转换成八进制为：',oct(int1))
print('转换成十六进制为：',hex(int1))