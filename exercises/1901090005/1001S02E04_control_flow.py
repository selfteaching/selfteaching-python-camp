for i in range(1,10):
    for j in range(1,10):
        if j >i:
            print(end='\t')
        else:
            print(j,'*',i,'=',i*j,end='\t')
        if j == 9:
            print('\t')

i = 1
while i < 10:
  j = 1
  while j <= i:
    print('%d*%d=%d\t' %(i, j, i*j) , end=(''))
    j +=1
  print('')
  i +=2
print('')