# for 9*9 table
for i in range(1,10):
  for j in range(1,i+1):
    print('{}X{}={}\t'.format(i,j,i*j),end='')
print()

a=1
while 0<a<10:
    if a % 2==1:
        for j in range(1,a+1):
            print('{}X{}={}\t'.format(a,j,a*j),end='')
        print()
    a=a+1
    