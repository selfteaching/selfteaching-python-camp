for x in range(1, 10):
    while x % 2 == 0:
        break
    
    else:
        for y in range(1, x+1):
            print('{}*{}={}\t'.format(y, x, x*y), end='')
    print()
    