print('九九乘法表\n')
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}'.format(i,j,i*j),end = '\t')
    print()


print('去偶数行的九九乘法表\n')    
i = 1
while i<=9:
    j = 1
    if i%2!=0:
        while j<=i: #and 
            print("{}*{}={}".format(i,j,i * j),end = "\t")
            j += 1    
    else:
        print()        
    i += 1
