#第一步
i = 256 * 256
print('The value of i is', i)


#第二步
for t in range(1,10):
    print(t)
print('++++++++++++++++++++++++++++++')

for t in range(1,10):
    print( t,'*2''=',t*2)
print('++++++++++++++++++++++++++++++')






#第三步  99乘法表
for t in range(1,10):   
    for m in range(1,t+1):
        #print(t,'*',m,'='m*t)
        print(t,'*',m,'=',m*t,end='\t')    #在一个完整的循环内，end='\t'的作用是取消print默认输出时结尾自带的回车功能，使一个循环内的结果都显示在同一行
    
    print()                                #print()起到换行的作用，当完成一个循环内的所有参数计算后，在开启下一个循环之前，进行换行，另起一行显示。这样每一个循环各在一行显示
                                           #注意，第21行的print()函数和第17行的for循环具有相同的地位，因为它们的缩进是相同的
                                           #第二个for循环17，18，19的循环完成所有的range参数处理，此时结束循环才会执行21行的print()函数.没有完成第二个for循环就不会执行21行的print()





#第4步 while  去除偶数行
print()
a = 1
while a <10:
    if a %2 !=0:
        b = 1
        while a >= b:
            print(a,'*',b,'=',a*b,end='\t')
            b +=1
        print()    
    a +=1        

  




#第5步  99乘法表的无限循环输出
t =1
while t %2 !=0:
    for t in range(1,10):   
        for m in range(1,t+1):

        
            #print(t,'*',m,'='m*t)
            print(t,'*',m,'=',m*t,end='\t')    #在一个完整的循环内，end='\t'的作用是取消print默认输出时结尾自带的回车功能，使一个循环内的结果都显示在同一行
         
        print()                                 
