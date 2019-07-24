import string

array = [0,1,2,3,4,5,6,7,8,9]

# 将数组进行翻转
array_reverse = array[::-1]
print('翻转:',array_reverse)


# 先将int型数字转换成str,然后才能拼接
array_reverse = [str(i) for i in array_reverse]
print("字符：",array_reverse)

# 将翻转后的数组拼接成字符串
array_string = ''.join(array_reverse)
print('拼接：',array_string)

# 用切片的方式取出第3—第8个字符
array_slice = array_string[2:8]
print('第2-8个字符：',array_slice)

# 将获得的字符串进行翻转
array_slice_reverse = array_slice[::-1]
print('切片翻转：',array_slice_reverse)
# 使用reversed()函数进行翻转。只能返回一个迭代器，不能返回字符串。
# print(list(reversed(array_slice)))


# 将结果转换成int
array_int = int(array_slice_reverse)
print('将结果转换成int：',array_int)

# 输出二进制、八进制、十六进制
print("二进制：",bin(array_int))
print("八进制：",oct(array_int))
print("十六进制：",hex(array_int))








