#简易计算器，支持两个数字间的加、减、乘、除。
#我不想只能计算整数，就用了float，但float的小数位有时候很迷，不是很理解。

print('欢迎使用python计算器！你想计算什么？' )
print('1.加法')
print('2.减法')
print('3.乘法')
print('4.除法')

def add(x, y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x,y):
    return x / y

choice = int(input('请输入序号 1/2/3/4:'))


if (choice>=1 and choice <=4):
    print('请分别输入两个数字')

    x = float(input('输入第一个数字：'))
    y = float(input('输入第二个数字：'))

    if choice == 1:
        print(x,'+',y,'=', add(x,y))

    elif choice == 2:
        print(x,'-',y,'=', substract(x,y))

    elif choice == 3:
        print(x,'*',y,'=', multiply(x,y))

    else:
        print(x,'/',y,'=', devide(x,y))

else:
    print('无效输入，请重试！')


