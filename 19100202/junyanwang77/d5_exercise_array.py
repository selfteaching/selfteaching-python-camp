#3.1翻转数组
array = [1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)

#3.2翻转后的数组拼接成字符串
str1 = ''.join(str(i) for i in array)
print(str1)

#3.3字符串切片
str2 = str1[3:9]
print(str2)

#3.4将所得切片翻转
str3 = str2[::-1]
print(str3)

#3.5将结果转为int型
int1 = int(str3)
print(int1)

#3.6分别转换成二进制，八进制，十六进制
print('十进制整数为: ',int1)
print('转换成二进制为: ',bin(int1))
print('转换成八进制为: ',oct(int1))
print('转换成十六进制为: ',hex(int1))