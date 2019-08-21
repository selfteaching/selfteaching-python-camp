x=int(input("the first number"))
A=input("operator")
y=int(input("second number"))
if A=="+":
    print(x+y)
elif A=="-":
    print(x-y)
elif A=="*":
    print(x*y)
else:
    print(x/y)