array = [0,1,2,3,4,5,6,7,8,9]

# -1表示从后往前
reversed_list = array[::-1]

print('列表翻转==>',reversed_list)

join_str = ''.join([str(i) for i in reversed_list])
print('数组拼接成字符串==>',join_str)

# 切片  包含开始索引号，不包括结束索引号
slice_str = join_str[2:8]
print('第三个到第八个字符是',slice_str)

reversed_str = slice_str[::-1]
print('字符串翻转==>',reversed_str)

int_value = int(reversed_str)
print('转为int类型==>',int_value)
print('转十六进制==>',hex(int_value))
print('转八进制==>',oct(int_value))
print('转二进制==>',bin(int_value))

'''
数组操作，难点：切片理解
[2,8] 索引号2开始到索引号7的字符截取
[::-1] 从后往前翻转
'''