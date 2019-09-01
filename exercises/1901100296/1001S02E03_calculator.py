'''
计算器
'''
'''
方法一：
输入公式如：9+8
回车后出来结果
'''
'''
x=0
while x<1:
    try:
        value=input("请输入运算公式，如：9+8：")
        print("计算结果是：",eval(value))
    except (BaseException):
        x=2
        print("输入有误！")
'''  
'''
方法二：
按运算顺序输入
'''
n1=input('第一个数字：')
s=input("选择运算符(+、-、*、/)：")
n2=input('第二个数字：')
if s=='+':
    print('运算结果：',n1,s,n2,'=',int(n1)+int(n2))
elif s=='-':
    print('运算结果：',n1,s,n2,'=',int(n1)-int(n2))
elif s=='*':
    print('运算结果：',n1,s,n2,'=',int(n1)*int(n2))
elif s=='/':
    print('运算结果：',n1,s,n2,'=',int(n1)/int(n2))
else:
    print("输入有误！")