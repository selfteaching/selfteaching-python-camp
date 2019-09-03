calculator=input('请输入运算符（+，-，*，/）:')
first_number=input('请输入第一个数字：')
second_number=input('请输入第二个数字：')
a=int(first_number)
b=int(second_number)

print('calculator:', first_number, type(first_number))
print('first_number:', first_number, type(first_number), type(a))
print('second_number:', second_number, type(second_number), type(b))

if calculator=='+':
    print(a,'+',b,'=',a+b)
elif calculator=='-':
    print(a,'-',b,'=',a-b)
elif calculator=='*':
    print(a,'*',b,'=',a*b)
elif calculator=='/':
    print(a,'/',b,'=',a/b) 
else:
    print('无效的运算符')
      