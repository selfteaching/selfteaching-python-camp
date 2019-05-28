#3.2 翻转数组
sample_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1]
print('翻转列表', reversed_list)
#3.3翻转后的数组拼接成字符串
joined_str = ''.join([str(i) for i in reversed_list])
print('翻转后拼接成字符串',joined_str)
#3.4取出第3到第8字符
sliced_str = joined_str[2:8]
print('第三到第八字符',sliced_str)
#3.5对字符串翻转
reversed_str = sliced_str[::-1]
print('字符串翻转',reversed_str)
#3.6结果转换int类型
int_value = int(reversed_str)
print('转换int类型',int_value)

print('二进制',bin(int_value))
print('八进制',oct(int_value))
print('十六进制',hex(int_value))
