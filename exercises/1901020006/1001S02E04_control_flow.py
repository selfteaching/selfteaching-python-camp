#九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        n=x*y
        print('{}*{}={}'.format(x,y,n),end='\t')
    print()



    
#奇数层
for x in range(1,10):
    if x%2!=0:
        for y in range(1,x+1):
            n=x*y
            print(x,"x",y,"=",x*y,sep='',end='\t')
        print()
