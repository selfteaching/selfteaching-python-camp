array=[0,1,2,3,4,5,6,7,8,9]
array.reverse() #将数组翻转
print(array)

s = ''      #翻转后的数组拼接成字符串
for i in range(0,10):  
    array[i]=str(array[i])
string=s.join(array)
print(string)

r1=string[2:8]  #用切片方式取出第三到第八个字符
print(r1)

integer=int(r1[::-1])  #将字符串进行反转，并转换为int类型
print(integer)

print(bin(integer),oct(integer),hex(integer)) #转换成二进制、八进制、十六进制