i=0
while i <9:
    i+=1
    a=0
    while a <9:
        a+=1
        if int(i)%2!=0:
            print('%d*%d=%d'%(i,a,i*a),end=' ')
            if i==a:
                print('')
                break


for i in range(1,10):
    for a in range(1,i+1):
        print('%d*%d=%d'%(i,a,i*a),end=' ')
        if i==a:
            print('')
            break