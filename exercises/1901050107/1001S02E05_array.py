text = [0,1,2,3,4,5,6,7,8,9]
#将数组[0,1,2,3,4,5,6,7,8,9]翻转
text.reverse() #方法一
text = text[::-1]
# 翻转后的数组拼接成字符串串
str1 = ''.join(str(i) for i in text)
print(str1)
# 用字符串切片的方式取出第三到第八个字符
sliced_str = str1[2:8]
# 将获得的字符串串进⾏行行翻转
str2 = list(sliced_str)
str2.reverse()
# 将结果转换为int类型
int_str = int(sliced_str)
# 分别转换成⼆进制，⼋进制，十六进制
# 最后输出三种进制的结果
print("二进制-》", bin(int_str))
print("八进制-》", oct(int_str))
print("二进制-》", hex(int_str))