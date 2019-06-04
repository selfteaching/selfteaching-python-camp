#使用for循环打印乘法表
for x in range(1,10):       #x在1-10之间变量
    for y in range(1,x+1):  #y变量在1-10之间
        print ("%d * %d = %d" %(x,y,x*y),end="\t")#打印出x和y 并相乘
print("")

#使用while循环打印乘法表并用条件判断把偶数行去掉
n = 1  #定义n变量
while n <= 9 : #n从1开始循环到9
    if (n % 2 !=0):#如果n不能被2整除就开始运行下面语句
        i = 1
        while i <= n :
            if (i % 2 !=0 ):
                print ("%d * %d = %d" %(n,i,n*i),end="\t")
            i = i + 1 #i变量加1
            print('\n',end='\t') 
    n = n+1#n变量加1
    print ("\n",end = '\t')
            
       
        

             

            