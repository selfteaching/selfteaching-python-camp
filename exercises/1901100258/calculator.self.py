operator=input('please enter your operator + - * /: ')
first_number=input('please enter the first number: ')
second_number=input('plesae enter the second number: ')

a=int(first_number)
b=int(second_number)

if operator=='+':
    print('calculation result:',first_number,'+'+second_number+'=',a+b)
elif operator=='-':
    print('calculation result:',first_number+'-'+second_number+'=',a-b)
elif operator=='*':
    print('calculation result:',first_number+'*'+second_number+'=',a*b)
elif operator=='/':
    print('calculation result:',first_number+'/'+second_number+'=',a/b)
else : 
    print('invalid operator')
