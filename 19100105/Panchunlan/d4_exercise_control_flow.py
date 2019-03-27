for i in range (1,10):
    for j in range (1,10):
        print(i,"*",j,"=",i*j,"\t",end="")
        if i == j:
            print("")

            break




i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print(i,"*",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            i=i+1
            print("")
            break


