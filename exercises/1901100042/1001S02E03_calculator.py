#this is a calculator
'''
Version:n.0
Author:Taskow
'''
x = float(input('please input first number：'))
operator = input('please input operator(only +,-,*,/)')
#Druing the version1.0 code（the firse attempt）,the type of x was ignored,
#then,str + str happended.
y = float(input('please input the second number：'))

if operator  == '+':
    print (x,operator,y,'=',x + y)
elif operator =='-':
    print (x,operator,y,'=',x - y)
elif operator == '*':
    print (x,operator,y,'=',x * y)
elif operator == '/':
    print (x,operator,y,'=',x / y)
else :
    print ('Operational error,please check:',operator)
    

