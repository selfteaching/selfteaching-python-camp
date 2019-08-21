array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2. 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
array.reverse()

#3. 翻转后的数组拼接成字符串
array_s1 = ''
for i in array:
    array_s1 = array_s1 + str(i)

#4. ⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）
array_s2 = array_s1[2:8]

#5. 将获得的字符串进⾏翻转
array_s3 = array_s2[::-1]

#6. 将结果转换为 int 类型
array_s4 = int(array_s3)

#7. 分别转换成⼆进制，⼋进制，⼗六进制
result_2 = bin(array_s4)
result_8 = oct(array_s4)
result_16 = hex(array_s4)

#8. 最后输出三种进制的结果
print("二进制:",result_2)
print("八进制:",result_8)
print("十六进制:",result_16)

