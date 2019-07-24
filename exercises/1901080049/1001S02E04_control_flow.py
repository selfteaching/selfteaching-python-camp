print("test 1")
for a in range(1, 10):
    for b in range(1, a+1):
        print(a,"*",b,"=",a*b,"\t",end='')
    print()


print("test 2")
c = 0
d = 0
while c <= 9:
    c += 1
    if c % 2 !=0:
        while d <=9:
            d += 1
            print(c,"*",d,"=",c*d,"\t",end="")
            if c == d:
                d = 0
                print("")
                break