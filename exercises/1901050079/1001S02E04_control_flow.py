for a in range(1,10):
    for b in range(1,a+1):
        print('{}*{}={}'.format(a,b,a*b),end='\t')
    print()
print('偶数行去掉后')
x=1
while x<=9:
    y=1
    while y<=x and x%2>0:
        print('{}*{}={}'.format(x,y,x*y),end='\t')
        y+=1
    print()
    x+=1