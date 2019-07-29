
#for loop
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            x = i * j
            print(f"{i} * {j} = {x}",end='   ')
    print()

#while loop
i = 1
while i < 10:
    if i%2 !=0:
        j = 1
        while j <= i:
            print(f"{i} * {j} = {i*j}", end='   ')
            j = j + 1
        print()
    i = i + 1
