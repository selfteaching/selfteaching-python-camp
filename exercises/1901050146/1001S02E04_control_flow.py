for i in range(1,10):
    for x in range(1,i+1):
        print(i,"*",x,"=",i*x,end='\t',sep='')
    print()



a=1
while a<10:
    b=1
    while b<a+1:
        if a % 2 !=0:
            print(a,"*",b,"=",a*b,end="\t",sep="")
        b +=1
    print()
    a +=1            