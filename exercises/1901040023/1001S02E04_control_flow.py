for i in range (1,10):
    for j in range (1,i+1):
        print("{}*{} = {:<4}".format(i,j,i*j),end = " ")
    print("")
    print(''+"-"*96)

i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j < i+1:
        print(i,"*",j,"=",i*j," ",end="")
        j += 1
    print("",end="\n")
    i += 1