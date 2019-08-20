L=[1,2,3,4,5,6,7,8,9]
M=[1,2,3,4,5,6,7,8,9]
for x in L:
    while x%2==0: 
        break
    for y in M:
        print(x,'*',y,'=',x*y,'\t',end="")    
        if x==y:
            print('')
            break
