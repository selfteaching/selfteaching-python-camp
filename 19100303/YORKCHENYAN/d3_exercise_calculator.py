# 第三天作业：简单计算器
 
caculation = input("这是一个简单的计算程序，请输入要进行的运算，加法，减法，乘法，除法: ")

number_1 = int(input("请输入第一个数字: "))

number_2 = int(input("请输入第二个数字: "))


if caculation == "加法":

    print("两者相加的结果是：" )
    print(number_1 + number_2)

elif caculation == "减法":

    print("两者相减的结果是：" )
    print(number_1 - number_2)

elif caculation == "乘法":

    print("两者相乘的结果是：" )
    print(number_1 * number_2)

elif caculation == "除法":

    print("两者相除的结果是：" )
    print(number_1 / number_2)

else:

    print("输入有误")