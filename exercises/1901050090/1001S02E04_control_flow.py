for i in range(1, 10):
   var1=''
   for j in range(1,i+1): 
     var1= var1+str(i)+'*'+str(j)+'='+str(i*j)+'   '
     if j==i:
       print(var1)

print('\n')
a=1
while(a<10):
  b=1
  var2=''
  while (b<=a):
    var2= var2+str(a)+'*'+str(b)+'='+str(a*b)+'   '
    if(b==a and a%2>0):
      print(var2)
    b=b+1
  a=a+1
     
