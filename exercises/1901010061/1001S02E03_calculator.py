def add(x, y):       #自定义一个相加add的函数，返回x+y的值。x、y是形参，没有具体的值。
   return x + y      #缩进字符是python强制语法规则。缩进用有来界定代码块的，相当于其他编程语言的括号。
def subtract(x, y):  #缩进方法（tab/4个空格）
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
 
choice = input("输入你的选择(1/2/3/4):")  #input输入，能让用户从电脑输入一些字符，读取变量。
                                         #choice批处理。input赋值给choice
num1 = int(input("输入第一个数字: "))     #int整数型转换。num1(nunber1)
num2 = int(input("输入第二个数字: "))
 
if choice == '1':                            #一个等号是赋值，二个等号是逻辑运算符中的相等于关系。
   print(num1,"+",num2,"=", add(num1,num2))  #if choice +elif choice +else 语句
                                             #如果choice=1,打印num1+num2=计算并返回num1+num2的值(调用add函数)
elif choice == '2':                          #当choice不等于1时，elif那么判断是否等于2，满足则执行事件2的操作
   print(num1,"-",num2,"=", subtract(num1,num2))
 
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
 
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("非法输入") #如果choice不等于1或2或3或4时，是else其他情况时，那么默认执行else后面的代码，打印非法输入。