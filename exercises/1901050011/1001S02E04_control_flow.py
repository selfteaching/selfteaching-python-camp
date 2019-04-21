for i in range(1,10):
   for j in range(1,i+1):
      print(j, '*', i, '=', i*j,'\t',end='')
   print()        
print()


x=1
while x<10:
    if x%2==1:
       for y in range(1,x+1):
            print(y, '*', x, '=', x*y,'\t',end='')
      print()
     x=x+1
print() 
