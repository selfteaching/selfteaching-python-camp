list1=[0,1,2,3,4,5,6,7,8,9]
list1.reverse()#翻转列表
#拼接字符串
list2=[str(x) for x in list1]#将列表中每个元素转换为字符串
a=''.join(list2)

b=a[3:9]
d=b[::-1]
e=int(d)

f=bin(e)#二进制
g=oct(e)#八进制
h=hex(e)#十六进制
print(f)
print(g)
print(h)
