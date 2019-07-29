t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#把t做翻转
t2=t[::-1]
#把t2从数组转换为字符串
t3="".join(map(lambda x:str(x),t2))
#把字符串切片
t4=t3[3:8]

#再一次做翻转
t5=t4[::-1]
#把字符串转换为int型
t6=int(t5)
print(t6)
#转换为2进制
t7=t6
t8=bin(t7)
print(t8,type(t8))
#转换为8进制
t9=oct(t7)
print(t9,type(t9))
#转换为16进制
t10=hex(t7)
print(t10,type(t10))