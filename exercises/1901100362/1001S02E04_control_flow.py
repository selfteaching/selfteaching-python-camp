#for x in range(1,10):
#    for y in range(1,10):
#        if x>=y:
#            print(f'{x} * {y} = {x*y}',end=' ')
#    print()

x = 1
while x<=9:
    y=1
    while y<=9:
        if x>=y:
            if x % 2 !=0:
                print(f'{x} * {y} = {x*y}',end=' ')
        y +=1
    print()
    x +=1

