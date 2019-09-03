#数组翻转
arr = [i for i in range (10)]
arr.sort(reverse=True)
#print(arr)

#拼接成字符串
str =''.join(str(i) for i in arr)
#print(str)

#切片，取3-8的字符
str1 = str[3:9]
#print(str1)

#字符翻转
str2 =str1[::-1]
#print(str2)

#转换为int型
num = int(str2)
print('整型为:',num)
#输出成二进制，八进制，十六进制
print('\n二进制为：\n',bin(num))
print('\n八进制为：\n',oct(num))
print('\n十六进制为：\n',hex(num))