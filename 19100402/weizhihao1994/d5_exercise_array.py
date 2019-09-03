a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a_list = list(reversed(a_list))  # 将列表翻转

b_list = []
for i in range(len(a_list)):
    b_list.append(str(a_list[i]))
a_str = ''.join(b_list)
print (a_str) # 将以数值为元素的列表转换成字符串，这里不能直接用join函数！

b_str = a_str[2:8] # 截取第3-8个字符

b_str = b_str[::-1] # 翻转第3-8个字符

b = int(b_str) # 将结果转换为int类型

b_2 = bin(b) # 将结果转换为二进制
b_8 = oct(b) # 将结果转换为二进制
b_16 = hex(b) # 将结果转换为二进制

print(b_2)
print(b_8)
print(b_16)
