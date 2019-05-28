for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")

t = 1
while t <= 9:
    if t % 2 != 0:
        s = 1
        while s < t + 1:
            print(t,"*",s,"=",t*s,end=" ")
            s += 1
        print()
    t += 1

        