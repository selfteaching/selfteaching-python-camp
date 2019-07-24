# 用 for...in 打出九九乘法表
def multiply(x,y):return x*y
for i in range(1,10):
    
    for j in range(1,i+1):
        print(j,'*',i,'=',multiply(j,i),end = '\t')
    
    print('')

# 用 while 打出九九乘法表
def multiply(x,y):return x*y
i = 1
while i < 10:
    j = 1
    while j < i+1:
        print(j,'*',i,'=',multiply(j,i),end = '\t')
        j = j + 1
    print('')
    i = i + 1

# 用while打出奇数行的九九乘法表
def multiply(x,y):return x*y
i = 1
while i < 10:
    j = 1
    while i % 2 != 0 and j < i+1:
        print(j,'*',i,'=',multiply(j,i),end = '\t')
        j = j + 1
    print('')
    i = i + 1