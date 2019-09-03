a = [0,1,2,3,4,5,6,7,8,9]
a.reverse() #用reverse()函数把列表类型a翻转
print(a)

b = "".join(str(i) for i in a) #以i遍历列表a,取得a中所有元素，并以无分隔”“粘合i中的元素，得字符串str
print(b)

c = b[slice(2,8,1)] #设定c为数列b中，由第三至第八个数字、步距为1的切片（即765432）
print(c)

d = c[::-1] #意思就是整个列表的索引编号*-1，由此实现翻转。我说不明白
print(d)

e = int(d) #将字符串234567转化为十进制数值234567
print(e)

f1 = bin(e) #十进制转二进制
f2 = oct(e) #十进制转八进制
f3 = hex(e) #十进制转十六进制
print(f1)
print(f2)
print(f3)