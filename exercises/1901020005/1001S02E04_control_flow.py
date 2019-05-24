#使用for…in循环打印九九乘法表

print('打印完整的九九乘法表')
for i in range(1,10):
    print('%s'%i,end = '\t')
    for j in range(1,i+1):
        print('%s * %s = %s' %(i,j,i*j),end = '\t')
    print()

print('\n打印跳过偶数行的九九乘法表')
i = 1
while i < 10:  
   if i % 2 == 0:     
      print()
   else:
      for j in range(1,i+1): 
         print('{} * {} = {}'.format(i,j,i * j),end = '\t')         
   i += 1
