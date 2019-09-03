#数组操作，进制转换
a=[0,1,2,3,4,5,6,7,8,9]
print(a)
b=a[::-1]                         #将数组按顺序翻转
print("将数组翻转")
print(b)

c= [str(x) for x in b]      # b里的数字转换为字符串
d="".join(c)                #将列表中各个字符拼接成字符串
print("将列表中各个字符拼接成字符串")
print(d)  

e=d[2:8]                    #分切取出3~8的字符
f=list(e)
g=f[::-1]                   #翻转列表                  
h="".join(g)                #将列表转化为字符串
print("分切取出3~8的字符并翻转")
print(h)

j=int(h)                      #将字符串转化为int类型数字
print("转换为2进制")            #将整数转化成二进制，八进制，十六进制
print(bin(j))

print("转换为8进制")
print(oct(j))

print("转换为16进制")
print(hex(j))
