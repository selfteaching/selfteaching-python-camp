num1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#默认为字符串
num2=list(reversed(num1))#翻转后转换成列表
print(num2)#打印

str=''.join(str(i)for i in num2)
print(str)

num3=str[2:9] #切片
print(num3)

result= num3[::-1]#字符串翻转
print(result)

a=int(result)#转换成整数（int）型
print(a)

print(bin(a))#2进制
print(oct(a))#8进制
print(hex(a))#16进制
