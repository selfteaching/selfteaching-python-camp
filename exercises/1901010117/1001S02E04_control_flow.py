print('打印九九乘法表')     
for a in range(1,10):    
    for b in range(1,a+1):   
            print(a,  '*', b, '=', a * b, sep='', end='  ')   
    print()             






print('打印九九乘法表并去出偶数行')
a = 1       
while a <= 9:      
     if a % 2 != 0:     
          b = 1     
          while b < a + 1:      
              print(a, "*", b, '=',a*b, sep='', end='  ')       
              b += 1        
          print()       
     a += 1     