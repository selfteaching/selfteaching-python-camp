print ('打印99乘法表')
for i in range(1,10):
       print('第%d行'%i,end='\t')
       for j in range(1,i+1):
               #print(i,'*',j,'=',i*j,end='\t')
               print ('{} * {} = {} '.format(i,j,i*j),end='\t')
       print()



print('打印奇数行乘法表','\n')
i=1
while i<10:
       if i%2 ==0:
              print()

       else:
        for j in range(1,i+1):
              print(i,'*',j,'=',i*j,end='\t')
       i+=1