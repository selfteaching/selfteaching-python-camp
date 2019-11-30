print('九九乘法表一:')
for a in range(1,10):
    for b in range(1,a+1):
        print('%s*%s=%s'%(a,b,a*b),end=' ')
    print()

print( '九九乘法表二:')
a=1
while a<10:
    if a % 2 !=0:
        for b in range(1,a+1):
            print('%s*%s=%s'%(a,b,a*b),end=' ')
        print()
        a += 2