#程序不完善
operator=input('+、-、*、/')
first_number=input('数值one')
second_number=input('数值two')

a=int(first_number)
b=int(second_number)

if operator=='+':
        print(a,'+',b,'=',a+b)
elif operator=='-':
        print(a,'-',b,'=',a-b)
elif operator=='*':
        print(a,'*',b,'=',a*b)
elif operator=='/':
        print(a,'/',b,'=',a/b)
else:
        print('程序有待完善')