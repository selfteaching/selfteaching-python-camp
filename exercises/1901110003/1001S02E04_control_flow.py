#DAY4 控制流程 2019-08-04
#Task1：使⽤用for...in循环打印九九乘法表
for i in range (1,10):
    for j in range (1,10):
        print(i,"X",j,"=",i*j,"\t",end="")
        if i == j:
            print("")
            break
#Task2:使用while循环打印九九乘法表并⽤条件判断把偶数⾏去除掉
i = 1
while i < 10:  
   if i % 2 == 0:     
      print()
   else:
      for j in range(1,i+1): 
         print('{} * {} = {}'.format(i,j,i * j),end = '\t')         
   i += 1