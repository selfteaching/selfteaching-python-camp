#day4 homework which is flow control running 99 mul
#way 1 使用for...in循环打印出九九乘法表
print('**打印九九乘法表**')
for i in range(1,10):   
  for n in range(1,i+1):
      print(f'{i} * {n} =',n*i,end='\t')
  print()

#way 1 使用for...in循环打印出九九乘法表,把偶数行去掉
print('**×打印九九乘法表,奇数行×**')
for x in range(1,10,2):
    for m in range(1,x+1):
        print(f'{x} * {m} =',m*x,end='\t')
    print()
 
 # way 1 使用for...in循环打印出九九乘法表，把奇数行去掉
print('**打印九九乘法表,偶数行**')
for x in range(2,10,2):
    for m in range(1,x+1):
        print(f'{x} * {m} =',m*x,end='\t')
    print()

#way 2 使用while循环打印九九乘法表并用条件判断把偶数行去掉
print('+++ 打印九九乘法表,奇数行+++ ')

n = 1 #定义变量i
while n < 10:  #判断条件
    if n % 2==0: #判断n是否是偶数，是偶数则加1
        n += 1
    m= 1  #定义变量j
    while m < n+1:  #判断m小于i
        print(f'{n} * {m}= ',n*m,end="\t") #打印结果
        m+= 1
    n += 1
    print()
    