for i in range(9):
    i+=1
    for r in range(1,i+1):
        print(f'{i}*{r}={i*r}',end='  ')
    print('  ')
print('.....................以下是第二道题..............................')
a=0
while a<10:
    a+=1
    if a % 2==0:
        continue
    for b in range(1,a+1):
        print(f'{a}*{b}={a*b}',end=('  '))
    print('   ')