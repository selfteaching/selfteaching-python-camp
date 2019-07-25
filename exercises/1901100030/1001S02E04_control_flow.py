# day4 流程控制练习
# 2019年7月6日
# 陈浩 学号 

print('打印九九乘法表：')
for n in range(1,10) :
    print('第%d行' %n, end='\t')
    for i in range(1,n+1):
        print(n,'*',i,'=',n*i, end='\t')
    print()

print('打印跳过偶数行的九九乘法表：')
for n in range(1,10) :
    if n%2 == 0:
        continue
    for i in range(1,n+1):
        print(n,'*',i,'=',n*i, end='\t')
    print()