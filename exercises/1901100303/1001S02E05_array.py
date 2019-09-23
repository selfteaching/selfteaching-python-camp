#import array
x = [0,1,2,3,4,5,6,7,8,9]
print(x)
x.reverse()           #1.数组翻转
print(x)

y=''                        #2.字符串拼接
for i in range(0,len(x)):
    y=y+str(x[i])
print(y)

#字符串切片
print(y[3:9])

#切片后的字符串翻转
a=y[3:9]
b=a[::-1]
#转换成int
b_num = int(b)
#转换成三种进制
print(bin(b_num))
print(oct(b_num))
print(hex(b_num))


