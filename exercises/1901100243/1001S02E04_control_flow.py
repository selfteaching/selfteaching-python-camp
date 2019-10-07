for i in range(1,10):
    for j in range(1,i+1):
        print ('{}*{}={}'.format(j, i, i*j),end="\t")
    print()

i = 1
j = 1
while i < 10:
    if i == 2 or i == 4 or i == 6 or i == 8:
        i += 1
        continue
        
    for j in range(1,i+1):
        print ('{}*{}={}'.format(i, j, i*j),end="\t") 
    
    print()
    i += 1
    
   
    
