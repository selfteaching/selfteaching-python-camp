for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='  ')
    print('')

print('================我是分隔符=================')

i=1
j=1
while i<10:
    if i % 2 != 0:
        while j<=i:
            print('{}*{}={}'.format(i,j,i*j),end='   ')
            j=j+1
        print('')
    j=1
    i=i+1