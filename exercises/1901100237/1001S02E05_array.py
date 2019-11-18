a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[::-1]
print('翻转 ==>',b)
c = ''.join([str(i) for i in b])
print('字符串 ==>', c)
d = c[2:8]
print('切片取出 ==>', d)
e = d[::-1]
print('翻转 ==>', e)
int_x = int(e)
print('int类型 ==>', int_x)
print('二进制 ==>', bin(int_x))
print('八进制 ==>', oct(int_x))
print('十六进制 ==>', hex(int_x))