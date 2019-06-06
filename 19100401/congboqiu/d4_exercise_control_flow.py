print('用for...in编九九乘法表')
for i in range(1,10): 
     for j in range(1,i+1): 
         print(i,'*',j,'=',i*j,end='   ')#print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
         if i == j: #当i等于j的时候，
             print()#换行。
print('用while编去偶数行的九九乘法表')
i=0
j=0
while i<9:
    i+=1
    if i%2==0:
        continue#i为偶数是不执行后续循环代码
    while j<9:
        j+=1
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break