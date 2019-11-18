list_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort_list=list_a[::-1]
print('翻转后的数组',sort_list)

join_str=''.join([str(i) for i in sort_list])

print('数组拼接成字符串',join_str)

cut_str=join_str[2:8]

print('取第三个到第八个字符',cut_str)

rev_str=cut_str[::-1]

print('翻转后的字符串',rev_str)

int_value=int(rev_str)

print('转化为int类型',int_value)

print('转化为 二进制',bin(int_value))

print('转化为 八进制',oct(int_value))

print('转化为 十六进制',hex(int_value))

