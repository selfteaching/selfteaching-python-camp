def add(x,y): # 定义函数
    return x+y
def subtract(x,y):
    return x-y
def mutiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print('请选择运算：') # 整体思路是先确定运算方法，再确定加减乘除连接的两个数字
print('1.加法')
print('2.减法')
print('3.乘法')
print('4.除法')
choice=input('输入你的选择（1/2/3/4）：') # 输入用input('')
num1=int(input('输入第一个数字：')) # 将输入的内容整数化
num2=int(input('输入第二个数字：'))
if  choice=='1': # 每句记得以:结尾
    print(num1,"+",num2,"=",add(num1,num2)) #变量无需引号，字符才需要
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",mutiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print('输入不支持')
