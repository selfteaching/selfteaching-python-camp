a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()
#print(a)
b = [str(i) for i in a] #这里是使用列表推导式把列表中的单个元素全部转化为str类型
c = ''.join(b) #或者使用' ' 使元素间用空格分隔开
#print(c) #输出类型为字符串

d = c[2:8][::-1] #这是混合操作 直接切完片反转
'''c_slice = c[2:8]  这是分开操作 先切片 再反转
print(c_slice)
c_reverse = c_slice[::-1]
print(c_reverse)'''
e = int(d) #字符串转为整数

#将整数转换为二进制、八进制或十六进制的文本串，可以分别使用bin() ,oct() 或hex() 函数：

f = bin(e)
print('这是十进制转二进制的结果：\n%s' % f)

g = oct(e)
print('这是十进制转八进制的结果：\n%s' % g)

h = hex(e)
print('这是十进制转十六进制进制的结果：\n%s' % g)