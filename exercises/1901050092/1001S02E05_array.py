sample_list=[0,1,2,3,4,5,6,7,8,9]
reversed_list=sample_list[::-1]
print('列表反转====',reversed_list)
joined_str=''.join([str(i) for i in reversed_list])
print('反转后转换成字符串===',joined_str)
sliced_str=joined_str[2:8]
print('切片后取出第三到第八个字符',sliced_str)
reversed_str=sliced_str[::-1]
print('字符串反转',reversed_str)
int_value=int(reversed_str)
print('转换为int====',int_value)
print('转换为二进制====',bin(int_value))
print('转换为八进制====',oct(int_value))
print('转换为十六进制====',hex(int_value))