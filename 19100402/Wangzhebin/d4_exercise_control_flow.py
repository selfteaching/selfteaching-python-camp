for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    if j==i:
        print(end="\n")
print(end="\n")
for i in range(1,10): 
    if i % 2 ==0:
        continue   
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    if j==i:
        print(end="\n") 
print(end="\n")
for i in range(1,10):
    while i % 2 ==0:
        break
    else:
        for j in range(1,i+1):
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
        if j==i:
            print(end="\n")
