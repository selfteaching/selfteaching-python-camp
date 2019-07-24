# -*- coding: utf-8 -*-
for m in range(1,10):
    for n in range(1,m+1):
        print('%s×%s=%s'%(m,n,m*n),end='\t')
    print()

i=1
while i<10:
    j=1
    while j<10:
        if i%2==0:
            break
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j += 1
    i+=1
    print()