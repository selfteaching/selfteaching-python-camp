x=int(input("Enter your first number:"))
A=input("Enter the type of calculation:")
y=int(input("Enter your second number:"))
if A=="+":
    print(x+y)
elif A=="-":
    print(x-y)
elif A=="*":
    print(x*y)
else:
    print(x/y)
