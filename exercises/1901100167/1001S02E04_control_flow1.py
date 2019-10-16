for x in range(1,10):
    for y in range(1,x+1):
        if x>=y:
            print('%s*%s=%s'%(x,y,x*y),end='\t')
    print()

