#简易加减乘除计算器程序
#定义加法函数
def add(x,y):
    return x+y
#定义减法函数
def subtract(x,y):
    return x-y
#定义乘法函数  
def multiply(x,y):
    return x*y
#定义除法函数
def divide(x,y):
    return x/y
#定义执行方式，当执行脚本本身，执行如下代码
if __name__ == '__main__':               
 
  num1 = int(input("输入第一个数字: "))
  choise = print("输入你的选择\n+\n-\n*\n/")
  c=input('')
  num2 = int(input("输入第二个数字: "))
  if c == '+':
     print(num1,"+",num2,"=",add(num1,num2))
  elif c == '-':
     print(num1,"-",num2,"=", subtract(num1,num2)) 
  elif c == '*':
     print(num1,"*",num2,"=", multiply(num1,num2))
  elif c == '/':
     print(num1,"/",num2,"=", divide(num1,num2))
  else:
     print("你输入的有误，请重新输入")
