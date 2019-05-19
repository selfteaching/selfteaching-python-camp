for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end = ' ')
    print()



f = 1
while f <= 9:
     h = 1
     while h < f + 1:
          if f%2==0:
               break

          print(f, "*", h, '=', f*h, sep='', end='\t')

          h += 1
     print()
     f += 1