#使用for in...循环打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j,"\t",end='')
        if i==j:
            print("")
            break

i=0
j=0
while i<9:
    i+=1
    if i %2!=0:
        while j <9:
            j +=1
            print(i,"x",j,"=",i*j,"\t",end="")
            if i == j:
                j=0
                print("")
                break