#Selteaching day3 homework which creat a calculater!
# Way1:Use "def" to create new functions

#1.加法
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

#2.减法
def sub(x, y):
    print("x is {} and y is {}".format(x, y))
    return x-y # Return values with a return statement


#3.乘法
def mul(x, y):
    print("x is {} and y is {}".format(x, y))
    return x*y  # Return values with a return statement

#4.除法
def div(x, y):
    print("x is {} and y is {}".format(x, y))
    return x/y # Return values with a return statement

#  Way2：call lambda

#1.加法
add1 = lambda x, y: x + y

#2.减法
sub1 = lambda x, y: x - y

#3.乘法
mul1 = lambda x, y: x*y

#4.除法
div1 = lambda x, y: x/y

# 功能启用
print("计算器功能列表")
print("1.加法","2.减法","3.乘法","4.除法",sep="***",end='\n')

choice = input("(1/*/2/*/3/*/4)请输入对应功能序号:")
n1 = input("请输入第一个数字:")
n2 = input("请输入第二个数字:")

if choice == '1':
    print(n1,"+",n2,"=",add1(n1,n2))

elif choice == '2':
    print(n1,"-",n2,"=",sub1(n1,n2))

elif choice == '3':
    print(n1,"*",n2,"=",mul1(n1,n2))

elif choice == '4':
    print(n1,"/",n2,"=",div1(n1,n2))
else:
    print("输入错误，请重试")
pass
