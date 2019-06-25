print('九九乘法表')
for a in range(1,10):
    for  b in range(1,10):
      print(a,'*',b,'=',a*b,"\t",end="")
      if a==b:
          print("")
          break 
print('九九乘法表(去除偶数行)')    
print(end='\n')
n = 1
while n <= 9 : 
    if (n % 2 !=0):
        i = 1
        while i <= n :
            if (i % 2 !=0 ):
                print ("%d * %d = %d" %(n,i,n*i),end='\t')
            i = i + 1
        print('\n',end='') 
    n = n+1  