#99乘法表
for i in range(1,10):
    for j in range(1,10):
        print(j,"*",i,"=",i*j,"\t",end="")  
        if i==j:
            print("")
            break
i=1
while i<10:
    j = 1
    while j<i+1:
        if i%2 == 0:
            print()
            break
        else:
            print(j,"*",i,"=",i*j,"\t",end="")
        j += 1
    i +=1