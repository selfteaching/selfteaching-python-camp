
i = 1
while i < 10:
       j = 1
       while j < i + 1:
       	      if i%2 == 0:
                    break
              print(j,  '*', i, '=', i * j, sep='', end='\t')
              j += 1

       print()

