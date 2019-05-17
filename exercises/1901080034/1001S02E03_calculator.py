a=input('请输入第一数字：')
a=float(a)
c=input('请输入+-*/')
d=['+','-','*','/']
while c not in d :
    print('算数输入格式错误，请重新输入')
    c=input('请输入+-*/')
b=input('请输入第二个数字：')
b=float(b)
if c=='+':
    print('计算结果：',float(a+b))
elif c=='-':
    print('计算结果：',float(a-b))  
elif c=='*':
    print('计算结果：',float(a*b))
elif c=='/':
    print('计算结果：',float(a/b))


