#九九乘法表
def mul_table():
    i=0
    for i in range(1,10):
        for n in range(1,10):
            if n<=i:
                print(str(i),'*',n,'=',i*n,end='\t')
        print(' ')
mul_table()
def odd_table():
    for i in range(1,10):
        for n in range(1,10):
            if n<=i:
               while n*i%2!=0:
                     print(str(i),'*',n,'=',i*n,end='\t')
                     break
        print(' ') 
odd_table()


