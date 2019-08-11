#加减乘除计算器，支持输入参数，支持输出结果
A=input("输入数字number1:")
A=float(A)
B=input("输入数字number2:")
B=float(B)
C=input("选择想要进行的运算:\n+\n-\n*\n/\n")
if C=="+":
    print(A+B)
elif C=="-":
    print(A-B)
elif C=="*":
    print(A*B)
elif C=="/":
    print(A/B)
