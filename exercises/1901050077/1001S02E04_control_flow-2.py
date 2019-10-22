# 输出奇数行的99乘法表
m=-1
n=0
while m<9:
    m%2!=0
    m+=2
    while n<9:
        n+=1
        print(m,'*',n,'=',m*n,end='')
        if m==n:
            n=0
            print()
            break
