A=input("The symbol that you want to run")
a=input("first_nunber")
b=input("second_number")
if A == '+':
    c=int(a)+int(b)
    print(c)
elif A=="-":
    c=int(a)-int(b)
    print(c)
elif A=="*":
    c=int(a)*int(b)
    print(c)
elif A=='/':
    c=int(a)/int(b)
    print(c)
else:
    print('叫你输入加减乘除，你不会吗？？')