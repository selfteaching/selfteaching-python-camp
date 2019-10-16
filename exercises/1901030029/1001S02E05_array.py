
a1=[0,1,2,3,4,5,6,7,8,9]

#数组翻转
a2=a1.reverse()
print(a1)

#将数组拼接成字符串
str1="".join(str(i)for i in a1)
print(str1)

#取出第三到第八个字符
str2=str1[2:8]
print(str2)

#将字符串翻转
str3=str2[::-1]
print(str3)

#字符串转int
num=int(str3)
print(num)

print("十进制数为：",num)
print("转二进制为：",bin(num))
print("转八进制为：",oct(num))
print("转十六进制为：",hex(num))