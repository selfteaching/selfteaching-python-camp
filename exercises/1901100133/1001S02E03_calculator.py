operator=input("请输入运算符(+、-、*、/):")
first_number=input("请输入第一个数：")
second_number=input("请输入第一个数：")
a=int(first_number)
b=int(second_number)
print("operator:",operator,type(operator))
print("first_number:",first_number,type(first_number))
print("second_number:",second_number,type(second_number))
if operator=="+":
    print(a,'+',b,'=:',a+b)
elif operator == "-":
    print(a,'-',b,'=:',a-b)
elif operator == "*":
    print(a,'*',b,'=:',a*b)
elif operator == "/":
    print(a,'/',b,'=',a/b)
else:
    print('无效的运算符')