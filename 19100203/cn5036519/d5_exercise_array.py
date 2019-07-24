# 2、将数组[0,1,2,3,4,5,6,7,8,9]翻转
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# number_list.reverse()
# print(number_list)

# 使用切片也可以完成翻转
new_list = number_list[::-1]
print(number_list)
print(new_list)

# 3、翻转后的数组拼接成字符串
for i in range(len(new_list)):
    new_list[i] = str(new_list[i])
new_string = ''.join(new_list)
print(new_string)

# 4、用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
print(new_string[2:8])

# 5、将获得的字符串进行翻转
new_string2 = new_string[::-1]
print(new_string2)

# 6、将结果转换为int类型
number = int(new_string2)
print(number)
print(type(number))

# 7、分别转换成二进制、八进制、十六进制
print("二进制数：", bin(number))
print("八进制数：",oct(number))
print("十六进制数：",hex(number))

# 8、最后输出三种进制的结果
# 以上第7题已经输出结果了，不知道这题我理解的对不对。和第7题重复了





