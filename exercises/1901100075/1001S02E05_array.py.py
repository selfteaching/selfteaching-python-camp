a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse=a[::-1]
print('将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转==>',reverse)

#翻转后的数组拼接成字符串
#调用''(空字符串)str类型的join方法可以连接列表里面的元素，用''(空字符串)表示连接的时候元素间不用字符隔开
#因为reserve里面都是int类型的元素，所以拼接之前要把reserve变成一个包含str类型元素的列表
join_str=''.join([str(i)for i in reverse])
print('翻转后的数组拼接成字符串==>',join_str)

#⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）
slice_str=join_str[2:8]
print('⽤字符串切⽚的⽅式取出第三到第⼋个字符（包含第三和第⼋个字符）==>',slice_str)

#将获得的字符串进⾏翻转
reserve_str=slice_str[::-1]
print(reserve_str)
#将结果转换为 int 类型
#分别转换成⼆进制，⼋进制，⼗六进制
int_value=int(reserve_str)
print('转换为int类型==>',int_value)
print('转换为二进制==>',bin(int_value))
print('转换为八进制==>',oct(int_value))
print('转换为十六进制==>',hex(int_value))
