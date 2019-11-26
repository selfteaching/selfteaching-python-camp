a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ab=list(reversed(a))#这里注意一定要用list(reversed())这种写法
print(ab)
#百度了一下，列表转字符串可以用join这个方法
str1=''.join(str(i) for i in ab)#这一句的意思，语法还是不太懂
print(str1)#转换成数字
str2=str1[2:8]
print(str2)
str3=list(reversed(str2))
print(str3)
str4=''.join(str(j) for j in str3)#列表转换不了成为数值，所以先要转化成字符串
int2=int(str4)#把字符串转换成数值型
print(int2)
print(bin(int2))
print(oct(int2))
print(hex(int2))