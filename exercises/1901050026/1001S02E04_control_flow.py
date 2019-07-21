
for x in range(1,10): 
    print() 
    for y in range(1,x+1): 
        print(x,'x',y,'=' ,y*x,sep='',end='\t')
    print()  


print("------------------------------")

i = 1
while i <= 9:
    j = 1
    while j <= i and i%2!=0:
        print("%d*%d=%-2d"%(i,j,i*j),end = ' ')  
        j += 1
    print()
    i += 1
