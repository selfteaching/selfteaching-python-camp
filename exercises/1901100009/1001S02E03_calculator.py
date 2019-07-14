

def cal():
    n=0
    while n<3:
        print(n)
        code=input('请输入四位验证码:')
        if code =="i520":
            print('{0:*^30}'.format('计算器开始'))
            numA = float(input('请输入一个数字: '))
            op = input('请选择一个操作(+-*/): ')
            #numB = float(input('请输入另一个数字: '))
            if op == '+':
                numB = float(input('请输入另一个数字: '))
                print ("结果: ",numA+numB)
            elif op == '-':
                numB = float(input('请输入另一个数字: '))
                print( "结果: ",numA-numB)
            elif op == '*':
                numB = float(input('请输入另一个数字: '))
                print ("结果: ",numA*numB)
            elif op == '/':
                numB = float(input('请输入另一个数字: '))
                print ("结果: ",numA/numB)
            else:
                print ("无效操作",op)
        else:
            n+=1
            if n<3:
                print("对不起,您已输错%s次,还有%s次,请重试!"%(n,(3-n)))
            else:
                print("您已输错3次,计算器结束!")
 
if __name__=="__main__":
         
         c=cal()