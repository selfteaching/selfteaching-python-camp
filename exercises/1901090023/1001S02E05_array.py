list1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.reverse()
print(list1)

list2= [str(x) for x in list1]      # list1里的数字是int值，因此要转换为字符串
print(list2)

str1=''.join(list2)                 #将列表中各个字符拼接成字符串
print(str1)              

str2=str1[2:8]                      # 切片，取出第3-8个位置的字符
print(str2)               

str3=int(str2)
print(str3)                         # str3和str2长相一样，但类型不同，str2是字符串，str3转换为数字了。

print('转换成二进制')
print(bin(str3))

print('转换成八进制')
print(oct(str3))

print('转换成十六进制')
print(hex(str3))