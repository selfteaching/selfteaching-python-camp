for x in range(1,10):
    for y in range(1,10):
        if x>=y:
            print(x,'*',y,'=',x*y,end='\t')
    print()

a=1
while a<=9:
    b=1
    while b<=a:
        if a%2==0:
            pass
        else:
            print('{:}*{:}={:} '.format(b,a,b*a),end='')
            if a==b:
                break
        b=b+1
    print('\n')
    a+=1 

    

        
