a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print('----将数组翻转----\n', a)

str1 = ''.join(map(str, a))
print('----拼接成字符串----\n', str1)

str2 = str1 [2:8]
print('----取出第三到第八个字符(包含第三和第八个字符)----\n', str2)

str3 = str2 [::-1]
print('----将字符串进行翻转----\n', str3)

b = int(str3)
print('----转换为int类型----\n', b)

print('----分别转换成二进制，八进制，十六进制----')
print('二进制:', bin(b), '\n', '八进制:', oct(b), '\n', '十六进制:', hex(b))