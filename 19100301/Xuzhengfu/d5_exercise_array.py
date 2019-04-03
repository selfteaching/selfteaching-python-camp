# 三、数组操作，进制转换
# 1、……
# 2、将数组 [0，1，2，3，4，5，6，7，8，9] 翻转
numbers = [0,1,2,3,4,5,6,7,8,9]
numbers.reverse()

# 3、翻转后的数组拼接成字符串
num_str_list = [str(num_str) for num_str in numbers]     # 使用list comprehension生成列表
numbers_str = "".join(num_str_list)                      # Join all items in the list "num_str_list" into the string "numbers_str"

# 4、用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
substring = numbers_str[2:8]

# 5、将获得的字符串进行翻转
substring = substring[::-1]

# 6、将结果转换为int类型
subint = int(substring)

# 7、分别转换成二进制，八进制，十六进制
bin_result = bin(subint)
oct_result = oct(subint)
hex_result = hex(subint)

# 8、最后输出三种进制的结果
print(bin_result, oct_result, hex_result, sep="\n")