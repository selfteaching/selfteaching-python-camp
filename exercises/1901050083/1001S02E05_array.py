a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print ("翻转后的列表", a)
a1=[str(i) for i in a]
b="".join (a1)
print ("合并成字符串", b)
c= b[2:8]
print ("三到八", c)
d=list(int(i) for i in c)
d.sort()
d1=[str(i) for i in d]
e="".join (d1)
print ("翻转", e)
f= int(e)
print ("转换成int", f)
print ("转换成二进制", bin(f))
print ("转换成八进制", oct(f))
print ("转换成十六进制", hex(f))