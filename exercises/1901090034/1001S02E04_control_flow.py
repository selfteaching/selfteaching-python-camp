
print('打印九九乘法表')
for i in range(1,10):
    print('第%d行'%i,end='\t')
    for j in range(1,i+1):

        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print()

print('\n\n打印奇数行九九乘法表')

i=1
while i<10:
    if i%2==0:
        print('跳过第%d行'%i)
    else:
        print('第%d行'%i,end='\t')
        for j in range(1,i+1):
            
            print('{}*{}={}'.format(i,j,i*j),end='\t')
        print() 
    i+=1