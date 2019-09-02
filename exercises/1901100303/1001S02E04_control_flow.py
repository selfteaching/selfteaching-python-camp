
for col in range(1,10):
    for row in range(1,col+1):
        print(str(col),"*",str(row),'=',row*col,' ',end='')
    print()





r=1
while r<=9:
    c=1
    while c<=r and (r%2!=0):
        print(str(r),"*",str(c),"=",c*r,' ',end='')
        c=c+1
    print()
    r=r+1    
    