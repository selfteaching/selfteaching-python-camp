a = [0,1,2,3,4,5,6,7,8,9]
print("列表a中的元素:\n",a)
# 翻转列表a中的元素
b = a[::-1]
print("翻转列表a中的元素:\n",b)
# 翻转列表a中的元素
# c = []
# c = [a.reverse()]
# print(c)
a.reverse()
# print(a)
d = a
print("翻转列表a中的元素:\n",d)

# 拼接列表a中元素为字符串
e = ''.join([str(i) for i in b])
print("拼接列表a中元素为字符串:\n",e)
# s = ''
# t = ["P","y","t","h","o","n"]
# s.join(t)

# 取出第三到第八个字符
print("取出第三到第八个字符:\n",e[2:8])

# 字符串串进⾏翻转
f = e[2:8]
print("对字符串串进行翻转:\n",f[::-1])

# 将结果转换为int类型
g = f[::-1]
print("将结果转换为int类型:\n",int(g))
h = int(g)   
print("将结果转换为二进制:\n",bin(h))
print("将结果转换为八进制:\n",oct(h))
print("将结果转换为⼗六进制:\n",hex(h))

