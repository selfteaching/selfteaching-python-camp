print('day4用in...for循环打印九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end=('     '))
        if i==j:
            print()
print('while语句打印去偶数行的九九乘法表')
i=0
j=0
while i<9:
    i+=1
    if i%2==0:
        continue
    while j<9:
        j+=1
        print(i,'*',j,'=',i*j,end=('   '))
        if i==j:
            j=0
            print("")
            break