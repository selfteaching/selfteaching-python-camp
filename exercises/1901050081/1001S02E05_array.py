list1=[0,1,2,3,4,5,6,7,8,9]
list2=list1[::-1]
str1="".join(str(x)for x in list2)
str2=str1[3:9]
str3=str2[::-1]
num1=int(str3)
num2=bin(num1)
print('转换为二进制：',num2)
num3=oct(num1)
print('转换为八进制：',num3)
num4=hex(num1)
print('转换为十六进制：',num4)