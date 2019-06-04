for a in range(1,10):
    for b in range(1,a+1):
        print(a,"*",b,"=",a*b,"\t",end="")
    print("")



i=1
while i<10:
    j=1
    while j<i+1:
        if i%2==0:
            print()
            break
        print(i,"*",j,"=",i*j,"\t",end="")
        j+=1
    i+=1
   

