for n in range(1,10):
    for x in range(1,10):
        if n>=x:
            print(n,'*',x,'=',n*x,' ',end='')
    print()


i = 1
while i <= 9:
    if i%2==1:            
        j = 1
        while j <= i:    
            print("%d*%d=%-2d"%(i,j,i*j),end = ' ')  
            j += 1
    print()
    i += 1
