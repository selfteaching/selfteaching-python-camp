for i in range (1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break


i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break





print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
    




