
for i in range(1,10):
   
    for n in range(1,i+1):
        print(i,"*",n,"=",eval('n*i'),'',end="")
        
    
    print()



i = 1
while i <= 9:
    n = 1
    while n <= i:
        if i % 2 != 0:
            print(i,"*",n,"=",eval('n*i'),'',end="")
        n += 1
    i += 1
    if i % 2 == 0:print()
