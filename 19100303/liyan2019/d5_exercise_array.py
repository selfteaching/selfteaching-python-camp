#将数组翻转
vec=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
vec.reverse()
print(vec)

#翻转后数组拼接成字符串
str1=[str(i)for i in vec] # 数字转成字符串
print(str1)

str2="".join(str1)
print(str2)# 字符串拼接
str3=str2[2:8]#字符串切片方式取出第3到底8个字符
print(str3)

str4=''.join(str3[i] for i in range(len(str3)-1,-1,-1))  #将字符串反转 意义待理解【@@@@】
print(str4)

a=int(str4) #将字符串转化为int
print(a)

#转换为二、十、十六进制并打印
print(bin(a),oct(a),hex(a))