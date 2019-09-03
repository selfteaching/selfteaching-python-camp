for x in range(1,10):
    for y in range (1,x+1):
        z=x*y
        print("%d*%d=%d"%(x,y,z),end="    ")
    print()

print("\n")


#for x in range(1,10,2):
for x in range(1,10):
    while x % 2 == 0:
        break
    else:
        for y in range (1,x+1):
            z=x*y
            print("%d*%d=%d"%(x,y,z),end="    ")
        print()