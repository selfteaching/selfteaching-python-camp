list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list.reverse()  #反转列表
str1=''
for i in list:  
    str1=str1+str(i)  #将列表里的数字转换成字符串
str2=str1[2:8]  #截取第3到第8个字符
str3=str2[::-1] #反转字符串
num=int(str3)  #将字符串转成int
num16=hex(num) #16进制
num8=oct(num) #8进制
num2=bin(num) #2进制
print(num,num16,num8,num2)
