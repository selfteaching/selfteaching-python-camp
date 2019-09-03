num1 = input("输入一个数：")
num1 = num1.strip()
num1 = float(num1)
yunsuanfu = input("输入运算符：")
yunsuanfu = yunsuanfu.strip()
num2 = input("输入另外一个数：")
num2 = num2.strip()
num2 = float(num2)

if yunsuanfu == '+':
        num3 = num1 + num2
        print("结果是：",num3)

elif yunsuanfu == "-":
        num3 = num1 - num2
        print("结果是：",num3)

elif yunsuanfu == "*":
        num3 = num1 * num2
        print("结果是：",num3)

elif yunsuanfu == "/":
        num3 = num1 / num2
        print("结果是：",num3)
    
else:
        print("输入有误！")
