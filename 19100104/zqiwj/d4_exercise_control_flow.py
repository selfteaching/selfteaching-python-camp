#用for...in打印9*9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
       print('{}x{}={}\t'.format(j, i, i*j), end='')

    print()
    



#用while循环打印9*9乘法表，并剔除偶数行
a=0
b=0
while(a<9):
    a=a+1
    if a%2==0:
      a=a+1
    while(b<9): 
        b=b+1
        print(a,"*",b,'=',a*b,end='\t')
        if a==b:
            b=0
            print('')
            break''' '''  ''' '''