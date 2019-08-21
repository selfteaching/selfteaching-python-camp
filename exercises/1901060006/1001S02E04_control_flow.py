for i in range(1,10):
    # print(i,end='')

    for j in range(1,i+1):

        print('%d*%d=%d'%(i,j,i*j),end=" ")

    print()


i=1
while i<10:
    if i%2!=0:
        j=1
        while j<i+1: 
           print(i,"*",j,'=',i*j,sep='',end='\t')
           j+=1
        print()
    i+=1
