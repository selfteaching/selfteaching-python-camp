print('九九乘法表')
for a in range(1, 10):
    for b in range(1,a+1):
        print(a,"*",b,"=", a*b,"\t",end="")
        if a==b:
            print("")
            break
print('奇数乘法表')
m=-1
while m<8:
    k=m%2
    if k==0:
        pass
    else:
        m=m+2
    for n in range(1,m+1):
            print(m,"*",n,"=", m*n,"\t",end="")
            if n==m:
                print("")
                break