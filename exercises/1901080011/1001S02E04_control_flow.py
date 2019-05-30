for i in range(1,10):
    for t in range(1,i+1):
        print(str(i) + '*' + str(t) + '=' + str(i*t),end='\t')
    print()


i = 1
while i < 10:
    if i%2 == 0:
        i += 1
        continue
    t = 1
    while t < i + 1:
        print(str(i) + '*' + str(t) + '=' + str(i*t),end='\t')
        t += 1
    print()
    i += 1
    