list=[0,1,2,3,4,5,6,7,8,9]
reverse_list=list[::-1]
print('翻转列表',reverse_list)
joined_str="".join([str(i) for i in reverse_list])
print('翻转后拼接字符串',joined_str)
spliced_str=joined_str[2:8]
print('取出第三至第八个字符',spliced_str)
reverse_str=spliced_str[::-1]
print('翻转字符串',reverse_str)
int_value=int(reverse_str)
print('转换为int类型',int_value)
print(bin(int_value))
print(oct(int_value))
print(hex(int_value))
