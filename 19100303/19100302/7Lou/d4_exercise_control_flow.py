#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):      
        print('{}*{}={}\t'.format(i,j,i*j), end='')
    print('')

#打印九九乘法表奇数行.不同的思路不同的方式，没有唯一
i=1
while i<10:
    j=1
    while j<=i:
        if i%2 != 0:
            #print("%d * %d = %d"%(i,j,i*j),end='\t')
            print('{}*{}={}\t'.format(i,j,i*j),end='')
            #print(i,'*',j,'=',i*j,end='\t')
        j+=1
    print('')
    i+=1





