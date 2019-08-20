def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x / y 

num1=int(input('what is your first value: '))
num2=int(input('what is your second value: '))

print ('select an operation(please only enter the number)')
print ('1.add')
print ('2.subtract')
print ('3.multiply')
print('4.divistion')

selection = input('your selection is: ')

if selection == "1":
    print (num1,"+",num2,"=",add(num1,num2))
elif selection == '2':
    print (num1,"-",num2,"=",subtract(num1,num2))
elif selection == "3":
    print (num1,"*",num2,"=",multiplication(num1,num2))
elif selection == '4':
    print (num1,"/",num2,"=",division(num1,num2))
else:
    print ("You cannot enter a number larger than 4!")

