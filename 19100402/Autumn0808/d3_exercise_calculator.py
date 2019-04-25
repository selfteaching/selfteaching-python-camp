#两个数的四则运算
# 定义函数
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

#选择运算
print("请选择：加、减、乘、除")

#进行运算
choice = input("加/减/乘/除：")
a = int(input("输入第一个数字："))
b = int(input("输入第二个数字："))

if choice == "加":
    print(add(a,b))

elif choice == "减":
    print(sub(a,b))

elif choice == "乘":
    print(mul(a,b))

elif choice == "除":
    if b != 0:
        print(div(a,b))
    else:
        print("无效输入")

else:
    print("无效输入")







