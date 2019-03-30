#下面开始使用while循环打印九九乘法表并使用条件判断把偶数行去
i=1
while i<=9:
    j=1
    while j<=i: 
        if i%2==1:
             print(i,"*",j,"=",i*j,end='\t')
        j += 1
    if i%2==0:
        print()
    i+=1

    