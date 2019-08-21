#计算器支持加减乘除
operator= input("pls input character (+,-,*,/):")#()内内容为提示内容
firstnumber=input("first number:")
secondnumber=input("second number:")

a=float(firstnumber)
b=float(secondnumber)

print("operator:",operator,type(operator))
print("first_number:",firstnumber,type(firstnumber),type(a))
print("second_number:",secondnumber,type(secondnumber),type(b))

if operator=="+":
    print(a,"+",b,"=",a+b)
elif operator=="-":
    print(a,"-",b,"=",a-b)
elif operator=="*":
    print(a,"*",b,"=",a*b)
elif operator=="/":
    print(a,"/",b,"=",a/b)
else:
    print("not found")


