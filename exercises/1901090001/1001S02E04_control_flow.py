for i in range(1,10):
        for j in range(1,i+1):
                if j <= i:
                        print(i,'*',j,'=',i*j,'\t', end="") 
        print("")
                

r = 1
c = 1
while r <= 9:
        while c <= r:
                print("%s*%s=%s"%(r,c,c*r),end=" ")
                c += 1
        r += 2
        c = 1
        print("")