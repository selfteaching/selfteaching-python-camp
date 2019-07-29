dirt = {1:'1，加法',2:'2，减法',3:'3，乘法',4:'4，除法',0:'0，退出系统'}
def Jisuan(suanfa):
    if suanfa in range(1,5):
        YourNumber1 = int(input('请输入您要计算的第一个数字：'))
        YourNumber2 = int(input('请输入您要计算的第二个数字：'))
        if suanfa ==1:
            print('运算结果是：{}'.format(YourNumber1+YourNumber2))
        elif suanfa == 2:
            print('运算结果是：{}'.format(YourNumber1-YourNumber2))
        elif suanfa == 3:
            print('运算结果是：{}'.format(YourNumber1*YourNumber2))
        else :
            print('运算结果是：{}'.format(YourNumber1/YourNumber2))
    elif suanfa == 0:
        print('程序结束，谢谢使用')
    else:
        print('输入错误请重新输入')
    return suanfa


while True:
    print('欢迎使用计算系统')
    for i in range(0,5):
        print(dirt[i])
    YourChoice = int(input('请选择您需要的运算：'))
    if YourChoice not in range(0,5):
        print('您的输入有误，请重新输入')
        continue
    print('您选择的算法是{}'.format(dirt[YourChoice]))
    if Jisuan(YourChoice) == 0:
        break
