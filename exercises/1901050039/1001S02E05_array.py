#数组翻转
#翻转后的数组拼接成字符串
#用字符串切片的方式取出第三到第八个字符（含第三和第八个字符）
#将3获得的字符串进行翻转
#将结果转换为int类型
#转换成二进制，八进制，十六进制，输出三种进制的结果

#数组翻转
arr = [i for i in range (10)]
arr.sort(reverse=True)

#拼接成字符串
str =''.join(str(i) for i in arr)

#切片，取字符
s = str[3:9]

#字符翻转
s2 = s[::-1]

#转换为int
num = int(s2)

#转换成二进制，八进制，十六进制
print('转换成二进制为：', bin(num))
print('转换成八进制为：', oct(num))
print('转换成十六进制为：', hex(num))
