 #使用for循环打印九九乘法表
#for i in range(1,10):
 #   for j in range(1,i+1):
 #       print(i,"*",j,'=',i*j,end='\t')
 #  print()
    

i = 1
while i<10:  #当i小于10
  if i%2 == 0: #如果除2的余数为0:
     print()  #就换行
  else:  #否则就执行
     for j in range(1,i+1): #j是从1到i的数
        print(i,"*",j,'=',i*j,end='\t')    
  i+=1    
     