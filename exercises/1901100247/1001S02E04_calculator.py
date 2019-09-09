print("乘法口诀")
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, '*', i, '=', i * j,end="   ")
    print("")

print('奇数乘法口诀')
for i in range(1, 10):
    if i%2==1:
        for j in range(1, i+1):
            print(j, '*', i, '=', i * j,end="   ")
        print("")
