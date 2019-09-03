i=1
while i<=9:
    if (i%2) == 0:
        i+=1
        continue
    j = 1
    while j<=i:
        print('%d*%d=%d'%(i,j,i*j),end='\t') 
        j+=1
    print('\n')
    i += 1
   