print('九九乘法表')
for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a*b,end='\t')
    print()

print('去掉偶数的九九乘法表')
a=1
while a<10:
    if a%2==0:
        print()
    else:
        for b in range (1,a+1):
            print(a,'*',b,'=',a*b,end='\t')
    a+=1