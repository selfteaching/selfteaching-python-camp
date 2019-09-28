# 将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转
a_list =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(iterable)
for i in a:
print(i,reverse=True)
a_list.reverse()
# 翻转后的数组拼接成字符串
s=''
s.join(a)
# ⽤字符串切片的方式取出第三到第⼋个字符（包含第三和第⼋个字符)
print(a_list[3:9])
# 将获得的字符串进行翻转
b=a_list[3:9].reverse()
print(b)
# 将结果转换为 int 类型
c=int(b)
print(c)
# 分别转换成⼆进制，⼋进制，十六进制
d=bin(int(c, 2))
e=oct(int(c, 2))
f=hex(int(c, 2))
# 最后输出三种进制的结果
print(d)
print(e)
print(f)