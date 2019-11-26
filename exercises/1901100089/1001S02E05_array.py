# 1.对列表 [0,1,2,3,4,5,6,7,8,9] 翻转
sample_list = [0,1,2,3,4,5,6,7,8,9]
reversed_list = sample_list[::-1]
print('\n列表翻转 ==>',reversed_list)

# 2.翻转后的列表转换为字符串
joined_str = ''.join([str(i) for i in reversed_list])
print('\n翻转后的数组拼接成字符串 ==>',joined_str)

# 3.用字符串切片的方式取出第3到第8个字符（包含第3和第8个字符）
sliced_str = joined_str[2:8]
print('\n用字符串切片的方式取出第3到第8个字符 ==>',sliced_str)

# 4.将获得的字符串进行翻转
reversed_list = sliced_str[::-1]
print('\n列表翻转 ==>',reversed_list)

# 5.转换为 int 类型
int_value = int(reversed_list)

print('\n转换为 int 类型 ==>',int_value)

print('转换为 二进制 类型 ==>',bin(int_value))
print('转换为 八进制 类型 ==>',oct(int_value))
print('转换为 十六进制 类型 ==>',hex(int_value))