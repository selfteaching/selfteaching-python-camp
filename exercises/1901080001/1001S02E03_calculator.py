# 流程图：定义函数-输入数值-输入运算操作-输入数值-输出结果

# 定义加法、减法、乘法、除法的运算操作函数
def add( x, y):
    return x + y

def sub( x, y):
    return x - y

def multi( x, y):
    return x*y

def div( x, y):
    return x/y

num1 = input('请输入第一个数字:')
opt = input('请选择要进行的运算操作相关数字（1、加 2、减 3、乘 4、除）：')
num2 = input('请输入第第二个数字：')

opt = int(opt)
num1 = int(num1)
num2 = int(num2)
if opt == 1:
    print(add(num1, num2))
elif opt == 2:
    print(sub(num1, num2))
elif opt == 3:
    print(multi(num1, num2))
elif opt == 4:
    print(div(num1, num2))
else:
    print('你的输入有误，请重新输入:')




    


