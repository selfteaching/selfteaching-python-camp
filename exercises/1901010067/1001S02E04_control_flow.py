for i in range(1,10):
    for r in range(1,1+i):
        print('%d * %d = %d' %(i,r,i*r), end=' ')
    print('')

t = 0
while t <9:
    t +=1
    o = 0
    while o <t:
        o +=1
        if t%2==1:
            print('%d * %d = %d' %(t,o,t*o), end=' ')
    print('')