for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(i,j,i*j),end='\t')
    print()

for i in range(1,10):
    while i%2==0:
        break
    else:
        for j in range(1,i+1):
            print(i,"*",j,"=",i*j,end="\t")
        print()
        continue