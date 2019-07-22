#day4 homework which is flow control running 99 mul
#way 1 使用for...in循环打印出九九乘法表
print('**打印九九乘法表**')
for i in range(1,10):   
  for n in range(1,i+1）:#i+!,确保能取到i值
      print(f'{i}* n}=',n*i,end='\t')
  print(）#完成一个i次的循环，换行

#way 1 使用for...in循环打印出九九乘法表,把偶数行去掉
print('**×打印九九乘法表,奇数行×**')
for x in range(1,10,2):
    for m in range(1,x+1):
        print(f'{x}*{m}=',m*x,end='\t')
    print()
 
 # way 1 使用for...in循环打印出九九乘法表，把奇数行去掉
print('**打印九九乘法表,偶数行**')
for x in range(2,10,2):
    for m in range(1,x+1):
        print(f'{x}*{m}=',m*x,end='\t')
    print()
    
 # way 1 使用for...in循环打印出九九乘法表，把偶数列去掉
print('**×打印九九乘法表,奇数列×**')
for x in range(1,10):
    for m in range(1,x+1,2):
        print(f'{x}*{m}=',m*x,end='\t')
    print()
    
 # way 1 使用for...in循环打印出九九乘法表，把偶数行和列去掉 
print('**×打印九九乘法表,奇数行和列×**')
for x in range(1,10,2):
    for m in range(1,x+1,2):
        print(f'{x}*{m}=',m*x,end='\t')
    print()

#way 2 使用while循环打印九九乘法表
print('+++ 打印九九乘法表+++ ')   
n = 1 #定义变量n
while n < 10:  #判断条件
    m= 1  #定义变量m
    while m < n+1:  
          print(f'{n}*{m}=',n*m,end="\t") #打印结果
          m+= 1
    n += 1
    print()
           
#way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,奇数行+++ ')

n = 1 #定义变量n
while n < 10:  #判断条件
    if n % 2==0: #判断n是否是偶数，是偶数则加1
        n += 1
    m= 1  #定义变量m
    while m < n+1:  #判断m小于n
        print(f'{n}*{m}=',n*m,end="\t") #打印结果
        m+= 1
    n += 1
    print()

#way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,奇数行+++ ')    
n = 1 #定义变量n
while n < 10:  #判断条件
    if n % 2!=0: #判断n是否是奇数
        m= 1  #定义变量m
        while m < n+1:  #判断m小于n
            print(f'{n}*{m}=',n*m,end="\t") #打印结果
            m+= 1 # 完成1-->n+1循环
        #print()
    n += 1
    print() #打印留下偶数空行
 
#way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,偶数行+++ ')    
n = 1 #定义变量n
while n < 10:  #判断条件
    if n % 2==0: #判断n是否是偶数
        m= 1  #定义变量m
        while m < n+1:  #判断m小于n
            print(f'{n}*{m}=',n*m,end="\t") #打印结果
            m+= 1 # 完成1-->n+1循环
        #print()
    n += 1
    print() #打印留下奇数空行 

#way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,偶数行和列+++ ')         
n = 1 #定义变量n
while n < 10:  #判断条件
    if n % 2==0: #判断n是否是偶数
        m= 1  #定义变量m
        while m < n+1:  #判断m小于n
            if m % 2==0: #判断n是否是偶数
                #break
                 print(f'{n}*{m}=',n*m,end="\t")  #打印结果
            #print()
            m+= 1 # 完成1-->n+1循环
            #print()
    n += 1
    print() #打印留下奇数空行

        #way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,奇数行和列u+++ ')         

n = 1 #定义变量
while n < 10:  #判断条件
    if n % 2!=0: #判断n是否是奇数
        m= 1  #定义变量m
        while m < n+1:  #判断m小于n
            if m % 2!=0: #判断n是否是奇数
                #break
                 print(f'{n}*{m}=',n*m,end="\t")  #打印结果
            #print()
            m+= 1 # 完成1-->n+1循环
            #print()
    n += 1
    print() #打印留下偶数空行        

    