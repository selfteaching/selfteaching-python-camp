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
b=1
for b in range(1,10):
    for a in range (1, b+1):
      c=a*b
      if b%2==0:
        a=a+1
        break   
      else:
        print(a,'*',b,'=',c,end=' ')
        if b==a:
          print('\n')
      a=a+1
