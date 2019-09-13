print('打印九九乘法表')
for n in range(1,10):
    for x in range(1,n+1):
        print(n,'*',x,'=',n*x,end='\t')
    print()
    
print('打印跳过偶数行')  
n=1
while n<10:
    if n%2>0:
        for x in range(1,n+1):
            print(n,'*',x,'=',n*x,end='\t')
        print()
    n+=1
