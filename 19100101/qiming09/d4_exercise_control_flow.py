# this is day 4 exercise, control flow
# date: 2019.3.21
# author by : qiming

# task1：使用for…in循环打印九九乘法表

# 设计思路：
#  1. 九九乘法表抽象数学公式为：a*b=c.
#  2. a、b初始值均为1.
#  3. 当b<=a条件时，a值不变，b值循环+1，打印输出a*b=c.
#  4. 当b>a条件时，b值循环+1结束，a值+1,继续循环步骤3.
#  5. 当a=9且b=9时，结束循环。

# 程序实现：
# 初始化变量赋值
print('this is task 1:')
a=1
b=1
# 循环条件判断和输出
for a in range(1,10):
    for b in range(1,a+1):
        if b < a :
            print(a,'*',b,'=',a*b,end='\t')
            b=b+1
        elif b == a :
            print(a,'*',b,'=',a*b)
        else:
            break
    a=a+1
# 任务1结束，打印空行
print()

# task2: 使用while循环打印九九乘法表并用条件判断把偶数行除掉

# 设计思路：
#  1. while循环与for…in循环实现逻辑相同.
#  2. 使用条件判断，只打印m为奇数行.
#  3. 当m为偶数行时，跳出循环，m值+1.

# 程序实现：
# 初始化变量赋值
print('this is task2:')
m = 1
# while循环和输出
while m < 10 :
    if m % 2 != 0 :
        n = 1
        while n < m+1 :
            if n < m :
                print(m,'*',n,'=',m*n,end='\t')
                n=n+1
            elif n == m :
                print(m,'*',n,'=',m*n)
                break
            else:
                break
        m = m+1
    else:
        m = m+1
# 结束语.
print()
print('The End. Thank you.')
print()

