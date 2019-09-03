#定义一个sample list
sample_list = [0,1,2,3,4,5,6,7,8,9]

#对定义过的列表进行翻转
reversed_list = sample_list[::-1]
print('列表翻转==>', reversed_list)

#将翻转后的数组拼接成字符串
#调用‘’（空字符串） str类型的join方法可以连接列表里的元素 用‘’（空白字符）表示链接的时候不用任何字符隔开
joined_str = ''.join([str(i) for i in reversed_list])
print('反转后的数组拼成字符串 ==>', joined_str)

#用字符串切片的方式取出第三到第八个字符（包含第三和第八字符）
#切片的时候包含开始索引，不包含结果的索引
sliced_str = joined_str[2:8]
print('将用字符串切片的方式取出第三到第八个字符 ==>', sliced_str)

#获得的字符串进行翻转
reversed_str = sliced_str[::-1]
print('字符串翻转 ==>',reversed_str)

#转化为int形式
int_value = int(reversed_str)
print('转化为 int 类型 ==>',int_value)
print('转换为二进制 ==> ',bin(int_value))
print('转换为八进制 ==>',oct(int_value))
print('转换为十六进制 ==>',hex(int_value))