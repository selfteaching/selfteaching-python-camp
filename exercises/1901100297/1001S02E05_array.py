#将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1]
print(reversed_list)
#翻转后的数组拼接成字符串
str_list = ''.join(str(i) for i in reversed_list)
print(str_list)
#⽤用字符串串切⽚片的⽅方式取出第三到第⼋八个字符
slice_str = str_list[2:8]
print(slice_str)
#将获得的字符串串进⾏行行翻转
reversed_str = slice_str[::-1]
print(reversed_str)
#将结果转换为 int 类型
int_str = int(reversed_str)
print(int_str)
#分别转换成⼆二进制，⼋八进制，⼗十六进制,最后输出三种进制的结果
print('二进制:',bin(int_str))
print('八进制:',oct(int_str))
print('十六进制:',hex(int_str))