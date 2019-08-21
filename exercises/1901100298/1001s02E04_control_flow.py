for i in rang(1,10):
    for j in range (1,i+1):
        print(j,'*',i,'=',i*j,end="\t")
    print()

i = 1
while i <=9:
　　j = 1
　 while j <= i:
　　　　print('%d*%d=%2d\t'%(i,j,i*j),end='')
　　　　j+=1
 print()
 i +=1