for i in range(1,10,2):       #i是一个临时变量   range(1,10)从1打印到10 
    for j in range(1,10):   #j是一个临时变量   range(1,10)从1打印到10 
        print(j,"x",i,"=",i*j,"\t",end="") #i和j相乘  end是空行
        if i==j:  #换行
            print("")
            break



i = 1  #第一个计数器
while i <10:
    j = 1#第二个计数器
    while j <= i:
        print('%dx%d=%d\t' %(j, i, i*j) , end=(''))
        j +=1
    print('') #换行
    i +=1
print('')#输出换行  
    