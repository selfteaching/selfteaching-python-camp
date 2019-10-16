print('HELLO,this is a calculator program:')
first = int(input('Please input first number>>>'))
kind = input('Please input operator: + - * / >>>')
second = int(input('Please input second number>>>'))
if kind == "+":
    print(first + second)
elif kind == "-":
    print(first - second)
elif kind == "*":
    print(first * second)
elif kind == "/":
    print(first / second)
else:
    print("invaild input")