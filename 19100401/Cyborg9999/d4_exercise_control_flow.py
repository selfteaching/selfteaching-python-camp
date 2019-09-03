#九九乘法表
for x in range(10): 
    for y in range(1,x+1):
        print ("%d * %d = %d" %(x,y,x*y),end="\t")
    print("\n",end='')    

        
#九九乘法表（去除偶数行）
print(end='\n')
n = 1
while n <= 9 : 
    if (n % 2 !=0):
        i = 1
        while i <= n :
            if (i % 2 !=0 ):
                print ("%d * %d = %d" %(n,i,n*i),end='\t')
            i = i + 1
        print('\n',end='') 
    n = n+1  
    