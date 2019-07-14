i = 1
while i <= 9:
    j = 1
    while j <=9:
        if i%2==0:# i indicates the number of row
            pass
        else:
            print('{:}*{:}={:} '.format(j,i,j*i),end='')
            if i==j:
                break
        j=j+1
    print('\n')
i += 1 