def add(x,y):
    return x+y
"""相加"""
def subtract(x,y):
    return x-y
"""相减"""
def multiply(x,y):
    return x*y
"""相乘"""
def devide(x,y):
    return x/y
"""相除"""

#用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")1

choice=int(input("输入你的选择：1/2/3/4："))

num1=int(input("输入的第1个数字"))
num2=int(input("输入的第2个数字"))
print(type(choice),type(num1))
if choice ==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice==3:
    print1(num1,"*",num2,"=",multiply(num1,num2))
elif choice ==4:
    print(num1,"/",num2,"=",devide(num1,num2)) 
else:
    print("非法输入")