def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

first_num = float(input("Enter first number: ")) 
second_num = float(input("Enter second number: ")) 
operator = input("Enter operator: ")

if operator=='+':
    result = add(first_num,second_num)
elif operator=='-':
    result = subtract(first_num,second_num)
elif operator=='*':
    result= multiply(first_num,second_num)
elif operator=='/':
    result = divide(first_num,second_num)
else:
    result = 0

print(result)


while True:
    num = float(input("Enter number again: ")) 
    opt = input("Enter operator again(非+、-、*、／输出结果归零): ") 
    if opt=='+':
        result = add(result,num)
    elif opt=='-':
        result = subtract(result,num)
    elif opt=='*':
        result= multiply(result,num)
    elif opt=='/':
        result = divide(result,num)
    else:
        result = 0
    print(result)