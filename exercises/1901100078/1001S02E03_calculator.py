def calculator(a,b, operator='+'):
    result = 0
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a- b
    elif operator == '*':
        result = a * b
    elif operator =='/':
        result = a/b
    return result
print(calculator(1,2,'*'))
            