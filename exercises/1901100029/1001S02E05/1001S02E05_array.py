sample_list = [0,1,2,3,4,5,6,7,8,9,]
reversed_list = sample_list[::-1]
print('列表翻转 ==>', reversed_list)

joined_str = ''.join([str(i) for i in reversed_list])
print('翻转后的数组品鉴成字符串 ==>', joined_str)

slice_str = joined_str[2:8]
print('用字符串切片的方式取出第三到第八个字符 ==>', slice_str)

reversed_str = slice_str[::-1]
print('字符串翻转 ==>',reversed_str)

int_value = int(reversed_str)
print('转换为 int 类型 ==>', int_value)

print('转换为 二进制==>',bin(int_value))
print('转换为 八进制==>',oct(int_value))
print('转换为 十六进制==>',hex(int_value))