# use for...in
print("this is printing 9×9 multiplication table using for ... in......")
for i in range(10):         #外层循环，又表示行数
    for j in range(1,i+1):  #内层循环，由于range是左闭右开，所以这里的右边界为i+1
        if j < i:           #表示在同一行
            print(i,'*',j,'=',i*j,end='\t')     #此时用制表符结尾
        else:
            print(i,'*',j,'=',i*j,end='\n')     #该行结束时，换行，不写end='\n'，python也会自动换行

print('\n')
print('*'*150)
print('\n')

#use while
print("this is printing 9×9 multiplication table except even line using...... ")
x = 0                                               #为x赋值为0
while x < 9:                                        #判断条件，当x小于9时
    y=1                                             #每次从内循环跳出时，y的值都要置零
    x=x+1                                           #跳出内循环后，为x加一，进入下一行的计算
    while y <= x:                                   #开始内循环
        if x % 2 != 0:                              #判断是否是奇数行
            if y < x:                               #行内以制表符隔开
                  print(x,'*',y,'=',x*y,end='\t')   
                  y = y+1                           #最后要为y加一
            else:
                print(x,'*',y,'=',x*y,end='\n')     #该行结束时，换行
                y = y+1                             #同样，运行完之后y加一
        else:
            y=y+1                                   #偶数行，即使不打印也要y加一，从而进入下一个奇数行的循环
                
        
        
    
                