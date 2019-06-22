num1=[0,1,2,3,4,5,6,7,8,9]
num2=list(reversed(num1))  #翻转
print(num1)

str=''.join(str(i)for i in num2)
print(str)

num3=str[2:8]  #字符串切片
print (num3)

result=num3[::-1]
print(result)

int(result)
print(int(result))

a=int(result)
print(bin(a))
print(oct(a))
print(hex(a))