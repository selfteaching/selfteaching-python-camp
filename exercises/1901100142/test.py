print('打印奇数行九九乘法表')
for i in range(1,10):
    while i%2 == 0:
        break
    else:
        for j in range (1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    print()

