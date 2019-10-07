Num1 = float(input('请输入第一个数字:'))
Num2 = float(input('请输入第二个数字:'))
operation = input('请选择运算符号:+，-，*，/:')   
if operation == '+':
    print(Num1,"+",Num2,"=",Num1+Num2)
if operation == '-':
    print(Num1,"-",Num2,"=",Num1-Num2)
if operation == '*':
    print(Num1,"*",Num2,"=",Num1*Num2)
elif operation == '/':
    print(Num1,"/",Num2,"=",Num1/Num2)
else:
    print("请输入正确的运算符号")
    
