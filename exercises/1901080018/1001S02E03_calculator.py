def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("选择运算：")
print("1、加")
print("2、减")
print("3、乘")
print("3、除")

c=input("请输入你的选择（1/2/3/4）:")

n1=int(input("输入第一个数："))
n2=int(input("输入第二个数："))
if c == '1':
    print(n1,"+",n2,"=",add(n1,n2))
elif c=='2':
    print(n1,"-",n2,"=",subtract(n1,n2))
elif c=='3':
    print(n1,"*",n2,"=",multiply(n1,n2))
elif c=='4':
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("非法输入")