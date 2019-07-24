print('\n九九乘法表\n')

#这是从unscientific的作业那里抄过来的，
# range(1,10)生成了一个从1开始到9的数字序列。本来是从0 到9 的，因为写成了range（1,10）所以就从1开始了。
# 定义y 的范围为1-x+1，因为X 最大只能是到9 ，而y 最后也就是range（1,10）.
# print('{}x{}={}'.format(x, y, x * y), end='\t')，可以换成print('%d * %d = %d' %(x,y,x*y), end='\t')
# 12行的print()就是在完成y这个循环后，换行的作用

for x in range(1, 10):
    for y in range(1, x + 1):
        print('{}x{}={}'.format(x, y, x * y), end='\t')
    print()

print('\n')  # 这三行是做了个分割线
print('-' * 50, '分割线', '-' * 50)

print('\n去除偶数行的乘法表\n')
x = 1
while x <= 9: # 在行数为1-9中
    y = 1
    while y <= x: #在列数小于等于行数的时候。如果没有这个条件的话，
        if x % 2 == 0: #如果x除以2没有余数的话，就中断，靠这两句把x中的2,4,6,8干掉了
            break
        print('{}x{}={}'.format(x,y,x*y),end = '\t')
        y += 1
    x += 1
    print()
print('-' * 50, '分割线', '-' * 50)

print('\n试验\n')
for x in range(1, 10): # 在行数为1-9中
    #y = 1
    #while y <= x: #在列数小于等于行数的时候。如果没有这个条件的话，
    if x % 2 == 0:
        break
    y = x
    print('{}x{}={}'.format(x,y,x*y),end = '\t')
        #y += 1
    x += 1
    print()
