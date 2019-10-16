for a in range(1,10):
     for b in range(1,a+1):
         c=a*b
         print ('{}*{}={}'.format(a,b,c),end='\t')
     print ()


#以下是另一种
a=0
while a<10:
    a=a+1
    for b in range(1,a+1):
        c=a*b
        if a==1:
            print ('{}*{}={}'.format(a,b,c),end='\t')
        elif a==3:
            print ('{}*{}={}'.format(a,b,c),end='\t')
        elif a==5:
            print ('{}*{}={}'.format(a,b,c),end='\t')
        elif a==7:
            print ('{}*{}={}'.format(a,b,c),end='\t')
        elif a==9:
            print ('{}*{}={}'.format(a,b,c),end='\t')
    print ()