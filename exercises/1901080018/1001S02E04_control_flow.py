for i in range(1, 10):
    for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j),end='')
    print()

print()
print()

for i in range(1, 10):
    if i % 2 != 0:
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j),end='')
        print()


print()


i = 1
while i < 10:
        j = 1
        while j <= i:
                print('{}x{}={}\t'.format(i, j, i*j),end='')
                j = j + 1
        print()
        i = i + 2

