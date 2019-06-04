#编辑一个简单的加减乘除计算器
choice =int(input("请选择运算:\n1,相加\n2,相减\n3,相乘\n4,相除\n请输入运算(1/2/3/4):"))
num1 = float(input("请输入第一个5数:"))
num2 = float(input("请输入第二个数:"))
if choice ==1:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif choice ==2:
    print("{}-{}={}".format(num1,num2,num1-num2))
elif choice ==3:
    print("{}x{}={}".format(num1,num2,num1*num2))
elif choice ==4:
    print("{}/{}={}".format(num1,num2,num1/num2))