for a in range(1, 10):
    for b in range(1,a+1):
        print(a,"*",b,"=",a*b,end='\t')
        if a == b:
              print(' ',)
              break
a=-1             
while a<8:
    c=a%2
    if c==0:
        pass
    else:
        a=a+2
    for b in range(1,a+1):
            print(a,"*",b,"=",a*b,"\t",end="")
            if a==b:
                print("")
                break                    
      