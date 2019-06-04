for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end='  ')
        if j==i:break
    print("\n")
print("\n\n")        
for i in range(1,10,2):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end='  ')
        if j==i:break
    print("\n") 