def add(x, y):  #加法运算
    return x + y

def subtract(x, y):   #减法运算
    return x - y

def multiply(x, y):   #乘法运算
    return x * y

def divide(x, y):  #除法运算
    return x / y

#用户输入
print('选择运算：')
print('1、相加')
print('2、相减')
print('3、相乘')
print('4、相除')

choice = input('输入你的选择（1/2/3/4):')

x = int(input('输入第一个数字：'))
y = int(input('输入第二个数字：'))

if choice == '1':
    print(x, '+', y, '=', add(x, y) )

elif choice == '2':
    print(x, '-', y, '=', subtract(x, y))

elif choice == '3':
    print(x, '*', y,'=', multiply(x, y) )

elif choice == '4':
    print(x, '/', y, '=', divide(x, y))

else :
    print('非法输入')
