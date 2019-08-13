x=1 
while x<10:
    y=1
    while y<=x:
        print('%s*%s=%s'%(x,y,x*y),end='\t')
        y+=1
    x+=2
    print()
