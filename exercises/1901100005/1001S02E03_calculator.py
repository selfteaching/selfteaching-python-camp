#计算器确定三个输入值，分别是运算符、运算左边的数字和右边的数字

# 把内置函数 input 接受的 输入字符 赋值 给 变量
operator = input("Please enter an operator（+, -, *, /）:") # input 里面的字符串的作用是在等待输入的时候进行提示
first_number = input("Please enter the first number: ")
second_number = input("Please enter the second number: ")

a = int(first_number) #int(first_number) 在这里的作用是把 str 类型的 first_number 转换成 int类型 
b = int(second_number)

print("opperator: ", operator, type(operator))
print("first_number: ", first_number, type(first_number), type(a))
print("second_number: ", second_number, type(second_number), type(b))

print("text addition str addition: ", first_number + second_number)
# print("text subtraction str subtraction: ", first_number - second_number)

if operator == "+":
    print(a, "+", b, "=", a + b)
elif operator == "-":
    print(a, "-", b, "=", a - b)
elif operator == "*":
    print(a, "*", b, "=", a * b)
elif operator == "/":
    print(a, "/", b, "=", a / b) 
else:
    print("Invalid operator")
    # raise ValueError('无效的运算符')
    