list_a = [x for x in range(10)]
list_a.reverse()    # 翻转数组

# 将翻转后的数组拼成字符串
word = ''
word = word.join([str(x) for x in list_a])

# 取出3-8个字符
list_b = word[2:8]

# 将获得的字符串翻转
revers_list_b = list_b[::-1]
print(revers_list_b)

value = int(revers_list_b)
print('转换为int类型: ',value)
print('转换为二进制: ', bin(value))
print('转换为八进制: ', oct(value))
print('转换为十六进制: ', hex(value))
