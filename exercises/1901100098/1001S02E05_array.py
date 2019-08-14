#数组操作，进制转换
#将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
reversed_list = sample_list[::-1]
print('列表反转==>',sample_list)

#翻转后的数组拼接成字符串
#调用''（空字符串）str 类型的 join 方法可以连接列表里的元素，用''（空字符串）表示连接的时候元素间不用任何字符隔开
#因为rebersed_list 里边都是int 类型元素，所以拼接之前要把rebersed_list 编程一个包含str类型元素的列表
joined_str =''.join([str(i) for i in reversed_list])
print('翻转后的字符拼接成字符串',joined_str)

# 3 用字符串切片的方式取出第3到第8个字符（包含第3到第8个字符）
# 切片时候包含开始索引，不包含结尾索引 
sliced_str = joined_str[2:8]
print('用字符串切片的方式取出第3到第8个字符==>',sliced_str)

#4 获得的字符串进行反转
reversed_str = sliced_str[::-1]
print('字符串进行反转==>',reversed_str)

# 5 转换成 int 类型
int_value = int(reversed_str)

print('转换成int类型==》',int_value)

print('转换成二进制==>',bin(int_value))
print('转换成八进制==>',oct(int_value))
print('转换成十六进制==>',hex(int_value))