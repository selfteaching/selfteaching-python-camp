for i in range(1,10):
    for j in range(1,i+1):
        d=i*j
        print('%d*%d=%2d'% (i,j,d),end=" ")
    print()

print()

a=1
while a<10 :
    if a%2==1:
        b=1
        while  b<=a:
            print ('%d*%d=%2d'% (a,b,a*b),end=" ")
            b=b+1
    a=a+1
    print()
