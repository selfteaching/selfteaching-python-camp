####################################################
# from system prompt input two number 
# the Calculator will give the add, subtration, multiplication and division operation
# will give error information if the second number zero
####################################################

print("Please input number to a")
a = float(input())
print("Please input number to b")
b = float(input())
if b == 0:
    print("The divisor can not be a Zero, please re-run the program and re-enter 2 numbers.")
else:
    print("The a+b, a-b, a*b, a/b equal to", (a+b), (a-b), (a*b), (a/b) )
