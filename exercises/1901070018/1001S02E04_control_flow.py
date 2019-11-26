for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(i, j,i*j),end='    ')
    print()

x = 0
while x < 9:
    x += 1
    for i in range(1, x + 1):
        if x % 2 == 0:
            break
        else:
            print('{}*{}={}'.format(x, i, x*i),end="    ")
    else:
        print()
