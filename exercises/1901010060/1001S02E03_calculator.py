def jia(a,b):
    return(a+b)
def jian(a,b):
    return(a-b)
def chen(a,b):
    return(a*b)
def chu(a,b):
    return(a/b)
num1 =int(input('请输入第一个数字：'))
num2 =int(input('请输入第二个数字：'))
fuhao=input('请选择运算符：1、相加   2、相减   3 、相乘   4、相除  :   ')

if fuhao =="1":
    print(num1,'+',num2,'=',jia(num1,num2))
elif fuhao =="2":
    print(num1, '-', num2, '=', jian(num1, num2))
elif fuhao =="3":
    print(num1, '*', num2, '=', chen(num1, num2))
elif fuhao =="4":
    print(num1, '/', num2, '=', chu(num1, num2))
else:
    print('错误输入')

