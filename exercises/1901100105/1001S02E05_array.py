#1.列表翻转
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1] #从后向前取值，每次进值1
print('列表翻转==>', reversed_list)

#2.拼接成字符串
joined_str = ''.join([str(i) for i in reversed_list]) 
#用''（空字符串）表示连接时不用任何字符隔开。尝试用'*'，结果是中间有*连接
print('翻转后的数组拼接成字符串==>', joined_str)

# 3.用字符串切片方式取出第三到第八个字符
sliced_str = joined_str[2:8]
print('用字符串切片取出第三到第八字符==>', sliced_str)

#4.获得的字符串进行翻转
reversed_str = sliced_str[::-1]
print('字符串翻转==>', reversed_str)

#5.转换为int类型
int_value = int(reversed_str)
print('转换为int类型==>', int_value)
# int_value = bin(int_value)
# print('转换为二进制==>', int_value)
# int_value = oct(int_value)
# print('转换为八进制==>', int_value)
int_value = hex(int_value)
print('转换为十六进制==>', int_value)

