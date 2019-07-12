# 1.将数组[0,1,2,3,4,5,6,7,8,9]翻转
arr1 = [0,1,2,3,4,5,6,7,8,9]
arr1.reverse()

# 2.翻转后的数字拼接成字符串
str1 = ''.join(map(str,arr1))

# 3.用字符串切片的方式取出第三到第八个字符
str2 = str1[2:8]

# 4.将获得的字符串进行翻转
str3 = str2[::-1]

# 5.将结果转换为int类型
str4 = int(str3)

# 5.分别转换为二进制，八进制，十六进制
str5 = bin(str4)
str6 = oct(str4)
str7 = hex(str4)
print(str5,str6,str7)

