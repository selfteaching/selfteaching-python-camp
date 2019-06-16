for i in range(1,10):
    for j in range (1,i+1):
        print(j,"x",i,"=",i*j,end='\t')
    print()
print()
i=0
j=0
while i<9:
    i+=1
    while j<i:
        j+=1
        if (i%2)==0:
            j=0
            break
        print(j,"x",i,"=",i*j,end='\t')
        if i==j:
            j=0
            print()
            break
