[0,1,2,3,4,5,6,7,8,9]
#1 翻转数组
number= [0,1,2,3,4,5,6,7,8,9]
number1 = list(reversed(number))
print(number1)
#翻转后的数组拼接成字符串
str1= ''.join([str(i) for i in number1]) 
print(str1)
#用字符串切片的方式取出第三到第八个字符
str2 = str1[2:8]
print(str2)
#字符串翻转 
str3 = str2[::-1]
print(str3)

#转为int型
int1= int(str3)

#6 分别转换二进制，八进制，十六进制
print(int1)
print(bin(int1))
print(oct(int1))
print(hex(int1))