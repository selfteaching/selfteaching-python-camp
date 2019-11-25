e='y' #初始赋值,为下方while循环提供第一次计算
print('欢迎使用四则运算计算器，请在下方输入相应内容')
a=input('输入一个数值：')
while a.isdigit()==False: #判断是否输入数字，需要注意的是int和float没有isdigit属性
    a=input('似乎缺少一个数字，请再次输入第一个数值：') #所以这个判断必须在类型转换前
while e=='y': #执行是否继续计算的判断，如果是，则用最后的结果继续算下去
    b=input('输入计算符号（+，-，*，/）：')
    c=input('输入另一个数值：')
    while c.isdigit()==False:
        c=input('似乎缺少一个数字，请再次输入第二个数值：')
    z=b
    a= float(a) #转换类型
    c= float(c)
    print('计算结果为:')
    if z=='+':
        d=(a+c)
        print(d)
    elif z=='-':
        d=(a-c)
        print(d)
    elif z=='*':
        d=(a-c)
        print(d)
    elif z=='/':
        d=(a/c)
        print(d)
    else:
        print('符号输入错误，请重试')
    a=d
    e=input('是否继续计算,输入y继续，输入其他内容则结束使用:')
print('谢谢使用再见')