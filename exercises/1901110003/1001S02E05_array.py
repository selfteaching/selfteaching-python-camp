#将数组[0,1,2,3,4,5,6,7,8,9]翻转
num1=[0,1,2,3,4,5,6,7,8,9]
num2=list(reversed(num1))
print(num2)

#翻转后的数组拼接成字符串
str=''.join(str(i)for i in num2)
print(str)

#⽤字符串切⽚的⽅式取出第三到第八个字符(包含第三和第⼋个字符)
num3=str[2:8]  #字符串切片
print(num3)

#将获得的字符串进行翻转
num4=num3[::-1]
print(num4)

#将结果转换为int类型
int(num4)
print(int(num4))

#分别转换成⼆进制，八进制，十六进制
a=int(num4)
print(bin(a))
print(oct(a))
print(hex(a))