#将数组进行翻转
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data.reverse()
print(data)

#将翻转后的数组拼接成字符串
data_string = ''
for i in data:
    data_string += str(i)
print(data_string)

#字符串切片取出第三到第八个字符（包含第三和第八）
data1 = data_string[2:8]
print(data1)

#将获得的字符串进行翻转
data1 = data1[::-1]
print(data1)

#将其转换为int类型
data1 = int(data1)
print(data1)

#转换成二进制，八进制，十六进制
print('二进制:', bin(data1))
print('八进制:', oct(data1))
print('十六进制:', hex(data1))