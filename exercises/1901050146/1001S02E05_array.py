a=[0,1,2,3,4,5,6,7,8,9]
a.reverse()
print ('数组翻转',a)

b=[str(i)for i in a]
c=''.join(b)
print("字符串",c)

d=c[2:8]
print("切片",d)

e=d[::-1]
print("翻转",e)

f=int(e)
print("转整",f)

print("转二进制",bin(f))
print("转八进制",oct(f))
print("转十六进制",hex(f))