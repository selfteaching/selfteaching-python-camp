def cal():
    print("我的个人计算器")
    numA=float(input("第一个参数:"))
    op=input("(操作符):")
    if op=="+":
        numB=float(input("第二个参数:"))
        print("结果为",numA+numB)
    elif op=="-":
        numB=float(input("第二个参数:"))
        print("结果为",numA-numB)
    elif op=="*":
        numB=float(input("第二个参数:"))
        print("结果为",numA*numB)
    elif op=="/":
        numB=float(input("第二个参数:"))
        print("结果为",numA/numB)

cal()

