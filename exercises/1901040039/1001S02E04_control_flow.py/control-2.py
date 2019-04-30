i=1
while i<=9 :
  print()
  if i % 2 == 0:
    j = 1
    while j<=i:
      print("%d*%d=%2d"%(j,i,i*j),end=" ")
      j+=1
    i+=1
else:
        print(' ')