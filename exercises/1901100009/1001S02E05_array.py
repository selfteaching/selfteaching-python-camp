list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list.reverse()
print('翻转列表',list)


#('翻转列表==>'，reversed_list)


#翻转后拼接成字符串
joined_str = ''.join([str(i) for i in list])
print('拼接后的字符',joined_str)

sliced_str = joined_str[2:8]
print('选取部分',sliced_str)

reversed_str = sliced_str[::-1]
print('翻转部分',reversed_str)

int_value = int(reversed_str)

print('转换为int',int_value)
print('转换为二进制',bin(int_value))
print('转换为八进制',oct(int_value))
print('转换为十六进制',hex(int_value))