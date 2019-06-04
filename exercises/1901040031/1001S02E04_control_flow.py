#for……in  
for i in range(1,10):
    for j in range(1,10):
        print(i,'*', j, '=' ,i*j, end='\t')
        if i == j :
            print("")
            break
       

#while循环

i = 1
while i < 10:
    j = 1
    while j < i+1:
        if i % 2 == 0:
            print()
            break
        else:
            print(i , '*', j ,'=', i*j, end='\t')
        j += 1
    i += 1


#while 循环
i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        if i % 2 >0:
            print(i,"*",j,"=",i*j,end='\t')
        if i==j:
            j =0
            print()
            break
         


        
