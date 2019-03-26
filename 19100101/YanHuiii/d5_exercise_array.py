#这是一个关于数组操作和进制转换的程序

#3.1翻转数组
arr1 = [1,2,3,4,5,6,7,8,9]
arr1.reverse()   #翻转数组arr1

#3.2将数组拼接成字符串
str1 = ''.join(map(str,arr1))   

#3.3用字符串切片方式去除str1中第三到第八个字符
str2 = str1[2:8]

#3.4将字符串str2反转
str3 = str2[::-1]

#3.5将str3转换为int型
str4 = int(str3)

#3.6分别将str4转换成二进制、八进制、十六进制，并分别输出结果
print("最终结果为:")  
print(str4,"转换为二进制为：",bin(str4))
print(str4,"转换为八进制为：",oct(str4))
print(str4,"转换为十六进制为：",hex(str4))