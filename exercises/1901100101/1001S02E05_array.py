# 列表也可以叫做数组
# 1. 对列表[0,1,2,3,4,5,6,7,8,9]翻转
sample_list =[0,1,2,3,4,5,6,7,8,9]
reversed_list = sample_list[::-1]
print('列表翻转 ==>',reversed_list)
# 2. 翻转后的列表拼接成字符串
joined_str = ''.join([str(i)for i in reversed_list])
print('翻转后的数组拼接成字符串 ==>', joined_str)
sliced_str = joined_str[2:8]
print('用字符串切片的方式取出第三到第八个字符 ==>', sliced_str)
reversed_str = sliced_str[::-1]
print('字符串翻转 ==>',reversed_str)
int_value = int(reversed_str)
print('转换为 int 类型 ==>', int_value)
print('转换为二进制 ==>',bin(int_value))
print('转换为八进制==>',oct(int_value))
print('转换为十六进制==>',hex(int_value))
