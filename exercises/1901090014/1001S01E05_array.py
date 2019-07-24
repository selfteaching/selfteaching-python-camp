a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
b=len(a) #确定一共多少个字符
#print (b)
for i in range(b) :
    #print (i)
    for j in range(b-i-1) :
        #print("第二个",j)
        c=a[j+1]
        #print(c)

s=[str(i) for i in a]
d="".join(s)
print(d)
print(d[2:8])
e = d[::-1]
print(e)
f=int(e)
print("转化为十进制",f)
print("转换为二进制为：", bin(f))
print("转换为八进制为：", oct(f))
print("转换为十六进制为：", hex(f))



