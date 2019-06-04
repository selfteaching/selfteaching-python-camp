#这是我第三天的作业，制作一个计算器，会带有加减乘除功能，可以输入小数

#这里定义输入的值的运算规则，默认加减乘除都会运算，但是因为选择不同，只会输出相应的结果，比如选“1”，这时加减乘除的结果都算出来了，但是只会输出add（x,y）里的加法结果。
def add(x,y):#这里计算x加y并返回一个值
   return x + y
   
def sub(x,y):#这里计算x减y并返回一个值
   return x - y

def mul(x,y):#这里计算x乘y并返回一个值
   return x * y

def div(x,y):#这里计算x除y并返回一个值
   return x / y

#这里是输入和反馈的代码
choice = input("请选择需要的运算：加法输入1；减法输入2；乘法输入3；除法输入4:")#选择加减乘除

x = float(input("输入需要计算的第一个数字："))#输入第一个计算数字
y = float(input("输入需要计算的第二个数字："))#输入第二个计算数字

z1 = add(x,y)
z2 = sub(x,y)
z3 = mul(x,y)
z4 = div(x,y)

#这里对输入进行处理后选择输出
if choice == '1':
   print(x,"+",y,"=",z1)

elif choice == '2':
   print(x,"-",y,"=",z2)

elif choice == '3':
   print(x,"*",y,"=",z3)

elif choice == '4':
   print(x,"/",y,"=",z4)

else:
   print("亲亲，输错了，第一步请输1、2、3、4中的一个数")
