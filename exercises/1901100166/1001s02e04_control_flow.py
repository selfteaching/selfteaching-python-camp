
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

# 用for in 打印九九乘法口诀表
for a in range(1,10):
        for b in range(1,a+1):
               print(a,'*',b,'=',a*b,end="\t")
        print()        
                  
  
print()
 
# 用While 打印九九乘法表并用条件判断把偶数⾏行行去除掉
a=1
while a<10:
    if a%2>0:
        b=1
        while b<a+1:
            print(a,'*',b,'=',a*b,end="\t")
            b+=1       
        print()    
    a+=1 