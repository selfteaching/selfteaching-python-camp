#<<<<<<< master
def calculator():
    while True:
        x=int(input('x='))
        opo=str(input('输入运算符'))
        y=int(input('y='))
        if opo == '+':
            return (x+y)
        elif opo == '-':
            return (x-y)
        elif opo == '*':
            return (x*y)
        elif opo == '/':
            return (x/y)
        else:
            print('输入有误，请重输')
print(calculator()) 
#知道这个程序不够完善，若要运算多个数，则会出错，但考虑这些情况进去，以目
#=======
def calculator():
    while True:
        x=int(input('x='))
        opo=str(input('输入运算符'))
        y=int(input('y='))
        if opo == '+':
            return (x+y)
        elif opo == '-':
            return (x-y)
        elif opo == '*':
            return (x*y)
        elif opo == '/':
            return (x/y)
        else:
            print('输入有误，请重输')
print(calculator()) 
#知道这个程序不够完善，若要运算多个数，则会出错，但考虑这些情况进去，以目
#>>>>>>> master
#前水平还写不出来，且Day3的任务耗的时间有点多，所以先写了简陋版的计算器                    