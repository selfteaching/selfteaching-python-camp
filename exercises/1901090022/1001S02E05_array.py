# 3. 数组操作，进制转换
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3.2. 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
print("===== 2. 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转 =====")
arr.sort(reverse=True)
print(arr)

# 3.3 翻转后的数组拼接成字符串
print("===== 3.3 翻转后的数组拼接成字符串 =====")
arr_join_str = ""
for n in arr:
    arr_join_str += str(n)
print(arr_join_str)

# 3.4. ⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）
print("===== 3.4. ⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符） =====")
arr_join_str_slice = arr_join_str[2:8]
print(arr_join_str_slice)

# 3.5. 将获得的字符串进⾏翻转
print("===== 3.5. 将获得的字符串进⾏翻转  =====")
l = list(arr_join_str_slice)
l.reverse()
s = "".join(l)
print(s)

# 将结果转换为 int 类型
print("===== 3.6. 将结果转换为 int 类型 =====")
s_int = int(s)
print(s_int)

# 3.7. 分别转换成⼆进制，⼋进制，⼗六进制
print("===== 3.7. 分别转换成⼆进制，⼋进制，⼗六进制 =====")
print("转换为二进制为：", bin(s_int))
print("转换为八进制为：", oct(s_int))
print("转换为十六进制为：", hex(s_int))
