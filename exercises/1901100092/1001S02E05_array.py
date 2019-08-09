numbers=[0,1,2,3,4,5,6,7,8,9]
numbers.reverse() #将数组numbers翻转
print(numbers)
numbers_1=''.join(str(i) for i in numbers) #将翻转后的数组拼接成字符串
print(numbers_1)
numbers_2=numbers_1[2:8] #用切片方式取出第三到第八个字符
print(numbers_2)
numbers_3=numbers_2[::-1] #将获得的字符串进行翻转
print(numbers_3)
a=int(numbers_3) #将字符串转换成int类型
b=bin(a)
print('转换为二进制是：',b)
c=oct(a)
print('转换为八进制是：',c)
d=hex(a)
print('转换为十六进制是：',d)