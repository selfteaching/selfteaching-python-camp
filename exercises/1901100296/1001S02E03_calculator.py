x=0
while x<1:
    try:
        value=input("请输入计算：")
        print("计算结果是：",eval(value))
    except (BaseException):
        x=2
        print("输入有误！")
    