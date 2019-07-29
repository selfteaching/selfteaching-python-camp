operator = input ("请输入运算符（+、-、*、/) :" ) 
first_number = input("请输入第一个数字；") 
second_number = input("请输入第二个数字；") 

a = int(first_number) 
b = int (second_number)

print("operator:"), operator, type(operator) 
print("first_number:", first_number, type(first_number), type(a)) 
print("second_nmber:", second_number, type(second_number),type(b)) 

if operator == "+":
    print(a, "+", b, "=", a + b) 
elif operator == "-":
    print(a, "-", b, "=", a - b)
elif operator =="*":
    print(a, "*", b, "=", a * b) 
elif operator =="/":
    print(a, "/", b, "=", a / b) 
