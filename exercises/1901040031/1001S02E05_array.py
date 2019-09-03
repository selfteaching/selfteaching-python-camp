a =[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)

str = "".join(str(i) for i in a) #将从a列表中提取出来的数字转换为字符后，用 join连接成字符串，不分隔
print(str)

s = str[3:9]
print(s)
#  s1 = s.reverse()  报错 ，无法输出，'str' object ha no attribute 'reverse'
s1 = s[::-1]    #为什么采用这种方法就可以输出
print (s1)  

s2 = int(s1)
print(s2)

s2_bin = bin(s2)
s2_oct = oct(s2)
s2_hex = hex(s2)

print (s2_bin,s2_oct,s2_hex)