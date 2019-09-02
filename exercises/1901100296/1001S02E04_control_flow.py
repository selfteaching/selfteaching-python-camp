'''
九九乘法表
'''
'''
n=1
while n<10:
    for i in range(1,n+1):
        print(n,"*",i,"=",n*i,end='\t')
    n=n+1
    print('')
'''
'''
九九乘法表，将偶数行去掉
'''
n=1
while n<10:
    for i in range(1,n+1):
        if  n%2!=0:
            print(n,"*",i,"=",n*i,end='\t')
    n=n+1
    print('')