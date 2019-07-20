#1 翻转数组
a = [1,2,3,4,5,6,7,8,9]
c = sorted(a,reverse=True)  
#2 拼接为字符串
str1=''.join(map(str,c))     
#3 提取字符
str2 = str1[2:8]

#4 翻转字符串
str3 = str2[::-1]
print(str3)
#5 转为int型
int11 = int(str3)

#6 分别转换二进制，八进制，十六进制
print(int11)
print(bin(int11))
print(oct(int11))
print(hex(int11))




