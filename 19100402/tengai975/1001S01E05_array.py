list1=[0,1,2,3,4,5,6,7,8,9]
#将数组翻
list1.reverse()
print(list1)

#翻转后的字符拼接成字符串
list2=[str(i)for i in list1]#每个数字转成字符串
print(list2)

str1=''.join(list2)   #把单个字符串拼接成一个字符串
print(str1)

#把字符串切片取出第三到第八的字符（包含第三和第八个字符）
str2=str1[2:8]
print(str2)

#把获得的字符串从右边第一个开始翻转
str3=str2[::-1]
print(str3)

#把结果转换成int类型
i=int(str3)
print(i)

#分别转换成二进制，八进制，十六进制
print(bin(i))
print(oct(i))
print(hex(i))