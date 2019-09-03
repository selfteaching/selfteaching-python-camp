numbers = [0, 1, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print('This is the homework 3.2 reverse:', numbers)
# 翻转后的数组拼接成字符串
numbers_string = []
for number in numbers:
    numbers_string.append(str(number))
s = ''
str_join = s.join(numbers_string)
print('This is homework 3.3 join string:\n', str_join)
# ⽤字符串切⽚的⽅式取出第三到第⼋个字符(包含第三和第⼋个字符)
str_sliced = str_join[2:8]
print('This is homework 3.4:\n', str_sliced)
# 将获得的字符串进行翻转
str_rever = str_sliced[::-1]
print('This is homework 3.5\n', str_rever)
# 将结果转换为int类型
str_int = int(str_rever)
print('This is homework 3.6 ==>int\n', str_int)
print(bin(str_int))
print(oct(str_int))
print(hex(str_int))