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