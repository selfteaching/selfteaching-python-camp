choice = float(input('请选择运算： \n1.加\n2.减\n3.乘\n4.除\n5.幂\n6.余\n请选择你的算法： '))
num1 = float(input('请输入第一个数： '))
num2 = float(input('请输入第二个数： '))
if choice == 1:
    print('{} + {} = {}'.format(num1, num2 ,num1+num2))
elif choice == 2:
    print('{} - {} = {}'.format(num1, num2 ,num1-num2))
elif choice == 3:
    print('{} *{} = {}'.format(num1, num2 ,num1*num2))
elif choice == 4:
    print('{} / {} = {}'.format(num1, num2 ,num1/num2))
elif choice == 5:
    print('{} ** {} = {}'.format(num1, num2 ,num1**num2))
elif choice == 6:
    print('{} % {} = {}'.format(num1, num2 ,num1%num2))