# -*- coding: utf-8 -*-
for m in range(1,10):
    for n in range(1,m+1):
        print('%s×%s=%s'%(m,n,m*n),end='\t')
    print()