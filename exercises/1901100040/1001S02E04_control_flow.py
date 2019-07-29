#打印九九乘法表
for row in range(1,10):
    for col in range(1,row+1):
       print('%s*%s=%s' %(row,col,row*col),end='\t')
    print('')
#打印九九乘法表奇数行
row=1
while row<10:
    col=1
    while col<=row:
        if(row%2)==0:
           break
        else:
            print('%s*%s=%s' %(row,col,row*col),end='\t')
            col=col+1
    print('')
    row=row+1
