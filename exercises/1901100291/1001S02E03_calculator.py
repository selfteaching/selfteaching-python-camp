#这是一个简单的加减乘除计算器.

#接收输入的字符.
operater=input("请输入运算符（+、-、*、/）：")

first_number=int(input("请输入第一个数字："))
second_number=int(input("请输入第二个数字："))

if operater == "+":
    print(first_number,operater,second_number,"=",first_number+second_number)
elif operater =="-":
    print(first_number,operater,second_number,"=",first_number-second_number)
elif operater =="*":
    print(first_number,operater,second_number,"=",first_number*second_number)
elif operater =="/":
    print(first_number,operater,second_number,"=",first_number/second_number)
else:
    print("无效运算符")
