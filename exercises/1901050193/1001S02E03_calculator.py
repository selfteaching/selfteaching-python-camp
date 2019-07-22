def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("请输入数字1")
num1=int(input(""))

print("请选择运算符:\n1.+\n2.-\n3.*\n4./")
choice=input("")

print("请输入数字2")
num2=int(input(""))

if choice=="+":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="-":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="*":
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice=="/"and num2!=0:
    print(num1,"*",num2,"=",div(num1,num2))
else:
    print("Error")