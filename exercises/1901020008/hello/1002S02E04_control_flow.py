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