for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end=" \t ")  
    print()


for i in range(1, 10,2):
    for j in range(1, i + 1):
        print(i, '*', j, '=', j * i, end=" \t ")  
    print()