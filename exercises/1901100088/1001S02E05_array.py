li = [0,1,2,3,4,5,6,7,8,9]

print()

print("2.将数组li翻转")
array_1 = list(reversed(li))
print(array_1)
print()

print("3. 翻转后的数组拼接成字符串")
b = []
for c in array_1:
    b.append(str(c))
arr_3 = "".join(b)
print(arr_3)
print()

array_2 = "".join(str(a)for a in array_1)
print(array_2)
print()


print("4.用字符串切片的方式取出第三到第八个字符(包含第三和第八个字符)")
array_3 = array_2[3:9]
print(array_3)
print()

print("5.将获得的字符串翻转")
array_4 = array_3[::-1]
print(array_4)
print()

print("6.将结果转换为int类型")
array_5 = int(array_4)
print(array_5)
print(type(array_5))
print()

print("7.分别转换为二进制，八进制和十六进制")
binary_num = bin(array_5)
octonary_num = oct(array_5)
hex_num = hex(array_5)
print()

print("8.最后输出三种进制结果")
binary_num = binary_num.lstrip("0b")
print(binary_num)
octonary_num = octonary_num.lstrip("0o")
print(octonary_num)
hex_num = hex_num.lstrip("0x")
print(hex_num)