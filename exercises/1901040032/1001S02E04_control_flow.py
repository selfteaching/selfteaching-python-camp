for i in range (1,10):
    for j in range(1,10):
        print(j,"*",i,"=",i*j,end="\t")
        if i==j:
            print("")
            break


print()


i=1
while i<=9:
    j=1
    while j<=i and i%2!=0:
        print(i,"*",j,"=",i*j,end="\t")
        j+=1
    print()
    i+=1
