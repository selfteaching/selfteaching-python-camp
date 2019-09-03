for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(i,j,j*i),end='')
    print()

i=1
while i<=9 :
    j=1
    while j<=i:
        print('{}*{}={}\t'.format(i,j,j*i),end='')
        j+=1
    print()
    i+=2
         