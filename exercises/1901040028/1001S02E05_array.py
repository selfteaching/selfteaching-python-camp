
arr=[0,1,2,3,4,5,6,7,8,9]
b=list(reversed(arr))    #将数组翻转
str1 = ''.join(str(i) for i in b)#拼接为字符串
str2 = str1[2:8]#取数第3到8个字符
str3=str2[::-1]#字符串翻转
int1 = int(str3)#转换为int型
print(int1)
print('转换成二进制为: ',bin(int1))
print('转换成八进制为: ',oct(int1))
print('转换成十六进制为: ',hex(int1))

