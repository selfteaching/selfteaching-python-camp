calculate = input('选择您要进行的运算:1.加法2.减法3.乘法4.除法 \n请输入数字进行选择: 1 / 2 / 3 /4 \n') 
num1 = float(input('请输入第一个运算数字'))
num2 = float(input('请输入第二个运算数字'))
if calculate == '1':
    print(num1+num2)
elif calculate == '2':
    print(num1-num2)    
elif calculate == '3':
    print(num1*num2)
elif calculate == '4':
    print(num1/num2)
