# 1.将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转

sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1]
print("列表翻转 ==>", reversed_list)

# 2.翻转后的数组拼接成字符串
# 调用 ""(空字符串) str 类型的 join 方法可以连接 列表 里的元素，用""(空字符串) 表示连接的时候元素间不用任何字符隔开
# 因为 reversed_list 里面都是 int 类型元素，所以拼接之前要把 reversed_list 变成包含一个包含 str 类型元素的 列表
join_str = "".join([str(i) for i in reversed_list])
print("翻转后的数组拼接成字符串 ==>", join_str)

# 3.⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）

# 切片的时候包含 开始 索引，不包含结尾的索引
sliced_str = join_str[2:8]
print("⽤字符串切⽚的⽅式取出第三到第⼋个字符 ==>", sliced_str)

# 4.将获得的字符串进⾏翻转
reversed_str = sliced_str[::-1]
print("将获得的字符串进⾏翻转 ==>", reversed_str)

# 5.将结果转换为 int 类型
int_value = int(reversed_str)

print("将结果转换为 int 类型 ==>", int_value)

print("转换成⼆进制 ==>", bin(int_value))
print("转换成八进制 ==>", oct(int_value))
print("转换成十六进制 ==>", hex(int_value))