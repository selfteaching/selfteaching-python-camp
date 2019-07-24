for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    else:
        print()

print() 
a = 1
b = 1
while a < 10:
    if a % 2 != 0:
        if a != b:
            print('{}*{}={}'.format(a,b,a*b),end='\t')
            b = b + 1
        else:
            print('{}*{}={}'.format(a,b,a*b))
            a = a + 1
            b = 1
    else:
        a = a + 1