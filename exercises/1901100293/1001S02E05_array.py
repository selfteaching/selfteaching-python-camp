#数组是只包含特定格式内容的列表
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #将数组赋予a
a.reverse() #翻转数组
print('翻转的数组',a)
a=''.join(str(i) for i in a) #遍历a，并把a的元素转化为字符串重新赋予a
print('翻转后的字符串',a)
b=a[2:8] #取出3到8节赋予字符串b
b=b.split() #必须转化为列表才能进行翻转
b.reverse() #翻转b
print('3到8字符切片的翻转',b)
b=''.join(b) #需要先转化为str才能转化为int
i=int(b) #转化为int类型
print('转换为int类型',i) #打印
print('转换为2进制',bin(i)) #转化为2进制并打印
print('转换为8进制',oct(i)) #转化为8进制并打印
print('转换为16进制',hex(i)) #转化为16进制并打印