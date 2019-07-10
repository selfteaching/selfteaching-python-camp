# 简易计算器
a = int(input("请输入第一个数字: "))
b = int(input("请输入第二个数字: "))
c = input("请选择计算类别: A +、B -、C *、D / ")
if c == "A":
    print("a + b = "+str(a + b))
elif c == "B":
    print("a - b = "+str(a - b))
elif c == "C":
    print("a * b = "+str(a * b))
elif c == "D":
    print("a / b = "+str(a / b))
else:
    print("运算符错误")   
