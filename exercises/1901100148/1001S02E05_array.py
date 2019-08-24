# 1.将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转 (列表也可以叫做数组)
list=[0,1,2,3,4,5,6,7,8,9]
reversed_list=list[::-1]
print('列表翻转--->',reversed_list)
print()

#2.翻转后的数组拼接成字符串
# 调用''（空字符串）str 类型的 join()方法可以连接 列表 里的元素，用''(空字符串)表示连接的时候元素间不用任何字符隔开
# 因为 reversed_list 里面都是 int 类型元素，所以拼接之前要把 其变成一个包含 str 类型元素的 列表
joined_str=''.join([str(i) for i in reversed_list])
print('翻转后的数组拼接成字符串--->',joined_str)
print()

# 3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
# 切片的时候包含 开始 的索引，不包含 结尾 的索引
sliced_str=joined_str[2:8]
print('用字符串切片的方式取出第三到第八个字符--->',sliced_str)
print()

# 4.将获得的字符串进行翻转
reversed_str=sliced_str[::-1]
print('字符串翻转---->',reversed_str)
print()

# 5. 将结果转换为 int 类型
int_value=int(reversed_str)
print('转换位int类型--->',int_value)
print()

# 6. 分别转换成二进制，八进制，十六进制，最后输出三种进制的结果
print('转换为二进制--->',bin(int_value))
print('转换为八进制--->',oct(int_value))
print('转换为十六进制--->',hex(int_value))

