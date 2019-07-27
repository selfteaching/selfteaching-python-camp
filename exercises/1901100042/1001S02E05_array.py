'''
array
time：2019年7月21日21:53:28
version:1.0
'''
a = [0,1,2,3,4,5,6,7,8,9]
#1.将数组翻转
reversed_a = a[::-1]
print('翻转后的列表==>',reversed_a)

#2.将veversed_a拼接成字符串
#首先将列表a中的元素转变成str，再利用str的join方法
joined_str =''.join([str(i) for i in reversed_a])#''表示空字符串
print('拼接成的字符串==>',joined_str)

#3.用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
sliced_str = joined_str[2:8]
print('第三至第八个字符==>',sliced_str)

#4.将获得的字符串翻转
reversed_str =sliced_str[::-1]
print('翻转字符串==>',reversed_str)

#5.将结果转换成int
int_str =int(reversed_str)
print('转换成int后的结果==>',int_str)
print('转换成二进制==>',bin(int_str))
print('转换成八进制==>',oct(int_str))
print('转换成十六进制==>',hex(int_str))