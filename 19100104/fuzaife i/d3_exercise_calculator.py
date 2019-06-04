def add(num_a, y):  #加法运算
    return num_a + y

def subtract(num_a, y):   #减法运算
    return num_a - y

def multiply(num_a, y):   #乘法运算
    return num_a * y

def divide(num_a, y):  #除法运算
    return num_a / y

#用户输入
print('选择运算：')
print('1、相加')
print('2、相减')
print('3、相乘')
print('4、相除')

choice = input('输入你的选择（1/2/3/4):')

num_a = float(input('输入第一个数字：'))
y = float(input('输入第二个数字：'))

if choice == '1':
    print(num_a, '+', y, '=', add(num_a, y) )

elif choice == '2':
    print(num_a, '-', y, '=', subtract(num_a, y))

elif choice == '3':
    print(num_a, '*', y,'=', multiply(num_a, y) )

elif choice == '4':
    print(num_a, '/', y, '=', divide(num_a, y))

else :
    print('非法输入')
 