#谷歌到的程序代码还是跟想象中的不一样，没有生活中遇到的计算器灵活方便（这也是我对以下代码的理解，不确定是否理解正确）：
       搜索到的程序并不能直接输入数字，再按顺序输入运算符号（加减乘除），再输入数字，最后产生结果，
       不知道能不能有更好的代码？我想一定有，只是我现在还不会编写，第一次写这个代码，我都是搜索，抄写的，暂且先就这样吧？
#定义加法运算
def add(x,y):
     return x+y

#定义减法运算
def add (x,y):
    return x-y

#定义乘法运算
def multiply(x,y)
    return x*y

#定义除法运算
def divide(x,y)
    return x/y

#输入数字1、2、3、4，选择要执行哪种运算
choice = input("请选择需要的运算：加法输入1；减法输入2；乘法输入3；除法输入4：")

x = float(input("请输入要计算的第一个数字：“))

y = float(input（”输入要计算的第二个数字：“)）

z1 = add(x,y)
z2 = sub(x,y)
z3 = mul(x,y)
z4 = div(x,y)

#下一步对输入的数字或命令进行处理后选择输出
if choice == '1':
   print(x,"+",y,"=",z1)

   elif choice == '2':
        print(x,"-",y,"=",z2)
    
elif choice =='3':
     print(x,"*",y,"=",z3)

elif choice =='4':
     print(x,"/",y,"=",z4)

else:
    print("输入错误，请首先输入数字1、2、3、4以确定对应的加、减、乘、除运算)