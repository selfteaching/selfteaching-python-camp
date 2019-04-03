#for...in打印九九乘法表
for i in range (1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break


#使用while打印九九乘法表把偶数列去掉
i=0
j=0
while i<9:
    i+=1
    if i%2==0: #i等于偶数不执行后续循环代码，i是数减一
       continue
    while j<9:
        j+=1
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break
               