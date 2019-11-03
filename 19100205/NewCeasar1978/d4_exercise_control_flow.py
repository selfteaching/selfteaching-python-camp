for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i * j,end = '\t')
    print()

i = 0
while i < 9: 
    i += 1
    j = 1
    while j <= i:
        print (j,'*',i,'=', j*i , end = '\t')
        j += 1
    print()

i = 0
while i < 9: 
    i += 1
    if  i % 2 != 0:
        j = 1
        while j <= i:
            print (j,'*',i,'=', j*i , end = '\t')
            j += 1
        print()
    