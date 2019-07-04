# Filename : 1001S02E05_array.py
# author by : 张金磊

#数组翻转
list = [0,1,2,3,4,5,6,7,8,9]
list_rev = list[::-1]
print(list_rev)

#转换成字符串
str1 = "".join(map(str,list_rev))
print(str1)


#取出2-8的元素
str2 = str1[2:8]
print(str2)


#翻转上一次（2-8）的结果
str3 = str2[::-1]
print(str3)


#转换成正整型
str4 = int(str3)
print(str4)


#转换成二进制、八进制、十六进制
str5 = bin(str4)
str6 = oct(str4)
str7 = hex(str4)


print(str5)
print(str6)
print(str7)