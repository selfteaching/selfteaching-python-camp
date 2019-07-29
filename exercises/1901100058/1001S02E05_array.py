# 数组操作，进制转换
Sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转

reversed_list = sorted(Sample_list, reverse=True)
print('翻转结果', reversed_list)

#reversed_list = Sample_list[::-1]

# 2. 翻转后的数组拼接成字符串

combined_str = ''
for i in reversed_list:
    combined_str += combined_str.join(str(i))
print(combined_str)

# joined_str=''.join([str(i) for i in reversed_list])
# print(joined_str)


# 3. ⽤字符串切⽚的⽅方式取出第三到第⼋个字符（包含第三和第八个字符）

cut_str=combined_str[2:8]
print(cut_str)


# 4. 将获得的字符串串进⾏行翻转

reversed_str=cut_str[::-1]
print(reversed_str)

# 5. 将结果转换为 int 类型

int_value=int(reversed_str)
print(int_value)

# 6. 分别转换成⼆进制，⼋进制，⼗六进制,最后输出三种进制的结果

print('转化为二进制', bin(int_value))
print('转化为八进制', oct(int_value))
print('转化为十六进制', hex(int_value))
