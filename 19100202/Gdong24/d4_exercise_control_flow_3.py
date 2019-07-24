i=1  #row 
while i<=9:
    j = 1  #column
    while j<=i:
        print("%dx%d=%d"%(i,j,i*j),end=' ')
        j=j+1
    print(' ')
    i+=2