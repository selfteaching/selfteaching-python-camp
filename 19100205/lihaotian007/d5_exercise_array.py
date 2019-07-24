a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
e = 0
f = []
a.reverse() #列表翻转
b = [str(i) for i in a]
c = ''.join(b) #拼接成字符串
d = c[2:8] #字符串切片
d = d[::-1] #字符串翻转
e = int(d) #转换成int
f.append(bin(e).replace('0b','')) #二进制
f.append(hex(e)) #八进制
f.append(oct(e)) #十六进制
print(f)
