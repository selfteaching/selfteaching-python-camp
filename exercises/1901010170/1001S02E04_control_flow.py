#for。。in循环打印99乘法表

for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a*b,end='\t')
    print()

    
#while打印去偶数99乘法表

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