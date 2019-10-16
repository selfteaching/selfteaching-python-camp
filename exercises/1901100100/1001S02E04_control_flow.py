for i in range(10):
    for j in range(i):
        j = j + 1
        print("%d * %d = %d" % (i,j,i*j),end="\t")
    print()
i = 1
j = 1
while i < 10:
    if i % 2 != 0:
        #i = i +1
        while j <= i:
            print("%d * %d = %d" % (i,j,i*j),end="\t")
            j = j+ 1
        print()
    i = i + 1
    j = 1
   