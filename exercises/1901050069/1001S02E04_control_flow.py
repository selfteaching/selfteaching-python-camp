for i in range(1,10):
    for j in range (1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()


x=1
while x < 10:
    for y in range(1,x+1):
        if x % 2 != 0:
            print('{}*{}={}'.format(x,y,x*y),end='\t')
    x+=1
    print()