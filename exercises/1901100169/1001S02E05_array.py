#1.将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
sample_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[1:-1]
print('list reversed',reversed_list)

#2. 翻转后的数组拼接成字符串
joined_str = ''.join([str(i) for i in reversed_list])
print('翻转后的数组拼接成字符串 ==>',joined_str)

#3. 用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
sliced_str = joined_str[2:8]
print('用字符串切片的方式取出第三到第八个字符==>',sliced_str)

#4. 将获得的字符串进行翻转
reversed_str = sliced_str[1:-1]
print('字符串翻转',reversed_str)

#5. 将结果转换为 int 类型
int_value = int(reversed_str)
print('转换为 int 类型',int_value)
#6. 分别转换成二进制，八进制，十六进制
print('转换成二进制',bin(int_value))
print('转换成八进制',oct(int_value))
print('转换成进十六制',hex(int_value))