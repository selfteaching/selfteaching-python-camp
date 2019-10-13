
# 1.对列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
sample_list =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_list=sample_list[::-1]
print('列表翻转==>',reverse_list)

# 2.翻转后的列表拼接成字符串
#调用''(空字符串)str类型的join方法可以连接列表里的元素，用''(空字符串)表示连接的时候元素间不用任何字符隔开
#因为reverse_list里面都是int类型元素，所以拼接之前要把reverse_list变成一个包含str类型元素的列表
joined_str = ''.join([str(i) for i in reverse_list])
print('翻转后的数组接拼成字符串-->',joined_str)

# 3.⽤字符串切片的方式取出第三到第⼋个字符（包含第三和第⼋个字符)
# 切片的时候包含开始索引，不包含结尾的索引
slice_str=joined_str[2:8]
print('用字符串切片的方式取出第三到第八个字符-->',sliced_str)

# 4.将获得的字符串进行翻转

reversed_str=sliced_str[::-1]
print('字符串翻转-->',reversed_str)

# 5.将结果转换为 int 类型
int_value=int(reversed_str)
print('转换为 int 类型-->',int_value)

# 6.分别转换成⼆进制，⼋进制，十六进制

print('转换为二进制==>',bin(int_value))
print('转换为八进制==>',oct(int_value))
print('转换为十六进制==>',hex(int_value))


