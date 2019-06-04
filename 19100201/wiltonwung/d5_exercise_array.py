a=[0,1,2,3,4,5,6,7,8,9]
a.reverse() #反转
#print(a)
s = ''      
for i in range(0,10):  
    a[i]=str(a[i])
string =s.join(a)
#print(string)#组成字符串
b=string[2:8]
#print(b)#切片
c=b[::-1]  #将字符串进行反转，并
d = int(c)#转换为int类型
#print(d)
print(bin(d),oct(d),hex(d))    #转换并输出成二进制、八进制、十六进制结果
  
