print('打印九九乘法表')
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='\t')
    print()
    print()
print('打印奇数行的乘法表')
x=1
while x<10:
    if x%2==0:
        print()
        print()
    else:
        for y in range(1,x+1):
            print(x,'*',y,'=',x*y,end='\t')
    x=x+1