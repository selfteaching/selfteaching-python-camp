for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print('\n')


i=1
while i<10:
    if (i%2)==0:
        i=i+1
        continue
    else:
        j=1
        while j<i+1:
            print(i,'*',j,'=',i*j,end='\t')
            j=j+1
        print('\n')
        i=i+1

