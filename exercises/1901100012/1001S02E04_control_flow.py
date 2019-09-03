# for...in...九九乘法表
for i in range(10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j)
    else:
        print(' ',end='\n')
    print()

#while九九乘法表剔除偶数行
n=1
while n<10:
    if n%2==0:
        print()
    else:
        for m in range(1,n+1):
            print(n,"*",m,"=",n*m,' ',end='\t')
    n+=1

    
    
        

    