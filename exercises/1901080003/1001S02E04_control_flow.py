for a in range (1,10):
    for b in range(1,10):    
         print (b, "*", a,'=' ,a * b,"\t", end=' ')
         if a == b:
             print("")
             break 

a = 0
b = 0
while a < 9:
    a += 1
    if (a % 2) == 0:
        continue
    while b < 9:
        b += 1
        print(a,"*",b,"=", a*b,"\t", end="")
        if a == b:
            b=0
            print("")
            break             