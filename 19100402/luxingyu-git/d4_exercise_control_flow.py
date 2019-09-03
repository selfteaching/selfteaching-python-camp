for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='\t')
    print()


x = 0
y = 0
while x < 9:
    x += 1
    if x % 2 == 0:
        continue
    while y < 9:
        y += 1
        print(x,'*',y,'=',x*y,end='\t')
        if x == y:
            y = 0
            print()
            break