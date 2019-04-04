#for...in打印九九乘法表
for i in range (1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break


#使用while打印九九乘法表把偶数列输掉
i=0
j=0
while i<9:
    i+=1
    if i%2==0:#i等于偶数不执行后续循环代码
        continue
    while j<9:
        j+=1
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break

#一句话打印九九乘法表
print ('\n'.join([' '.join(['%s*%s=%-2s' % (i,j,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
            
