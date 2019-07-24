def ninenine():
    for n in range(1,10):
        for x in range(1,n+1):
            print(n,'*',x,'=',n*x,end='\t')
        else:
            print(end='\n')
ninenine()

def ninenineodd():
    n=1
    x=1
    while (n<=9):
        while (n % 2 != 0):
            while(x <= n):
                print(n,'*',x,'=',n*x,end='\t')
                x=x+1
            else:
                print(end='\n')   
            break 
        n=n+1
        x=1
ninenineodd()