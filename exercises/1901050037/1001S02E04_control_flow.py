
for i in range(1,10):
    print('')
    for j in range(1,10):
        if i>=j:  
            k=i*j
            print('%d*%d=%d' %(i,j,k),sep=' ',end=' ')
        else:
            continue
			
a=1
while a<10 :
    b=1
    while a>=b and a%2!=0:
        c=a*b
        print('%d*%d=%d' %(a,b,c),sep=' ',end=' ')
        b=b+1
    a=a+1
    print('')