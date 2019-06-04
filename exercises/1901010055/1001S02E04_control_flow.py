#九九乘法表
def mul_table():
    i=0
    for i in range(1,10):
        for n in range(1,10):
            if n<=i:
                print(str(i),'*',n,'=',i*n,end='\t')
        print()
mul_table()
def odd_table():
    i=1
    while i<10:
        j=1
        if(i%2==1):
            while j<=i:
                print('{}*{}={}'.format(i,j,i*j),end='\t')
                j+=1
            print()
            i+=1
        else:
            i+=1 
odd_table()


