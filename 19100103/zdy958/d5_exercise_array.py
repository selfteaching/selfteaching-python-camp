a =[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)  #将数组翻转
 
b=str(a[0])  #翻转后拼接
for i in range(1,10):
    b+=str(a[i])
print(b)

c=b[2:8]
print(c)   #切片第三到第八的元素

d=''.join(c[i] for i in range(len(c)-1,-1,-1))  #将字符串反转
print(d)

e=int(d)
print(e)   #将字符串转成int

print(bin(e),oct(e),hex(e)) #转换成二进制、十进制、十六进制并打印