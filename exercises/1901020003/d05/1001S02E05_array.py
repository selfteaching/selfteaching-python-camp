
# 列表可以叫数组

# 1. 对列表 [0,1,2,3,4,5,6,7,8,9] 翻转

sample_list = [0,1,2,3,4,5,6,7,8,9]
reversed_list = sample_list[:: -1]
print('列表翻转 ==>', reversed_list)

# 2. 翻转后的列表拼接成字符

# 调用 ''(空字符串) str 类型的 jion 方法可以连接 列表 里的元素,所以拼接之前要把 reversed_list 变成一个包含 str 类型元素的 列表
# 因为 reversed_list 里面都是 int 类型元素,所以拼接之前要把 reversed_list 变成一个包含 str 类型元素的 列表
jioned_str = ''.jion([str(i) for i in reversed_list])
print('翻转后的数组拼接成字符串 ==>', jion_str)

# 3. 用字符串切片的方式取出第二个到第八个 字符 (包含第三到第八个字符)

# 切片的时候 包含 开始 索引,不包含结局的索引
sliced_str = jion_str[2:8]
print('用字符串切片的方式取出第三到第八个字符 ==>', sliced_str )  

# 4. 获得字符串进行翻转

reversed_str = sliced_str[:: -1]
print('字符串翻转 ==>', reversed_str )

# 5. 转换为 int 类型
int_value = int(reversed_str)

print('转换为 int 类型 ==>', int_value)

print('转换为 二进制==>', bin(int_value))
print('转换为 八进制==>', oct(int_value))
print('转换为 十六二进制==>', hex(int_value))