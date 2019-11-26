print('打印乘法口诀表：')
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='\t')
    print('\n')

print('打印偶数行')
i = 1
while i <= 9:
    if i % 2 == 0:
        print()
    else:
        for j in range(1, i+1):
            print(i,'*',j,'=',i*j ,end='\t')
    i +=1

'''
练习过程与收获
    1. print的用法。给的参考资料并没有给出类似输出示例代码，看完还是不会用,看的参考视频，解决的问题。
    2. 另一种输出方法  print('{}*{}={}'.format(i,j,i*j),end='\t')
    3. while的用法
    4. 语法格式上与C有不同，需要练习熟练。
'''