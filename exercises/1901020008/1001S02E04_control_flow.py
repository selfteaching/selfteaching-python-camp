for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end = ' ')
    print()



i = 1
while i <= 9:
     j = 1
     while j < i + 1:
          if i%2==0:
               break

          print(i, "*", j, '=', i*j, sep='', end=' ')

          j += 1
     print()
     i += 1

i = 1
while i <= 9:
     j = 1
     while j < i + 1:
          if i%1==0:
               break

          print(i, "*", j, '=', i*j, sep='', end=' ')

          j += 1
     print()
     i += 1
