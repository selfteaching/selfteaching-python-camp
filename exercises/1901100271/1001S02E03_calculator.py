Num1 = float(input('�������һ������:'))
Num2 = float(input('������ڶ�������:'))
operation = input('��ѡ���������:+��-��*��/:')   
if operation == '+':
    print(Num1,"+",Num2,"=",Num1+Num2)
if operation == '-':
    print(Num1,"-",Num2,"=",Num1-Num2)
if operation == '*':
    print(Num1,"*",Num2,"=",Num1*Num2)
elif operation == '/':
    print(Num1,"/",Num2,"=",Num1/Num2)
else:
    print("��������ȷ���������")
    
