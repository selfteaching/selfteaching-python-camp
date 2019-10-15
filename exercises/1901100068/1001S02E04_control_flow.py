print('九九乘法表')
for c in range(1,10):
    for d in range(1,c+1):
        print(c,'*',d,'=',c*d,end='    ')
    print()

print('去除偶数的九九乘法表')
c=1
while c<10:
    if c%2==0:
        print()
    else:
        for d in range (1,c+1):
            print(c,'*',d,'=',c*d,end='    ')
    c+=1