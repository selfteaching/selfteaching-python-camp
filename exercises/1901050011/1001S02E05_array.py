
a1 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#数组翻转
a1 = a1[::-1]
#print(a1)

#数组转字符串
str1 = ''.join(str(i) for i in a1) 
print(str1)

str2 = str1[2:8]
print(str2)

#字符串翻转
str3 = str2[::-1]
print(str3)

#字符串转int
dec = int(str3)
print(dec)


print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))