print("数组翻转：")
a=[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)

print("拼接成字符串：")
b=''.join(str(i) for i in a)
print(b)

print("把字符串切片，取出第3到第8个字符：")
c=b[2:8]
print(c)

print("字符串翻转：")
d=c[::-1]
print(d)

print("转换成int类型：")
e=int(d)
print(e)

print("转换成二进制、八进制、十六进制：")
print('二进制为：',bin(e))
print('十进制为：',oct(e))
print('十六进制为：',hex(e))
