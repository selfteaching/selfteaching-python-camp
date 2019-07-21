a = [0,1,2,3,4,5,6,7,8,9]#数组a
a.reverse()#翻转数组
print(a)

s=''#把数组拼接为字符串
for i in range(0,10): 
    s=s+str(a[i]) 
print(s)
s1=s[2:8]#切片取出第3到8个字符
print(s1)
s2=s1[::-1]#翻转字符串
print(s2)
s3=int(s2)#取整数
print(s3)
print(bin(s3),'\n',oct(s3),'\n',hex(s3)) #转换为二进制，八进制，十六进制并输出结果
