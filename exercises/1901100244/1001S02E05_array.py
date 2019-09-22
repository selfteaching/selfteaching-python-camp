# -*- coding: UTF-8 -*-

# Filename : 1001S02E05_string.py
# author by : @shen-huang

# 数组操作，进制转换

print("3. 数组操作，进制转换", end="\n\n")

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ## 将 num_list 翻转

# 使用切片
re_num_list = num_list[::-1]

# # 也可直接翻转
# num_list.reverse()

# ## 将 re_num_list 拼接成字符串

re_num_str = ''.join(str(x) for x in re_num_list)

# ## 用字符串切片的方式取出 re_num_str 的第三到第八个字符
# ## （包含第三和第八个字符）

re_num_str_3to8 = re_num_str[2:8]

# ## 翻转字符串 re_num_str_3to8

re_re_num_str_3to8 = re_num_str_3to8[::-1]

# ## 将字符串 re_re_num_str_3to8 转为 int 类型数字

int_re_re_num_str_3to8 = int(re_re_num_str_3to8)

# ## 将 int_re_re_num_str_3to8 转二进制、八进制、十六进制数字

bin_int_re_re_num_str_3to8 = bin(int_re_re_num_str_3to8)
oct_int_re_re_num_str_3to8 = oct(int_re_re_num_str_3to8)
hex_int_re_re_num_str_3to8 = hex(int_re_re_num_str_3to8)

print("原始十进制数：　　 ", int_re_re_num_str_3to8)
print("转换为二进制数：　 ", bin_int_re_re_num_str_3to8)
print("转换为八进制数：　 ", oct_int_re_re_num_str_3to8)
print("转换为十六进制数： ", hex_int_re_re_num_str_3to8)
