list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list. reverse()                       # 翻转
print("原列表被翻转:",list) 

# 翻转后的数组拼接成字符串
list_str = "".join((str(i) for i in list))   
print("翻转后的数组拼接成字符串:",list_str)

#  用字符串切片的方式取出第二个到第八个 字符 (包含第三到第八个字符)
jiequ_str = list_str[2:8]   
print("取出第二个到第八个 字符 (包含第三到第八个字符)",jiequ_str)

# 将获得的字符串进行翻转
fz_str = jiequ_str[::-1]
print("将获得的字符串进行翻转 :",fz_str)

# 将结果转换为 int 类型
m = int(fz_str)
print("将结果转换为 int 类型:",m)

print("转换为二进制:",bin(m))
print("转换为八进制:",oct(m))
print("转换为十六进制:",hex(m))
