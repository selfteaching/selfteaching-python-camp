for a in range(1,10):
  for b in range(1,a+1):
    print(a,'*',b,'=',a*b,end='\t')
    if a==b:
      print('\n')
      break

        
a=1 
b=1
while (a<=9):
  while (a%2 !=0):
   while(b<=a):
      print(a,'*',b,'=',a*b,end='\t')
      b=b+1
   else:
      print(end='\n')
   break
  a=a+1
  b=1
