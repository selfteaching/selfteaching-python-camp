first_num = float(input('Please enter your first number:'))
second_num = float(input('Please enter your second number:'))
op = input('Please erter your operarion ')
if op == '+':
    s = (first_num + second_num)
    print(s)   
elif op == '-':
    s = (first_num - second_num)
    print(s)
elif op == '×':
    s = (first_num * second_num)
    print(s)
elif op == '÷':
    if second_num == 0 :
        print('Error')
    if second_num != 0 :
        s = (first_num / second_num)
        print(s)           
