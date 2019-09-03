'''
for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d*%d=%-2d'%(i,j,d),end = '\t' )
    print()
'''

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d"%(i,j,i*j),end = '\t')  # %d： 整数的占位符，'-2'代表靠左对齐，两个占位符
        j += 1
    if i == 0 :
    	i += 1
    else:
    	i += 2
    print()
 