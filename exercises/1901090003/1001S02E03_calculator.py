num1=float(input("Enter num1 ="))
opt=(input("Enter operation (+,-,*,/)"))
num2=float(input("Enter num2 ="))

if opt == "+":
    result = (num1+num2)
elif opt == "-":
    result = (num1-num2)
elif opt =="*":
    result = (num1*num2)
elif opt =="/":
    result = (num1/num2)
else:
    result="Invalid input"
print(num1,opt,num2,'=',result)

