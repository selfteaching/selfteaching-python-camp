# 翻转数组，拼接字符串，切片方式取出第三至八个字符，翻转字符串，转为int类型，转为2，8，16进制，输出三种结果

listhw = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 翻转
# list01 = reversed(listhw)
list011 = listhw[::-1]
# print(list011)
# print(list01)

# 字符串
list02 = [str(i) for i in list011]
# print(list02)
str01 =''.join(list02)
# print(str01)

# 切片取出
str02 = str01[2:8]
# print(str02)

# 翻转字符串
str03 = str02[::-1]
# print(str03)

# int类型
int01 = int(str03)
# print(int01)
int2 = bin(int01)
print(int2)
int8 = oct(int01)
print(int8)
int16 = hex(int01)
print(int16)
# print(type(int01), type(int2),type(int8),type(int16),type(str03))