x=1
while x<=9:
    y=1
    while y<=x:
        if x%2 == 1:
            print('%d*%d=%d\t' %(x,y,x*y),end='')
        y += 1
    if x%2 == 0:
           print()
    x += 1

for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%2d" % (x,y,x*y),end=" ")
    print(" ")