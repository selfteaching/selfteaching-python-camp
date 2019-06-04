for i in range (1,10):
    for j in range (1,i+1):
        while  i%2!=0:
            print ("%s*%s=%s"%(i,j,i*j),end='\t')
            break
print ()