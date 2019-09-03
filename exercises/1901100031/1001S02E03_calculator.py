
operator=input('请输入运算符（+，-，*，/，**）：')
numb_1=input('请输入第一个数字:')
numb_2=input('请输入第二个数字:')
a=int(numb_1)
b=int(numb_2)
print('operator:',operator,type(operator))
print('numb_1:',numb_1,type(numb_1),type(a))
print('numb_2:',numb_2,type(numb_2),type(b))

if operator=="+":
    print(a,'+',b,'=',a+b)
elif operator=="-":
    print(a,'-',b,'=',a-b)
elif operator=="*":
    print(a,'*',b,'=',a*b)
elif operator=="/":
    print(a,'/',b,'=',a/b)
elif operator=="**":
    print(a,'**',b,'=',a**b)
else:
    print('无效的运算符')



