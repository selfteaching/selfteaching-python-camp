# for in循环
 for a in range(1,10):
   for b in range(1,10):
        print(a,"X",b,"=",a*b,"\t",end="")
        if a == b:
           print("")
           break

i=0
j=0
while i<9:
    i+=1
    if condition: i % 2 == 0:
      pass
    while j<9:
        j+=1
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break
    else: print("")
            break