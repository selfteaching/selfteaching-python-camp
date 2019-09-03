#终端操作
operator = input('请输入运算符（+、-、*、/):') #input 里面的字符串的作用是在等待输入的时候进行提示
first_number=input('请输入第一位数字：')
second_number=input('请输入第二位数字：')

a=int(first_number)  #int（first_number) 在这里的作用是将first_number的str类型转换成int类型
b=int(second_number)

print('operator', operator, type(operator))
print('first_number', first_number, type(first_number), type(a))
print('second_number', second_number, type(second_number), type(b))

#<<<<<<< master
print('测试加法 str 加法 ：',a + b)
print('测试加法 str 减法 ：',a - b)

#=======
print('测试加法 str 加法 ：',first_number + second_number)
#>>>>>>> master

if operator == '+':
   print(a,'+',b,'=',a + b)
elif operator == '-':
    print(a,'-',b,'=',a - b)
elif operator == '*':
    print(a,'*',b,'=',a * b)
elif operator =='/':
    print (a,'/',b,'=',a / b)
else:
    print('运行错误')