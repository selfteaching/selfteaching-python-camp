#coding=utf-8

"""
学习内置函数input()的基本用法
学习if……eslse……，实现选择的功能
学习变量的定义和赋值
学习type()函数
学习print()函数
初步了解逻辑运算符
初步了解raise 的用法
"""


def  cal_1_tor() : 

    # 从终端获得数字和运算规则
    f_nber = input('请输入第一个数字：')
    while f_nber.isdigit() == False :
        print('输入有误！！————请重新输入第一个数字：')
        f_nber = input()
    else:
        print("参与计算的第1个数字是：", f_nber,'\n','*'*50,'\n')




    optor = ['+','-','*','/']
    operator_in_four = input("请输入4个运算符（+，-，*，/）中的1个：")
    while operator_in_four in optor == False :
        print('输入有误！！')
        operator_in_four = input("请输入4个运算符（+，-，*，/）中的1个：")
    else :
        print("计算规则是：",operator_in_four,'\n','*'*50,'\n')




    s_nber = input('请输入第二个数字：')
    while (s_nber.isdigit() == False)  or (s_nber==str(0) and operator_in_four=='/'):
        print('输入有误！！————请重新输入第二个数字：')
        s_nber = input()
    else:
        print("参与计算的第2个数字是：", s_nber,'\n','*'*50,'\n')




    # 将从input()获得的str型的数据，强制转换成int型的数据
    a = int(f_nber)
    b = int(s_nber)

    # 先判断计算规则，然后计算结果
    if operator_in_four == '+' :
        last_result = a + b
    elif operator_in_four == '-' :
        last_result = a - b
    elif operator_in_four == '*' :
        last_result = a * b
    else: 
        last_result = a / b



    print('*'*50)
    print("最终结果是：", last_result)
    print('*'*50,'\n')



while  1 > 0 :
    print('要开始计算，请输入：start\n要退出，请输入：over\n','********************* start OR over **********************')
    start_c = input() 

    if start_c == 'start' :
        cal_1_tor()
    elif start_c == 'over' :
        exit(0)
    else:
        print('输入有误，请重新输入：')