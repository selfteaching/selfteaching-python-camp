operator=input
first_number=input
second_number=input
a=int(first_number)
b=int(second_number)
print("operator:",operator,type(operator))
print("first_number:",first_number,type(first_number))
print("second_number:",second_number,type(second_number))
if operator=="+":
    print(a,'+',b,'=:',a+b)
elif operator=="-":
    print(a,'-',b,'=:',a-b)
elif operator=="*":
    print(a,'*',b,'=:',a*b)
elif operator=="/":
    print(a,'/',b,'=',a/b)
else:
    print('无效的运算符')