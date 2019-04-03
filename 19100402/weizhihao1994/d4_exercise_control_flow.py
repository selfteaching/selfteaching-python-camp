for i in range(1,10):
    for n in range(1,10):
        if i>=n:
            print(i,'*',n,'=',i*n,end='\t')
        elif i<n:
            print(' ')
            break

x=0
while x<9:
    x += 1
    if x%2 != 0:
        y=1
        while x>=y:
            print(x,'*',y,'=',x*y,end='\t')
            y += 1
        else:
            print('')

 