# day5 字符串练习
# 2019年7月9日
# 陈浩 学号 1901100030

#对列表进行翻转
sample_list = [0,1,2,3,4,5,6,7,8,9]
#print(sample_list)
#<<<<<<< master
#=======
#reversed_list = sample_list.reverse()
#>>>>>>> master
sample_list.reverse()
reversed_list = sample_list
print(reversed_list)

#拼接字符串
#<<<<<<< master
#join_str=""
#for i in reversed_list:
#    join_str = join_str + str(i)
join_str = "".join([str(i) for i in reversed_list])
#=======
join_str=""
for i in reversed_list:
    join_str = join_str + str(i)
#>>>>>>> master
print(join_str)

#切片取出3到8字符
sliced_str = join_str[2:8]
print(sliced_str)

# 翻转字符串
reversed_str = sliced_str[::-1]
print(reversed_str)

# 格式转换
int_value = int(reversed_str)

print("转换为int类型：", int_value)

print("转换为二进制：", bin(int_value))
print("转换为八进制：", oct(int_value))
print("转换为十六进制：", hex(int_value))
