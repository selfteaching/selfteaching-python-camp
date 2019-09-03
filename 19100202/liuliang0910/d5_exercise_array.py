


# 3.1翻转列表
list_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_b=list(reversed(list_a))       # 将列表翻转
# print(list_b)

# 3.2把list_b弄成字符串
a=''
b=[]
for i in range(len(list_a)):
    b.append(str(list_b[i]))
c=a.join(b)
# print(c)        #这里不能直接用join，为什么，我也搞不懂，但还是一步一步来敲

#  3.3截取第三到第八的字符，含第三和第八
d38=c[2:8]
#  print(d38)
#  3.4翻转第3-8个字符
d83= d38[::-1] 
# print(d83)

# 3.5将结果转换为int类型
e=int(d83) 
# print(e)

# 3.6将结果转换为二进制,十进制，十六进制
e_2=bin(e) 
e_8=oct(e) 
e_16=hex(e) 

print(e_2)
print(e_8)
print(e_16)






















