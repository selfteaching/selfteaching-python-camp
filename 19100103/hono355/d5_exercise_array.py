a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 =  a1[::-1]#将数组翻转
print(a2)

#将数组拼接成字符串
str1 = [str(i) for i in a2]#使用列表推导，将数值型转为字符串型，若列表中包含int型元素用join()函数会报错
str2 = ''.join(str1)#使用join()将列表拼接为字符串
print(str2)

str3 = str2[2:8]#用字符串切片的方式取出第三到第八个字符
print(str3)

str4 = str3[::-1]#将字符串进行反转
print(str4)

str5 = int(str4)#将结果转换成int类型


str_2 = bin(str5)#转换为二进制
str_8 = int(str4,8)#转换为八制
str_16 = int(str4,16)#转换为十六进制
print(str_2)
print(str_8)
print(str_16)