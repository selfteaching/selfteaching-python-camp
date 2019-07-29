p, q, operator = int(input("输入第一个数字p:")), int(input("输入第二个数字q:")), input("输入运算符：")
if operator == "+":
    print("{} + {} = {}".format(p, q, p+q))
elif operator == "-":
    print("{} - {} = {}".format(p, q, p-q))
elif operator == "*":
    print("{} * {} = {}".format(p, q, p*q))
elif operator == "/":
    print("{} / {} = {}".format(p, q, p/q))