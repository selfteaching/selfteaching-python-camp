num = [0,1,2,3,4,5,6,7,8,9]
#翻转
num.reverse()
#反转后拼成字符串
str1 = ''.join(str(i) for i in num)
print(type(str1))

#用字符串切片的方式取出第三道第八个字符（包含第三盒第八个字符串
str2 = str1[2:8]

#将获取的字符串进行反转
str3 = str2[::-1]

#将结果转为int型
str4 = int(str3)
print(type(str4))

#转换成二进制 八进制 十六进制
print(str4)
print(bin(str4))
print(oct(str4))
print(hex(str4))