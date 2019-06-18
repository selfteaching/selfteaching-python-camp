a_list=[0,1,2,3,4,5,6,7,8,9]          #创建列表
a_list.sort(reverse=True)             #翻转
print(a_list)                         

s1=(''.join(str(i) for i in a_list))  #先把i从int转换成str，然后调用Join函数，转化成字符创的形式
print(s1)

s2=s1[3:9]                            #取出3~8
print(s2)

s3=[]                                 #创建一个空列表S3
for i in s2:
    s3.append(i)                      #把i插入S3列表
print(s3)
s4=sorted(s3)                         #进行翻转
print(s4)

for i in s4:
    print(int(i))                     #把str转化成int

print(bin(int(i)))                    #2进制
print(oct(int(i)))                    #8进制
print(hex(int(i)))                    #16进制