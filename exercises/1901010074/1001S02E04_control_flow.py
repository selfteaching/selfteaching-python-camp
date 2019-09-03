for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print ("%d * %d = %2d"%(i,j,d), end='\t')


print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

i = 1
while i <  10:
    j = 1
    while j <= i:
        d=i*j;
        if (d%2) != 0:
            print('%d*%d=%2d   '% (i,j,d), end='\t') #end=‘’  表示不换行（系统默认输出完毕换行）
        j+=1
    i+=1


