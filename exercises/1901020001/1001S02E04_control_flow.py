#用for...in循环打印九九乘法表@
for a in range(1,10):   
    for b in range(1,a+1): 
            print(a, '*', b, '=', a * b, sep='', end='  ')   
    print()              
#用while循环打印九九乘法表且把偶数行去掉
i = 1      
while i <= 9:
    j = 1
    while j < i + 1:
        if i%2==0:
             break

        print(i, "*", j, '=', i*j , sep='', end='') 
        
        j += 1
    print()
    i += 1

i = 1      
while i <= 9:
    j = 1
    while j < i + 1:
        if i%1==0:
             break
        
        print(i, "*", j, '=', i*j, sep='', end='') 
        
        j += 1
    print()
    i += 1  
