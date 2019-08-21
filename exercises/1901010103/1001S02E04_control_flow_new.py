print("welcome to 9*9 tables:")
# loop in 9*9 tables
for a in range(1,10): # 指定a的范围是1到9
    for b in range(1,a+1):#指定b的范围是1到a+1, 起点是1,止点是:如果a是1,b就是a+1=2
        print('{}*{}={}\t'.format(b,a,a*b), end='')# 输出形态是用format定义为a*b,用end来自动回车
    print()

#########过滤偶数########
print("welcome to 9*9 tables without even number:")
a=1 #行的数值控制起始是1
while a<=9: # 当1~9的时候循环以下
    b = 1#列控制点是1
    while b<=a:#而当1<=1的时候,输出a*b
        if a % 2 == 0: # 过滤偶数,当行控制里出现余数,则输出结果
            break
        print('{}*{}={}\t'.format(a,b,a*b), end='')
        b=b+1 # b函数每次加1
    print(' ')
    a+=1 # a函数最后加1