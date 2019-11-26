sample_list = [0,1,2,3,4,5,6,7,8,9]
reversed_list = sample_list[::-1]
print('列表翻转==>',reversed_list)

joined_str =''.join([str(i) for i in reversed_list])
print('拼接成字符串==>',joined_str)

sliced_str = joined_str[2:8]
print('取出第三至第八字符==>',sliced_str)

reversed_str = sliced_str[::-1]
print('字符串翻转==>',reversed_str)

int_value = int(reversed_str)
print('转为int类型==>',int_value)

print('转为二进制==>',bin(int_value))
print('转为八进制==>',oct(int_value))
print('转为十六进制==>',hex(int_value))