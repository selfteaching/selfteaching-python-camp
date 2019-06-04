print('九九乘法表')
for i in range(1,10):  #####当i在1到9的范围
    for j in range(1,i+1): #####当j在1到i+1的范围
        print('{}*{}={}'.format(i,j,i*j),end='\t') ###按格式输出
    print('')

############################

print(' ') #空一行
print('九九乘法表去偶数')
i=1 #####用while判断 i为偶数时不计算
while i<=9: #i小于等于9且i不为偶数，j<=i
    j=1
    while j<=i:
        if i % 2 == 0:
            break
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j += 1
    i += 1
    print( )


     
    