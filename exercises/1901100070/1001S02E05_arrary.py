sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1]
print('\n我要开始运作了哦!\n看我颠倒次序:\n', reversed_list, end='\n\n')

joined_str = ''.join([str(i) for i in reversed_list])
print('翻转后的数组拼接成字符串\n', joined_str, end='\n\n')

slice_str = joined_str[2:8]
print('看我选择性的打印\n', slice_str, end='\n\n')

reversed_str = slice_str[::-1]
print('再翻转一遍\n', reversed_str, end='\n\n')

int_value = int(reversed_str)
print('变成数字类型int\n', int_value, end='\n\n')

print('伪装成二进制\n', bin(int_value), end='\n')
print('伪装成八进制\n', oct(int_value), end='\n')
print('伪装成十六进制\n', hex(int_value), end='\n')