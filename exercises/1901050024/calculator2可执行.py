print("简易计算器")
print ("请输入你想要计算的类型")
def add(x,y):
    result = x + y
    return result
def sub(x,y):
    result = x-y
    return result
def mul(x,y):
    result = x*y
    return result
def div(x,y):
    result = x/y
    return result
a = input("1:加法；2:减法；3:乘法；4:除法:\n")
b = float(input('请输入数字:'))
c = float(input('请输入数字:'))
if a == '1' :
        print(b,'+',c,'=',add(b,c))
elif a == '2':
        print(b,'-',c,'=',sub(b,c))
elif a == '3':
        print(b,'*',c,'=',mul(b,c))
elif a == '4':
        print(b,'/',c,'=',div(b,c))
else: 
        print("输入错误")
print("结束")