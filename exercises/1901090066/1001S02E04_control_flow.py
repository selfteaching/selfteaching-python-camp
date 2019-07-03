#for打印乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print (m,'*',n,'=',m*n,end='    ')
    print()
#while 打印乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        if i%2 !=0:
            print (i,'*',j,'=',i*j,end='    ')
        j =j+1
    print ()   
    i=i+2