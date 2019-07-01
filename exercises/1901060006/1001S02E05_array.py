a_list=[0,1,2,3,4,5,6,7,8,9]
a_list.reverse()#数组反转
print(a_list)#输出反转之后的数组
#把翻转后的数字转换成字符串
b = ''.join([str(i) for i in a_list])
print(b)
s=b 
c=s[2:8]
print(c)
d=int(c[::-1]) #将字符串反转,并转换成int类型数据
print(d)
print('二进制:',bin(d))#转换成二进制,八进制,十六进制
print('八进制:',oct(d))
print('十六进制:',hex(d))



