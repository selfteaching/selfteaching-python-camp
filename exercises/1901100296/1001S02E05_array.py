array=[0,1,2,3,4,5,6,7,8,9]
# 1、翻转数组
array.reverse()
print('翻转后的数组：',array)

# 2、翻转后的数组拼接成字符串
#先将列表里的int型转换成str类型，再拼接

# 方法一：int转换成str，使用list的内置推导式
# str_array=''.join(str(i) for i in array)
# print('数组拼接成字符串：',str_array)

# 方法二：int转换成str,使用内置函数 map
str_array=''.join(map(str,array))
print('数组拼接成字符串：',str_array)

# 3、用字符串切片的方式取出第三到第八个字符(包含第三和第八个字符)
str_array=str_array[2:8]
print('取出第3-8个字符：',str_array)

# 4、将获得的字符串进行翻转
str_array=str_array[::-1]
print('字符串翻转：',str_array)

# 5、将结果转换为int类型
int_str_array=int(str_array)
print('将字符串转换成int：',int_str_array)
#6、分别转换成二进制，八进制，十六进制
# 十进制转二进制
print('二进制：',bin(int_str_array))
# 十进制转八进制
print('八进制：',oct(int_str_array))
# 十进制转十六进制
print('十六进制：',hex(int_str_array))