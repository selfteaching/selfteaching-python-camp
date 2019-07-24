num1 = float(input("Please type the first number:")),
num2 = float(input("Please type the second number:")),
operator = input("Which oprate do you want?")

i=0
result = 0
def calculator(x,y):
    if operator == '+':
        result = num1[i]+num2[i]
    elif operator == '-':
        result = num1[i]-num2[i]
    elif operator == '*':
        result = num1[i]*num2[i]
    elif operator == '/':
        result = num1[i]/num2[i]
    else:
        print('this calculator can not do this,try something else!')
    
    print(result)

calculator(num1,num2)