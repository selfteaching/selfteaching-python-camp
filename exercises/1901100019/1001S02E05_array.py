# 定义整型列表，即数组
array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 逆序
array1.sort(reverse=True)

# 将整型列表转换为字符型列表
array2 = list(map(str, array1))

# 将字符列表拼接成字符串
text = "".join(array2)
# 取出字符串的3~8个字符
text1 = text[2:8]
# 将字符串转成列表，然后反转
list1 = list(text1)
list1.reverse()

# 将列表转成字符串
text2 = "".join(list1)
# 将字符串转成整型
num = int(text2)
print(bin(num), oct(num), hex(num))