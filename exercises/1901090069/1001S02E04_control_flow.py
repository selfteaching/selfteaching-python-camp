#使用for语句完成乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end='\t')
    print(end='\n')
        
#使用while语句及if语句输出乘法表的奇数行
m = 1
while (m<10):
    n = 1
    while(n<m+1):
        if m%2!=0:       
            print(m,"*",n,"=",m*n,end='\t')
        n+=1
    if m%2!=0:
        print(end='\n')
    m+=1
    
