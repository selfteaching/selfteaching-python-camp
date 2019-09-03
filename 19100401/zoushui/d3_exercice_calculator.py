#创建一个支持加减乘除的计算器
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
  print("选择运算:")
  print("1、加")
  print("2、减")
  print("3、乘")
  print("4、除")
  choise = input("输入你的选择（1/2/3/4):")
  num1 = int(input("输入第一个数字: "))
  num2 = int(input("输入第二个数字: "))
  if choise == '1':
     print(num1,"+",num2,"=",add(num1,num2))
  elif choise == '2':
     print(num1,"-",num2,"=", subtract(num1,num2)) 
  elif choise == '3':
     print(num1,"*",num2,"=", multiply(num1,num2))
  elif choise == '4':
     print(num1,"/",num2,"=", divide(num1,num2))
  else:
     print("你输入的有误，请重新输入")  
