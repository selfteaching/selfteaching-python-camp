print('请输入第一个数字:')
a=input()
print('请输入运算符号:')
operator=input()
print('请输入第二个数字:')
b=input()
if operator=='+':
    result=float(a)+float(b)
elif operator=='-':
    result=float(a)-float(b)
elif operator=='*':
    result=float(a)*float(b)
elif operator=='/':
    result=float(a)/float(b)              
print('计算结果是'+str(result))
