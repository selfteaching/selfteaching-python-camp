a=[0,1, 2, 3, 4, 5, 6, 7, 8, 9]
a=a[::-1]#将数组反转
print(a)
str = ''.join(str(i) for i in a) #将数组转换成字串符
print(str)

b=str[2:8] #⽤字符串切⽚的⽅式取出第三到第⼋个字符
print(b)

b=b[::-1]#将取出的结果反转
print(b)

c=int(b)#将结果转换为 int 类型
print(c)

#分别转换成⼆二进制，⼋八进制，⼗十六进制,最后输出三种进制的结果
print('二进制:',bin(c))
print('八进制:',oct(c))
print('十六进制:',hex(c)) 
