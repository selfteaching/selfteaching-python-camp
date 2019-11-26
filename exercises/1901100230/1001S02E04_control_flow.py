for i in range(1,10):
    for n in range(1,i+1):
        print('{}*{}={} '.format(i,n,i*n),end="")
    print()

k=-1
while k<9:
    k+=2
    for j in range(1,k+1):
        print('{}*{}={} '.format(k,j,k*j),end="")
    print()