print('欢迎使用普通计算机')
print('-------------------')
while True:
    num1 = float(input('输入数字按回车继续： '))
    num2 = float(input('输入数字按回车计算： '))

    print('和：' , num1+num2 ,)
    print('差：' , num1-num2)
    print('商：' , num1/num2 ,)
    print('积：' , num1*num2)
    print('-------------------')

    end = input('请输入y退出计算机 ')
    if end == 'y' :
        break