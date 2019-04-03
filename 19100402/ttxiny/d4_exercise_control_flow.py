print('task1:\n')    
a=1
b=1
for b in range(1,10):
    for a in range (1, b+1):
      c=a*b
      print(a,'*',b,'=',c,end=' ')
      if b==a:
         print('\n')
      a=a+1
      
print('task2:\n')
a=1
while a<10:
     b=1
     while b<=a:
        print(a,'*',b,'=',a*b,end=' ')
        b=b+1
     print('\n')
     a=a+2
    
