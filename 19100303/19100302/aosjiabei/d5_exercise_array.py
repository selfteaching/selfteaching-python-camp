arry = [0,1,2,3,4,5,6,7,8,9]
arry.reverse() 
arry=[str (x) for x in arry]
str1 = ''.join(arry)#列表拼接为字符串
str2=str1[3:9]
str3=str2[::-1]
int1=int(str3)

print(arry)
print(str1)
print(str2)
print(str3)
print(int1)
print("转换为二进制 ：",bin(int1))
print("转换为八进制 ：",oct(int1))
print("转换为十六进制：",hex(int1))
