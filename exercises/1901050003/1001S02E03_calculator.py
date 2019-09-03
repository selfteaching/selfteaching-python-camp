#做加减乘除的简单计算器

num1 = float (input('enter first number'))
op = input ('enter operator')
num2 = float (input('enter second number'))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)  
elif op == "*":
    print (num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print ('invalid operator')

