list_a=[0,1,2,3,4,5,6,7,8,9]
#翻转数列
list_a.sort(reverse=True)
print(list_a)

print()
#拼接成字符串
list_b=''.join(map(str,(list_a)))
print(list_b)

print()
#用字符串切片提取第3~第8个字符（包含第3和第8）
str_0=list_b[3:9]
print(str_0)

print()
#将字符串翻转并转换为int类型
str_1=str_0[::-1]
print(str_1)
str_2=int(str_1)
print(str_2)
print(type(str_2))

print()
#分别转换成二进制，八进制，十六进制
print('二进制：',bin(str_2))
print('八进制:',oct(str_2))
print('十六进制:',hex(str_2))