p1_str = input("输入数值1")
p3_str = input("运算符")
p2_str = input("输入数值2")


p1 = float(p1_str)

p2 = float(p2_str)


if p3_str == '+':
     val = p1 + p2
elif p3_str == '*':
     val = p1 + p2
elif p3_str == '-':
     val = p1 - p2
elif p3_str == '/':
     val = p1 / p2
else:
    print('输入错误请重再试')

print("结果是",val)