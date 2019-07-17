for a in range(1,10):
    b = 0
    while b < a :
        b = b + 1
        print(a,'*',b,'=',a*b,' ',end=' ')
    else:
        print(end ='\n')  

for x in range(1,10):
    y = 0
    while y < x :
        y = y + 1
        if x % 2 == 0:
            break
        else:
            print(x,'*',y,'=',x*y,' ',end=' ')
    
    else:
        print(end = '\n')