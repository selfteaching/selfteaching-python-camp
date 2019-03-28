# 定义函数
def add(x,y):return x+y
def abstract (x,y):return x-y
def multiply (x,y):return x*y
def divide (x,y):return x/y

# 用户输入
for    print("""
       请输入您需要执行的运算：
        1：加法
        2：减法
        3：乘法
        4：除法
        """)
# 运行计算
        choice = input("请输入您需要执行的运算(1/2/3/4)：")
        num1 = int(input("第一个数字:"))
        num2 = int(input("第二个数字:"))
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice == '2':
             print(num1,"-",num2,"=",abstract(num1,num2))

        elif choice == '3':
             print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice == '4':
             print(num1,"/",num2,"=",divide(num1,num2))

            else :
            print("输入错误")
        