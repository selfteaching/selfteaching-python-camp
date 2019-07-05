a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()
#print(a)
b = ''.join(str(i) for i in a)#需要遍历数组才能输出
#print (b)
c = b[2:8]#字符串切片取3到8字符
#print(c)
d=c[::-1]#字符串切片方式翻转
#print(d)
e = int(d)#字符串转数值
#print(e)
print("转换为二进制为：", bin(e))
print("转换为八进制为：", oct(e))
print("转换为十六进制为：", hex(e))