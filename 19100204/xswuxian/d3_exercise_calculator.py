#这是一个简易计算器程序
#定义一个函数，接收用户输入的三个变量，分别为数值1，运算符，数值2
def calculator(a,b,c):
    if b=="+":
        return int(a)+int(c)
    if b=="-":
        return int(a)-int(c)
    if b=="*":
        return int(a)*int(c)
    if b=="/":
        return int(a)/int(c)
#输入运算式
d1=input("请输入第一个数:") #把用户的输入赋值给d1
d2=input("请输入运算符:")   #把用户的输入赋值给d2
d3=input("请输入第二个数:") #把用户的输入赋值给d3
print(d1,d2,d3,"=",calculator(d1,d2,d3)) #把d1,d2,d3代入calculator函数计算打印出结果