for a in range(1,10):
    for b in range(1,a+1):
        c = a * b
        print('%d*%d=%-2d'%(a,b,c),end = ' ' )
    print()
    #用while函数只打印奇数行的九九乘法
    i=0
j=0
while(i<9):
    i+=1
    if i%2==0:
        i+=1
    while (j<9):
        j+=1
        print(i, "*", j, '=', i*j, end='\t')
        if  i==j:
            j=0
            print('')
            break