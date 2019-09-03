# 以下是照抄学友的
# float( )支持小数运算
# int( )函数只支持整数
# input( )接收键盘输入

a=float(input('2.0'))
b=input('+')
c=float(input('3.0'))
if b=="+":
    print (a+c)
elif b=="-":
    print (a-c)
elif b=="*":
    print (a*c)
elif b=="/":
    print (a/c)
elif b=="**":
    print (a**c)
elif b=="%":
    print (a%c)