for i in range(1, 10): 
     # print(i)
    for j in range(1, i+1):
        print('%s*%s=%s '%(i,j,i*j),end = '')
    print()
 

i = 1
while i <= 9:
    j = 1
    while j <=i:
        if i % 2 ==0:
            break
        print('{}x{}={}'.format(i,j,i*j),end = ' ')
        j += 1
    i += 1
    print()
