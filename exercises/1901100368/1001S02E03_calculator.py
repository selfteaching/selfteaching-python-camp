#使⽤用 Python 编写一个支持 加、减、乘、除功能 的计算器，⽀持输⼊参数，⽀持输出结果

print("这是一个仅支持两个参数的计算器\n，请输入第一个参数！\n")

parment_a = input()

print("请选择输入你的运算符：1为+,2为-,3为*,4为/")

code_input = input()

print("请输入第二个参数！\n")

parment_b = input()


if int(code_input) == 1:
    result = int(parment_a) + int(parment_b)
elif int(code_input) == 2:
    result = int(parment_a) - int(parment_b)
elif int(code_input) == 3:
    result = int(parment_a) * int(parment_b)
else:
    result = int(parment_a) / int(parment_b)

print("结果是：" + str(result))