operator = input("请输入需要进行的运算（加，减，乘，除）：")
number_one = float(input("请输入第一个参数："))
number_two = float(input("请输入第二个参数："))
if operator == "加":
    a = number_one + number_two
    print(a)
if operator == "减":
    b = number_one - number_two
    print(b)
if operator == "乘":
    c = number_one * number_two
    print(c)
if operator == "除":
    d = number_one / number_two
    print(d)
