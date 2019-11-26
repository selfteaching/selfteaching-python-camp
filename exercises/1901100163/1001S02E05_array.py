#讲数组反转
arr1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr1.reverse()
#print(arr1)

str1=''.join(str(i) for i in arr1)
#print(str1)
str2=str1[2:8]
#print(str2)
str3=str2[::-1]
#print(str3)
int1=int(str3)
print(int1)
print('十进制正数为：',int1)
print('转换为二进制为：',bin(int1))
print('转换为八进制为：',oct(int1))
print('转换为十六进制为：',hex(int1))