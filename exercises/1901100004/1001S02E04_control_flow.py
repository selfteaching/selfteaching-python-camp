#<<<<<<< master

print('打印九九乘法表')
for i in range(1, 10):
    print('第%d行'% i, end='\t')
    for j in range(1, i + 1):
        print(i, '*', i * j, end='\t')
    print()
    
    print('\n打印跳过偶数行的九九乘法表')
    i = 1
    while i < 10:
        if i % 2 == 0:
            print()
        else:
            for j in range(1, '*', i * j, end='\t')

        i += 1
#=======
print(str('九九乘法表'))
for i in range (1,10):
    # print('第%d行'% i,end = '\t')
    for j in range (1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end='\t')
    print()

print(str('去掉偶数行的九九乘法表'))
i = 1  #这是啥意思呀？把1赋值给i这个变量？这是干什么呢？
while i < 10:   #当i小于10的时候
    if i % 2 == 0: # 如果i除以2的余数为0
        print() #就换行
    else:  #否则就执行
        for j in range(1,i+1):  #j是从1到i的数
            print(i,'*',j,'=',i*j,end='\t')  #显示i*j=i*j 结尾用占位符隔开
    i += 1  #结尾又出现一遍，重新赋值了吗？搞不懂
#>>>>>>> master
