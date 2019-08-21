print('**打印九九乘法表**')
for i in range(1,10): 
    for j in range (1,i+1):
        print(f'{i}*{j}=',j*i,end='\t')
    print()
print('+++打印九九乘法表，偶数行+++')
n=1
while n<10:
    if n%2==1:
        m=1
        while m<n+1:
            print(f'{n}*{m}=',n*m,end='\t')
            m+=1
        print()
    n+=1
    print()
