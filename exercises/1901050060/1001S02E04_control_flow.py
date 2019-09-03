
for a in range(1,10):
        for b in range(1,a+1):
                print(f'{a}*{b}={a*b}',end=" ")
        print('')


a=1
while a <=9:
    b=1
    while b <= a:
        if a % 2 == 0:
            break
        print(f'{a}*{b}={a*b}',end=" ")
        b += 1
    a += 1
    print('')
