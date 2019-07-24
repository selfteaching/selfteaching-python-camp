#使用for...in打印九九乘法表

for i in range(1,10):  #当i在1～9时开始循环

    for j in range(1,i+1):  #当j在1～i+1时开始循环

        print('{}+{}={}\t'.format(j,i,i*j),end='') #\t表示锁进一个tab，end=''表示末尾不换行，加空格
    
    print()


#使用while循环打印九九乘法表并用条件判断把偶数行去除

x= 1                   
while x < 10:          
    y = 1              
    if(x%2==1):       
        while y<x+1:   
            print(x,'x',y,'=',x*y,end=' ')
            y=y+1
        print (end='\n')
        x=x+1
    else:
        x=x+1