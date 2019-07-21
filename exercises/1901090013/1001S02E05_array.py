# 1.将列表进行反转
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list.reverse()
# print(list)

# 2.反转后的列表拼成字符串
str_mine = ''
for num in list:
    str_mine += str(num)
# print(str_mine)

# 3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
# 切片的时候，注意区间是左闭右开的
new_str = str_mine[2:8]
# print(new_str)


# 4.将获得的字符串进行翻转
# 语法：切片的语法：[起始:结束:步长]
str_reverse = new_str[::-1]
# print(str_reverse)


# 5.将结果转换为int类型
str_to_int = int(str_reverse)
# print(str_to_int)


# 6.将上面的结果转换成二进制、八进制和十六进制
two = bin(str_to_int)
eight = oct(str_to_int)
sixteen = hex(str_to_int)
print(two)
print(eight)
print(sixteen)