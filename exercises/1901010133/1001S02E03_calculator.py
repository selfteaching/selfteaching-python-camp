s1=eval(input('请输入第一个数字'))
s2=eval(input('请输入第二个数字'))
s3=input('请输入运算符')
if s3=='+':
    print(s1+s2)
elif s3==('-'):
    print('s1-s2')
elif s3==('/'):
    print(s1/s2)
elif s3==('*'):
    print(s1*s2)
else:
    print('输入有误')   