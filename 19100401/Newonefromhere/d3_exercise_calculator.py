#创建一个支持加减乘除的计算器
d1=input('请输入数字1：')        #让用户输入第一个运算数字
op=input('请输入运算符（+ - * /）：')    #让用户输入运算符号
d2=input('请输入数字2：')         #让用户输入第二个数字
if d1.isdigit() and d2.isdigit(): #判断用户输入是否是数字
    d1=float(d1)  #将输入值类型转换为浮点型
    d2=float(d2)
    if op=='+':  #判断用户是否做加法
        result=d1+d2     #计算做加法的值          
        print(f'{d1}+{d2}={result}')  #显示结果
    elif op=='-':
        result=d1-d2                            
        print(f'{d1}-{d2}={result}')                     
    elif op=='*':                      
        result=d1*d2                           
        print(f'{d1}*{d2}={result}')  
    elif op=='/':                      
        result=d1/d2                  
        print(f'{d1}/{d2}={result}')  
    else:
        print('请输入正确的运算符号！') #用户输入参数不正确，给用户提示
else:
    print('请输入数字！') #用户输入不是数字给予提示
        

