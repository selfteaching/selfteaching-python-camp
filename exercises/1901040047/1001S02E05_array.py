#进制转换
s = [0,1,2,3,4,5,6,7,8,9]
print('1.翻转数组\n')
s.reverse()
print(s)
print('-'*50)    #制作一条分隔线
print('2.翻转数组后拼接成字符串\n')
a = [9,8,7,6,5,4,3,2,1,0]
b = [str(i) for i in a]
c = ''.join(b) #.jion()method
print(c)
print('-'*50)
print('3.用字符串切片取出第三到第八个字符\n')
d = c[3:9]
print(d)
print('-'*50)
print('4.将获得的字符串进行翻转\n')
e = d[::-1] # -1为反向排序
print(e)
print('-'*50)
print('5.将结果转化为int\n')
f = int(e)
print(f)
print('-'*50)
print('6.转化成二、八、十六进制')
print('二进制：',bin(f))
print('八进制： ',oct(f))
print('十六进制: ',hex(f))
