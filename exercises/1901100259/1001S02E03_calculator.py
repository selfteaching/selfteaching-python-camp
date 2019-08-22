operator=input("输出第一个字符(+、-、*、/、//、%、**)：")
number_1=input("输入第1个数字：")
number_2=input("输入第2个数字：")
a=int(number_1)
b=int(number_2)
#print(operator,type(operator),)
#print(number_1,type(number_1),type(a))
#print(number_2,type(number_2),type(b))
#print(a*b)
           
if operator =="+":
    print(a,"+",b,"=",a+b)

elif operator =="-":
    print(a,"-",b,"=",a-b)

elif operator =="*": 
    print(a,"*",b,"=",a*b)

elif operator =="/":
    print(a,"/",b,"=",a/b)

elif operator =="//":
    print(a,"//",b,"=",a//b)

elif operator =="%":
    print(a,"%",b,"=",a%b)

elif operator =="**":
    print(a,"**",b,"=",a**b)

else:
     print("error")   