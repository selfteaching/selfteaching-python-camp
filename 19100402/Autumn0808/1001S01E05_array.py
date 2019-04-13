mylist = [0,1,2,3,4,5,6,7,8,9]
print(mylist)
#将mylist数组反转
list1 = mylist[::-1]
print(list1)
#反转后的数组拼接成字符串
##用map()将list1中的元素一一映射为str并拼接成新的字符串
str1 = "".join(map(str,list1))
print(str1)
#用字符串切片的方式取出第三到八个字符，包含三和八
str2 = str1[2:7]
print(str2)
#将获得的字符串进行反转
str3 = str2[::-1]
print(str3)
#将结果转换为int类型
str4 = int(str3)
print(str4)
#将结果转换成二进制、八进制和十六进制
str5 = bin(str4)
str6 = oct(str4)
str7 = hex(str4)
#结果输出
print(str5)
print(str6)
print(str7)
