array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()#将数组翻转
print('翻转后的数组：')
print(array)
 #通过join（）方法将翻转后的数组拼接成字符串
s = ''
for i in range(0,10):
    array[i]=str(array[i])
string=s.join(array)
print('拼接成的字符串：')
print(string)
#用切片方式取出第三到第八个字符
r1=string[2:8] 
print('切片取出的字符串：')
print(r1)
#将字符串进行反转，并转换为int类型
int1=int(r1[::-1]) 
print('翻转并转为整数：')
print(int1)
 #转换成二进制，八进制，十六进制
print('转换成二进制，八进制，十六进制分别是：')
print(bin(int1),oct(int1),hex(int1)) 