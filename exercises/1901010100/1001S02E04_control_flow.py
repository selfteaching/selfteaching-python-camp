for i in range(1, 10):
    for j in range(1, i+1):
        print(j,"*",i,"=",i*j,end="\t")
        if i == j:
            print()
for i1 in range(1, 10, 2):
    for j1 in range(1, i1+1):
        print(j1,"*",i1,"=",i1*j1,end="\t")
        if i1 == j1:
            print()
