a=[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)
b=''.join(str(i) for i in a)
print('拼接后的字符串：',b)
c=b[2:8]
print('第三到八：',c)
print('翻转：',c[::-1])
d=int(c[::-1])
print('整数：',d)
print('二进制：',bin(d))
print('八进制：',oct(d))
print('十进制：',hex(d))
