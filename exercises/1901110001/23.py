for x in range(1,10):
    for y in range(1,10):
        if x>=y:
            print(x,'*',y,'=',x*y,end='\t')
    print()

i=1
while i<= 9:
    j=1
    while j<=9:
        if i%2==0:
            pass
        else:
            print('{:}*{:}={:} '.format(j,i,j*i),end='')
            if i==j:
                break
        j+=1
    print()
    i+=1