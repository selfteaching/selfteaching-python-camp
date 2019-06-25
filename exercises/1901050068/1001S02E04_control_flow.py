for i in range (1,10):
    for j in range (1,10):
        print(i,"*",j,"=",i*j,"\t",end=" ")
        if i==j:
           print("")
           break

i=1
while i<10:
      j=1
      while j<i+1:
            if i%2 == 0:
                break
            print(j,"*",i, "=",i*j,sep="",end="\t")
            j += 1
      print()
      i += 1