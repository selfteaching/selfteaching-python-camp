#自学训练营第一个程序，献给非常喜欢计算器的王有梧。
#1.定义四则运算
def plus(a ,b): #定义加法
    return a + b #输出结果

def minus(a , b): #定义减法
    return a - b #得出结果

def by(a ,b ):#定义乘法
    return a*b

def div(a ,b):#定义除法
    return a/b
#2.给出运算选项
print("可进行的运算行:")
print("1.加")
print("2.减")
print("3.乘")
print("4.除")

#给出四则运算选项
choice = input("请选择要进行的运算（1，2，3，4）： ")

numb1 = float(input("请输入要运算的数字1："))#要求输入要运算的第一个数字
numb2 = float(input("请输入要运算的数字2："))#要求输入要运算的第二个数字

if choice == '1':#如果选择加法运算
    print(numb1 ,"+" ,numb2,"=", plus(numb1,numb2) )#列出计算式和计算出的结果
elif choice == '2':#如果选择减法哟算
    print(numb1, "-", numb2,"=", minus(numb1,numb2))#列出计算式和计算出的结果
elif choice == '3':#如果选择乘法
    print(numb1 ,"x" ,numb2 ,"=", by(numb1,numb2))#列出计算式和计算出的结果
elif choice== '4':#如果选择除法
    print(numb1, "➗" ,numb2 ,"=", div(numb1,numb2))#列出计算式和计算出的结果
else:
    print("请输入正确的数字或选择给定的运算方式")#如果输入错误的给出处理建议
