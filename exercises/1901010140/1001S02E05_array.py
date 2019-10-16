#将数组  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#-------------------------解决大部分中文乱码的问题都能解决---------------------
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(reversed(a))    
print(b)

#翻转后的数组拼接成字符串
#3.2 翻转数组
sample_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = sample_list[::-1]#切片[::-1]是将列表或字符
#consequence[start_index: end_index: step]

print( reversed_list)
#3.3翻转后的数组拼接成字符串
joined_str = ''.join([str(i) for i in reversed_list])
print(joined_str)
#3.4取出第3到第8字符
sliced_str = joined_str[2:8]
print(sliced_str)
#3.5对字符串翻转
reversed_str = sliced_str[::-1]
print(reversed_str)
#3.6结果转换int类型
int_value = int(reversed_str)
print(int_value)

print("二进制：",bin(int_value))
print("八进制：",oct(int_value))
print("十六进制：",hex(int_value))

