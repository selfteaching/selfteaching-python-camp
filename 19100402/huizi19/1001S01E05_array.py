a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=a[::-1]
print(b)

c= [str(i) for i in b]
print(c)

d= ''.join(c)
print(d)

e=c[2:7]
print(e)

f=e[::-1]
print(f)

dec=[int(i) for i in f]
print(dec)

 

print("转换为二进制为：", [bin(i) for i in dec])
print("转换为八进制为：", [oct(i) for i in dec])
print("转换为十六进制为：", [hex(i) for i in dec])
